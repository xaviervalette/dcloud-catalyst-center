---
title: "Cisco Assurance: Client 360 Page Demo Guide"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/client360/
images: 38
links: 0
---

# Cisco Assurance: Client 360 Page Demo Guide

This guide provides a comprehensive walkthrough of the Client 360 page within Cisco Assurance, a powerful tool designed to offer a holistic view of individual client health and performance. The Client 360 page consolidates critical information such as device health, issue details, event logs, and user data, enabling network administrators to efficiently monitor, troubleshoot, and understand client experiences. This document outlines the methods to access the Client 360 page and details the various sections and insights it provides.

## Accessing the Client 360 Page

There are two primary methods to navigate to the Client 360 page within Cisco Assurance:

### Method 1: Via Assurance Health Dashboard

1. Navigate to **Assurance > Health**.
   ![Screenshot](../../images/assurance/img/client360-image001.png)
2. From the Dashboard, select the **Client Tab**.
3. Locate the desired client in the client table and select it. This action will automatically redirect you to the Client 360 page for that specific client.
   ![Screenshot](../../images/assurance/img/client360-image003.png)
   ![Screenshot](../../images/assurance/img/client360-image005.png)

### Method 2: Using Global Search

1. Utilize the **Global search** bar, typically located at the top of the interface.
   ![Screenshot](../../images/assurance/img/client360-image007.png)
2. Enter the client's name into the search field.
   ![Screenshot](../../images/assurance/img/client360-image009.png)
3. From the search results, select the entry corresponding to the client's name (often labeled as "client 360"). This will redirect you to the Client 360 page.
   ![Screenshot](../../images/assurance/img/client360-image011.png)

## Client 360 Global Graph

Upon entering the Client 360 page, you will see a global graph providing an overview of the client's performance and activity. Hovering over specific points on this graph will display detailed information and metrics relevant to that particular time or event.
![Screenshot](../../images/assurance/img/client360-image013.png)

## Summary Dashlet

The Summary dashlet offers key insights into the client's onboarding, roaming, and connectivity status, providing a quick glance at their overall network experience.

![Screenshot](../../images/assurance/img/client360-image015.png)

### 1. Onboarding Details

This section displays details related to the client's onboarding process. Click "View Details" to access a more granular breakdown of onboarding events.
![Screenshot](../../images/assurance/img/client360-image017.png)

- **Event Viewer**: Provides a chronological log of events related to the client's onboarding.
  ![Screenshot](../../images/assurance/img/client360-image019.png)
- **Impact Analysis**: Shows the potential impact of specific onboarding events on the client's experience.
  ![Screenshot](../../images/assurance/img/client360-image021.png)
- **Correlation**: Helps in understanding the correlation between different onboarding events and their outcomes.
  ![Screenshot](../../images/assurance/img/client360-image023.png)

### 2. Roaming Details

This section covers the client's roaming activities, including transitions between access points. Click "View Details" to explore further.
![Screenshot](../../images/assurance/img/client360-image025.png)

- **Event Viewer**: Displays events specifically related to the client's roaming behavior.
  ![Screenshot](../../images/assurance/img/client360-image027.png)
- **Impact Analysis**: Assesses the impact of roaming events on the client's connectivity and performance.
  ![Screenshot](../../images/assurance/img/client360-image029.png)
- **Correlation**: Identifies correlations within roaming events to pinpoint potential issues or patterns.
  ![Screenshot](../../images/assurance/img/client360-image031.png)

### 3. Connectivity Details

This section provides insights into the client's network connectivity, including critical metrics like Signal-to-Noise Ratio (SNR) and Received Signal Strength Indicator (RSSI).

#### SNR (Signal-to-Noise Ratio)

Click "View Details" to access detailed SNR information, which is crucial for assessing signal quality.
![Screenshot](../../images/assurance/img/client360-image033.png)

- **Event Viewer**: Shows events related to SNR fluctuations and thresholds.
  ![Screenshot](../../images/assurance/img/client360-image035.png)
- **Impact Analysis**: Analyzes the impact of SNR levels on the client's connection stability and performance.
  ![Screenshot](../../images/assurance/img/client360-image037.png)
- **Correlation**: Helps correlate SNR data with other network events to diagnose connectivity issues.
  ![Screenshot](../../images/assurance/img/client360-image039.png)

#### RSSI (Received Signal Strength Indicator)

Click "View Details" to access detailed RSSI information, indicating the strength of the client's received signal.
![Screenshot](../../images/assurance/img/client360-image041.png)

- **Event Viewer**: Displays events related to RSSI levels and changes.
  ![Screenshot](../../images/assurance/img/client360-image043.png)
- **Impact Analysis**: Assesses the impact of RSSI levels on the client's connection quality.
  ![Screenshot](../../images/assurance/img/client360-image045.png)
- **Correlation**: Identifies correlations within RSSI data to understand signal strength patterns.
  ![Screenshot](../../images/assurance/img/client360-image047.png)

## Issue Dashlet

This dashlet highlights any active or historical issues associated with the selected client. If the client is currently experiencing or has recently experienced network-related problems, they will be prominently displayed here for quick identification and action.
![Screenshot](../../images/assurance/img/client360-image049.png)

## Onboarding Dashlet

The Onboarding dashlet provides a clear view of the client's current connection status, showing which SSID the client is connected to and the specific device being used.
![Screenshot](../../images/assurance/img/client360-image051.png)

Clicking the **"View device 360"** button will seamlessly redirect you to the Device 360 page, offering more detailed information about the client's device itself.
![Screenshot](../../images/assurance/img/client360-image053.png)
![Screenshot](../../images/assurance/img/client360-image055.png)

## Event Viewer

This dedicated section provides a comprehensive, filterable view of all events associated with the client. It offers a chronological log of activities, changes, and alerts, which is invaluable for detailed troubleshooting and auditing.
![Screenshot](../../images/assurance/img/client360-image057.png)

## Application Experience

This section provides insights into the client's application performance and overall experience, helping to identify if network issues are impacting specific applications.
![Screenshot](../../images/assurance/img/client360-image059.png)

## Detailed Information

The Detailed Information section is organized into four distinct tabs, each providing in-depth data about various aspects of the client's configuration and performance.

### Device Info

This tab displays comprehensive information about the client's device, including hardware details, operating system, and other relevant specifications.
![Screenshot](../../images/assurance/img/client360-image061.png)

### Connectivity

This tab provides detailed statistics and parameters related to the client's network connectivity, such as IP address, MAC address, and connection duration.
![Screenshot](../../images/assurance/img/client360-image063.png)

### RF (Radio Frequency)

This tab offers insights into the client's radio frequency performance and the surrounding RF environment, including channel utilization and interference levels.
![Screenshot](../../images/assurance/img/client360-image065.png)
![Screenshot](../../images/assurance/img/client360-image067.png)

### User Defined Network

This tab shows information related to any user-defined network configurations or policies applied to the client.
![Screenshot](../../images/assurance/img/client360-image069.png)

## Special Client Cases

Certain clients may display additional or specific information based on their characteristics or device type.

### Grace Smith - iPad

For the "Grace Smith-ipad" client, a unique downfall graph is displayed, illustrating specific performance trends or issues over time.
![Screenshot](../../images/assurance/img/client360-image071.png)

Additionally, for both "Grace Smith-ipad" and "Grace Smith Galaxy-S23" clients, detailed issue data is available within the Issue dashlet. For all other clients, this section will typically show "no data available."
![Screenshot](../../images/assurance/img/client360-image073.png)

### Grace Smith - iPad and Grace Smith - MacBook: iOS Analytics

For "Grace Smith-iPad" and "Grace Smith-MacBook" clients, an extra tab named **"IOS Analytics"** will be present under the Detailed Information section. This tab provides specific analytical data tailored for iOS devices, offering deeper insights into their performance and behavior.
![Screenshot](../../images/assurance/img/client360-image075.png)
