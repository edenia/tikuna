---
id: stateoftheart
title: Estado del Arte
sidebar_label: Estado del Arte
description: Tikuna - an Ethereum blockchain network security monitoring system
keywords: [tikuna, ethereum, research grant]
hide_table_of_contents: true
custom_edit_url: null
---
Ethereum fue presentado formalmente por Vitalik Buterin en su whitepaper en 2014 [[2]](references.md) y lanzando en 2015; se considera una de las plataformas de blockchain de criptomonedas públicas de código abierto más conocidas que admite la funcionalidad de contratos inteligentes con Ether (ETH o Ξ) somo su criptomoneda nativa y Solidity como su lenguaje de programación. De acuerdo con [[1]](references.md), hubo un total de 105.58 millones de transacciones y 1.45 millones de contratos inteligentes creados en el primer cuarto (Q1) de 2022. Adicionalmente, sobre la capitalización de mercado, Ethereum es la segunda criptomoneda más grande después de Bitcoin, con al rededor de $234 billones en Agosto de 2022 [[3]](references.md).

Además, Ethereum permite a los desarrolladores crear aplicaciones descentralizadas (dApps) en diversos sectores, como las finanzas descentralizadas (DeFi) [[4]](references.md), juegos [[5,6]](references.md), tokens no fungibles (NFTs) [[7]](references.md), e Internet de las Cosas (IoT) [[10]](references.md) que se ejecutan en una red peer-to-peer (P2P), minimizando las posibilidades de fraude, censura, tiempo de inactividad o participación de terceros y haciéndolos más confiables. Además, la red principal pública de Ethereum acaba de pasar por una actualización significativa a Ethereum 2 (oficialmente después de cambiar el nombre llamado The Merge ($ETH) [[8, 9]](references.md)) para mejorar su rendimiento, eficiencia y escalabilidad.

Las blockchains tienen muchas capas, como la capa de consenso [[11-13]](references.md), capa de scripting, capa de red, or DApps, pero la que nos interesa es la capa de nivel más bajo, es decir, la red P2P que permite que los nodos se interconecten entre sí y compartan información, la cual es un componente de vital importancia para la blockchain Ethereum. La idea básica detrás de la red P2P es que un grupo de computadoras llamadas nodos se conectan para compartir datos sin necesidad de una computadora centralizada, es decir, todos los nodos de la red tienen las mismas capacidades sin tener ningún privilegio especial, como el que se usa en los sistemas de intercambio de archivos Napster, LimeWire y Gnutella.

La red peer-to-peer (P2P) es el componente fundamental que sirve como base para cualquier tecnología blockchain. Pero, al igual que otras formas de tecnología, las redes P2P pueden verse afectadas por una serie de problemas de seguridad. Los atacantes pueden explotar algunas de las vulnerabilidades de la red P2P, para llevar a cabo varios vectores de ataque en la  blockchain, como el ataque eclipse, ataque de mineria selfish, ataques Sybil, o ataques DDoS. Por esta razón, para abordar tanto los diferentes vectores de ataque en la plataforma Ethereum como las vulnerabilidades de seguridad de la red P2P, muchos investigadores han comenzado recientemente a enfocar su investigación en esta dirección.

A continuación se presentan algunos de los trabajos más recientes que abordan los desafíos de seguridad de las redes P2P de blockchain de Ethereum:

- Este paper [[14]](references.md) se enfoca generalmente en los problemas de seguridad de cada capa en la blockchain de Ethereum, como la capa de red, proporcionando un análisis en profundidad que cubre las siguientes tres áreas:

    1. Los potenciales ataques como el ataque eclipse y el ataque account hijacking.
    2. Las vulnerabilidades que conducen a estos, por ejemplo, la vulnerabilidad de creación de nodos ilimitados y la vulnerabilidad de conexiones entrantes sin límite.
    3. Los efectos de cada incidente, como el doble gasto o la denegación de servicio (DoS). 

 Además de ofrecer una visión general de la eficacia y las limitaciones de los Sistemas de Detección de Intrusos (IDS) existentes como técnica de defensa frente a estos ataques.

- Este paper [[15]](references.md) propone el protocolo GossipSub y sus dos componentes, la construcción de la malla y la función de puntuación. El GossipSub es un protocolo de mensajería que permite una transmisión de mensajes rápida y robusta en redes permisivas, como la capa de red de Ethereum 2.0, para hacerlo, por un lado, más seguro contra varios tipos de ataques (como el ataque Sybil, el ataque Eclipse y el ataque Cold Boot), y por otro lado, para facilitar una transmisión más rápida de los mensajes dentro del la red. Además, los autores describen algunas de las contramedidas que se presentan en el protocolo GossipSub, como el mantenimiento controlado de la malla, el grafting aportunista, y distribución adaptativa de los mensajes gossip. En conclusión, los escritores evalúan el protocolo GossipSub contra varios ataques y demuestran su resistencia a estos ataques.

- En este estudio [[16]](references.md), los autores primero destacan parte de la estructura de la red Eth2, el ecosistema de la red y los peligros potenciales que podría plantear. Además, los escritores investigan exhaustivamente la red P2P de la red principal Eth2 mediante el desarrollo de una herramienta de monitoreo llamada Armiarma. Esta herramienta consta de dos componentes, el rastreador Armiarma y el analizador Armiarma, para abordar la ausencia de información y la falta de información sobre el rendimiento del protocolo GossipSub y sus peers en la red principal Eth2. Adicional, se realizó un experimento para evaluar las capacidades del enfoque propuesto y se agrupó un análisis de los resultados obtenidos en las siguientes tres partes:
   1. Análisis de red Eth2.
   2. Interacción de clientes Eth2.
   3. Análisis de peers individuales

 Además, el análisis identifica varios problemas con la cadena Beacon de Eth2, incluido el alojamiento fisico geográfico de los validadores de Eth2. Finalmente, los autores concluyen que la red se está comportando de manera saludable; sin embargo, aún deben considerarse algunos temas relacionados con la descentralización.

- Esta investigación [[17]](references.md) analiza "los ataques eclipse" en la red P2P de Ethereum P2P. Un ataque eclipse es un ataque que permite a un atacante aislar un nodo dentro de la red P2P, al obtener el control completo del acceso a la información de un nodo o el control sobre todo lo que ve el nodo. Este ataque se analiza en el contexto de la red P2P de Ethereum. Los autores desarrollaron un modelo de detección de ataques eclipse llamado ETH-EDS que se dirige principalmente a la plataforma Ethereum. Este modelo utilizó la técnica de clasificación de bosques aleatorios para examinar los paquetes de datos normales y de ataque en la red. Los paquetes de datos recopilados incluían detalles como el tamaño de las etiquetas de los paquetes, la frecuencia con la que se accedía y el tiempo de acceso. Los hallazgos de los experimentos muestran que los nodos de red maliciosos podrían identificarse con un alto grado de precisión.