"use strict";(self.webpackChunktikuna=self.webpackChunktikuna||[]).push([[349],{3905:(e,t,a)=>{a.d(t,{Zo:()=>h,kt:()=>m});var n=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var c=n.createContext({}),l=function(e){var t=n.useContext(c),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},h=function(e){var t=l(e.components);return n.createElement(c.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},p=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,o=e.originalType,c=e.parentName,h=s(e,["components","mdxType","originalType","parentName"]),u=l(a),p=r,m=u["".concat(c,".").concat(p)]||u[p]||d[p]||o;return a?n.createElement(m,i(i({ref:t},h),{},{components:a})):n.createElement(m,i({ref:t},h))}));function m(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=a.length,i=new Array(o);i[0]=p;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s[u]="string"==typeof e?e:r,i[1]=s;for(var l=2;l<o;l++)i[l]=a[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}p.displayName="MDXCreateElement"},5255:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>d,frontMatter:()=>o,metadata:()=>s,toc:()=>l});var n=a(7462),r=(a(7294),a(3905));const o={slug:"tikuna-final-blogpost-fase1",title:"Marking the Delivery of our Tikuna Project Proof-Of-Concept Phase",authors:["andres","francis","loui"]},i=void 0,s={permalink:"/blog/tikuna-final-blogpost-fase1",source:"@site/blog/2023-03-17-tikuna-final-blogpost-fase1.md",title:"Marking the Delivery of our Tikuna Project Proof-Of-Concept Phase",description:"---",date:"2023-03-17T00:00:00.000Z",formattedDate:"March 17, 2023",tags:[],readingTime:9.635,hasTruncateMarker:!1,authors:[{name:"Andres Gomez Ramirez",title:"Ph.D. in cybersecurity from the University of Frankfurt and CERN. A blockchain security researcher at Edenia. Co-Founder at Sakundi.",url:"https://www.linkedin.com/in/andres-gomez-ramirez-bb7226156/",imageURL:"https://tikuna.io/img/team/andres.jpeg",key:"andres"},{name:"Francis Gomez Ramirez",title:"Computer scientist and specialist in project management with wide experience in banking industry and fintech. Co-Founder at Sakundi.",url:"https://www.linkedin.com/in/francis-adrian-gomez-ramirez-599598138/",imageURL:"https://tikuna.io/img/team/francis.jpeg",key:"francis"},{name:"Loui Al Sardy",title:"Ph.D. candidate at Chair of Software Engineering at the University of Erlangen-Nuremberg. Co-Founder at Sakundi.",url:"https://www.linkedin.com/in/loui-alsardy/",imageURL:"https://tikuna.io/img/team/loui.jpeg",key:"loui"}],frontMatter:{slug:"tikuna-final-blogpost-fase1",title:"Marking the Delivery of our Tikuna Project Proof-Of-Concept Phase",authors:["andres","francis","loui"]},prevItem:{title:"The power of MEV: Why Maximal Extractable Value (MEV) is a Game-Changer in DeFi",permalink:"/blog/the-power-of-mev"},nextItem:{title:"Tikuna - Our contribution to security on the blockchain",permalink:"/blog/tikuna-contribution"}},c={authorsImageUrls:[void 0,void 0,void 0]},l=[{value:"Overview",id:"overview",level:2},{value:"Phase I roadmap",id:"phase-i-roadmap",level:3},{value:"Meaningful findings",id:"meaningful-findings",level:2},{value:"The model and simulations",id:"the-model-and-simulations",level:3},{value:"Dashboards",id:"dashboards",level:2},{value:"The research paper",id:"the-research-paper",level:2},{value:"Next steps",id:"next-steps",level:2}],h={toc:l},u="wrapper";function d(e){let{components:t,...a}=e;return(0,r.kt)(u,(0,n.Z)({},h,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("hr",null),(0,r.kt)("p",null,"We are thrilled to announce the completion of the first phase of our Tikuna project! After months of hard work, dedication, and collaboration, we are excited to share the results of the first round of the Ethereum Foundation (EF) academic research grant. We will highlight our project's milestones and examine our team's findings in this blog post."),(0,r.kt)("h2",{id:"overview"},"Overview"),(0,r.kt)("p",null,"Blockchain security is becoming increasingly relevant in today's cyberspace, and it is essential to strengthening each layer's security in its architecture. Our project focuses on the lowest level layer in the blockchain, particularly the P2P network that allows the nodes to communicate with each other and share information. This layer is a vital component of any blockchain, including Ethereum, due to the decentralized nature of its architecture. However, the P2P network layer may be vulnerable to several attacks, such as a Distributed Denial of Service (DDoS), eclipse attacks, or Sybil attacks. Consequently, this layer is still prone to many threats inherited from P2P networks, and there is a need to analyze and understand them by collecting data and extracting insights from the network behavior to reduce those risks. We introduce Tikuna, an open-source tool for monitoring and detecting potential attacks on the Ethereum blockchain network at an early stage. Tikuna employs an unsupervised Long Short-Term Memory (LSTM) method based on Recurrent Neural Networks (RNNs) for anomaly detection to find attacks on the P2P layer. Empirical results indicate that the proposed approach significantly improves detection performance, with the ability to detect and classify attacks, including Eclipse attacks, Covert Flash attacks, and others that target the Ethereum blockchain P2P network layer, with high accuracy."),(0,r.kt)("p",null,"Our project aimed to implement Tikuna, a proof-of-concept P2P network security monitoring system for the Ethereum blockchain. With Tikuna, we aim to enhance the visibility of the status of the P2P network. The project is composed of three primary deliverables as follows:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Development of an open-source P2P monitoring solution accessible to the EF community."),(0,r.kt)("li",{parentName:"ol"},"Creation of dashboards to visualize different monitoring aspects of the P2P network."),(0,r.kt)("li",{parentName:"ol"},"A draft research paper to present the scientific findings of our Tikuna approach.")),(0,r.kt)("p",null,"Tikuna, the first project in Latin America to get academic research funding from the Ethereum Foundation, has created a novel strategy to increase awareness of the P2P network's security state. We are proud to contribute to advancing blockchain safety and enhancing the Ethereum blockchain's security. To learn more about Tikuna, ",(0,r.kt)("a",{parentName:"p",href:"https://tikuna.io"},"visit our website")," ",(0,r.kt)("a",{parentName:"p",href:"/docs/research/references"},"[19]"),"."),(0,r.kt)("h3",{id:"phase-i-roadmap"},"Phase I roadmap"),(0,r.kt)("div",{className:"roadmapImageBlog"}),(0,r.kt)("h2",{id:"meaningful-findings"},"Meaningful findings"),(0,r.kt)("p",null,"We introduce three main contributions:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Our proposed machine learning anomaly detection approach can detect several attacks at the Ethereum P2P layer using peer event trace data in a simulation environment using the protocol labs\u2019 framework testground.")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"We demonstrate how to detect eclipse attacks in a mainnet node by extracting custom-generated connection log data from the Ethereum client Prysm and utilizing an LSTM neural network.")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"We developed a custom exploit implementing a real-world eclipse attack. It was tested against a modified Prysm client in mainnet, so it did not forward spam to the network. With this, we could test the effectiveness of our approach."))),(0,r.kt)("p",null,"Our team's initial step was to conduct in-depth research and analysis to gain a thorough understanding of the various existing P2P security approaches, i.e., state of the art techniques. Based on this, we developed a comprehensive plan of action outlining our Tikuna approach and methodology."),(0,r.kt)("p",null,"Subsequently, we proceeded to implement an LSTM based approach for Ethereum blockchain network security monitoring and anomaly detection. Additionally, our team developed and implemented three dashboards aimed at enhancing P2P security. These dashboards are the Ethereum P2P Network Status dashboard, the Beacon Node Monitor, and the Eclipse Attacks Dashboard."),(0,r.kt)("p",null,"Finally, throughout the development process, we rigorously tested our approach to ensure that it was functional. We also conducted several experiments in two distinct network environments, i.e., the simulated testground and the Ethereum mainnet, to thoroughly evaluate the effectiveness as well as the performance of the Tikuna approach."),(0,r.kt)("p",null,"The following is a sample of the training data used for Tikuna in the Ethereum mainnet, consisting of discovery connection data (UDP) from honest and simulated attacking peers. The normal data was collected from several nodes during 3 days under regular operation, and the malicious data was gathered from a single victim Ethereum node, using our developed exploit. Each line has several input features, including timestamp, IP, and Port removed from the peer table, IP and Port added to the peer table, and bucket where the peer is added."),(0,r.kt)("div",{className:"trainingImageBlog"}),(0,r.kt)("h3",{id:"the-model-and-simulations"},"The model and simulations"),(0,r.kt)("p",null,"We have used RNNs for our research.  They are a type of model frequently utilized for processing sequential data such as time series. These models are specialized for processing a sequence of values that are a function of time. RNNs can scale to long sequences that would not be practical for networks without sequence-based specialization. Most recurrent networks can also process sequences of variable length. "),(0,r.kt)("p",null,"One of these models is especially of interest to this research. The long short-term memory model (LSTM) uses a gating mechanism to ensure proper information propagation through many time steps. LSTM networks have a specific memory cell and can capture long-term dependencies in sequential data. LSTM are valuable tools for language modeling problems. LSTM networks are a version of recurrent neural networks useful for long interrelated sequences of data. LSTM was chosen in this research for anomaly detection to find malicious discovery connections to an Ethereum client."),(0,r.kt)("p",null,"Following there is an example of the ML model output for mainnet where we obtained the best results detecting eclipse attacks, with 1\u2019000,000 regular connection log lines for training and around 3,000 lines of eclipse attack logs for evaluation:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-bash"},"2023-03-06 18:52:07,641 P7 INFO Epoch 84/100, training loss: 1.98741\n2023-03-06 18:52:07,661 P7 INFO Evaluating test data.\n2023-03-06 18:52:18,910 P7 INFO Finish inference. Show iteration top-k results:\n2023-03-06 18:52:19,272 P7 INFO {'f1': '0.847', 'Recall': '0.883', 'Precision': '0.813', 'Accuracy': '0.866'}\n2023-03-06 18:52:19,284 P7 INFO {'f1': '0.804', 'Recall': '0.757', 'Precision': '0.858', 'Accuracy': '0.846'}\n2023-03-06 18:52:19,296 P7 INFO {'f1': '0.740', 'Recall': '0.645', 'Precision': '0.868', 'Accuracy': '0.811'}\n2023-03-06 18:52:19,308 P7 INFO {'f1': '0.704', 'Recall': '0.588', 'Precision': '0.879', 'Accuracy': '0.794'}\n2023-03-06 18:52:19,320 P7 INFO {'f1': '0.683', 'Recall': '0.554', 'Precision': '0.889', 'Accuracy': '0.785'}\n")),(0,r.kt)("p",null,"We used standard measures metrics for intrusion detection with ML, such as f1, recall, precision, and accuracy. Please review the Github repository and stay tuned for our research paper publication if you want more details."),(0,r.kt)("h2",{id:"dashboards"},"Dashboards"),(0,r.kt)("p",null,"As part of our research, our team considered it important to demonstrate the results we obtained as well as a possible implementation. To achieve this, we created three Grafana dashboards that are integrated with Prometheus. These dashboards capture monitoring metrics and display the behavior of the P2P network, neighborhood, and Prysm node in real-time."),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Ethereum P2P Network Status:")," The information that is displayed on the Ethereum P2P Network Status dashboard comes from our Prysm node and is obtained by monitoring the port 8080. It gives data on the neighborhood area as well as how this node interacts with the other nodes in the blockchain. This comprises the number of connected peers, the current and head slot, the various types of P2P libraries that are linked to our node together with their ratings, as well as information on the participation rate and network liveness of the P2P network. In addition to this, it provides information concerning validators, such as their total numbers, the status of their accounts, and the average amount of ether in their balances.")),(0,r.kt)("div",{className:"dashboardp2pstatus"}),(0,r.kt)("p",{align:"center"},"Fig. 1 The Ethereum P2P network status dashboard"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Beacon Node Monitor:"),"  This dashboard belongs to the infrastructure of our own Ethereum node, which displays information such as the use of CPU, RAM, disk space, bandwidth within the network, and details about storage space. This information was retrieved from the Kubernetes cluster that serves as the host for the consensus node, which is the infrastructure in our particular instance.")),(0,r.kt)("div",{className:"dashboardBeacoNode"}),(0,r.kt)("p",{align:"center"},"Fig. 2 The beacon node monitor dashboard"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Eclipse Attacks Dashboard:")," The creation of the final dashboard required the development of an interface that could record the potential eclipse attacks discovered by our machine learning algorithm and then input those records into the AlertManager component of Prometheus. After that, Grafana creates a table that displays a row for each identified eclipse attack in a given node.")),(0,r.kt)("div",{className:"dashboardEclipseAttacks"}),(0,r.kt)("p",{align:"center"},"Fig. 3 The eclipse attacks dashboard"),(0,r.kt)("p",null,"At Tikuna, we believe that making a more secure and reliable P2P network requires accessibility and transparency, which is why we have developed a comprehensive User section for our proof-of-concept. Our User section offers detailed instructions and tutorials that guide users of all technical levels through the installation process and explain how to interpret the information presented in the dashboards. With Tikuna, a wider audience can benefit from our P2P monitoring system. We are proud to contribute to advancing blockchain security through our innovative ideas and commitment to user-friendly solutions. To learn more about Tikuna and how to use our monitoring system, ",(0,r.kt)("a",{parentName:"p",href:"https://tikuna.io"},"visit our website")," ",(0,r.kt)("a",{parentName:"p",href:"/docs/research/references"},"[19]")," and browse through our User section."),(0,r.kt)("h2",{id:"the-research-paper"},"The research paper"),(0,r.kt)("p",null,'We are currently working on a draft research paper that is based on the findings and results obtained during this research grant. Once we receive feedback from EF, we intend to submit the research paper to an International Conference. The research paper is organized into five main chapters.\nThe first chapter is an introduction to the Ethereum blockchain, which emphasizes the importance of understanding the risks associated with P2P blockchain networks and developing security-focused solutions to ensure their reliability. It also highlights the three main contributions of the paper, which include a proposed machine learning approach for detecting attacks in the P2P layer, a method for detecting eclipse attacks using custom-generated connection log data and LSTM neural networks, and a custom exploit for eclipse attack testing against a modified Prysm client in mainnet. The second chapter, titled "Related Work", provides an overview of the most recent works that address the security challenges of the Ethereum blockchain P2P networks. The third chapter introduces the Tikuna approach by describing each of the three steps and discussing the various types of blockchain P2P network attacks. The fourth chapter evaluates the effectiveness of the Tikuna approach using a simulation and mainnet connection dataset. The last chapter presents a summary of the proposed work, conclusions, and potential future research directions. Finally, the authors acknowledge that the work presented was supported by the Ethereum Foundation Academic Research Grants.'),(0,r.kt)("h2",{id:"next-steps"},"Next steps"),(0,r.kt)("p",null,"We take immense pride in our team's accomplishments, and we extend our gratitude to everyone who played a part in ensuring the project's success. Our team's expertise, dedication, and collaborative ethos were crucial to delivering the first phase of the Tikuna project.\nThis is just the beginning of our project as we aim to further develop Tikuna as a tool to contribute to the Ethereum community and other Blockchains. Our efforts will be focused on identifying additional attacks, minimizing false positives, detecting real-world incidents, and incorporating different Blockchain (including Ethereum) node clients. Moreover, we intend to investigate other areas of research where Tikuna can be utilized, such as Maximal Extractable Value (MEV)."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"We have applied for the second round of the EF academic research grants. Please see our application ",(0,r.kt)("a",{parentName:"strong",href:"https://docs.google.com/document/d/1CwbYBc0wa0eMh9erJv1lYXKrHHT5RlFGphr5PiV7yZ8/edit"},"here"),". If you are interested in learning more about Tikuna or working with us, we welcome the opportunity to collaborate with you. Kindly reach out to us, and we'll be happy to hear from you.")),(0,r.kt)("p",null,"Here you can find the Tikuna's full ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/edenia/tikuna"},"source code"),"."))}d.isMDXComponent=!0}}]);