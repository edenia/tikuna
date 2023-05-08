---
slug: the-power-of-mev
title: "El poder del MEV: Por qué el Máximo Valor Extraíble (MEV) es el Game-Changer en DeFi"
authors: [andres, francis, loui]
---
---

El término "Valor máximo extraíble (MEV)", se refiere a la cantidad máxima de valor que un validador puede extraer de una cadena de bloques basada en proof-of-stake (PoS), o un minero en una cadena de bloques basada en proof-of-work (PoW), durante el proceso de producción de un bloque. Esto se puede lograr incluyendo, excluyendo o reorganizando el orden de las transacciones. De acuerdo a la estadística proporcionada por MEV-Explore [[22]](/docs/research/references), a continuación, el valor total de MEV que se puede extraer de Ethereum antes del cambio de PoW a PoS, y hasta septiembre de 2022 es de alrededor de $676 millones. En 2019 los autores en [[23]](/docs/research/references) fueron los primeros en mostrar los comportamientos de los mineros que podrían generar ganancias fuera de las tarifas de transacción y las recompensas por bloque de minería, es decir, el denominado MEV.

<div className="blogGrosProfit"></div>

Consideremos el ejemplo simplificado que se muestra en la figura a continuación para ilustrar cómo funciona MEV en la cadena de bloques de Ethereum, particularmente en el contexto de intercambios descentralizados (DEX) como Uniswap. Imagine que Alice quiere comprar una moneda digital específica en Uniswap usando Ethereum.

<div className="blogMev"></div>

Cuando Alice envía su transacción de compra, un validador en la red, que también posee una gran cantidad de la misma moneda digital que Alice, puede ver todas las transacciones pendientes que esperan ser procesadas. El validador aprovecha la oportunidad de beneficiarse de la transacción de Alice reordenando las transacciones pendientes y colocando su propia transacción para vender la moneda digital antes de la compra de Alice. Esto hace que el precio de la moneda digital disminuya y la compra de Alice se ejecuta a un precio más bajo de lo esperado.

Una vez que se completa la compra de Alice, el validador vuelve a comprar la moneda digital a un precio más bajo y obtiene una ganancia de la diferencia en los precios de compra y venta de la moneda digital. Esto se llama arbitraje.

Este proceso de cambiar el orden de las transacciones que esperan ser procesadas para obtener una ganancia se llama MEV. Si bien esto puede parecer injusto, vale la pena señalar que MEV también puede incentivar a los validadores a procesar transacciones de manera más rápida y eficiente, lo que en última instancia beneficia a toda la red. Además, MEV puede manifestarse de varias maneras en diferentes redes y sitios web de blockchain [[23]](/docs/research/references). Los ataques de sándwich son un ejemplo en el que el usuario envía una transacción de intercambio al mempool con un deslizamiento non-zero lo que hace que el precio de un token fluctúe y cree una oportunidad de arbitraje. Otro ejemplo es la liquidación, que ocurre cuando una posición de deuda en la cadena queda subcolateralizada, lo que lleva a la venta forzosa de la garantía.

Finalmente, MEV se ha convertido en una preocupación apremiante en la cadena de bloques de Ethereum, ya que puede generar ventajas injustas para los validadores y otros participantes en la red. En respuesta, se han desarrollado varias iniciativas, como Flashbots [[24]](/docs/research/references), para mitigar el impacto de MEV y promover la transparencia y la equidad en el procesamiento de transacciones. Nuestros equipos en Sakundi [[21]](/docs/research/references) y Edenia [[20]](/docs/research/references) también investigan activamente MEV y se basan en la tecnología de monitoreo que desarrollamos en nuestro proyecto Tikuna [[19]](/docs/research/references), con el objetivo de ofrecer una mejor visibilidad del espacio MEV. En última instancia, estas iniciativas beneficiarán a los usuarios y al ecosistema blockchain en general.

En la próxima serie de publicaciones, exploraremos otros temas relacionados con MEV en el contexto de la tecnología blockchain. ¡Mantente sintonizado para más!

¿Tiene preguntas? Contáctenos hoy para obtener más información sobre nuestros servicios.