---
title: "Cisco Assurance: Peer Comparison Demo Guide"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/peer-compare/
images: 17
links: 0
---

# Cisco Assurance: Peer Comparison Demo Guide

**Introduction**

This guide provides a comprehensive walkthrough of the Peer Comparison feature within Cisco Assurance. Designed for network administrators and demo users, this feature allows you to effectively analyze and benchmark your network's performance against similar environments. By leveraging detailed Key Performance Indicator (KPI) filters, you can gain actionable insights to enhance network reliability, optimize user experience, and proactively address potential issues.

Throughout this guide, you will learn how to:
\* Navigate to the Peer Comparison dashboard.
\* Apply and interpret various KPI filters.
\* Utilize comparative metrics to identify trends and anomalies.

Let's begin exploring how to maximize the value of Cisco Assurance's Peer Comparison capabilities.

## Peer Comparison Walkthrough

### Step 1: Navigate to Peer Comparison Dashboard

To access the Peer Comparison feature:

- From the Cisco Assurance platform, follow this navigation path:
  `Assurance -> Peer Comparison`
- This action will open the Peer Comparison dashboard, where you can begin assessing your network's performance relative to peer environments.

![Screenshot](../../images/assurance/img/peer-compare-image001.png)

### Step 2: Using KPI Filters for Comparative Analysis

The Peer Comparison dashboard is equipped with several Key Performance Indicator (KPI) filters, enabling you to focus on specific aspects of network health and performance. For each selected KPI, you can view comparative metrics, identify performance trends, and spot anomalies across your network and peer networks.

To use the filters:

- Select the desired KPI from the dropdown list available on the Peer Comparison dashboard.

Below is an overview of each available KPI and how it can be utilized for effective comparative analysis:

---

#### KPI: RSSI (Received Signal Strength Indicator)

- **Purpose:** To compare the signal strength received by client devices across your network and peer networks.
- **Usage:** Apply the RSSI filter to identify areas with weak wireless coverage or potential connectivity issues. The dashboard visualizes signal distribution, helping you target improvements in wireless signal quality.

![Screenshot](../../images/assurance/img/peer-compare-image003.png)

![Screenshot](../../images/assurance/img/peer-compare-image005.png)

---

#### KPI: Cloud Apps Throughput

- **Purpose:** To analyze throughput and bandwidth usage specifically for cloud applications among your peers.
- **Usage:** Select this filter to benchmark cloud application performance, pinpoint potential bottlenecks, and ensure optimal bandwidth allocation for your critical cloud-based applications.

![Screenshot](../../images/assurance/img/peer-compare-image007.png)

![Screenshot](../../images/assurance/img/peer-compare-image009.png)

---

#### KPI: Interference

- **Purpose:** To assess and compare wireless interference levels that could degrade network quality.
- **Usage:** Use this KPI to detect sources of interference (such as neighboring networks or devices) and take proactive corrective measures to maintain signal integrity and improve network performance.

![Screenshot](../../images/assurance/img/peer-compare-image011.png)

![Screenshot](../../images/assurance/img/peer-compare-image013.png)

---

#### KPI: Onboarding Error Source

- **Purpose:** To identify the root causes of onboarding failures when client devices attempt to connect to the network.
- **Usage:** Filter by onboarding errors to uncover common issues preventing successful device connections and streamline troubleshooting processes for faster resolution.

![Screenshot](../../images/assurance/img/peer-compare-image015.png)

![Screenshot](../../images/assurance/img/peer-compare-image017.png)

---

#### KPI: Packet Failure Rate

- **Purpose:** To measure the rate of failed packets, which is crucial for evaluating overall network reliability.
- **Usage:** Analyze packet failure trends across your network and peer environments to detect reliability issues and take action to minimize data loss or retransmissions, ensuring a stable network.

![Screenshot](../../images/assurance/img/peer-compare-image019.png)

![Screenshot](../../images/assurance/img/peer-compare-image021.png)

---

#### KPI: Radio Resets

- **Purpose:** To monitor occurrences of radio resets, events that can significantly impact wireless stability and client connectivity.
- **Usage:** Track and compare radio reset events to identify problematic access points or recurring patterns that require further investigation and remediation.

![Screenshot](../../images/assurance/img/peer-compare-image023.png)

![Screenshot](../../images/assurance/img/peer-compare-image025.png)

---

#### KPI: Radio Throughput

- **Purpose:** To review radio throughput statistics, ensuring optimal data transfer rates across your wireless network.
- **Usage:** Use this filter to verify if wireless radios are delivering expected throughput and benchmark their performance against peer networks to identify areas for optimization.

![Screenshot](../../images/assurance/img/peer-compare-image027.png)

![Screenshot](../../images/assurance/img/peer-compare-image029.png)

---

#### KPI: Roaming Error Source

- **Purpose:** To analyze the specific causes of errors encountered during client roaming between access points.
- **Usage:** Compare roaming error sources to enhance seamless mobility for users and reduce disruptions as they move across different network areas, improving overall user experience.

![Screenshot](../../images/assurance/img/peer-compare-image031.png)

![Screenshot](../../images/assurance/img/peer-compare-image033.png)
