---
title: "Cisco Assurance: Issues and Events"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/issues/
images: 93
links: 0
---

# Cisco Assurance: Issues and Events

## Introduction

This guide provides a step-by-step walkthrough of the Cisco Assurance Issues and Events interface. You will learn how to:
- View and filter issues based on different time ranges
- Interpret issue tables and priority breakdowns
- Use AI-driven filtering
- Navigate and analyze specific common issues (such as device disconnections, wireless client failures, and more)
- Run machine reasoning and suggested actions to diagnose and resolve issues

All screenshots and image references are retained from the original guide to assist you visually in each step.

---

## Table of Contents

1. [Viewing Issues and Events](#viewing-issues-and-events)
   - 1.1 [Accessing the Issues Graph](#accessing-the-issues-graph)
   - 1.2 [Adjusting the Time Range](#adjusting-the-time-range)
2. [Understanding the Issues Table](#understanding-the-issues-table)
   - 2.1 [Records per Time Range](#records-per-time-range)
   - 2.2 [Priority Counts (P1–P4)](#priority-counts-p1p4)
   - 2.3 [AI-Driven Issue Filter](#ai-driven-issue-filter)
3. [Investigating Specific Issue Types](#investigating-specific-issue-types)
   - 3.1 [Interface Connecting Network Devices is Down](#interface-connecting-network-devices-is-down)
   - 3.2 [Layer 2 Loop Symptoms](#layer-2-loop-symptoms)
   - 3.3 [Switch Unreachable](#switch-unreachable)
   - 3.4 [Switch Power Failure](#switch-power-failure)
   - 3.5 [Fabric Devices Connectivity - ISE Server](#fabric-devices-connectivity---ise-server)
   - 3.6 [WLC Unreachable](#wlc-unreachable)
   - 3.7 [Fabric Devices Connectivity - Control Border Underlay](#fabric-devices-connectivity---control-border-underlay)
   - 3.8 [Wireless Client Connection Issues](#wireless-client-connection-issues)
   - 3.9 [StackWise Virtual Link Failure](#stackwise-virtual-link-failure)
   - 3.10 [Wireless Client - Excessive Association Failures](#wireless-client---excessive-association-failures)
   - 3.11 [Excessive Failures to Connect - High Deviation from Baseline](#excessive-failures-to-connect---high-deviation-from-baseline)

---

## 1. Viewing Issues and Events

### 1.1 Accessing the Issues Graph

- Navigate to **Assurance → Issues and Events**.
- Go to the **Issues** section.
- By default, you will see the issues graph for the last 24 hours.

![Issues Graph - 24 Hours](../../images/assurance/img/issues-image001.png)

---

### 1.2 Adjusting the Time Range

You can select various time ranges to view issues.

**Step 1: Select 3 Hours**

- Choose the **3 hours** time range and click **Apply**.

![3 Hours Time Range Option](../../images/assurance/img/issues-image003.png)

- The graph updates to display issues from the last 3 hours.

![Issues Graph - 3 Hours](../../images/assurance/img/issues-image005.png)

**Step 2: Select 7 Days**

- Choose the **7 days** time range and click **Apply**.

![7 Days Time Range Option](../../images/assurance/img/issues-image007.png)

- The graph updates to display issues from the last 7 days.

![Issues Graph - 7 Days](../../images/assurance/img/issues-image009.png)

---

## 2. Understanding the Issues Table

### 2.1 Records per Time Range

The **Issues Table** updates based on the selected time range.

- **24 hours:** 15 records  
  ![Issues Table - 24 Hours](../../images/assurance/img/issues-image011.png)
- **3 hours:** 10 records  
  ![Issues Table - 3 Hours](../../images/assurance/img/issues-image013.png)
- **7 days:** 30 records  
  ![Issues Table - 7 Days](../../images/assurance/img/issues-image015.png)

---

### 2.2 Priority Counts (P1–P4)

- The table shows issue priorities: P1, P2, P3, and P4.
- For example, in the **All** tab:  
  P1: 4, P2: 6, P3: 8, P4: 7 (Total: 25)

![Priority Count Overview](../../images/assurance/img/issues-image017.png)

- The sum of P1–P4 issues matches the total count in the Issues Table.

#### Viewing by Priority

- Click on **P1** to filter and confirm the count matches the table.
  ![P1 Issues](../../images/assurance/img/issues-image019.png)
- Click on **P2**, **P3**, and **P4** to view their respective issue counts.
- ![P2 Issues](../../images/assurance/img/issues-image021.png)
- ![P3 Issues](../../images/assurance/img/issues-image023.png)
- ![P4 Issues](../../images/assurance/img/issues-image025.png)

---

### 2.3 AI-Driven Issue Filter

- Toggle the **AI Driven** switch to display only AI-driven issues and their counts.

![AI Driven Issue Filter](../../images/assurance/img/issues-image017.png)

- Navigate to **Assurance → Issues and Events → Issues** to see all issues in the table.

#### Issues Not Displayed in Table

If certain issues are not shown:

![Issues Not Displayed](../../images/assurance/img/issues-image029.png)

---

## 3. Investigating Specific Issue Types

This section provides a quick reference for analyzing and resolving various issues using the interface.

---

### 3.1 Interface Connecting Network Devices is Down

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image031.png)
2.  
![Step 2](../../images/assurance/img/issues-image033.png)
3. Click **Run Machine Reasoning** to view Reasoning Activity and Conclusions.  
![Step 3](../../images/assurance/img/issues-image035.png)

---

### 3.2 Layer 2 Loop Symptoms

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image037.png)
2.  
![Step 2](../../images/assurance/img/issues-image039.png)
3. Click **Root Cause Analysis**.  
![Step 3](../../images/assurance/img/issues-image041.png)
4. Click **Run Machine Reasoning**.  
![Step 4](../../images/assurance/img/issues-image043.png)

---

### 3.3 Switch Unreachable

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image045.png)
2.  
![Step 2](../../images/assurance/img/issues-image047.png)

---

### 3.4 Switch Power Failure

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image049.png)
2.  
![Step 2](../../images/assurance/img/issues-image051.png)
3.  
![Step 3](../../images/assurance/img/issues-image053.png)

> **Tip:** Change the Time Range from 24 hours to 7 days to see all issues.
> ![Change Time Range](../../images/assurance/img/issues-image055.png)

---

### 3.5 Fabric Devices Connectivity - ISE Server

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image057.png)
2.  
![Step 2](../../images/assurance/img/issues-image059.png)
3. Click **Suggested Actions**.  
![Step 3](../../images/assurance/img/issues-image061.png)
4. Click **Run**.  
![Step 4](../../images/assurance/img/issues-image063.png)

---

### 3.6 WLC Unreachable

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image065.png)
2.  
![Step 2](../../images/assurance/img/issues-image067.png)

---

### 3.7 Fabric Devices Connectivity - Control Border Underlay

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image069.png)
2.  
![Step 2](../../images/assurance/img/issues-image071.png)
3. Click **Suggested Actions**.  
![Step 3](../../images/assurance/img/issues-image073.png)
4. Click **Run**.  
![Step 4](../../images/assurance/img/issues-image075.png)

---

### 3.8 Wireless Client Connection Issues

#### A. Wireless Clients Took a Long Time to Connect - Failed Credentials

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image077.png)
2.  
![Step 2a](../../images/assurance/img/issues-image079.png)
![Step 2b](../../images/assurance/img/issues-image081.png)
3.  
![Step 3](../../images/assurance/img/issues-image083.png)
4.  
![Step 4a](../../images/assurance/img/issues-image085.png)
![Step 4b](../../images/assurance/img/issues-image087.png)
![Step 4c](../../images/assurance/img/issues-image089.png)
![Step 4d](../../images/assurance/img/issues-image091.png)

#### B. Wireless Clients Took a Long Time to Connect - WLC Failures

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image093.png)
2.  
![Step 2](../../images/assurance/img/issues-image095.png)
3.  
![Step 3](../../images/assurance/img/issues-image097.png)
4.  
![Step 4](../../images/assurance/img/issues-image099.png)
5.  
![Step 5](../../images/assurance/img/issues-image101.png)
6.  
![Step 6a](../../images/assurance/img/issues-image103.png)
![Step 6b](../../images/assurance/img/issues-image105.png)
7.  
![Step 7](../../images/assurance/img/issues-image107.png)

#### C. Wireless Clients Failed to Connect - Security Parameter Mismatch

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image109.png)
2.  
![Step 2](../../images/assurance/img/issues-image111.png)
3.  
![Step 3](../../images/assurance/img/issues-image113.png)
4.  
![Step 4](../../images/assurance/img/issues-image115.png)
5.  
![Step 5a](../../images/assurance/img/issues-image117.png)
![Step 5b](../../images/assurance/img/issues-image119.png)
6.  
![Step 6](../../images/assurance/img/issues-image121.png)

#### D. Wireless Clients Failed to Connect - AAA Server Rejected Clients

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image123.png)
2.  
![Step 2](../../images/assurance/img/issues-image125.png)
3.  
![Step 3](../../images/assurance/img/issues-image127.png)
4.  
![Step 4](../../images/assurance/img/issues-image129.png)
5.  
![Step 5a](../../images/assurance/img/issues-image131.png)
![Step 5b](../../images/assurance/img/issues-image133.png)
![Step 5c](../../images/assurance/img/issues-image135.png)
![Step 5d](../../images/assurance/img/issues-image137.png)

---

### 3.9 StackWise Virtual Link Failure

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image139.png)
2.  
![Step 2a](../../images/assurance/img/issues-image141.png)
![Step 2b](../../images/assurance/img/issues-image143.png)
![Step 2c](../../images/assurance/img/issues-image145.png)
3.  
![Step 3](../../images/assurance/img/issues-image147.png)
4. Click **Run**. The issue moves to the **Running** stage, then to **Success**.

![Run Stage 1](../../images/assurance/img/issues-image149.png)
![Run Stage 2](../../images/assurance/img/issues-image151.png)
![Run Stage 3](../../images/assurance/img/issues-image153.png)
![Run Stage 4](../../images/assurance/img/issues-image155.png)
![Run Stage 5](../../images/assurance/img/issues-image157.png)
![Run Stage 6](../../images/assurance/img/issues-image159.png)

---

### 3.10 Wireless Client - Excessive Association Failures

**Scenario:**  
Wireless client took a long time to connect (SSID: PseudoCo-Corp, AP: CW9166I-LDN1-01, Band: 2.4 GHz) due to excessive association failures.

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image161.png)
2.  
![Step 2](../../images/assurance/img/issues-image163.png)
3.  
![Step 3](../../images/assurance/img/issues-image165.png)

---

### 3.11 Excessive Failures to Connect - High Deviation from Baseline

**Steps:**
1.  
![Step 1](../../images/assurance/img/issues-image167.png)
2.  
![Step 2](../../images/assurance/img/issues-image169.png)
3.  
![Step 3](../../images/assurance/img/issues-image171.png)
4.  
![Step 4a](../../images/assurance/img/issues-image173.png)
![Step 4b](../../images/assurance/img/issues-image175.png)
5.  
![Step 5](../../images/assurance/img/issues-image177.png)
6.  
![Step 6](../../images/assurance/img/issues-image179.png)
7.  
![Step 7](../../images/assurance/img/issues-image181.png)
8.  
![Step 8](../../images/assurance/img/issues-image183.png)
9.  
![Step 9](../../images/assurance/img/issues-image185.png)

---

## Conclusion

This guide is intended to help you confidently navigate the Cisco Assurance Issues and Events interface, interpret issue data, and leverage advanced features such as AI-driven insights and machine reasoning. For further support or advanced troubleshooting, refer to the official Cisco documentation or reach out to Cisco support.

---
