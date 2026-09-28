---
title: "Network Settings – Servers Tab"
section: design
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/server_settings/
images: 8
links: 0
---

# Network Settings – Servers Tab

## Introduction

This demo guide provides step-by-step instructions for navigating and configuring network server settings in the **Design > Network Settings > Servers** tab. You will learn how to view and manage global and site-specific credentials, search and select sites, and configure essential network server features such as AAA, DHCP, DNS, SFTP, NTP, Stealthwatch Flow Destination, Time Zone, and Message of the Day. Screenshots are included to illustrate each step and enhance understanding.

---

## Step 1: Accessing Network Settings

From the Homepage menu, navigate to **Design > Network Settings**.

![Screenshot](../../images/design/img/server_settings-image001.png)

---

## Step 2: Viewing the Servers Tab

By default, the **Network Settings** page opens to the **Servers** tab.

> **Note:** In previous versions, this tab was named **Network**.

![Screenshot](../../images/design/img/server_settings-image003.png)

When the page opens, the global site credentials are displayed.

---

## Step 3: Viewing Site Credentials

On the left side of the page, select any site to view its specific credentials.

![Screenshot](../../images/design/img/server_settings-image005.png)

---

## Step 4: Searching and Selecting Sites

Use the search panel to find and select the desired sites quickly.

![Screenshot](../../images/design/img/server_settings-image007.png)

---

## Step 5: Configuring External Network Servers

- In the **AAA** tab, you can configure external network servers or endpoints.

![Screenshot](../../images/design/img/server_settings-image009.png)

- In the **DHCP** tab, specify one or more dedicated DHCP servers to manage client device networking configuration.

---

## Step 6: Configuring DNS, Image Distribution, and NTP

- In the **DNS** tab, configure your network’s domain name and specify DNS servers for hostname resolution.

![Screenshot](../../images/design/img/server_settings-image011.png)
![Screenshot](../../images/design/img/server_settings-image012.png)

- In the **Image Distribution** tab, select SFTP servers to act as image distribution servers.

  > Using a distributed SWIM architecture with strategically located SFTP servers helps support large-scale device software image upgrades and conserves WAN bandwidth.
- In the **NTP** tab, specify one or more NTP servers to facilitate system clock synchronization for your network.
- In the **Stealthwatch Flow Destination** tab, set the flow destination used to provision SSA on this site.

---

## Step 7: Time Zone and Message of the Day Configuration

- In the **Time Zone** tab, select the time zone that matches the physical location of the site.
  > The site time zone is used when scheduling device provisioning and updates.

![Screenshot](../../images/design/img/server_settings-image013.png)

- In the **Message of the Day** tab, customize the message that appears during login to routers, switches, and hubs.

---

## Summary

This guide covered how to navigate the **Servers** tab in Network Settings, view and manage site credentials, search for sites, and configure critical network server features including AAA, DHCP, DNS, SFTP, NTP, flow destinations, time zones, and the Message of the Day. For more details, refer to the screenshots provided at each step.

---
