import React from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import Translate from "@docusaurus/Translate";
import Layout from "@theme/Layout";
import Features from "@site/src/components/Features";

import styles from "./index.module.css";

const HomepageHero = () => {

  return (
    <header className={styles.heroBanner}>
      <div className={styles.content}>
        <div className={clsx("container", styles.container, )}>
          <div className={styles.image}></div>
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
      </div>
      <div className={clsx("container", styles.diagramContainer, )}>
        <div className={styles.subtitleDiagram}>
          <Translate>
            Here is how it works:
          </Translate>
        </div>
        <div className={styles.diagram}></div>
      </div>
    </header>
  );
};

const Home = () => {

  return (
    <Layout description="">
      <HomepageHero />
      <main>
        <Features />
      </main>
    </Layout>
  );
};

export default Home;
