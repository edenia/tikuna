---
id: understanding-dashboards
title: Entendiendo la data detrás de los Dashboards
sidebar_label: Entendiendo la data detrás de los Dashboards
description: Process install for Tikuna
keywords: [tikuna, ethereum, research grant]
hide_table_of_contents: true
custom_edit_url: null
---

---

## P2P Network status on ETH2:

Este dashboard muestra toda la información importante almacenada historicamente dentro del nodo de consenso. Esta dividido en dos categorías: Neighborhood y Network.

* El "neighborhood status" hace referencia a como el nodo de consenso está interactuando con otros nodos dentro de la red de blockchain. Se pueden encontrar estadísticas importantes como:

<div className="readmeStatusNeighborhood dashboard1"></div>

### Peer Count:  

Con cuantos nodos de la red, esta interactuando nuestro nodo beacon. 

### Max inactivity: 

Es una puntuación que refleja la inactividad actual de los validadores.

### Libp2p Peers pie chart: 

Muestra cómo se distribuyen los agentes entre los pares vecinos, qué tipo de cliente Libp2p están usando y cuál es el más usado.
 
### Libp2p Peers average scores: 

La puntuación media obtenida en cuanto a las métricas y el rendimiento.

* Por otro lado, el estado de la red muestra datos resumidos, medidos por el propio nodo, sobre los aspectos generales en el estado de la red tales como:

<div className="readmeStatusNetwork dashboard2"></div>

### Participation rate: 

Cuántos saldos de ETH se están certificando (validando) en la red.

### Network Liveness: 

This metric expresses the distance between the current finalized epoch and the expected finalized epoch based on the genesis time.

### Epochs:  

Esta métrica expresa la distancia entre el epoch finalizado actual y el epoch finalizado esperado en función del tiempo del epoch génesis.