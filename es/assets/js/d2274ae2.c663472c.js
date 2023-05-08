"use strict";(self.webpackChunktikuna=self.webpackChunktikuna||[]).push([[970],{3905:(e,a,n)=>{n.d(a,{Zo:()=>d,kt:()=>m});var r=n(7294);function o(e,a,n){return a in e?Object.defineProperty(e,a,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[a]=n,e}function t(e,a){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);a&&(r=r.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var a=1;a<arguments.length;a++){var n=null!=arguments[a]?arguments[a]:{};a%2?t(Object(n),!0).forEach((function(a){o(e,a,n[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):t(Object(n)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(n,a))}))}return e}function s(e,a){if(null==e)return{};var n,r,o=function(e,a){if(null==e)return{};var n,r,o={},t=Object.keys(e);for(r=0;r<t.length;r++)n=t[r],a.indexOf(n)>=0||(o[n]=e[n]);return o}(e,a);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);for(r=0;r<t.length;r++)n=t[r],a.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=r.createContext({}),c=function(e){var a=r.useContext(l),n=a;return e&&(n="function"==typeof e?e(a):i(i({},a),e)),n},d=function(e){var a=c(e.components);return r.createElement(l.Provider,{value:a},e.children)},u={inlineCode:"code",wrapper:function(e){var a=e.children;return r.createElement(r.Fragment,{},a)}},p=r.forwardRef((function(e,a){var n=e.components,o=e.mdxType,t=e.originalType,l=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),p=c(n),m=o,f=p["".concat(l,".").concat(m)]||p[m]||u[m]||t;return n?r.createElement(f,i(i({ref:a},d),{},{components:n})):r.createElement(f,i({ref:a},d))}));function m(e,a){var n=arguments,o=a&&a.mdxType;if("string"==typeof e||o){var t=n.length,i=new Array(t);i[0]=p;var s={};for(var l in a)hasOwnProperty.call(a,l)&&(s[l]=a[l]);s.originalType=e,s.mdxType="string"==typeof e?e:o,i[1]=s;for(var c=2;c<t;c++)i[c]=n[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}p.displayName="MDXCreateElement"},9557:(e,a,n)=>{n.r(a),n.d(a,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>t,metadata:()=>s,toc:()=>c});var r=n(7462),o=(n(7294),n(3905));const t={slug:"the-power-of-mev",title:"El poder del MEV: Por qu\xe9 el M\xe1ximo Valor Extra\xedble (MEV) es el Game-Changer en DeFi",authors:["andres","francis","loui"]},i=void 0,s={permalink:"/es/blog/the-power-of-mev",source:"@site/i18n/es/docusaurus-plugin-content-blog/2023-05-08-the-power-of-mev.md",title:"El poder del MEV: Por qu\xe9 el M\xe1ximo Valor Extra\xedble (MEV) es el Game-Changer en DeFi",description:"---",date:"2023-05-08T00:00:00.000Z",formattedDate:"8 de mayo de 2023",tags:[],readingTime:3.06,hasTruncateMarker:!1,authors:[{name:"Andres Gomez Ramirez",title:"Doctor en ciberseguridad de la Universidad de Franksfurt y CERN. Investigador de seguridad en blockchain en Edenia. Co-Founder de Sakundi.",url:"https://www.linkedin.com/in/andres-gomez-ramirez-bb7226156/",imageURL:"https://tikuna.io/img/team/andres.jpeg",key:"andres"},{name:"Francis Gomez Ramirez",title:"Inform\xe1tico y especialista en gesti\xf3n de proyectos con amplia experiencia en la industria bancaria y fintech. Co-Founder de Sakundi.",url:"https://www.linkedin.com/in/francis-adrian-gomez-ramirez-599598138/",imageURL:"https://tikuna.io/img/team/francis.jpeg",key:"francis"},{name:"Loui Al Sardy",title:"Candidato a doctor en catedra en ingenieria de software en la Universidad de Erlangen-Nuremberg. Co-Founder de Sakundi.",url:"https://www.linkedin.com/in/loui-alsardy/",imageURL:"https://tikuna.io/img/team/loui.jpeg",key:"loui"}],frontMatter:{slug:"the-power-of-mev",title:"El poder del MEV: Por qu\xe9 el M\xe1ximo Valor Extra\xedble (MEV) es el Game-Changer en DeFi",authors:["andres","francis","loui"]},nextItem:{title:"Anunciando la Entrega de Nuestro Proyecto Tikuna en la Fase de Prueba de Concepto",permalink:"/es/blog/tikuna-final-blogpost-fase1"}},l={authorsImageUrls:[void 0,void 0,void 0]},c=[],d={toc:c};function u(e){let{components:a,...n}=e;return(0,o.kt)("wrapper",(0,r.Z)({},d,n,{components:a,mdxType:"MDXLayout"}),(0,o.kt)("hr",null),(0,o.kt)("p",null,'El t\xe9rmino "Valor m\xe1ximo extra\xedble (MEV)", se refiere a la cantidad m\xe1xima de valor que un validador puede extraer de una cadena de bloques basada en proof-of-stake (PoS), o un minero en una cadena de bloques basada en proof-of-work (PoW), durante el proceso de producci\xf3n de un bloque. Esto se puede lograr incluyendo, excluyendo o reorganizando el orden de las transacciones. De acuerdo a la estad\xedstica proporcionada por MEV-Explore ',(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[22]"),", a continuaci\xf3n, el valor total de MEV que se puede extraer de Ethereum antes del cambio de PoW a PoS, y hasta septiembre de 2022 es de alrededor de $676 millones. En 2019 los autores en ",(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[23]")," fueron los primeros en mostrar los comportamientos de los mineros que podr\xedan generar ganancias fuera de las tarifas de transacci\xf3n y las recompensas por bloque de miner\xeda, es decir, el denominado MEV."),(0,o.kt)("div",{className:"blogGrosProfit"}),(0,o.kt)("p",null,"Consideremos el ejemplo simplificado que se muestra en la figura a continuaci\xf3n para ilustrar c\xf3mo funciona MEV en la cadena de bloques de Ethereum, particularmente en el contexto de intercambios descentralizados (DEX) como Uniswap. Imagine que Alice quiere comprar una moneda digital espec\xedfica en Uniswap usando Ethereum."),(0,o.kt)("div",{className:"blogMev"}),(0,o.kt)("p",null,"Cuando Alice env\xeda su transacci\xf3n de compra, un validador en la red, que tambi\xe9n posee una gran cantidad de la misma moneda digital que Alice, puede ver todas las transacciones pendientes que esperan ser procesadas. El validador aprovecha la oportunidad de beneficiarse de la transacci\xf3n de Alice reordenando las transacciones pendientes y colocando su propia transacci\xf3n para vender la moneda digital antes de la compra de Alice. Esto hace que el precio de la moneda digital disminuya y la compra de Alice se ejecuta a un precio m\xe1s bajo de lo esperado."),(0,o.kt)("p",null,"Una vez que se completa la compra de Alice, el validador vuelve a comprar la moneda digital a un precio m\xe1s bajo y obtiene una ganancia de la diferencia en los precios de compra y venta de la moneda digital. Esto se llama arbitraje."),(0,o.kt)("p",null,"Este proceso de cambiar el orden de las transacciones que esperan ser procesadas para obtener una ganancia se llama MEV. Si bien esto puede parecer injusto, vale la pena se\xf1alar que MEV tambi\xe9n puede incentivar a los validadores a procesar transacciones de manera m\xe1s r\xe1pida y eficiente, lo que en \xfaltima instancia beneficia a toda la red. Adem\xe1s, MEV puede manifestarse de varias maneras en diferentes redes y sitios web de blockchain ",(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[23]"),". Los ataques de s\xe1ndwich son un ejemplo en el que el usuario env\xeda una transacci\xf3n de intercambio al mempool con un deslizamiento non-zero lo que hace que el precio de un token fluct\xfae y cree una oportunidad de arbitraje. Otro ejemplo es la liquidaci\xf3n, que ocurre cuando una posici\xf3n de deuda en la cadena queda subcolateralizada, lo que lleva a la venta forzosa de la garant\xeda."),(0,o.kt)("p",null,"Finalmente, MEV se ha convertido en una preocupaci\xf3n apremiante en la cadena de bloques de Ethereum, ya que puede generar ventajas injustas para los validadores y otros participantes en la red. En respuesta, se han desarrollado varias iniciativas, como Flashbots ",(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[24]"),", para mitigar el impacto de MEV y promover la transparencia y la equidad en el procesamiento de transacciones. Nuestros equipos en Sakundi ",(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[21]")," y Edenia ",(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[20]")," tambi\xe9n investigan activamente MEV y se basan en la tecnolog\xeda de monitoreo que desarrollamos en nuestro proyecto Tikuna ",(0,o.kt)("a",{parentName:"p",href:"/docs/research/references"},"[19]"),", con el objetivo de ofrecer una mejor visibilidad del espacio MEV. En \xfaltima instancia, estas iniciativas beneficiar\xe1n a los usuarios y al ecosistema blockchain en general."),(0,o.kt)("p",null,"En la pr\xf3xima serie de publicaciones, exploraremos otros temas relacionados con MEV en el contexto de la tecnolog\xeda blockchain. \xa1Mantente sintonizado para m\xe1s!"),(0,o.kt)("p",null,"\xbfTiene preguntas? Cont\xe1ctenos hoy para obtener m\xe1s informaci\xf3n sobre nuestros servicios."))}u.isMDXComponent=!0}}]);