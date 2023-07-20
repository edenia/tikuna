---
slug: malicious-validators
title: "The Danger of Malicious Block Proposers in Maximal Extractable Value"
authors: [andres, francis, loui]
---
---

As we introduced in our previous blog post [[25]](/docs/research/references), the term Maximal Extractable Value (MEV) refers to the highest amount of value that can be extracted from a blockchain by a producer/validator during the process of creating a block. This can be achieved by including, excluding, or rearranging the order of transactions.

MEV is a relatively novel topic with many unexplored security consequences. For instance, on April 3rd, 2023, a malicious validator node operator exploited a vulnerability in the mev-boost-relay [[26]](/docs/research/references), the most popular MEV relay, to get access to the transaction bundle content, even when the block was created to fail the validation to be accepted by the beacon chain nodes. With the obtained list of transactions, the attacker could execute a front-running attack, earning 20 million USD from the victim block bundle builders.

The following graphic explains how the normal flow of block creation in Ethereum among validators, builders, and relays should work [[27]](/docs/research/references): 

<div className="blogMev2"></div>

Typically, block proposers (consensus validators) should blindly sign block headers created by block builders and then wait until the blocks are already announced to the network to be able to access the block content (the transactions). Hence, the proposers cannot steal the MEV created by the block builders. However, a vulnerability in the relay software allowed a malicious proposer to modify a block header with corrupt data that the network should not accept.q The relay assumed the signed block as valid and returned the block content to the proposer, which instead extracted the MEV for itself. It then created another valid block that was accepted by the network, therefore stealing the builder's profit.

Here [[28]](/docs/research/references), you can see the vulnerability disclosure write-up with a more detailed explanation and countermeasures taken by the developers. One of the mentioned countermeasures is that the relay does not send the block content directly to the block proposer; instead, it has to read it from the network when it's accepted. This approach is only partially practical because a malicious proposer could run many validator nodes or even launch an eclipse attack on the network so it can see the block's content much faster and try to front-run the relay. Tikuna may help detect such eclipse attacks and alert the affected relays.

As we see here, malicious validators are becoming a worrying reality. Monitoring the behavior of validators can help identify those trying to take advantage of the blockchain network. At Sakundi [[21]](/docs/research/references), we are developing technologies to monitor the blockchain using AI technologies that may help detect such malicious validators.

In the upcoming series of posts, we will be exploring other topics related to MEV in the context of blockchain technology. Stay tuned for more!

Have questions? Contact us today to find out more about our services.
