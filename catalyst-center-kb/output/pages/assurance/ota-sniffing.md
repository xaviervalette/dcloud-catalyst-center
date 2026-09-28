---
title: "OTA (Over-The-Air) Sniffing"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/ota-sniffing/
images: 22
links: 0
---

# OTA (Over-The-Air) Sniffing

## Introduction

This guide provides a step-by-step walkthrough for performing an Over-The-Air (OTA) Sniffing use case on Cisco access points. OTA Sniffing enables you to capture wireless packets directly from selected access points to analyze network activity and troubleshoot issues. The process covers accessing the device, configuring capture parameters, running and monitoring the capture, and downloading the resulting packet capture (PCAP) files. Follow each step carefully to successfully complete the OTA Sniffing workflow.

---

## Step 1: Access the Device 360 Page

To begin, navigate to the **Device 360** page for the desired access point. You can do this either through the global search or via the inventory page.

In this example, we use the global search to select the `CW9166-LDN1-01` access point.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image001.png)

---

## Step 2: Start the OTA Capture

Once on the Device 360 page, locate and click the **Run OTA Capture** button.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image002.png)

---

## Step 3: Select Access Points

After clicking **Run OTA Capture**, a left panel will appear. Select any two access points by clicking on their names. The selected access points will be displayed below the floor map. Click the **Next** button to proceed.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image003.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image004.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image005.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image006.png)

---

## Step 4: Configure Capture Parameters

For each selected access point, choose the **Band**, **Radio**, **Channel Width**, and **Channel** as required. Once configured, click the **Run** button. A popup will appear; click **OK** to confirm.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image007.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image008.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image009.png)

---

## Step 5: Apply Capture Settings

A confirmation popup will display. Click **Apply** to proceed.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image010.png)

---

## Step 6: Perform Initial Checks

The system will now perform initial checks. Once these checks are successful, click **Next** to continue.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image011.png)

---

## Step 7: Review Device Configuration and Deploy

- **Step 2:** The device configuration will be checked; the status will be shown as **In-progress**.
- **Step 3:** After the configuration checks are complete and successful, the **Deploy** button will become enabled. Click **Deploy** to move forward.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image012.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image013.png)

---

## Step 8: Submit and Run the Capture

After clicking **Deploy**, a deployment popup will appear. Click **Submit** to start the OTA Sniffing process.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image014.png)

---

## Step 9: Monitor Capture Progress

You will now see the **OTA Capture Progress** message next to the **Stop** link. The system will continue capturing packets until you manually stop the capture.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image015.png)

---

## Step 10: View Capture History

While the capture is running, clicking the **Download** link will display the previous history of OTA Captures.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image016.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image017.png)

---

## Step 11: Stop the Capture and Access Results

Press **Stop** to end the packet capture. After stopping, clicking the **Download** link will show two entries: one for the previous capture and one for the current capture.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image018.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image016.png)
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image019.png)

---

## Step 12: Download the Capture File

Click the **Download** icon to save the PCAP file for analysis.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image020.png)

---

## Step 13: View OTA Sniffing Progress in Assurance

You can also track OTA Sniffing progress by navigating to **Assurance → Settings → Intelligent Capture Settings → OTA Sniffer Capture** tab.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/ota-sniffing-image021.png)

---

## Conclusion

You have now completed the OTA Sniffing workflow, from device selection to packet capture and downloading the PCAP file. These steps enable efficient wireless packet analysis for troubleshooting and assurance purposes.

---
