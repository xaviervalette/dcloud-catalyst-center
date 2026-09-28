---
title: "LAN Automation Demo Guide"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/lan_automation/
images: 27
links: 0
---

# LAN Automation Demo Guide

## Introduction

This guide provides a comprehensive overview and step-by-step instructions for utilizing Cisco's LAN Automation feature. LAN Automation is designed to simplify network operations by automating the deployment of new networks, freeing network administrators from time-consuming and repetitive configuration tasks. It ensures the creation of a standard, error-free Layer 3 routed access design by leveraging the IS-IS routing protocol. This document will walk you through initiating, managing, and stopping LAN Automation sessions for single and multiple sites.

## LAN Automation Workflow

### Step 1: Accessing LAN Automation

To begin, navigate to the LAN Automation feature from the main menu:
**Provision -> Network devices -> LAN automation.**

This page displays all currently running or previously configured LAN Automation sessions. If no sessions are active or configured, the page will appear empty. To start a new session, click the **"Start LAN automation"** button.

![Screenshot](../../images/provision/img/lan_automation-image001.jpg)

![Screenshot](../../images/provision/img/lan_automation-image003.jpg)

![Screenshot](../../images/provision/img/lan_automation-image005.jpg)

### Step 2: Selecting a Seed Device

In this step, you will select a seed device for your LAN Automation session. This is done by choosing a specific site or floor that contains network devices. For example, in the screenshot below, "London 1" is selected as the site, and "1st floor" is one of the floors within that building. The page will display the network devices assigned to the selected floor.

![Screenshot](../../images/provision/img/lan_automation-image007.jpg)

![Screenshot](../../images/provision/img/lan_automation-image009.jpg)

### Step 3: Selecting Device Interfaces

Once the primary seed device is selected, you must choose the interfaces that will be used for LAN Automation. Click on **"Select Interfaces"** to open a pop-up window displaying the device's available interfaces.

![Screenshot](../../images/provision/img/lan_automation-image011.jpg)

![Screenshot](../../images/provision/img/lan_automation-image013.jpg)

### Step 4: Adding Interfaces

From the interface list, select the interfaces with an "up" status. You can add an interface by clicking the **"plus"** symbol next to its name or by double-clicking the interface name. Selected interfaces will move to the right-side window. You can remove interfaces from the right-side window if needed. You can add multiple interfaces.

For this demo, select interfaces 37 and 38 from the list. After selecting the desired interfaces, click the **"Select"** button in the pop-up window.

![Screenshot](../../images/provision/img/lan_automation-image015.jpg)

![Screenshot](../../images/provision/img/lan_automation-image017.jpg)

### Step 5: Proceed to Next Step

After selecting the interfaces, click the **"Next"** button to continue.

![Screenshot](../../images/provision/img/lan_automation-image019.jpg)

### Step 6: Selecting the Principal IP Address Pool

On this screen, you need to select the Principal IP address pool. Choose the building that contains the relevant IP address pool; for instance, we are selecting the "London 1" building in this example. Once selected, click the **"Review"** button.

![Screenshot](../../images/provision/img/lan_automation-image021.jpg)

### Step 7: Review and Start Automation

The review screen summarizes all the options you have selected in the previous steps. Carefully review these settings. Once you have confirmed that all selections are correct, click the **"Start"** button at the bottom of the page to initiate LAN Automation.

![Screenshot](../../images/provision/img/lan_automation-image023.jpg)

![Screenshot](../../images/provision/img/lan_automation-image025.jpg)

### Step 8: Monitoring LAN Automation Progress

After starting LAN Automation, you will be redirected to the main LAN Automation page. Here, you will see a dashlet indicating the status of your session. Initially, it will be in an "Initialized" state, signifying that LAN Automation is in progress. Within a few seconds, the dashlet's status will update to "Seed Provisioned," then "In Progress," and finally "Completed" as the automation progresses.

![Screenshot](../../images/provision/img/lan_automation-image027.jpg)

### Step 9: Starting LAN Automation for Multiple Sites

You can initiate LAN Automation for multiple sites simultaneously. To start another session, for example, for the "San Jose" site, click **"Start LAN Automation"** again.

The process for the second site is identical to the first:
\* Select the appropriate floor containing devices for the San Jose site.
\* Select the interfaces of the chosen device.
\* Select the IP address pool associated with the San Jose site.

![Screenshot](../../images/provision/img/lan_automation-image029.jpg)

### Step 10: San Jose Site - Device Selection

![Screenshot](../../images/provision/img/lan_automation-image031.jpg)

### Step 11: San Jose Site - Interface Selection

![Screenshot](../../images/provision/img/lan_automation-image033.jpg)

### Step 12: San Jose Site - Interface Confirmation

![Screenshot](../../images/provision/img/lan_automation-image035.jpg)

### Step 13: San Jose Site - IP Pool Selection

![Screenshot](../../images/provision/img/lan_automation-image037.jpg)

### Step 14: Viewing LAN Automation Sessions and Devices

Once both LAN Automation sessions (e.g., London and San Jose) have been started, you can view their details in the sessions table on the main LAN Automation page.

![Screenshot](../../images/provision/img/lan_automation-image039.jpg)

Additionally, the "LAN automated devices" tab provides further insights. This tab includes sub-tabs for "Seed devices," "Provision," "Discovered," and "Error," allowing you to monitor the status of devices involved in the automation process.

![Screenshot](../../images/provision/img/lan_automation-image041.jpg)

![Screenshot](../../images/provision/img/lan_automation-image043.jpg)

![Screenshot](../../images/provision/img/lan_automation-image045.jpg)

![Screenshot](../../images/provision/img/lan_automation-image047.jpg)

### Step 15: Stopping LAN Automation

To stop an active LAN Automation session, click the **"Stop LAN automation"** link within the corresponding dashlet. After a short period, that particular dashlet will disappear from the page, indicating the session has been terminated.

![Screenshot](../../images/provision/img/lan_automation-image049.jpg)

![Screenshot](../../images/provision/img/lan_automation-image051.jpg)

![Screenshot](../../images/provision/img/lan_automation-image053.jpg)
