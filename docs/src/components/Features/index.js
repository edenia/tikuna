import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";
import Link from "@docusaurus/Link";
import Translate from "@docusaurus/Translate";

const FeatureList = [
  {
    title: <Translate>Research</Translate>,
    Image: "img/first-card.webp",
    description: (
      <Translate>Take a look at the main purposes behind the project</Translate>
    ),
    link: "/docs/research/intro",
  },
  {
    title: <Translate>About Tikuna</Translate>,
    Image: "img/second-card.webp",
    description: (
      <Translate>Get to know about our team and involved companies</Translate>
    ),
    link: "/docs/about/team",
  },
  {
    title: <Translate>Blog</Translate>,
    Image: "img/third-card.webp",
    description: (
      <Translate>Go and read contents written by our team</Translate>
    ),
    link: "/blog",
  },
];

const Feature = ({ Image, title, description, link }) => (
  <div className={styles.cardWrapper}>
    <div className="text--center">
      <img className={styles.cardImage} src={Image} />
    </div>
    <div className={styles.cardBody}>
      <h2>{title}</h2>
      <div className={styles.cardDescription}>
        <p>{description}</p>
      </div>
      <div className={styles.buttonWrapper}>
        <button className={styles.cardButton}>
          <Link className={styles.cardText} to={link}>
            <Translate>Read more</Translate>
          </Link>
        </button>
      </div>
    </div>
  </div>
);

const Homepage = () => (
  <section className={styles.features}>
    <div className="container">
      <div>
        <div className={styles.cardsContainer}>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </div>
  </section>
);

export default Homepage;
