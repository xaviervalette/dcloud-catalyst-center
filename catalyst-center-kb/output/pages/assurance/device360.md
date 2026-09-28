---
title: "Device 360 Overview"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/device360/
images: 29
links: 0
---

```
# Device 360
```

## Introduction

This guide provides a step-by-step walkthrough for navigating and utilizing the Device 360 Page within Cisco Assurance. You will learn how to access device-specific details, interpret health and event data, use diagnostic tools, and view device topologies. The instructions include visuals and detailed steps to ensure you can confidently demonstrate the Device 360 Page's functionality across various device types, such as routers, access points, core/distribution/access devices, and wireless controllers.

---

## Step 1: Accessing the Health Tab

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image001.png)

- From the Homepage, open the main menu.
- Navigate to **Assurance > Dashboards > Health** tab.

---

## Step 2: Opening the Network Tab

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image003.png)

- The Health tab opens by default to the **Overall** view.
- Click the **Network** tab to switch the view.

---

## Step 3: Navigating to the Device 360 Page

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image005.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image007.png)

- In the **Network** tab, scroll down to the network devices table to find the device details.
- Click the desired **device name** to open its Device 360 Page.
- Alternatively, use the **global search** for the device name, and access the Device 360 Page from the search results.

---

## Step 4: Viewing Device Health and Details

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image009.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image011.png)
![device360-image013](../../images/assurance/img/device360-image013.png)

- The Device 360 Page provides an overview graph showing the device health score, issues, events, and telemetry status over time.
- Hover over any interval on the graph to view detailed information about health score, system plane, data plane, and event details.
- Device basic details are displayed below the graph. Click **View All Details** to open a pop-up with comprehensive device information.

---

## Step 5: Exploring Physical Neighbor Topology

![device360-image015](../../images/assurance/img/device360-image015.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image017.png)

- The **Physical Neighbor Topology** section visualizes the device's connection topology.
- Clicking on any device within the topology displays its basic details.

---

## Step 6: Using the Event Viewer Tab

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image019.png)

- The **Event Viewer** tab lists events handled by the device, with associated timestamps.
- Selecting an event opens its details in a pop-up on the right.
- Click **Go to Global Event Viewer** to navigate to **Assurance > Dashboard > Issues and Events > Events**.

---

## Step 7: Reviewing Device Details by Device Type

### Routers

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image021.png)

- Shows **CPU**, **Memory**, and **Uptime** fields.

### Access Points

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image023.png)

- Displays device information, availability, CPU, memory, and an AP to WLC Connectivity Chart.

### Core, Distribution, and Access Devices

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image025.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image027.png)

- Shows **CPU**, **CPU Name**, **Memory**, **Reachability**, **Temperature**, and **Temperature Sensor Name**.

### Wireless Controllers

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image029.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image031.png)

- Includes fields for **Availability**, **HA Redundancy**, **Client Count**, **CPU**, **CPU Name**, **Memory**, **Reachability**, **Temperature**, **Temperature Sensor Name**, **Monitored AP Count**, and **AP Licenses**.

---

## Step 8: Using the Tools Tab for Access Points

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image033.png)

- Access Points feature an **Extra Tools** tab in Device 360.

---

## Step 9: Using the Ping Tool

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image035.png)

- Select **Tools > Ping**.
- The output will be displayed in the right-side tab.

---

## Step 10: Using the Trace Route Tool

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image037.png)

- Select **Tools > Trace Route**.
- The output will be displayed in the right-side tab.

---

## Step 11: AP Data Collection

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image039.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image041.png)

- Select **Tools > AP Data Collection**.
- This action opens a new tab displaying Wireless LAN Controller (WLC) details.

---

## Step 12: AP Reboot

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image043.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image045.png)

- Select **Tools > AP Reboot**.
- A pop-up will appear; click **Reboot**.
- An **In Progress** pop-up will display. Click **OK**.
- After some time, a **Success** message appears.

---

## Step 13: Radio Reset

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image047.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image049.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image051.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image053.png)

- Select **Tools > Radio Reset**.
- A pop-up appears; select the radio and click **Reset**.
- An **In Progress** pop-up will display.
- Once complete, a **Success** pop-up confirms the reset.

---

## Step 14: Flash LED

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image055.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/device360-image057.png)

- Select **Tools > Flash LED**.
- A pop-up appears; click **Enable**.
- A **Success** message will confirm the action.

---

**End of Guide**
