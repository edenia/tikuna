---
id: understanding-dashboards
title: Understanding the data behind the Dashboards
sidebar_label: Understanding the data behind the Dashboards
description: Process install for Tikuna
keywords: [tikuna, ethereum, research grant]
hide_table_of_contents: true
custom_edit_url: null
---

---

## P2P Network status on ETH2:

This dashboard shows all the important information contained historically inside the node. There is disposed of in two status: Neighborhood & Network.

* The neighborhood status refers to how the own node is interacting with other nodes in the blockchain. It can be found important stats such as:

<div className="readmeStatusNeighborhood dashboard1"></div>

### Peer Count:  

How many other nodes in the beacon network the node itself is interacting with. 

### Max inactivity: 

Is a score that reflects the current inactivity of the validators.

### Libp2p Peers pie chart: 

Shows how the agents are distributed among neighboring peers, which type of Libp2p client are using and what’s the most used.
 
### Libp2p Peers average scores: 

The average score obtain in terms of the metrics and performance.

* In the other hand, the network status shows a summarized data, measured by the own node, about the general aspects in the network status such as:

<div className="readmeStatusNetwork dashboard2"></div>

### Participation rate: 

How many ETH Balances are attesting (validating) to the network.

### Network Liveness: 

This metric expresses the distance between the current finalized epoch and the expected finalized epoch based on the genesis time.

### Epochs:  

A period of time during which a specific set of chosen validators are responsible for creating new blocks and adding them to the blockchain.