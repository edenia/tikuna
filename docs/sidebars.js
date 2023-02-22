const sidebars = {
  tutorialSidebar: [
    {
      type: "category",
      label: "Research",
      items: ["research/intro", "research/stateoftheart","research/references","research/glossary"],
    },
    {
      type: "category",
      label: "About",
      items: ["about/team", "about/sakundi", "about/edenia"],
    },
    {
      type: "category",
      label: "Monitoring",
      items: ["monitoring/network-eth2", "monitoring/beacon-node", "monitoring/eclipse-attacks"],
    },
    {
      type: "category",
      label: "User Section",
      items: ["user-section/how-to-use-tikuna", "user-section/understanding-dashboards"],
    },
  ],
};

module.exports = sidebars;
