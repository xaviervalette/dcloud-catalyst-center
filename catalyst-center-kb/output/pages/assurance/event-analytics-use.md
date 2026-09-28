---
title: "Cisco Catalyst Center: Event Analytics"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/event-analytics-use/
images: 139
links: 2
---

# Cisco Catalyst Center: Event Analytics

## Introduction

This demo guide provides a step-by-step walkthrough of the **Event Analytics** feature in Cisco Catalyst Center (available since version 2.3.7). Event Analytics enables network administrators to effectively monitor their networks by detecting behavioral changes and correlating various event types across both wired and wireless devices. The guide covers:

- Navigating the Event Analytics dashboard
- Understanding the benefits and supported event types
- Using analytics to isolate and investigate relevant events
- Leveraging heatmaps and visualizations for rapid anomaly detection

By following this guide, you will gain hands-on experience in using Event Analytics for enhanced network visibility and management efficiency.

---

## 1. Overview of Event Analytics

### What is Event Analytics?

Event Analytics is a feature designed to give network administrators unparalleled insights into all types of network events, regardless of whether a specific issue signature is defined. Unlike traditional network management systems, which depend on predefined signatures, Event Analytics leverages machine learning, artificial intelligence, and data visualization techniques to process event data continuously and highlight anomalies or potential issues in real time.

### Key Benefits

- **Comprehensive Visibility:** Monitor both wired and wireless domains from a single dashboard.
- **Signature-Free Detection:** Detect issues without requiring pre-configured issue signatures.
- **Advanced Analytics:** Use AI/ML algorithms for deeper insights and faster anomaly detection.
- **Rich Visualizations:** Quickly move from a global view to detailed event analysis with just a few clicks.

---

## 2. Supported Event Types

Event Analytics supports a variety of network event types:

| Event Type | Wired | Wireless |
| --- | --- | --- |
| **Syslog** | X | X |
| **Reachability** | X | X |
| **Radio Events** |  | X |
| **Client Events** | \* | X |

> **Note:** Wired client events will be added in a future release.

### Event Type Descriptions

- **Syslog:** Messages collected from switches, routers, and Wireless LAN Controllers (WLCs). By default, only metadata is exported to the Cisco AI Cloud to comply with [Cisco AI Analytics Privacy Policy](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/#data-privacy-and-security-considerations). Full text export requires explicit user consent.
- **Reachability:** Indicates changes in device reachability as monitored by Catalyst Center. Wireless AP reachability is reported by WLCs and triggered by JOIN/DISJOIN events. Statuses include:
- REACHABLE: Fully manageable
- PING\_REACHABLE: Pingable but not manageable
- UNREACHABLE: Offline
- **Radio Events:** Includes channel changes, transmission power changes (RRM), coverage hole detections, and radio resets.
- **Client Events:** Onboarding and roaming events for wireless clients (wired support coming soon).

---

## 3. Accessing the Event Analytics Dashboard

To access the Event Analytics dashboard, navigate to:

**Menu > Assurance > Issues and Events > Event Analytics - Preview**

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image001.png)

---

## 4. Using Event Analytics

### 4.1 Heatmap Overview

The **Heatmap** provides a visual overview of the volume of network events, categorized by type and severity.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image003.png)

- The default view shows the last 24 hours for syslog and reachability events on all wired devices.
- You can adjust the view by:
- Filtering by location
- Extending the time range (up to 60 days)
- Switching between wired and wireless domains

#### Interpreting the Heatmap

- Darker colors indicate higher event volumes.
- Each event type/category has its own color scale to make rare events (like high-severity syslog messages) more visible.
- Syslog events are grouped by severity: **High** (Sev. 1 & 2), **Medium** (3 & 4), **Low** (5 & 6).

---

## 5. Detailed Event Exploration

### 5.1 Wired Events

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image005.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image007.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image009.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image011.png)

#### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image013.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image015.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image017.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image019.png)

#### Sub Graph: 2

![A screenshot of a computer screen  Description automatically generated](../../images/assurance/img/event-analytics-use-image021.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image023.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image025.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image027.png)

#### Sub Graph: 3

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image029.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image031.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image033.png)

> **Note:** If you see "unknown" displayed in a graph, it may indicate incomplete data or unsupported event types.

![event-analytics-use-image035](../../images/assurance/img/event-analytics-use-image035.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image037.png)

#### Sub Graph: 4

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image039.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image041.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image043.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image045.png)

#### Sub Graph: 5

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image047.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image049.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image051.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image053.png)

#### Sub Graph: 6

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image055.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image057.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image059.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image061.png)

#### Sub Graph: 7

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image063.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image065.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image067.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image069.png)

---

### 5.2 Reachability Transitions

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image071.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image073.png)

#### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image075.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image077.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image079.png)

#### Sub Graph: 2

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image081.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image083.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image085.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image087.png)

---

### 5.3 Client Onboardings

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image089.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image091.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image093.png)

#### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image095.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image097.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image099.png)

---

## 6. Wireless Event Analytics

[**Event Analytics**](https://localhost:7000/dna/assurance/dashboards/issues-events/events-analytics)

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image101.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image103.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image105.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image107.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image109.png)

#### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image111.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image113.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image115.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image117.png)

#### Sub Graph: 2

![A screenshot of a white paper with blue and red text  Description automatically generated](../../images/assurance/img/event-analytics-use-image119.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image121.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image123.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image125.png)

#### Sub Graph: 3

![A screenshot of a report  Description automatically generated](../../images/assurance/img/event-analytics-use-image127.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image129.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image131.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image133.png)

#### Sub Graph: 4

![A screen shot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image135.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image137.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image139.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image141.png)

#### Sub Graph: 5

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image143.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image145.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image147.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image149.png)

#### Sub Graph: 6

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image151.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image153.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image155.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image157.png)

#### Sub Graph: 7

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image159.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image161.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image163.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image165.png)

---

### 6.1 Wireless Reachability Transitions

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image167.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image169.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image171.png)

#### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image173.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image175.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image177.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image179.png)

#### Sub Graph: 2

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image181.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image183.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image185.png)

---

### 6.2 Radio Events

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image187.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image189.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image191.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image193.png)

#### Sub Graph: 1

![A screenshot of a data report  Description automatically generated](../../images/assurance/img/event-analytics-use-image195.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image197.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image199.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image201.png)

#### Sub Graph: 2

**Top APs by failure radio resets**

#### Sub Graph: 3

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image203.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image205.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image207.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image209.png)

#### Sub Graph: 4

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image211.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image213.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image215.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image217.png)

#### Sub Graph: 5

**Top APs by coverage hole detection events**

---

### 6.3 Client Onboardings

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image219.png)
![A screen shot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image221.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image223.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image225.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image227.png)

#### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image229.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image231.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image233.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image235.png)

#### Sub Graph: 2

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image237.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image239.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image241.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image243.png)

#### Sub Graph: 3

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image245.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image247.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image249.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image251.png)

#### Sub Graph: 4

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image253.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image255.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image257.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image259.png)

#### Sub Graph: 5

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image261.png)
![A barcode on a computer screen  Description automatically generated](../../images/assurance/img/event-analytics-use-image263.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image265.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image267.png)

#### Sub Graph: 6

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image269.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image271.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image273.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image275.png)

#### Sub Graph: 7

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/event-analytics-use-image277.png)

---

## Conclusion

This guide has walked you through the Event Analytics feature of Cisco Catalyst Center, highlighting how you can monitor your network efficiently, detect anomalies in real time, and drill down from a global to a granular event view. Event Analytics leverages advanced analytics and visualization to provide actionable insights, making network management more proactive and effective.

For additional details or questions, consult the Cisco Catalyst Center documentation or your network administrator.

---

*All image references and links remain as in the original document for continuity and accuracy.*
