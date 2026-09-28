---
title: "Intelligent Capture Device360"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/intelligent-capture-360/
images: 16
links: 0
---

# Intelligent Capture Device360

## Introduction

This guide provides a step-by-step walkthrough for using the **Intelligent Capture Device360** feature. It covers two main areas: analyzing RF statistics and performing spectrum analysis for Cisco access points. The instructions and corresponding screenshots will help you efficiently monitor, troubleshoot, and optimize network performance using Device360.

---

## Part 1: RF Statistics

### Step 1

On the homepage, click the **Menu**. Navigate to **Assurance > Health**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image001.png)

---

### Step 2

Open the **Network** tab and filter the network device table to show only access points. Click on any access point to proceed.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image003.png)

---

### Step 3

On the Access Point Device360 page, select **Intelligent Capture**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image005.png)

---

### Step 4

Click the **RF Statistics** tab as shown below. Review the data displayed for the dashboards in the 1, 3, and 5 hour time ranges. Check the available radio types in the radio drop-down menu.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image007.png)

---

### Step 5

Examine the data and graphs loaded in all the dashboards. Hover over the graphs to see individual values for each time range.

For the **Top Clients with Tx Failed Packets by SSID** dashboard, some access points may have data available. Also, check the SSID drop-down values in this dashboard.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image009.png)

---

## Part 2: Spectrum Analysis

### Step 1

Select the **Spectrum Analysis** tab, then click **Start Spectrum Analysis**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image011.png)

---

### Step 2

A pop-up window will appear. Click **Next** to continue.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image013.png)

---

### Step 3

In Step 1, the system will perform initial checks. Once complete, click **Next**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image015.png)

---

### Step 4

The wizard will advance to steps 2 and 3. Review the configurations to be deployed as shown in the screenshot. Ensure the status in the top-right corner is **Ready**. Click **Deploy**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image017.png)

---

### Step 5

A new pop-up will appear. Click **Submit** to continue.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image019.png)

---

### Step 6

After a short wait, the spectrum analysis will begin and the graphs will load.

- Review the **Spectrum Analysis** and **Interference and Duty Cycle** graphs for the 2.4 GHz band.
- Check the data for time ranges of 1, 3, and 5 hours.
- Also review the graphs in the **Realtime FFT** range, as shown in the second image.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image021.png)

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image023.png)

---

### Step 7

Switch to the 5 GHz band.

- Review the **Spectrum Analysis** and **Interference and Duty Cycle** graphs.
- Check the graphs for the 1, 3, and 5 hour time ranges.
- Also review the **Realtime FFT** graphs as shown below.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image025.png)

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image027.png)

---

### Step 8

To end the spectrum analysis, click **Stop Spectrum Analysis** in the top-right corner of the dashboard.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image029.png)

---

### Step 9

A pop-up window will appear. Click **Accept** to confirm and stop the spectrum analysis.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/intelligent-capture-360-image031.png)

---

## Notes

- Ensure you have the appropriate permissions to use these features.
- If data does not appear in some dashboards, verify the selected access point and time range.
- Hovering over graphs provides more detailed insights for each data point.

---
