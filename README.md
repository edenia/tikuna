
<div align="center">
<a href="https://tikuna.io">
	<img src="/docs/static/img/tikuna-white-logo.png" width="400">
</a>



![](https://img.shields.io/github/license/edenia/tikuna) 
![](https://img.shields.io/badge/code%20style-standard-brightgreen.svg) 
![](https://img.shields.io/badge/%E2%9C%93-collaborative_etiquette-brightgreen.svg) 
![](https://img.shields.io/twitter/follow/edeniaweb3.svg?style=social&logo=twitter)
![](https://img.shields.io/twitter/follow/Sakundi_io.svg?style=social&logo=twitter) 
![](https://img.shields.io/github/forks/edenia/tikuna?style=social)
</div>

Tikuna, a proof-of-concept P2P network security monitoring system for the Ethereum blockchain. By leveraging Machine Learning techniques, it will extract security and performance insights for early detection of relevant incidents. Tikuna will bring improved visibility to the security state of the P2P network. 

## Table of Contents

* [About the Project](#about-the-project)
* [Project Purpose](#project-purpose)
* [Project Roadmap](#project-roadmap)
* [Installation](#installation)
* [Teck Stack](#teck-stack)
* [File Structure](#file-structure)
* [Project Status](#project-status)
* [Contributing](#contributing)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [About Sakundi](#about-sakundi) -->
<!-- * [About Edenia](#about-edenia) -->
* [License](#license)

## About the Project

We will investigate how to apply Machine Learning algorithms to monitor the security of the Ethereum P2P network for early detection of a few specific attacks. We will develop Tikuna, a proof-of-concept tool (open source so that every user can use it) derived from such research, and will provide a scientific report based on the findings of applying the tool to the mainnet network. We will also provide a simple dashboard for the community to observe the insights that Tikuna provides. Additionally, we will create a draft of a scientific paper based on the research results.

## Project Purpose

Tikuna will help the Ethereum community to gain visibility on the status of the P2P network and be aware of potential attacks.

The overall goal of the project is to support the Ethereum community by providing them with an intelligent state of the art tool capable of collecting security-related information from the state of the P2P network and improve the network visibility by providing insights about its current state. Such measurable information and insights criteria can help us to measure the success of our approach by the number of identified incidents and the number of discovered insights. Therefore, our tool will play a major role in improving the overall Ethereum network security.

## Project Roadmap

1. Research state of the art of Ethereum P2P network security.
2. Set up ETH nodes for collecting + analyzing data, defining ML algorithms & developing/adapting selected algorithms for data analysis.
3. Find insights from the data analysis to develop or adapt a dashboard and alerts.
4. Deliverables include a scientific report about the findings, open-source code of the developed security tools, and a proof-of-concept dashboard with security-related insights.

## Installation

To run this project, install it locally using:
```console
- $ git clone https://github.com/edenia/tikuna
- $ cd tikuna
- $ docker build -t tikuna:latest .
```

## Quick start
To start using tikuna, do the following:
* Inside the tikuna project directory execute the following command:
  ```console $ ./start_tikuna.sh ```
* This will start a docker container. Once inside the docker container run the next command:
  ```console $ ./start_jupyter_notebook.sh ```
* It will start a jupyter notebook instance where you will be able to run the machine learning algorithms over ethereum data.
  Just open your browser and go to localhost:8890

## Documentation

The documentation website [tikuna.io](https://tikuna.io) is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Build the documentation

- Clone this repo using `git clone https://github.com/edenia/tikuna.git`
- Move to the appropriate directory: `cd tikuna/docs`.
- Run `yarn` in order to install dependencies. At this point you can run `yarn start` to see the development website at http://localhost:3000.

## File Structure

This could help the reader understand the organization inside the project, for example:

```text title="file-structure"
/
├── docs/ ........................... Docusaurus Documentation Engine
│   ├── docs/ ....................... Markdown Documents
│   └── docusaurus.config.js ........ Docusaurus Configuration File
├── LICENSE ......................... License Agreement
└── README.md ....................... This File
```

## Contributing

If you want to make a contribution, please follow the next steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m '<type>(<scope>): <subject>'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please Read EOS Costa Rica's [Open Source Contributing Guidelines](https://guide.eoscostarica.io/docs/open-source-guidelines/) for more information about programming conventions.

If you find a bug, please report big and small bugs by [**opening an issue**](https://github.com/edenia/tikuna/issues/new/choose)

## Project Status

Project is: _in progress_

## Acknowledgements

The Tikuna team gratefully acknowledges that the work presented was supported by the Ethereum Foundation.

## Contact

Created by Tikuna team [@Tikuna team](https://tikuna.io/docs/about/team) - feel free to contact us!

### About Sakundi

<div align="center">

<a href="https://sakundi.io">
	<img src="/docs/static/img/sakundi-logo-light.png" width="300">
</a> 
<br/>

[![Twitter](https://img.shields.io/twitter/follow/Sakundi_io?style=for-the-badge)](https://twitter.com/Sakundi_io)
[![Discord](https://img.shields.io/discord/946500573677625344?color=black&label=Discord&logo=discord&logoColor=white&style=for-the-badge)](https://discord.gg/Ys5f6H9DFm)

</div>

Sakundi is a research-based Blockchain security and privacy organization. It offers security monitoring solutions for Blockchain organizations and distributed applications based on Artificial Intelligence tools.

[sakundi.io](https://sakundi.io)

### About Edenia

<div align="center">
	<a href="https://edenia.com">
		<img src="https://raw.githubusercontent.com/edenia/.github/master/.github/workflows/images/edenia-logo.png" width="300">
	</a>

[![Twitter](https://img.shields.io/twitter/follow/EdeniaWeb3?style=for-the-badge)](https://twitter.com/EdeniaWeb3)
[![Discord](https://img.shields.io/discord/946500573677625344?color=black&label=Discord&logo=discord&logoColor=white&style=for-the-badge)](https://discord.gg/YeGcF6QwhP)

</div>

Edenia runs independent blockchain infrastructure and develops web3 solutions. Our team of technology-agnostic builders has been operating since 1987, leveraging the newest technologies to make the internet safer, more efficient, and more transparent.

[edenia.com](https://edenia.com)

## License
This project is open source and available under the Apache License Version 2.0.


