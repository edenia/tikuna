---
id: stateoftheart
title: State of the Art
sidebar_label: State of the Art
description: Tikuna - an Ethereum blockchain network security monitoring system
keywords: [tikuna, ethereum, research grant]
hide_table_of_contents: true
custom_edit_url: null
---
---

Ethereum was formally introduced by Vitalik Buterin in his whitepaper in 2014 [[2]](references.md) and launched in 2015; it is considered one of the most well-known open-source public cryptocurrency blockchain platforms that support smart contract functionality with Ether (ETH or Ξ) as it is native cryptocurrency and Solidity its programming language. According to [[1]](references.md), there were a total number of 105.58 million transactions and 1.45 million smart contracts created in the first quarter (Q1) of 2022. In addition, concerning market capitalization, Ethereum is the second largest cryptocurrency after Bitcoin, with around $234 billion as of August 2022 [[3]](references.md).

Furthermore, Ethereum allows developers to create decentralized applications (dApps) in various sectors such as decentralized finance (DeFi) [[4]](references.md), gaming [[5,6]](references.md), Non-fungible tokens (NFTs) [[7]](references.md), and Internet-of-Things (IoT) [[10]](references.md) that run on a peer-to-peer (P2P) network. Therefore, minimizing the chances of fraud, censorship, downtime, or third-party involvement and making them more reliable. Additionally, the Ethereum public mainnet has just gone through a significant upgrade to Ethereum 2 (officially after renaming called The Merge ($ETH) [[8, 9]](references.md)) to improve its performance, efficiency, and scalability.

Blockchains have many layers, such as the consensus layer [[11-13]](references.md), scripting layer, network layer, or DApps, but what we are interested in is the lowest level layer in the blockchain, namely the P2P network that allows the nodes to interconnect to each other and share information, which is a vital component of the Ethereum blockchain. The basic idea behind the P2P network is that a group of computers called nodes are connected to share data without the need for a centralized computer, i.e., all the nodes on the network have the same capabilities without having any special privileges, such as the one used in the file sharing systems Napster, LimeWire, and Gnutella.

The peer-to-peer (P2P) networking is the fundamental component that serves as the foundation for any blockchain technology. But, similar to other forms of technology, P2P networks may be affected by a number of security issues. Moreover, adversaries can exploit some of the blockchain P2P network vulnerabilities to carry out several attack vectors on the blockchain, such as eclipse attack, selfish mining attacks, Sybil attacks, or DDoS attacks. Therefore, to address both the different attack vectors on the Ethereum platform and the P2P network security vulnerabilities, many researchers have recently started focusing their research in this direction.

In the following are some of the most recent works that address the security challenges of the Ethereum blockchain P2P networks:

- This paper [[14]](references.md) generally focuses on the security issues of each layer in the Ethereum blockchain such as the network layer by providing an in-depth analysis covering the following three areas:

    1. Its potential attacks like eclipse attack and account hijacking attack.
    2. The vulnerabilities that lead to them for example the unlimited nodes creation vulnerability, the uncapped incoming connections vulnerability.
    3. The effects of each incident such as double spending, or denial of Service (DoS). 

 In addition to providing an overview of the effectiveness and the limitations of the existing Intrusion Detection Systems (IDS) as a defense technique against these attacks.

- This paper [[15]](references.md) proposes the GossipSub protocol and its two components, the mesh construction and the score function. The GossipSub is a messaging protocol that enables rapid and robust message transmission in permissionless networks, such as the Ethereum 2.0 network layer, to make it, on the one hand, more secure against various types of attacks (such as the Sybil attack, the Eclipse attack, and the Cold Boot attack), and on the other hand, to facilitate a faster transmission of the messages within the network. In addition, the authors describe some of the countermeasures featured in the GossipSub protocol, such as controlled mesh maintenance, opportunistic grafting, and adaptive gossip distribution. In conclusion, the writers evaluate the GossipSub protocol against various attacks and demonstrate its resistance to these attacks.

- In this study [[16]](references.md), the authors first highlight some of the Eth2 network structure, the network ecosystem, and the potential dangers it could pose. In addition, the writers comprehensively investigate the Eth2 mainnet's P2P network by developing a monitoring tool called Armiarma. This tool consists of two components, the Armiarma crawler and the Armiarma analyzer, to address the absence of information and the missing insights regarding the performance of the GossipSub protocol and its peers on the Eth2 main network. Furthermore, an experiment was conducted to evaluate the capabilities of the proposed approach, and an analysis of the gathered outcomes was grouped into the following three parts:
   1. Eth2 Network Analysis
   2. Eth2 Clients Interaction
   3. Individual Peer Analysis

 Moreover, the analysis identifies several issues with the Eth2 Beacon Chain, including geographical, implementation, and physical hosting of the Eth2 validators. Finally, the authors conclude that the network is behaving healthily; however, some decentralization-related issues still need to be considered.

- This research [[17]](references.md) discusses "the eclipse attacks" on the Ethereum P2P Network. An eclipse attack is an attack that allows an adversary to isolate a target node within the P2P network by gaining complete control of a node's access to information or control over everything that the node sees. This attack is discussed in the context of the Ethereum P2P Network. The authors developed an eclipse-attack detection model called ETH-EDS that mainly targets the Ethereum platform. This model used the random forest classification technique to examine both normal and attack data packets in the network. The collected data packets included details like the size of the tags packets, the frequency with which they were accessed, and the access time. The findings of the experiments show that malicious network nodes could be identified with a high degree of precision.