package main

import (
	"context"
	"fmt"
	"math/rand"
	"sync"
	"time"

	ggio "github.com/gogo/protobuf/io"

	"github.com/libp2p/go-libp2p-core/host"
	"github.com/libp2p/go-libp2p-core/network"
	"github.com/libp2p/go-libp2p-core/peer"
	"github.com/libp2p/go-libp2p-core/protocol"

	pb "github.com/libp2p/go-libp2p-pubsub/pb"

	timecache "github.com/whyrusleeping/timecache"

	"github.com/testground/sdk-go/runtime"
)

type BadBoy struct {
	ctx    context.Context
	h      host.Host
	runenv *runtime.RunEnv
	seq    int64
	params SybilParams

	mx        sync.Mutex
	attacking bool
	censor    map[peer.ID]struct{}
	mesh      map[string]map[peer.ID]struct{}
	out       map[peer.ID]chan *pb.RPC
	seen      *timecache.TimeCache
}

const gossipSubID = protocol.ID("/meshsub/1.0.0")
const maxMessageSize = 1024 * 1024

var (
	// Regraft delay after getting pruned (slow graft attack); set to 0 to disable.
	// After getting pruned by some peer, it will attempt to regraft after a random delay with maximum
	// of BadBoyRegraftDelay.
	BadBoyRegraftDelay = 15 * time.Second

	// reGRAFT backoff period to evade the hardening backoff period; that's added to the random regraft
	// delay.
	BadBoyRegraftBackoff = time.Minute

	// Time to cache messages that have been seen
	BadBoySeenCacheDuration = 120 * time.Second
)

func NewBadBoy(ctx context.Context, runenv *runtime.RunEnv, h host.Host, seq int64, params SybilParams) (*BadBoy, error) {
	bb := &BadBoy{
		ctx:    ctx,
		h:      h,
		runenv: runenv,
		seq:    seq,
		params: params,
		censor: make(map[peer.ID]struct{}),
		mesh:   make(map[string]map[peer.ID]struct{}),
		out:    make(map[peer.ID]chan *pb.RPC),
		seen:   timecache.NewTimeCache(params.seenCacheDuration),
		// If there's a delay, don't start attacking until after the delay
		// has passed: see OnReady()
		attacking: params.attackDelay == 0,
	}

	h.SetStreamHandler(gossipSubID, bb.handleIncoming)
	return bb, nil
}

func (bb *BadBoy) OnReady() {
	if bb.params.attackDelay == 0 {
		return
	}

	bb.log("waiting %s to start attacks", bb.params.attackDelay)
	go func() {
		select {
		case <-bb.ctx.Done():
		case <-time.After(bb.params.attackDelay):
			bb.log("starting attacks (after %s delay)", bb.params.attackDelay)
			bb.startAttacking()
		}
	}()
}

func (bb *BadBoy) Censor(p peer.ID) {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	bb.censor[p] = struct{}{}
}

func (bb *BadBoy) log(msg string, args ...interface{}) {
	id := bb.h.ID().Pretty()
	idSuffix := id[len(id)-8:]
	prefix := fmt.Sprintf("[sybil %d %s] ", bb.seq, idSuffix)
	bb.runenv.RecordMessage(prefix+msg, args...)
}

func (bb *BadBoy) markSeen(msg *pb.Message) bool {
	id := string(msg.GetFrom()) + string(msg.GetSeqno())

	bb.mx.Lock()
	defer bb.mx.Unlock()

	if bb.seen.Has(id) {
		return false
	}

	bb.seen.Add(id)
	return true
}

func (bb *BadBoy) handleIncoming(s network.Stream) {
	defer s.Reset()

	p := s.Conn().RemotePeer()
	bb.log("new stream from %s", p.Pretty())

	err := bb.openOutputStream(p)
	if err != nil {
		bb.log("error opening stream to %s", p.Pretty())
		return
	}

	r := ggio.NewDelimitedReader(s, maxMessageSize)
	var rpc pb.RPC

	for {
		rpc.Reset()

		err := r.ReadMsg(&rpc)
		if err != nil {
			bb.log("error reading RPC: %s", err)
			return
		}

		// control messages
		bb.handleControl(p, &rpc)

		// published messages
		for _, msg := range rpc.GetPublish() {
			// check if we've seen this message already
			if !bb.markSeen(msg) {
				continue
			}

			if !bb.isAttacking() {
				// if we're not attacking yet, skip attack code
				goto forward
			}

			// censor: drop messages from censored peers
			if bb.isCensored(peer.ID(msg.GetFrom())) {
				continue
			}

			// degrade: drop messages with specified probability
			if bb.params.degrade > 0 && rand.Float64() < bb.params.degrade {
				continue
			}

		forward:

			// forward the message to grafted peers in topic
			for _, topic := range msg.GetTopicIDs() {
				bb.forward(topic, msg, p)
			}
		}
	}
}

func (bb *BadBoy) handleControl(p peer.ID, rpc *pb.RPC) {
	// subscibe and GRAFT to all topics the peer is announcing
	var subs []*pb.RPC_SubOpts
	var graft []*pb.ControlGraft
	var topics []string

	for _, sub := range rpc.GetSubscriptions() {
		if sub.GetSubscribe() {
			subs = append(subs, &pb.RPC_SubOpts{Subscribe: sub.Subscribe, Topicid: sub.Topicid})
			graft = append(graft, &pb.ControlGraft{TopicID: sub.Topicid})
			topics = append(topics, sub.GetTopicid())
		}
	}

	// If we are subscribing/grafting, send the RPC
	if len(subs) > 0 || len(graft) > 0 {
		ok := bb.sendCtl(p, &pb.RPC{Subscriptions: subs, Control: &pb.ControlMessage{Graft: graft}})
		if ok {
			for _, topic := range topics {
				bb.graft(p, topic)
			}
		}
	}

	if rpc.Control != nil {
		// process PRUNEs to remove the peer from the mesh and schedule regraft
		for _, prune := range rpc.Control.Prune {
			bb.prune(p, prune.GetTopicID())
			if bb.params.regraftDelay > 0 {
				go bb.regraft(p, prune.GetTopicID())
			}
		}

		// process GRAFTs to add the peer to the mesh
		for _, graft := range rpc.Control.Graft {
			bb.graft(p, graft.GetTopicID())
		}
	}
}

func (bb *BadBoy) regraft(p peer.ID, topic string) {
	delay := bb.params.regraftBackoff + time.Duration(rand.Float64()*float64(bb.params.regraftDelay))

	select {
	case <-time.After(delay):
		ok := bb.sendCtl(p, &pb.RPC{
			Control: &pb.ControlMessage{
				Graft: []*pb.ControlGraft{
					&pb.ControlGraft{TopicID: &topic}}}})
		if ok {
			bb.graft(p, topic)
		}
	case <-bb.ctx.Done():
	}
}

func (bb *BadBoy) graft(p peer.ID, topic string) {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	mesh, ok := bb.mesh[topic]
	if !ok {
		mesh = make(map[peer.ID]struct{})
		bb.mesh[topic] = mesh
	}

	mesh[p] = struct{}{}
}

func (bb *BadBoy) prune(p peer.ID, topic string) {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	delete(bb.mesh[topic], p)
}

func (bb *BadBoy) handleOutgoing(s network.Stream, ch chan *pb.RPC) {
	p := s.Conn().RemotePeer()

	defer s.Reset()
	defer func() {
		bb.mx.Lock()
		delete(bb.out, p)
		for _, peers := range bb.mesh {
			delete(peers, p)
		}
		bb.mx.Unlock()
	}()

	w := ggio.NewDelimitedWriter(s)
	for {
		select {
		case rpc := <-ch:
			err := w.WriteMsg(rpc)
			if err != nil {
				bb.log("error writing RPC: %s", err)
				return
			}
		case <-bb.ctx.Done():
			return
		}
	}
}

func (bb *BadBoy) openOutputStream(p peer.ID) error {
	s, err := bb.h.NewStream(bb.ctx, p, gossipSubID)
	if err != nil {
		return err
	}

	ch := make(chan *pb.RPC, 32)
	bb.mx.Lock()
	bb.out[p] = ch
	bb.mx.Unlock()

	go bb.handleOutgoing(s, ch)
	return nil
}

func (bb *BadBoy) isCensored(p peer.ID) bool {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	_, censor := bb.censor[p]
	return censor
}

func (bb *BadBoy) isAttacking() bool {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	return bb.attacking
}

func (bb *BadBoy) startAttacking() {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	bb.attacking = true
}

func (bb *BadBoy) sendCtl(p peer.ID, rpc *pb.RPC) bool {
	bb.mx.Lock()
	out, ok := bb.out[p]
	bb.mx.Unlock()

	if ok {
		out <- rpc
	}

	return ok
}

func (bb *BadBoy) forward(topic string, msg *pb.Message, from peer.ID) {
	bb.mx.Lock()
	defer bb.mx.Unlock()

	rpc := &pb.RPC{Publish: []*pb.Message{msg}}
	for p := range bb.mesh[topic] {
		if p != from && p != peer.ID(msg.From) {
			out, ok := bb.out[p]
			if ok {
				select {
				case out <- rpc:
				default:
					bb.log("Dropping RPC to %s; queue full", p)
				}
			}
		}
	}
}
