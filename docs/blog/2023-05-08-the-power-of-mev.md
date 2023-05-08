---
slug: the-power-of-mev
title: "The power of MEV: Why Maximal Extractable Value (MEV) is a Game-Changer in DeFi"
authors: [andres, francis, loui]
---
---
The term "Maximal Extractable Value (MEV)" refers to the maximum amount of value that can be extracted from a blockchain by a validator in a proof-of-stake (PoS) blockchain or a miner in a proof-of-work (PoW) blockchain during the process of producing a block. This can be achieved by including, excluding, or rearranging the order of transactions. According to the statistic provided by MEV-Explore [[22]](/docs/research/references) below, the total worth of MEV that may be extracted from Ethereum prior to the merge and up until September 2022 is around $676 million. In 2019, the authors in [[23]](/docs/research/references) were the first to introduce the miners behaviours that could result in profits outside of transaction fees and mining block rewards, i.e., the so-called MEV.

<div className="blogGrosProfit"></div>

Let us consider the simplified example shown in the figure below to illustrate how MEV works on the Ethereum blockchain, particularly in the context of decentralized exchanges (DEX) like Uniswap. Imagine Alice wants to purchase a specific digital currency on Uniswap using Ethereum.

<div className="blogMev"></div>

When Alice submits her purchase transaction, a validator on the network, who also happens to own a large amount of the same digital currency as Alice, can see all the pending transactions waiting to be processed. The validator takes advantage of the opportunity to profit from Alice's transaction by reordering the pending transactions and placing their own transaction to sell the digital currency before Alice's purchase. This causes the price of the digital currency to decrease, and Alice's purchase executes at a lower price than expected.

Once Alice's purchase is complete, the validator buys back the digital currency at a lower price and makes a profit from the difference in the buy and sell prices of the digital currency. This is called arbitrage.

This process of changing the order of transactions waiting to be processed to make a profit is called MEV. While this may seem unfair, it's worth noting that MEV can also incentivize validators to process transactions more quickly and efficiently, ultimately benefiting the entire network. Moreover, MEV can manifest itself in various ways on different blockchain networks and websites [[23]](/docs/research/references). Sandwich attacks are one example where a user sends a swap transaction to the general mempool with a non-zero slippage, causing the price of a token to fluctuate and creating an arbitrage opportunity. Another example is liquidation, which happens when a debt position on the chain becomes undercollateralized, leading to the forced sale of the collateral.

Finally, MEV has become a pressing concern on the Ethereum blockchain, as it can result in unfair advantages for validators and other participants in the network. In response, various initiatives, such as Flashbots [[24]](/docs/research/references), have been developed to mitigate MEV's impact and promote transparency and fairness in transaction processing. Our teams at Sakundi [[21]](/docs/research/references) and Edenia [[20]](/docs/research/references) are also actively researching MEV and building upon the previous monitoring technology we developed in our Tikuna project [[19]](/docs/research/references), with the goal of offering better visibility into the MEV space. Ultimately, these initiatives will benefit users and the blockchain ecosystem as a whole.

In the upcoming series of posts, we will be exploring other topics related to MEV in the context of blockchain technology. Stay tuned for more!

Have questions? Contact us today to find out more about our services.