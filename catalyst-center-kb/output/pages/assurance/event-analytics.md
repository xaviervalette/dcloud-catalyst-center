---
title: "Cisco Catalyst Center: Event Analytics"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/event-analytics/
images: 17
links: 0
---

# Cisco Catalyst Center: Event Analytics

## Introduction

This hands-on laboratory session introduces you to the powerful Event Analytics feature, designed to enhance network visibility and management efficiency. You'll learn how to monitor your network, detect behavioral changes, and correlate different event types for both wired and wireless devices.

This guide will walk you through:

- Navigating the Event Analytics dashboard
- Analyzing network events by domain and type
- Using analytics features to isolate relevant events during interesting time periods
- Accessing individual events for detailed insights
- Creating user-defined issues based on observed patterns

By the end of this demo, you'll be able to move from a global event overview down to the specifics of a single device or interface, improving your network troubleshooting and management workflow.

---

## What is Event Analytics?

**Event Analytics** is a feature introduced in Cisco Catalyst Center version 2.3.7, providing comprehensive network event visibility across wired and wireless domains. Unlike traditional systems that require predefined issue signatures, Event Analytics uses machine learning and AI to process network event data and detect anomalies—even when specific signatures are not defined. Innovative data visualization techniques help you quickly identify and investigate potential issues in real time.

### Benefits

- Broad visibility across all network domains
- Real-time anomaly detection using AI and ML
- Streamlined investigation workflow from overview to detailed event analysis
- Ability to define and be notified of custom, user-defined issues

---

## Supported Event Types

| **Event Type** | **Wired** | **Wireless** |
| --- | --- | --- |
| Syslog | X | X |
| Reachability | X | X |
| Radio events |  | X |
| Client events | \* | X |

*Note: Wired client events will be added in a future release.*

### Event Type Descriptions

- **Syslog:** Messages collected from switches, routers, and Wireless LAN Controllers (WLCs). By default, only metadata (message type, severity, mnemonic) is exported to the Cisco AI Cloud for privacy. Full text export requires explicit user consent.
- **Reachability:** Reflects changes in device status as monitored by Catalyst Center (e.g., device joins/disjoins, reachable, unreachable).
  - **REACHABLE:** Device is fully manageable
  - **PING\_REACHABLE:** Device responds to pings but is not fully manageable
  - **UNREACHABLE:** Device is offline
- **Radio events:** Includes channel changes, power adjustments, coverage hole detection, and radio resets (wireless only).
- **Client events:** Onboarding and roaming events for wireless clients. Wired client events to be added in a future release.

---

## Event Analytics Workflow

### 1. Accessing the Dashboard

Navigate to the **Event Analytics** dashboard:

**Menu > Assurance > Issue and Events > Event Analytics - Preview**

![AI-Driven issues - Hamburger menu](../../images/assurance/img/event-analytics-image001.png)

Select the **Event Analytics - Preview** tab at the top:

# event analytics preview is missing

![AI-Driven issues - Issues menu](../../images/assurance/img/event-analytics-image003.png)

---

### 2. Heatmap Overview

The **Heatmap** provides a visual overview of network event volumes by type and category for the selected time period.

![Event Analytics - Heatmap overview](../../images/assurance/img/event-analytics-image005.png)

- **Default View:** Last 24 hours, showing Syslog and Reachability events for all wired devices (switches and routers).
- **Customization:** Filter by location, extend the time period (up to 60 days), or switch between wired and wireless views.

**Interpreting the Heatmap:**

- Darker areas indicate higher event volumes.
- Each event category has its own color scale, making rare events (e.g., high-severity Syslog messages) easier to spot.

![Event Analytics - Heatmap scale](../../images/assurance/img/event-analytics-image007.png)

- **High severity** event spikes require immediate attention.
- Increases in **medium or low severity** events may indicate behavioral changes worth investigating.

**First Investigation Step:**
- Identify time periods with significant changes in event volume.
- Example: Observe dense Syslog message areas and increased reachability events within the same timeframe.

![Event Analytics - Correlation across different event types](../../images/assurance/img/event-analytics-image009.png)

---

### 3. Time Selection and Analytics

**Note:** From this point, the Event Analytics workflow can only be followed via this lab guide due to demo system limitations.

#### Time Selection

The heatmap helps you pinpoint when significant event volume changes occur and provides initial correlation across event types.

- Click on a heatmap time bucket to restrict your analysis to that period.
- Adjust the selection using the selector bars.

Example: A 1-hour period (each block in 24-hour view represents 15 minutes).

![Heatmap time selection](../../images/assurance/img/event-analytics-image011.png)

After selection, summary info below each category updates to reflect the event count in the chosen timeframe.

---

### 4. Card View: Show Analytics

Click **Show Analytics** to expand and view event summaries as cards, specific to each event type.

- **Syslog Cards:** Highlight highest severity events, highest volume, rare types, and those with volume changes.
- Identify **new events**—those that started near the end of the selected period.
- Also, see **top network devices** based on event volume.

![Heatmap card view](../../images/assurance/img/event-analytics-image013.png)

---

### 5. Detailed Event View

Choose a card of interest (e.g., Highest Severity Events) and click **Show details** for an in-depth view.

#### a. Detailed Heatmap

Shows the evolution of top event types over the selected period. By default, shows the top 3 events (up to 5 selectable), sorted by card criteria.

![Detailed view - Events heatmap](../../images/assurance/img/event-analytics-image017.png)

#### b. Sankey Diagram

Visualizes the impact of specific event types by site and device.

![Detailed view - Sankey](../../images/assurance/img/event-analytics-image019.png)

- Interact with the diagram to see event distribution across sites/devices.
- Example: Spanning tree messages from two specific devices.

![Detailed view - Sankey select event type](../../images/assurance/img/event-analytics-image021.png)

- Select a device with the most events to view details:
  - Example: Top events are `SPANTREE-2-BLOCK_BPDUGUARD` and `PORT_SECURITY-2-PSECURE_VIOLATION`.

![Detailed view - Sankey select network device](../../images/assurance/img/event-analytics-image023.png)

#### c. Event Table

Displays individual events for full details. By default, shows events for the heatmap selection. Interact with the Sankey diagram to filter by event type, location, or device.

- Example: Focus on a device producing the most high-severity events—see that spanning tree and port security messages are tied to interfaces `Gi1/0/37` and `Gi1/0/38`.

![Table view - Select device](../../images/assurance/img/event-analytics-image025.png)
![Table view - Analyize events](../../images/assurance/img/event-analytics-image027.png)

**In just a few clicks, you can move from an overview to a specific device and interface affected by an issue.**

---

### 6. Configuring User-Defined Issues

Event Analytics enables you to define custom issues based on identified patterns, even if they don't match known issue signatures.

- To be notified about similar future events, create a **user-defined issue** directly from the event table:

![User defined issue - link](../../images/assurance/img/event-analytics-image029.png)

- Confirm your choice in the prompt:

![User defined issue - confirm](../../images/assurance/img/event-analytics-image031.png)

- You'll be taken to Issue Settings to finalize the issue creation:

![User defined issue - create](../../images/assurance/img/event-analytics-image033.png)

- Specify matching patterns, issue priority, and notification settings:

![User defined issue - pattern](../../images/assurance/img/event-analytics-image035.png)

---

## Key Takeaways

- **Event Analytics** provides cross-domain visibility and supports multiple event types for both wired and wireless networks.
- Advanced analytics and visualization tools make it easy to detect and investigate significant network events, even without predefined issue triggers.
- Quickly correlate, isolate, and analyze events—then create custom notifications for ongoing monitoring.

**This concludes the exploration of the Event Analytics feature.**  
Continue with the next lab or explore additional use cases as needed.

---
