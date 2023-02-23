---
id: how-to-use-tikuna
title: Cómo usar Tikuna
sidebar_label: Cómo usar Tikuna
description: Proceso de instalación para Tikuna
keywords: [tikuna, ethereum, research grant]
hide_table_of_contents: true
custom_edit_url: null
---

---

## Antes de empezar

* Instalar docker `https://docs.docker.com/engine/install/`. Si ya tiene previamente instalado docker, verifiquelo usando el comando `docker --version` y continue con el siguiente paso.
* Crea un directorio local llamado `/data`; si este directorio ya existe localmente, continue con el siguiente paso.
* Copie los directorios que contienen la información al directorio `/data` creado en el paso anterior.


## Instalación

Para correr este proyecto, instalelo localmente usando:
```bash
- $ git clone https://github.com/edenia/tikuna
- $ cd tikuna
- $ docker build -t tikuna:latest .
```

## Inicio rápido

Para empezar a usar Tikuna, ejecute los pasos descrito a continuación.

* Dentro del directorio del proyecto Tikuna, vaya a la carpeta `bin` y ejecute el siguiente comando para iniciar un contenedor de docker:

  ```bash
     $ ./start_tikuna.sh
  ```
* Dentro del contenedor de docker ejecute el siguiente comando para lanzar una sesión de Jupyter Notebook en donde los algoritmos de machine learning pueden ser ejecutados usando la data de Ethereum: 

  ```bash
     $ ./bin/start_jupyter_notebook.sh
  ```
* Después de ejecutar el comando anterior, usted solo necesita abrir su navegador, y luego copie y pegue la url mostrada en pantalla.

<div className="readmeUrlJupyter url"></div>

* En el navegador, vaya hasta el directorio analysis, y luego haga click sobre él.

<div className="readmeClickAnalisys click"></div>

* Click sobre el archivo ethereum_lstm_log.ipynb.

<div className="readmeClickScript script"></div>

* Por cada paso, haga click sobre el botón `Run` y espere hasta que los resultados empiecen a ser mostrados en pantalla.

<div className="readmeRunResults run"></div>