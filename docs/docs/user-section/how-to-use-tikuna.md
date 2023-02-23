---
id: how-to-use-tikuna
title: How to Use Tikuna
sidebar_label: How to Use Tikuna
description: Process install for Tikuna
keywords: [tikuna, ethereum, research grant]
hide_table_of_contents: true
custom_edit_url: null
---

---

## Before starting

* Install docker `https://docs.docker.com/engine/install/`. If you have previously installed Docker, verify it using the `docker --version` command and proceed to the next step.
* Create a local directory named `/data`; if this directory already exists, proceed to the next step.
* Copy the folders that contain the data to the `/data` directory created in the previous step.


## Installation

To run this project, install it locally using:
```bash
- $ git clone https://github.com/edenia/tikuna
- $ cd tikuna
- $ docker build -t tikuna:latest .
```

## Quick start

To begin using Tikuna, perform the steps below.

* Inside the Tikuna project directory, go to the `bin` folder and execute the following command to start a docker container:

  ```bash
     $ ./start_tikuna.sh
  ```
* Once inside the docker container execute the following command to launch a Jupyter Notebook session in which the machine learning algorithms can be executed using Ethereum data: 

  ```bash
     $ ./bin/start_jupyter_notebook.sh
  ```
* After executing the previous command, you only need to open a browser, and then copy & paste the displayed URL.

<div className="readmeUrlJupyter url"></div>

* In the web browser, navigate to the analysis folder, and then click over it.

<div className="readmeClickAnalisys click"></div>

* Click on testing_analysis_trace.ipynb file.

<div className="readmeClickScript script"></div>

* For each step, click the `Run` button and wait until the results are displayed on the screen.

<div className="readmeRunResults run"></div>