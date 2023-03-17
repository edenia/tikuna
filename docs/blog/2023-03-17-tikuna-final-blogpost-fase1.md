---
slug: tikuna-final-blogpost-fase1
title: "Marking the Delivery of our Tikuna Project Proof-Of-Concept Phase"
authors: [andres, francis, loui]
---
---
We are thrilled to announce the completion of the first phase of our Tikuna project! After months of hard work, dedication, and collaboration, we are excited to share the results of the first round of the Ethereum Foundation (EF) academic research grant. We will highlight our project's milestones and examine our team's findings in this blog post.

## Overview

Blockchain security is becoming increasingly relevant in today's cyberspace, and it is essential to strengthening each layer's security in its architecture. Our project focuses on the lowest level layer in the blockchain, particularly the P2P network that allows the nodes to communicate with each other and share information. This layer is a vital component of any blockchain, including Ethereum, due to the decentralized nature of its architecture. However, the P2P network layer may be vulnerable to several attacks, such as a Distributed Denial of Service (DDoS), eclipse attacks, or Sybil attacks. Consequently, this layer is still prone to many threats inherited from P2P networks, and there is a need to analyze and understand them by collecting data and extracting insights from the network behavior to reduce those risks. We introduce Tikuna, an open-source tool for monitoring and detecting potential attacks on the Ethereum blockchain network at an early stage. Tikuna employs an unsupervised Long Short-Term Memory (LSTM) method based on Recurrent Neural Networks (RNNs) for anomaly detection to find attacks on the P2P layer. Empirical results indicate that the proposed approach significantly improves detection performance, with the ability to detect and classify attacks, including Eclipse attacks, Covert Flash attacks, and others that target the Ethereum blockchain P2P network layer, with high accuracy.

Our project aimed to implement Tikuna, a proof-of-concept P2P network security monitoring system for the Ethereum blockchain. With Tikuna, we aim to enhance the visibility of the status of the P2P network. The project is composed of three primary deliverables as follows:

1. Development of an open-source P2P monitoring solution accessible to the EF community.
2. Creation of dashboards to visualize different monitoring aspects of the P2P network.
3. A draft research paper to present the scientific findings of our Tikuna approach.

Tikuna, the first project in Latin America to get academic research funding from the Ethereum Foundation, has created a novel strategy to increase awareness of the P2P network's security state. We are proud to contribute to advancing blockchain safety and enhancing the Ethereum blockchain's security. To learn more about Tikuna, [visit our website](https://tikuna.io) [[19]](/docs/research/references).

### Phase I roadmap

<div className="roadmapImageBlog"></div>

## Meaningful findings

We introduce three main contributions:

* Our proposed machine learning anomaly detection approach can detect several attacks at the Ethereum P2P layer using peer event trace data in a simulation environment using the protocol labs’ framework testground.

* We demonstrate how to detect eclipse attacks in a mainnet node by extracting custom-generated connection log data from the Ethereum client Prysm and utilizing an LSTM neural network.

* We developed a custom exploit implementing a real-world eclipse attack. It was tested against a modified Prysm client in mainnet, so it did not forward spam to the network. With this, we could test the effectiveness of our approach.

Our team's initial step was to conduct in-depth research and analysis to gain a thorough understanding of the various existing P2P security approaches, i.e., state of the art techniques. Based on this, we developed a comprehensive plan of action outlining our Tikuna approach and methodology.

Subsequently, we proceeded to implement an LSTM based approach for Ethereum blockchain network security monitoring and anomaly detection. Additionally, our team developed and implemented three dashboards aimed at enhancing P2P security. These dashboards are the Ethereum P2P Network Status dashboard, the Beacon Node Monitor, and the Eclipse Attacks Dashboard.

Finally, throughout the development process, we rigorously tested our approach to ensure that it was functional. We also conducted several experiments in two distinct network environments, i.e., the simulated testground and the Ethereum mainnet, to thoroughly evaluate the effectiveness as well as the performance of the Tikuna approach.

The following is a sample of the training data used for Tikuna in the Ethereum mainnet, consisting of discovery connection data (UDP) from honest and simulated attacking peers. The normal data was collected from several nodes during 3 days under regular operation, and the malicious data was gathered from a single victim Ethereum node, using our developed exploit. Each line has several input features, including timestamp, IP, and Port removed from the peer table, IP and Port added to the peer table, and bucket where the peer is added.

<div className="trainingImageBlog"></div>

### The model and simulations

We have used RNNs for our research.  They are a type of model frequently utilized for processing sequential data such as time series. These models are specialized for processing a sequence of values that are a function of time. RNNs can scale to long sequences that would not be practical for networks without sequence-based specialization. Most recurrent networks can also process sequences of variable length. 

One of these models is especially of interest to this research. The long short-term memory model (LSTM) uses a gating mechanism to ensure proper information propagation through many time steps. LSTM networks have a specific memory cell and can capture long-term dependencies in sequential data. LSTM are valuable tools for language modeling problems. LSTM networks are a version of recurrent neural networks useful for long interrelated sequences of data. LSTM was chosen in this research for anomaly detection to find malicious discovery connections to an Ethereum client.

Following there is an example of the ML model output for mainnet where we obtained the best results detecting eclipse attacks, with 1’000,000 regular connection log lines for training and around 3,000 lines of eclipse attack logs for evaluation:

```bash
2023-03-06 18:52:07,641 P7 INFO Epoch 84/100, training loss: 1.98741
2023-03-06 18:52:07,661 P7 INFO Evaluating test data.
2023-03-06 18:52:18,910 P7 INFO Finish inference. Show iteration top-k results:
2023-03-06 18:52:19,272 P7 INFO {'f1': '0.847', 'Recall': '0.883', 'Precision': '0.813', 'Accuracy': '0.866'}
2023-03-06 18:52:19,284 P7 INFO {'f1': '0.804', 'Recall': '0.757', 'Precision': '0.858', 'Accuracy': '0.846'}
2023-03-06 18:52:19,296 P7 INFO {'f1': '0.740', 'Recall': '0.645', 'Precision': '0.868', 'Accuracy': '0.811'}
2023-03-06 18:52:19,308 P7 INFO {'f1': '0.704', 'Recall': '0.588', 'Precision': '0.879', 'Accuracy': '0.794'}
2023-03-06 18:52:19,320 P7 INFO {'f1': '0.683', 'Recall': '0.554', 'Precision': '0.889', 'Accuracy': '0.785'}
```

We used standard measures metrics for intrusion detection with ML, such as f1, recall, precision, and accuracy. Please review the Github repository and stay tuned for our research paper publication if you want more details.

## Dashboards

As part of our research, our team considered it important to demonstrate the results we obtained as well as a possible implementation. To achieve this, we created three Grafana dashboards that are integrated with Prometheus. These dashboards capture monitoring metrics and display the behavior of the P2P network, neighborhood, and Prysm node in real-time.

* **Ethereum P2P Network Status:** The information that is displayed on the Ethereum P2P Network Status dashboard comes from our Prysm node and is obtained by monitoring the port 8080. It gives data on the neighborhood area as well as how this node interacts with the other nodes in the blockchain. This comprises the number of connected peers, the current and head slot, the various types of P2P libraries that are linked to our node together with their ratings, as well as information on the participation rate and network liveness of the P2P network. In addition to this, it provides information concerning validators, such as their total numbers, the status of their accounts, and the average amount of ether in their balances.

<div className="dashboardp2pstatus"></div>
<p align="center">Fig. 1 The Ethereum P2P network status dashboard</p>

* **Beacon Node Monitor:**  This dashboard belongs to the infrastructure of our own Ethereum node, which displays information such as the use of CPU, RAM, disk space, bandwidth within the network, and details about storage space. This information was retrieved from the Kubernetes cluster that serves as the host for the consensus node, which is the infrastructure in our particular instance.

<div className="dashboardBeacoNode"></div>
<p align="center">Fig. 2 The beacon node monitor dashboard</p>

* **Eclipse Attacks Dashboard:** The creation of the final dashboard required the development of an interface that could record the potential eclipse attacks discovered by our machine learning algorithm and then input those records into the AlertManager component of Prometheus. After that, Grafana creates a table that displays a row for each identified eclipse attack in a given node.

<div className="dashboardEclipseAttacks"></div>
<p align="center">Fig. 3 The eclipse attacks dashboard</p>

At Tikuna, we believe that making a more secure and reliable P2P network requires accessibility and transparency, which is why we have developed a comprehensive User section for our proof-of-concept. Our User section offers detailed instructions and tutorials that guide users of all technical levels through the installation process and explain how to interpret the information presented in the dashboards. With Tikuna, a wider audience can benefit from our P2P monitoring system. We are proud to contribute to advancing blockchain security through our innovative ideas and commitment to user-friendly solutions. To learn more about Tikuna and how to use our monitoring system, [visit our website](https://tikuna.io) [[19]](/docs/research/references) and browse through our User section.

## The research paper

We are currently working on a draft research paper that is based on the findings and results obtained during this research grant. Once we receive feedback from EF, we intend to submit the research paper to an International Conference. The research paper is organized into five main chapters.
The first chapter is an introduction to the Ethereum blockchain, which emphasizes the importance of understanding the risks associated with P2P blockchain networks and developing security-focused solutions to ensure their reliability. It also highlights the three main contributions of the paper, which include a proposed machine learning approach for detecting attacks in the P2P layer, a method for detecting eclipse attacks using custom-generated connection log data and LSTM neural networks, and a custom exploit for eclipse attack testing against a modified Prysm client in mainnet. The second chapter, titled "Related Work", provides an overview of the most recent works that address the security challenges of the Ethereum blockchain P2P networks. The third chapter introduces the Tikuna approach by describing each of the three steps and discussing the various types of blockchain P2P network attacks. The fourth chapter evaluates the effectiveness of the Tikuna approach using a simulation and mainnet connection dataset. The last chapter presents a summary of the proposed work, conclusions, and potential future research directions. Finally, the authors acknowledge that the work presented was supported by the Ethereum Foundation Academic Research Grants.

## Next steps

We take immense pride in our team's accomplishments, and we extend our gratitude to everyone who played a part in ensuring the project's success. Our team's expertise, dedication, and collaborative ethos were crucial to delivering the first phase of the Tikuna project.
This is just the beginning of our project as we aim to further develop Tikuna as a tool to contribute to the Ethereum community and other Blockchains. Our efforts will be focused on identifying additional attacks, minimizing false positives, detecting real-world incidents, and incorporating different Blockchain (including Ethereum) node clients. Moreover, we intend to investigate other areas of research where Tikuna can be utilized, such as Maximal Extractable Value (MEV).

**We have applied for the second round of the EF academic research grants. Please see our application [here](https://docs.google.com/document/d/1CwbYBc0wa0eMh9erJv1lYXKrHHT5RlFGphr5PiV7yZ8/edit). If you are interested in learning more about Tikuna or working with us, we welcome the opportunity to collaborate with you. Kindly reach out to us, and we'll be happy to hear from you.**

Here you can find the Tikuna's full [source code](https://github.com/edenia/tikuna).