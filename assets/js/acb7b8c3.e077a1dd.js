"use strict";(self.webpackChunktikuna=self.webpackChunktikuna||[]).push([[274],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>p});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var d=r.createContext({}),l=function(e){var t=r.useContext(d),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},c=function(e){var t=l(e.components);return r.createElement(d.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},h=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,i=e.originalType,d=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),h=l(n),p=a,b=h["".concat(d,".").concat(p)]||h[p]||u[p]||i;return n?r.createElement(b,o(o({ref:t},c),{},{components:n})):r.createElement(b,o({ref:t},c))}));function p(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var i=n.length,o=new Array(i);o[0]=h;var s={};for(var d in t)hasOwnProperty.call(t,d)&&(s[d]=t[d]);s.originalType=e,s.mdxType="string"==typeof e?e:a,o[1]=s;for(var l=2;l<i;l++)o[l]=n[l];return r.createElement.apply(null,o)}return r.createElement.apply(null,n)}h.displayName="MDXCreateElement"},7078:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>d,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>s,toc:()=>l});var r=n(7462),a=(n(7294),n(3905));const i={id:"understanding-dashboards",title:"Understanding the data behind the Dashboards",sidebar_label:"Understanding the data behind the Dashboards",description:"Process install for Tikuna",keywords:["tikuna","ethereum","research grant"],hide_table_of_contents:!0,custom_edit_url:null},o=void 0,s={unversionedId:"user-section/understanding-dashboards",id:"user-section/understanding-dashboards",title:"Understanding the data behind the Dashboards",description:"Process install for Tikuna",source:"@site/docs/user-section/understanding-dashboards.md",sourceDirName:"user-section",slug:"/user-section/understanding-dashboards",permalink:"/docs/user-section/understanding-dashboards",draft:!1,editUrl:null,tags:[],version:"current",frontMatter:{id:"understanding-dashboards",title:"Understanding the data behind the Dashboards",sidebar_label:"Understanding the data behind the Dashboards",description:"Process install for Tikuna",keywords:["tikuna","ethereum","research grant"],hide_table_of_contents:!0,custom_edit_url:null},sidebar:"tutorialSidebar",previous:{title:"How to Use Tikuna",permalink:"/docs/user-section/how-to-use-tikuna"}},d={},l=[{value:"P2P Network status on ETH2:",id:"p2p-network-status-on-eth2",level:2},{value:"Peer Count:",id:"peer-count",level:3},{value:"Max inactivity:",id:"max-inactivity",level:3},{value:"Libp2p Peers pie chart:",id:"libp2p-peers-pie-chart",level:3},{value:"Libp2p Peers average scores:",id:"libp2p-peers-average-scores",level:3},{value:"Participation rate:",id:"participation-rate",level:3},{value:"Network Liveness:",id:"network-liveness",level:3},{value:"Epochs:",id:"epochs",level:3}],c={toc:l};function u(e){let{components:t,...n}=e;return(0,a.kt)("wrapper",(0,r.Z)({},c,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("hr",null),(0,a.kt)("h2",{id:"p2p-network-status-on-eth2"},"P2P Network status on ETH2:"),(0,a.kt)("p",null,"This dashboard shows all the important information contained historically inside the node. There is disposed of in two status: Neighborhood & Network."),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"The neighborhood status refers to how the own node is interacting with other nodes in the blockchain. It can be found important stats such as:")),(0,a.kt)("div",{className:"readmeStatusNeighborhood dashboard1"}),(0,a.kt)("h3",{id:"peer-count"},"Peer Count:"),(0,a.kt)("p",null,"How many other nodes in the beacon network the node itself is interacting with. "),(0,a.kt)("h3",{id:"max-inactivity"},"Max inactivity:"),(0,a.kt)("p",null,"Is a score that reflects the current inactivity of the validators."),(0,a.kt)("h3",{id:"libp2p-peers-pie-chart"},"Libp2p Peers pie chart:"),(0,a.kt)("p",null,"Shows how the agents are distributed among neighboring peers, which type of Libp2p client are using and what\u2019s the most used."),(0,a.kt)("h3",{id:"libp2p-peers-average-scores"},"Libp2p Peers average scores:"),(0,a.kt)("p",null,"The average score obtain in terms of the metrics and performance."),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"In the other hand, the network status shows a summarized data, measured by the own node, about the general aspects in the network status such as:")),(0,a.kt)("div",{className:"readmeStatusNetwork dashboard2"}),(0,a.kt)("h3",{id:"participation-rate"},"Participation rate:"),(0,a.kt)("p",null,"How many ETH Balances are attesting (validating) to the network."),(0,a.kt)("h3",{id:"network-liveness"},"Network Liveness:"),(0,a.kt)("p",null,"This metric expresses the distance between the current finalized epoch and the expected finalized epoch based on the genesis time."),(0,a.kt)("h3",{id:"epochs"},"Epochs:"),(0,a.kt)("p",null,"A period of time during which a specific set of chosen validators are responsible for creating new blocks and adding them to the blockchain."))}u.isMDXComponent=!0}}]);