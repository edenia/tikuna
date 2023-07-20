"use strict";(self.webpackChunktikuna=self.webpackChunktikuna||[]).push([[51],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>m});var o=r(7294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,o,n=function(e,t){if(null==e)return{};var r,o,n={},i=Object.keys(e);for(o=0;o<i.length;o++)r=i[o],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(o=0;o<i.length;o++)r=i[o],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var l=o.createContext({}),s=function(e){var t=o.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},u=function(e){var t=s(e.components);return o.createElement(l.Provider,{value:t},e.children)},p="mdxType",h={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},d=o.forwardRef((function(e,t){var r=e.components,n=e.mdxType,i=e.originalType,l=e.parentName,u=c(e,["components","mdxType","originalType","parentName"]),p=s(r),d=n,m=p["".concat(l,".").concat(d)]||p[d]||h[d]||i;return r?o.createElement(m,a(a({ref:t},u),{},{components:r})):o.createElement(m,a({ref:t},u))}));function m(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=r.length,a=new Array(i);a[0]=d;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[p]="string"==typeof e?e:n,a[1]=c;for(var s=2;s<i;s++)a[s]=r[s];return o.createElement.apply(null,a)}return o.createElement.apply(null,r)}d.displayName="MDXCreateElement"},2279:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>a,default:()=>h,frontMatter:()=>i,metadata:()=>c,toc:()=>s});var o=r(7462),n=(r(7294),r(3905));const i={id:"intro",title:"Welcome to Tikuna",sidebar_label:"Project Intro",description:"Tikuna - an Ethereum blockchain network security monitoring system",keywords:["tikuna","ethereum","research grant"],hide_table_of_contents:!0,custom_edit_url:null},a=void 0,c={unversionedId:"research/intro",id:"research/intro",title:"Welcome to Tikuna",description:"Tikuna - an Ethereum blockchain network security monitoring system",source:"@site/docs/research/intro.md",sourceDirName:"research",slug:"/research/intro",permalink:"/docs/research/intro",draft:!1,editUrl:null,tags:[],version:"current",frontMatter:{id:"intro",title:"Welcome to Tikuna",sidebar_label:"Project Intro",description:"Tikuna - an Ethereum blockchain network security monitoring system",keywords:["tikuna","ethereum","research grant"],hide_table_of_contents:!0,custom_edit_url:null},sidebar:"tutorialSidebar",next:{title:"State of the Art",permalink:"/docs/research/stateoftheart"}},l={},s=[{value:"About the Project",id:"about-the-project",level:2},{value:"Project Purpose",id:"project-purpose",level:2},{value:"Project Roadmap",id:"project-roadmap",level:2}],u={toc:s},p="wrapper";function h(e){let{components:t,...r}=e;return(0,n.kt)(p,(0,o.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("hr",null),(0,n.kt)("p",null,"Tikuna, a proof-of-concept P2P network security monitoring system for the Ethereum blockchain. By leveraging Machine Learning techniques, it will extract security and performance insights for early detection of relevant incidents. Tikuna will bring improved visibility to the security state of the P2P network."),(0,n.kt)("h2",{id:"about-the-project"},"About the Project"),(0,n.kt)("p",null,"We will investigate how to apply Machine Learning algorithms to monitor the security of the Ethereum P2P network for early detection of a few specific attacks. We will develop Tikuna, a proof-of-concept tool (open source so that every user can use it) derived from such research, and will provide a scientific report based on the findings of applying the tool to the mainnet network. We will also provide a simple dashboard for the community to observe the insights that Tikuna provides. Additionally, we will create a draft of a scientific paper based on the research results."),(0,n.kt)("h2",{id:"project-purpose"},"Project Purpose"),(0,n.kt)("p",null,"Tikuna will help the Ethereum community to gain visibility on the status of the P2P network and be aware of potential attacks."),(0,n.kt)("p",null,"The overall goal of the project is to support the Ethereum community by providing them with an intelligent state of the art tool capable of collecting security-related information from the state of the P2P network and improve the network visibility by providing insights about its current state. Such measurable information and insights criteria can help us to measure the success of our approach by the number of identified incidents and the number of discovered insights. Therefore, our tool will play a major role in improving the overall Ethereum network security."),(0,n.kt)("h2",{id:"project-roadmap"},"Project Roadmap"),(0,n.kt)("div",{className:"roadmapImage"}))}h.isMDXComponent=!0}}]);