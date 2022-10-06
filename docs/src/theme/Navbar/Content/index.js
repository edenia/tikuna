import React, { useEffect, useState } from "react";
import { useThemeConfig } from "@docusaurus/theme-common";
import {
  splitNavbarItems,
  useNavbarMobileSidebar,
} from "@docusaurus/theme-common/internal";
import { useLocation } from "@docusaurus/router";
import NavbarItem from "@theme/NavbarItem";
import NavbarColorModeToggle from "@theme/Navbar/ColorModeToggle";
import SearchBar from "@theme/SearchBar";
import NavbarMobileSidebarToggle from "@theme/Navbar/MobileSidebar/Toggle";
import NavbarLogo from "@theme/Navbar/Logo";
import NavbarSearch from "@theme/Navbar/Search";
import clsx from "clsx";

import styles from "./styles.module.css";

const useNavbarItems = () => useThemeConfig().navbar.items;

const NavbarItems = ({ items }) => (
  <>
    {items.map((item, i) => (
      <NavbarItem {...item} key={i} />
    ))}
  </>
);

const NavbarContentLayout = ({ left, right }) => {
  const location = useLocation();
  const [showBackground, setBackground] = useState();

  const showNavbarColor = (pathname) => {
    setBackground(pathname === "docs");
  };

  useEffect(() => {
    showNavbarColor(location.pathname);
  }, [showBackground, location.pathname]);

  return (
    <div
      className={clsx("navbar__inner", styles.customNavbar, {
        [styles.showRedBackground]: showBackground,
        [styles.showTransparentBackground]: !showBackground,
      })}
    >
      <div className="navbar__items">{left}</div>
      <div className="navbar__items navbar__items--right">{right}</div>
    </div>
  );
};

const NavbarContent = () => {
  const mobileSidebar = useNavbarMobileSidebar();
  const items = useNavbarItems();
  const [leftItems, rightItems] = splitNavbarItems(items);
  const searchBarItem = items.find((item) => item.type === "search");

  return (
    <NavbarContentLayout
      left={
        <>
          {!mobileSidebar.disabled && <NavbarMobileSidebarToggle />}
          <NavbarLogo />
          <NavbarItems items={leftItems} />
        </>
      }
      right={
        <>
          <NavbarItems items={rightItems} />
          <NavbarColorModeToggle className={styles.colorModeToggle} />
          {!searchBarItem && (
            <NavbarSearch>
              <SearchBar />
            </NavbarSearch>
          )}
        </>
      }
    />
  );
};

export default NavbarContent;
