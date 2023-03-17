---
slug: tikuna-final-blogpost-fase1
title: "Anunciando la Entrega de Nuestro Proyecto Tikuna en la Fase de Prueba de Concepto"
authors: [andres, francis, loui]
---
---
¡Estamos encantados de anunciar la finalización de la primera fase de nuestro proyecto Tikuna! Después de meses de arduo trabajo, dedicación y colaboración, nos complace compartir los resultados de la primera ronda de la beca de investigación académica de la Fundación Ethereum (EF). Destacaremos los hitos de nuestro proyecto y examinaremos los hallazgos de nuestro equipo en este blog.

## Descripción General

La seguridad en blockchain se está volviendo cada vez más relevante en el ciberespacio actual y por eso es importante fortalecer la seguridad de cada capa de su arquitectura. Nuestro proyecto se centra en las capas más bajas del blockchain, en particular en la red P2P que permite que los nodos se comuniquen entre sí y compartan información. Esta capa es de vital importancia para cualquier blockchain, incluido Ethereum, debido a la naturaleza descentralizada de su arquitectura. No obstante, la capa de red P2P puede ser vulnerable a varios ataques, como una Denegación de Servicio Distribuida (DDoS), ataques de eclipse y ataques Sybil. En conclusión, esta capa es propensa a muchas amenazas heredadas de las redes P2P, y existe la necesidad de analizarlas y comprenderlas recopilando datos y extrayendo información del comportamiento de la red para reducir los riesgos asociados a estos ataques. Nosotros presentamos Tikuna, una herramienta de código abierto para monitorear y detectar posibles ataques a la red blockchain de Ethereum, en una etapa temprana del ataque. Tikuna usa un método de memoria a corto plazo no supervisado (LSTM por sus siglas en inglés), basado en redes neuronales recurrentes (RRN) para la detección de anomalías asociadas a posibles ataques en la red P2P. Los resultados empíricos obtenidos, indican que el algoritmo propuesto mejora significativamente el rendimiento de detección de ataques, con la capacidad de encontrarlos y clasificarlos, incluyendo ataques Eclipse, ataques Covert Flash y de otro tipo dirigidos a la capa P2P del blockchain Ethereum, con alta precisión.

Nuestro proyecto tenía como objetivo implementar Tikuna, una Prueba de Concepto, para un sistema de monitoreo de seguridad, del blockchain Ethereum. Con Tikuna nuestro objetivo era mejorar la visibilidad del estado de la red P2P. El proyecto se compone de tres entregables:

1. Desarrollo de una solución de monitoreo P2P de código abierto accesible para la comunidad de EF.
2. Creación de dashboards para visualizar diferentes aspectos de monitoreo de la red P2P.
3. El borrador de un paper de investigación para presentar los hallazgos científicos de nuestro proyecto Tikuna.

Tikuna, el primer proyecto en América Latina en obtener fondos de investigación académica de la Fundación Ethereum, ha creado una estrategia novedosa para aumentar la conciencia sobre el estado de seguridad de la red P2P. Estamos orgullosos de contribuir al avance de la seguridad del blockchain y mejorar la seguridad del blockchain de Ethereum. Para obtener más información sobre Tikuna, [visite nuestro sitio web](https://tikuna.io) [[19]](/docs/research/references).

### Roadmap de la Fase I

<div className="roadmapImageBlog"></div>

## Hallazgos significativos

Presentamos tres contribuciones principales:

* Nuestro algoritmo propuesto de detección de anomalías de aprendizaje automático, puede detectar varios ataques en la capa P2P de Ethereum utilizando datos de seguimiento de eventos de nodos en un entorno de simulación.

* Demostramos cómo detectar ataques de eclipse en un nodo en la red principal mediante la extracción de datos de registro de conexión generados de forma personalizada del cliente Ethereum Prysm y el uso de una red neuronal LSTM.

* Desarrollamos un exploit personalizado que implementa un ataque de eclipse en el mundo real. Se probó con un cliente Prysm modificado en la red principal, por lo que no reenvía spam a la red. Con esto, podríamos probar la efectividad de nuestro algoritmo.

El paso inicial de nuestro equipo fue realizar una investigación y un análisis en profundidad para obtener una comprensión completa de los diversos algoritmos de seguridad P2P existentes, es decir, el estado del arte. En base a esto, desarrollamos un plan de acción integral que describe nuestro algoritmo y metodología en el proyecto Tikuna.

Posteriormente, procedimos a implementar un algoritmo basado en LSTM para el monitoreo de la seguridad y la detección de anomalías de la red blockchain de Ethereum. Además, nuestro equipo desarrolló e implementó tres dashboards destinados a mejorar la seguridad de la red P2P. Estos dashboards son: el de estado de la red P2P de Ethereum, el dashboard para el monitoreo de nodos Beacon y el dashboard de ataques de Eclipse, los cuales describiremos más adelante.

Finalmente, a lo largo del proceso de desarrollo, probamos rigurosamente nuestro algoritmo para asegurarnos de que fuera funcional. También llevamos a cabo varios experimentos en dos entornos de red distintos: el ambiente de pruebas simulado y la red principal de Ethereum, para evaluar minuciosamente la eficacia y el rendimiento del algoritmo de Tikuna.

La siguiente es una muestra de los datos de entrenamiento utilizados para Tikuna en la red principal de Ethereum, que consta de datos de conexión de descubrimiento (UDP) de nodos atacantes normales y nodos atacantes simulados. Los datos normales se recopilaron de varios nodos durante 3 días en funcionamiento normal, y los datos maliciosos se recopilaron de un solo nodo Ethereum víctima del atacado simulado, utilizando nuestro exploit. Cada línea tiene varias funciones de entrada, incluida la marca de tiempo, la IP y el puerto eliminados de la tabla de nodos, la IP y el puerto agregados a la tabla de nodos y el bucket donde se agrega el nodo.

<div className="trainingImageBlog"></div>

### El model y las simulaciones

Nosotros hemos utilizado RNN's para nuestra investigación. Son un tipo de modelo frecuentemente utilizado para procesar datos secuenciales como series de tiempo. Estos modelos están especializados en procesar una secuencia de valores en función del tiempo. Los RNN's pueden escalar a largas secuencias que no serían prácticas para redes sin especialización basada en secuencias. La mayoría de las redes recurrentes también pueden procesar secuencias de longitud variable.

Uno de estos modelos es de especial interés para nuestra investigación. El modelo de memoria a corto plazo largo (LSTM) utiliza un mecanismo de puerta para garantizar la propagación adecuada de la información a través de muchas iteraciones en el tiempo. Las redes LSTM tienen una celda de memoria específica y pueden capturar dependencias a largo plazo en datos secuenciales. LSTM son herramientas valiosas para problemas de modelado de lenguaje. Las redes LSTM son una versión de las redes neuronales recurrentes útiles para largas secuencias de datos interrelacionadas. LSTM fue elegido en esta investigación para la detección de anomalías para encontrar conexiones maliciosas en la comunicación con otros nodos de un cliente de Ethereum.

A continuación se muestra un ejemplo de la salida del modelo de ML para la red principal donde obtuvimos los mejores resultados detectando ataques de eclipse, con 1’000,000 de líneas de registro de conexión normales para entrenamiento y alrededor de 3,000 líneas de registros de ataques de eclipse para su evaluación:

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

Nostros utilizamos métricas de medidas estándar para la detección de intrusiones con ML, como f1, recuperación, precisión y exactitud. Revise el repositorio de Github y esté atento a la publicación de nuestro borrador del paper de investigación si desea obtener más detalles.

## Dashboards

Como parte de nuestra investigación, nuestro equipo consideró importante mostrar los resultados obtenidos, así como una posible implementación. Para lograr esto, creamos tres dashboards de Grafana que están integrados con Prometheus. Estos dashboards capturan métricas de monitoreo y muestran el comportamiento de la red P2P, el vecindario y el nodo Prysm en tiempo real.

* **Estado de la red P2P Ethereum:** La información que se muestra en el dashboard del estado de la red P2P Ethereum proviene de nuestro nodo Prysm y se obtiene al monitorear el puerto 8080. Brinda datos sobre el vecindario de nuestro nodo y cómo este interactúa con los otros nodos del Blockchain. Este muestra la cantidad de pares conectados, el socket actual y el principal, los diversos tipos de bibliotecas P2P que están conectados a nuestro nodo junto con sus calificaciones, así como información sobre la tasa de participación y la vitalidad de la red P2P. Además de esto, brinda información sobre los nodos validadores, como su número total, el estado de sus cuentas y la cantidad promedio de ether en sus saldos.

<div className="dashboardp2pstatus"></div>
<p align="center">Img. 1 El dashboard del estado de la red P2P Ethereum</p>

* **Beacon Node Monitor:**  Este dashboard está relacionado a la infraestructura de nuestro nodo de consenso Prysm, muestra información como el uso de CPU, RAM, espacio en disco, consumo de ancho de banda y detalles sobre el comportamiento de los discos. Esta información se recuperó del clúster de Kubernetes que sirve como host para nuestro nodo de consenso, donde reside actualmente.

<div className="dashboardBeacoNode"></div>
<p align="center">Img. 2 El dashboard de monitoreo del nodo Beacon</p>

* **Eclipse Attacks Dashboard:** La creación del tablero final requirió el desarrollo de una interfaz que pudiera registrar los posibles ataques de eclipse descubiertos por nuestro algoritmo de aprendizaje automático y luego ingresar esos registros en el componente AlertManager de Prometheus. Después de eso, Grafana crea una tabla que muestra una fila para cada ataque de eclipse identificado en un nodo determinado.

<div className="dashboardEclipseAttacks"></div>
<p align="center">Img. 3 El dashboard de ataques de eclipse</p>

En Tikuna, creemos que hacer una red P2P más segura y confiable requiere accesibilidad y transparencia, por lo que hemos desarrollado una sección de usuario integral para nuestra prueba de concepto. Nuestra sección de usuario ofrece instrucciones detalladas y tutoriales que guían a los usuarios de todos los niveles técnicos a través del proceso de instalación y explican cómo interpretar la información presentada en los dashboards. Con Tikuna, una audiencia más amplia puede beneficiarse de nuestro sistema de monitoreo P2P. Estamos orgullosos de contribuir al avance de la seguridad de blockchain a través de nuestras ideas innovadoras y compromiso con soluciones fáciles de usar. Para obtener más información sobre Tikuna y cómo usar nuestro sistema de monitoreo, [visite nuestro sitio web](https://tikuna.io) [[19]](/docs/research/references) y navegue a través de nuestra sección de usuario.

## El borrador del paper de investigación

Actualmente estamos trabajando en un borrador de un paper de investigación que se basa en los hallazgos y resultados obtenidos durante nuestra investigación. Está previsto que el paper sea enviado a la Conferencia Internacional sobre Criptografía aplicada y seguridad de redes [[18]](/docs/research/references) en Kioto, Japan en Junio 19-22, 2023. The paper de investigación está organizado en cinco capítulos principales.
El primer capítulo es una introducción a la cadena de bloques de Ethereum, que enfatiza la importancia de comprender los riesgos asociados con las redes P2P de Blockchain y desarrollar soluciones centradas en la seguridad para garantizar su confiabilidad. También destaca las tres contribuciones principales del proyecto, que incluyen el algoritmo de aprendizaje automático propuesto para detectar ataques en la capa P2P, un método para detectar ataques de eclipse utilizando datos de registro de conexión generados de forma personalizada y redes neuronales LSTM, y un exploit personalizado para ejecutar ataques de eclipse. El segundo capítulo, titulado "Trabajos relacionados", ofrece una descripción general de los trabajos más recientes que abordan los desafíos de seguridad de las redes P2P de blockchain de Ethereum. El tercer capítulo presenta el algoritmo de Tikuna describiendo cada uno de los tres pasos y discutiendo los diversos tipos de ataques a la red P2P de blockchain. El cuarto capítulo evalúa la efectividad del algoritmo de Tikuna utilizando un conjunto de datos de simulación y de conexión a la red principal. El último capítulo presenta un resumen del trabajo propuesto, las conclusiones y las posibles direcciones futuras de investigación. Finalmente, los autores reconocen que el trabajo presentado fue apoyado por las becas de investigación del EF.

## Siguientes pasos

Nos enorgullecemos enormemente de los logros de nuestro equipo y extendemos nuestra gratitud a todos los que contribuyeron a garantizar el éxito del proyecto. La experiencia, la dedicación y el espíritu colaborativo de nuestro equipo fueron cruciales para entregar la primera fase del proyecto Tikuna.
Este es solo el comienzo de nuestro proyecto, ya que nuestro objetivo es desarrollar Tikuna como una herramienta para contribuir a la comunidad Ethereum y otras Blockchains. Nuestros esfuerzos se centrarán en identificar ataques adicionales, minimizar los falsos positivos, detectar incidentes del mundo real e incorporar diferentes clientes de nodos de Blockchain (incluido Ethereum). Además, tenemos la intención de investigar otras áreas donde se puede utilizar Tikuna, como el valor máximo extraíble (MEV).

**Hemos solicitado la segunda ronda de las becas de investigación académicas del EF. Consulte nuestra aplicación [aquí](https://docs.google.com/document/d/1CwbYBc0wa0eMh9erJv1lYXKrHHT5RlFGphr5PiV7yZ8/edit). Si está interesado en aprender más sobre Tikuna o trabajar con nosotros, agradecemos la oportunidad de colaborar con usted. Comuníquese con nosotros y estaremos encantados de saber de usted.**
