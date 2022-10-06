import React from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Translate, { translate } from "@docusaurus/Translate";
import Layout from "@theme/Layout";
import Features from "@site/src/components/Features";

import styles from "./index.module.css";

const HomepageHero = () => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header className={styles.heroBanner}>
      <div className={clsx("container", styles.container)}>
        <img className={styles.image} src="img/tikuna-white-logo.png"></img>
        <h1 className={styles.subtitle}>
          <Translate>
            An AI-based Blockchain security monitoring system.
          </Translate>
        </h1>
        <div className={styles.buttons}>
          <Link
            className={clsx("button--lg", styles.buttonText)}
            to="/docs/research/intro"
          >
            <Translate>Project Intro</Translate>
          </Link>
        </div>
      </div>
    </header>
  );
};

const Home = () => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />"
    >
      <HomepageHero />
      <main>
        <Features />
      </main>
    </Layout>
  );
};

export default Home;
