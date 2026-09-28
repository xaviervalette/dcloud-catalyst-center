---
title: "AI-Driven Baseline Dashboard"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/baselines/
images: 15
links: 2
---

# AI-Driven Baseline Dashboard

## Introduction

Welcome to the AI-Driven Baseline Dashboard Demo Guide. This document will walk you through the key features and workflows of the Baseline Dashboard—a powerful tool designed to provide unparalleled visibility into your network’s performance. Using AI-driven analytics, the dashboard helps you identify problematic buildings, discover outliers, compare key performance indicators (KPIs), and perform deep dives to understand network impacts on clients and Access Points (APs).

In this lab, you will:

- Gain an overview of network performance across all buildings using beeswarm visualization.
- Identify interesting buildings based on AI-driven anomaly detection issues or outlier status.
- Compare expected versus actual behavior across multiple KPIs and WLANs.
- Drill into each entity and KPI to analyze the impact on clients and APs.

---

## Benefits

The Baseline Dashboard allows you to explore and analyze network performance by comparing expected and actual Wi-Fi KPI values across different buildings, SSIDs, and time periods.

Key benefits include:

- No manual configuration required—just ensure your devices are managed by the Cisco Catalyst Center appliance, are exporting telemetry data, and have Cisco AI Analytics enabled ([see Lab 8 - Service Operations](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/)).
- Extended visibility even when no anomalies are detected.
- Ability to identify both sudden changes (anomalies) and persistent behaviors.

*Note: This lab uses a pre-configured system, as baselines typically require about a week of data to become available.*

---

## Workflow Overview

The Baseline Dashboard workflow guides users through network data exploration, focusing on onboarding-related KPIs and their baselines:

- **Identify good, bad, or busy buildings at a glance.**
- **See the evolution of expected vs. actual KPI values** over time for an SSID within a building.
- **Compare baselines for different KPIs** for the same SSID within a selected building.
- **Compare baselines for the same KPI across different SSIDs** within a building.
- **Perform deeper analysis** using the detailed view.

---

## Getting Started

### Accessing the Baseline Dashboard

1. Open the [Baseline Dashboard Page](https://dcloud-dnac-inst-cl-lon.cisco.com/dna/assurance/trends/baselines):  
   **Menu > Assurance > AI Network Analytics > Baselines**
2. Follow the steps below to explore the dashboard.

![Baseline Dashboard - Menu item](../../images/assurance/img/baselines-image001.png)

---

### Time Selection

- By default, the dashboard displays data from the last 24 hours.
- To expand the time range, use the **Custom Range** selector.

![Baseline Dashboard default time selection](../../images/assurance/img/baselines-image002.png)
*Note: The end date selection is not available in the current version.*

---

## Building Overview and Selection

Get an overview of all buildings to select one for deeper investigation.

The default visualization is a **beeswarm plot**:

- Each circle represents a **building**.
- Circle size indicates average **client count** for the selected period—spot busy buildings easily.
- **Red circles**: At least one AI-driven issue detected in the time period.
- **Blue circles**: No issues detected.
- X-axis position: Average of the selected KPI (default is Onboarding Time), helping you spot good or bad performers.

![Baseline Dashboard Beeswarm view](../../images/assurance/img/baselines-image003.png)

### What Makes a Building "Interesting"?

Examples:

- **A busy building with good performance but marked in red:**  
  Example: *LONDON 1*
- Position: Left-hand side (average onboarding time < 2 seconds)
- Red color: At least one AI-driven issue reported

![Baseline Dashboard - Building with issues](../../images/assurance/img/baselines-image004.png)

- **A building with consistently bad performance but no issues:**  
  Example: *SAN FRANCISCO 1*
- Right-hand side of the beeswarm (high onboarding time)
- Blue color: No issues—AI/ML considers the persistent poor performance as "normal"

![Baseline Dashboard - Building no issues outlier](../../images/assurance/img/baselines-image005.png)

The beeswarm chart is highly effective for quickly assessing network health, even in large deployments.

**Tip:** If you already know which building to analyze (e.g., after a user complaint), use the map or table view for quick selection.

![Baseline Dashboard map or list](../../images/assurance/img/baselines-image006.png)

---

## Exploring Building Baseline Views

### Selecting a Building

*What building did you choose to analyze first?*

---

### Example 1: Building with Issues (*LONDON 1*)

After clicking the red circle for *LONDON 1*, you’ll see the baseline view, displaying all onboarding KPIs for one SSID.

- Adjust KPIs, SSIDs, and WLCs using the dropdowns at the top.

![Baseline Building KPI SSID WLC selection](../../images/assurance/img/baselines-image007.png)

#### Single SSID View

- Track how predicted and actual KPIs change over time.
- See AI-driven issue reports and access details.
- Identify if anomalies affect single or multiple KPIs.

![Baseline Dashboard - Default baseline view, 1 SSID with issue](../../images/assurance/img/baselines-image008.png)

#### Multiple SSIDs View

- Different SSIDs may show very different "normal" behaviors.
- Add SSIDs from the dropdown to compare predicted ranges and actual values across SSIDs.

To add a second SSID (e.g., *PseudoCo-Corp*):
- Click the **SSID** menu, select **PseudoCo-Corp**.

![Baseline Building add SSID](../../images/assurance/img/baselines-image009.png)

The updated view allows you to see, for example, that only the *PseudoCo-Guest* SSID was affected by an issue, while *PseudoCo-Corp* behaved normally.

![Baseline Dashboard - Baseline view, 2 SSIDs](../../images/assurance/img/baselines-image010.png)

---

### Example 2: Building with No Issues (*SAN FRANCISCO 1*)

Now, review the *SAN FRANCISCO 1* building, which had no issues but consistently high onboarding times.

- Click **Network Overview** (top-left) to return to the beeswarm, then select *SAN FRANCISCO 1*.
- Add the *PseudoCo-Corp* SSID as previously described.

![Baseline Building add SSID](../../images/assurance/img/baselines-image011.png)

Now compare both SSIDs in the same building.

![Baseline Building add SSID](../../images/assurance/img/baselines-image017.png)

Resulting view:

![Baseline Dashboard - Baseline view, 2 SSIDs no issues](../../images/assurance/img/baselines-image012.png)

---

## KPI Detailed View

Baselines in the detailed view are computed for each *entity* (usually aggregated by SSID and building).

To investigate further (e.g., *SAN FRANCISCO 1*, *PseudoCo-Corp* SSID):

- Click **View Details** next to the SSID name under the Onboarding Time KPI.

![Baseline Building add SSID](../../images/assurance/img/baselines-image014.png)

The **Detailed View** provides:

- Client count time series
- AP table: Onboarding KPIs and direct links to the AP360 page for each AP.

*Note: Client type is based on device classification from the Wireless LAN Controller (WLC). Unclassified devices are labeled as "Device".*

![Baseline Detailed View](../../images/assurance/img/baselines-image018.png)

---

## Key Takeaways

- **AI/ML-based baselining** is a powerful way to understand typical network behavior and manage large volumes of data.
- The algorithms adapt over time to learn what is "normal," reducing unnecessary alerts and focusing attention on significant issues.
- However, persistent poor performance may be normalized by the algorithms and not trigger alerts. Thus, the Baseline Dashboard is essential for maintaining visibility into both sudden and ongoing performance issues.

---

This concludes the exploration of the **Baselines Dashboard** feature.  
You can use the link below to proceed with the exploration of other use cases.

---
