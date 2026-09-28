---
title: "AP Performance Advisories"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/ap-perf/
images: 16
links: 1
---

# AP Performance Advisories

## Introduction

Welcome to the AP Performance Advisories demo guide. This document provides a step-by-step walkthrough of Cisco's AP Performance Advisory feature. You'll learn how to use AI/ML-driven insights to identify wireless Access Points (APs) that persistently deliver a poor client experience, understand root causes, and receive actionable recommendations to optimize your wireless network. The guide is structured to help you explore the feature’s workflow, analytics, and remediation guidance in a clear and concise manner.

---

## Table of Contents

1. [Overview](#overview)
2. [Benefits](#benefits)
3. [How the AP Performance Advisory Feature Works](#how-the-ap-performance-advisory-feature-works)
   - [Algorithm Steps](#algorithm-steps)
4. [Demo Workflow](#demo-workflow)
   - [Landing Page](#landing-page)
   - [Summary Page](#summary-page)
   - [Details Page](#details-page)
5. [Key Takeaways](#key-takeaways)
6. [Additional Use Case: High AP Density at 2.4GHz](#additional-use-case-high-ap-density-at-24ghz)

---

## Overview

The **AP Performance Advisory** feature leverages AI and ML to analyze wireless network data and surface APs or radios that consistently provide a poor client Quality of Experience (QoE). With up to four weeks of data considered, the system helps you quickly pinpoint and resolve performance issues by:

- Providing an overview of detected client experience issues, organized by root cause.
- Grouping problematic radios to help you understand common causes.
- Allowing you to drill down into individual radios for specific insights and guidance.

---

## Benefits

- **Proactive Issue Detection:** Automatically surface APs that consistently deliver suboptimal QoE.
- **Actionable Insights:** Receive clear diagnostics and remediation steps for identified issues.
- **Long-term Analytics:** Weekly-refreshed insights based on up to four weeks of data.
- **Minimal Setup:** No configuration is required beyond enabling controller telemetry and activating the Cisco AI Analytics cloud service (see [Lab 8 - Service Operations](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/)).

---

## How the AP Performance Advisory Feature Works

### Algorithm Steps

1. **Focus on Top Radios:** Limits analysis to the most important radios, improving relevance and detection accuracy.
2. **Identify Underperforming Radios:** Analyzes KPIs (e.g., RSSI, SNR) against a global baseline per frequency band (2.4 GHz, 5 GHz, 6 GHz).

   ![Global Baselining](../../images/assurance/img/ap-perf-image001.png)
3. **Apply Unsupervised Learning:** Uses multi-dimensional clustering to group radios with similar issues.

   ![Clustering](../../images/assurance/img/ap-perf-image003.png)
4. **Apply Supervised Learning:** Uses decision trees to identify key explanatory features (e.g., interference, power, CPU usage).
5. **Root Cause Analysis:** Leverages SME knowledge and AI/ML findings to derive root causes.
6. **Detailed Visualization:** Presents insights through visualizations and tables for easy exploration.

---

## Demo Workflow

The AP Performance Advisory workflow is designed to provide progressively deeper insights:

### Landing Page

Navigate to **Menu > Assurance > Trends and Insights**.

The landing page presents all discovered radios with potential client experience issues, grouped as cards by root cause and frequency band. Each card summarizes the root cause, number of radios affected, and the estimated number of impacted endpoints. The names of the top three impacted radios are shown as links for quick access to their details.

![AP Performance Advisories - Menu](../../images/assurance/img/ap-perf-image005.png)

![Landing Page](../../images/assurance/img/ap-perf-image007.png)

---

### Summary Page

Click a card (for example, **High co-channel interference on 2.4 GHz**) to investigate further.

The summary page provides:

- A **Hero Bar** summarizing the root cause, number of radios, impacted buildings, and a quick link to the top impacted radio.

  ![ap-perf-image009](../../images/assurance/img/ap-perf-image009.png)
- **Analysis Charts** showing the distribution of explanatory KPIs supporting the root cause analysis, compared with reference radios.

  - The x-axis shows KPI value ranges.
  - The y-axis shows frequency of observations.
  - Only KPIs relevant to the root cause are shown.
- **Remediation Guidance:** For example, high co-channel interference can often be mitigated by:

  - Tuning Transmit Power Control (TPC) to lower radio transmission power.
  - Disabling lower datarates to reduce airtime usage.

These suggestions are provided in the UI alongside explanations of each KPI.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ap-perf-image011.png)

- A **Radio Table** listing all radios in the group, ordered by their impact rating (combining the number of impacted clients and magnitude of KPI deviation). The “Insight Details” column links to the details page for each radio.

![Radio section](../../images/assurance/img/ap-perf-image013.png)

---

### Details Page

Click on a radio (e.g., **CW9166I-LDN1-05**) to see detailed analytics.

![Radio select](../../images/assurance/img/ap-perf-image015.png)

- The **Hero Bar** shows AP model, location, AP360 link, and impacted clients.

![Details Hero bar](../../images/assurance/img/ap-perf-image017.png)

- Below, you’ll find charts of client experience KPIs (e.g., RSSI, SNR, link speed, packet retries, packet failures) that were statistically significant for the selected radio.

![Context bar](../../images/assurance/img/ap-perf-image019.png)

#### Customizing KPI Views

You can add more KPIs for additional context by clicking the `+` button:

![Add KPI](../../images/assurance/img/ap-perf-image021.png)

For example, adding the **Speed** KPI can show that lower data rates are more common on the problematic radio, which can directly impact client experience.

![Speed KPI](../../images/assurance/img/ap-perf-image023.png)

#### Root Cause Analysis (RCA)

Below the KPI charts, root cause analysis charts display all anomalous KPIs for the individual radio. You may add even more KPIs (CPU/memory usage, model, image version, channel changes, etc.) using the `+` button.

![RCA](../../images/assurance/img/ap-perf-image025.png)

---

## Key Takeaways

- The **AP Performance Advisories** feature automates radio performance analytics and helps identify the most critical radios impacting client experience.
- It provides a streamlined way to target network optimizations, ensuring a consistently high-quality wireless experience.

---

## Additional Use Case: High AP Density at 2.4GHz

The following images illustrate another scenario—high AP density at 2.4GHz:

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ap-perf-image027.png)

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ap-perf-image029.png)

![A screenshot of a graph  Description automatically generated](../../images/assurance/img/ap-perf-image031.png)

---

**End of Guide**

Continue exploring other use cases as needed. For additional information, refer to the relevant Cisco documentation or follow the provided links.
