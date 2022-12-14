// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Blockchain Security Monitoring",
  tagline: "A P2P network security monitoring system for the Ethereum blockchain.",
  url: "https://tikuna.io",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "edenia", // Usually your GitHub org/user name.
  projectName: "tikuna", // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en", "es"],
    localeConfigs: {
      en: {
        label: "EN",
      },
      es: {
        label: "ES",
      },
    },
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          breadcrumbs: false,
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: "dark",
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      navbar: {
        logo: {
          alt: "Tikuna Logo",
          src: "/img/tikuna-light-logo.png",
          srcDark: "/img/tikuna-dark-logo.png"
        },
        items: [
          {
            type: "doc",
            docId: "research/intro",
            position: "left",
            label: "Research",
          },
          {
            type: "doc",
            docId: "about/team",
            position: "left",
            label: "About Tikuna",
          },
          {
            type: "doc",
            docId: "monitoring/beacon-node",
            position: "left",
            label: "Monitoring",
          },
          { to: "/blog", label: "Blog", position: "left" },
          {
            type: "localeDropdown",
            position: "right",
          },
        ],
        style: "primary",
      },
      footer: {
        style: "dark",
        links: [
          {
            items: [
              {
                html: `
                <a href="" target="_blank" rel="" aria-label="Tikuna Logo">
                  <div class="footer__logo" ><div/>
                </a>
              `
              }
            ],
          },
          {
            title: "Docs",
            items: [
              {
                label: "Research",
                to: "/docs/research/intro",
              },
              {
                label: "About Tikuna",
                to: "/docs/about/team",
              },
              {
                label: "Monitoring",
                to: "docs/monitoring/beacon-node",
              },
            ],
          },
          {
            title: "Tikuna Community",
            items: [
              {
                label: "GitHub",
                href: "https://github.com/edenia/tikuna",
              },
            ],
          },
          {
            title: "Edenia Community",
            items: [
              {
                label: "Discord",
                href: "https://discord.com/invite/YeGcF6QwhP",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/EdeniaWeb3",
              },
              {
                label: "LinkedIn",
                href: "https://www.linkedin.com/company/edeniaweb3/",
              },
            ],
          },
          {
            title: "Sakundi Community",
            items: [
              {
                label: "Discord",
                href: "https://discord.gg/Ys5f6H9DFm",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/Sakundi_io",
              },
              {
                label: "LinkedIn",
                href: "https://www.linkedin.com/company/sakundi/",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "Blog",
                to: "/blog",
              },
            ],
          },
        ],
        copyright: `Copyright ?? ${new Date().getFullYear()} Tikuna | Apache-2.0 Open Source License`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
      algolia: {
        appId: '2JIRYUNM5C',
        apiKey: '92706d89a3ac67750773ddb53a76193e',
        indexName: 'tikuna',
        contextualSearch: true,
        searchParameters: {},
        searchPagePath: 'search',
      },
    }),
};

module.exports = config;
