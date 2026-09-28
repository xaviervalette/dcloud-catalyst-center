---
title: "Wi-Fi 7 Demo Guide: Showcasing Advanced Wireless Capabilities"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/wifi7/
images: 29
links: 0
---

# Wi-Fi 7 Demo Guide: Showcasing Advanced Wireless Capabilities

## Introduction

This comprehensive demo guide provides a step-by-step walkthrough to showcase the key features of Wi-Fi 7 within the Cisco management interface. It focuses on demonstrating enhanced end-user device connectivity, efficient inventory management, and intuitive device topology visualization. Through user-focused scenarios, inventory exploration, and network health assurance tools, you will learn to highlight multi-band support, advanced device relationships, and the robust capabilities of Cisco's Wi-Fi 7 solutions. Screenshots are included throughout the guide to enhance understanding and facilitate your demonstration.

This guide covers three primary use cases:
\* **User 360 View:** Evaluate the connectivity and performance of devices associated with a specific user.
\* **Inventory Management:** Explore and manage Wi-Fi 7-enabled devices within your network.
\* **Device 360 Page & Physical Neighbor Topology:** Visualize device interactions and client distribution within your network.

---

## A) Use Case: Grace Smith (Wireless – User 360)

In this section, you will utilize the **User 360** feature to evaluate the connectivity and performance of devices associated with a sample user, Grace Smith. This provides a holistic view of the user's wireless experience across different devices and protocols, demonstrating Wi-Fi 7's impact on individual user performance.

### 1. Accessing User 360 for Grace Smith

**Step 1:** Open your Webex environment and navigate to the **Global Search** feature.

![Screenshot](../../images/assurance/img/wifi7-image001.png)

**Step 2:** Enter "Grace Smith" in the search bar.

**Step 3:** In the search results, locate and select the **User** section for Grace Smith. Click on the **User 360** button to access detailed insights into her device connections.

![Screenshot](../../images/assurance/img/wifi7-image003.png)

### 2. Reviewing Device Connectivity for Grace Smith's Devices

For each device owned by Grace Smith, follow the navigation path and review the key connectivity details to observe varying Wi-Fi protocols and frequencies in use.

#### A. Grace Smith – iPad

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-iPad`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 6
\* **Access Point:** CW9178I-LDN1-01
\* **Radio:** 1
\* **Frequency:** 5 GHz

![Screenshot](../../images/assurance/img/wifi7-image005.png)

![Screenshot](../../images/assurance/img/wifi7-image007.png)

#### B. Grace Smith – iPhone

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-iPhone`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 7
\* **Access Point:** CW9178I-LDN1-01
\* **Radios:** 0, 1, 3

![Screenshot](../../images/assurance/img/wifi7-image009.png)

![Screenshot](../../images/assurance/img/wifi7-image011.png)

#### C. Grace Smith – Galaxy

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-Galaxy`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 7
\* **Access Point:** CW9178I-LDN1-01
\* **Radios:** 0, 1, 3
\* **Frequencies:** 2.4 GHz, 5 GHz, 6 GHz

![Screenshot](../../images/assurance/img/wifi7-image013.png)

![Screenshot](../../images/assurance/img/wifi7-image015.png)

#### D. Grace Smith – MacBook Pro

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-MacBook Pro`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 7
\* **Access Point:** CW9178I-LDN1-01
\* **Radio:** 1
\* **Frequency:** 5 GHz

![Screenshot](../../images/assurance/img/wifi7-image017.png)

![Screenshot](../../images/assurance/img/wifi7-image020.png)

---

## B) Use Case: Inventory Management for Wi-Fi 7 Devices

This section demonstrates how to view and manage specific Wi-Fi 7 enabled devices within your network inventory, providing insights into their hardware, connectivity, and configuration settings.

![Screenshot](../../images/assurance/img/wifi7-image022.png)

### 1. Navigating to Device Inventory

To access the inventory details for your Wi-Fi 7 devices:

- **Path:** `Provision` → `Inventory` → `[Select Device]`
- From the Inventory dashboard, locate the following devices to view their details:
  - CW9178I-LDN1-01
  - CW9176I-LDN1-02
  - CW9178I-LDN1-03
  - CW9178I-LDN1-04

![Screenshot](../../images/assurance/img/wifi7-image024.png)

### 2. Viewing Individual Device Details

For each device listed above, follow these steps to access its specific information:

#### A. CW9178I-LDN1-01 Device Details

Click on the device name `CW9178I-LDN1-01`.

![Screenshot](../../images/assurance/img/wifi7-image026.png)

Select **View Device Details** to access hardware information, connectivity statistics, and configuration settings for this access point.

![Screenshot](../../images/assurance/img/wifi7-image028.png)

![Screenshot](../../images/assurance/img/wifi7-image030.png)

#### B. CW9176I-LDN1-02 Device Details

Click on the device name `CW9176I-LDN1-02` and select **View Device Details** to access its hardware information, connectivity statistics, and configuration settings.

![Screenshot](../../images/assurance/img/wifi7-image032.png)

![Screenshot](../../images/assurance/img/wifi7-image034.png)

#### C. CW9178I-LDN1-03 Device Details

Click on the device name `CW9178I-LDN1-03` and select **View Device Details** to access its hardware information, connectivity statistics, and configuration settings.

![Screenshot](../../images/assurance/img/wifi7-image036.png)

![Screenshot](../../images/assurance/img/wifi7-image038.png)

#### D. CW9178I-LDN1-04 Device Details

Click on the device name `CW9178I-LDN1-04` and select **View Device Details** to access its hardware information, connectivity statistics, and configuration settings.

![Screenshot](../../images/assurance/img/wifi7-image040.png)

![Screenshot](../../images/assurance/img/wifi7-image042.png)

---

## C) Use Case: Device 360 Page – Physical Neighbor Topology

This section guides you through visualizing the physical neighbor topology for a specific device, helping you analyze how devices and clients interact within your network and showcasing Wi-Fi 7's multi-band capabilities.

### 1. Accessing Device 360 and Physical Neighbor Topology

You have two options to access the Device 360 page for `CW9178I-LDN1-01`:

- **Option 1:** Navigate to `Assurance` → `Health` → `Network` → `Network Device Table`. From the table, select `CW9178I-LDN1-01`.
- **Option 2:** Use the `Global Search` feature to find `CW9178I-LDN1-01`, then open its Device 360 Page directly from the search results.

![Screenshot](../../images/assurance/img/wifi7-image044.png)

![Screenshot](../../images/assurance/img/wifi7-image046.png)

### 2. Analyzing Physical Neighbor Topology

Once on the Device 360 page, navigate to the **Physical Neighbor Topology** tab.

![Screenshot](../../images/assurance/img/wifi7-image048.png)

Observe the network map, which displays the `CW9178I-LDN1-01` device and its connected clients. This visualization helps you assess how Wi-Fi 7's multi-band capabilities and advanced client support impact network performance and client distribution across different frequency bands.

![Screenshot](../../images/assurance/img/wifi7-image050.png)

### 3. Client Distribution by Frequency

Within the Physical Neighbor Topology, examine the client distribution across different frequency bands:

#### A. 6 GHz Clients

This view includes 1 non-MLO (Multi-Link Operation) client and 2 clients utilizing MLO links on the 6 GHz band, highlighting Wi-Fi 7's advanced capabilities.

![Screenshot](../../images/assurance/img/wifi7-image053.png)

#### B. 5 GHz Clients

This view includes 1 non-MLO client and 2 clients utilizing MLO links on the 5 GHz band, demonstrating efficient client management across frequencies.

![Screenshot](../../images/assurance/img/wifi7-image055.png)

![Screenshot](../../images/assurance/img/wifi7-image057.png)

![Screenshot](../../images/assurance/img/wifi7-image059.png)
