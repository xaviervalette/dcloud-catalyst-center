---
title: "Using Rogue & AWIPS for Threat Containment"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/awips/
images: 14
links: 0
---

# Using Rogue & AWIPS for Threat Containment

## Introduction

This demo guide provides step-by-step instructions for utilizing the Rogue & AWIPS (Advanced Wireless Intrusion Prevention System) interface to identify, contain, and manage network threats—specifically focusing on handling Honeypot threats. You will learn how to initiate containment, review threat statuses, and manage allowed devices. All screenshots and UI steps are included for a seamless demo experience.

---

## 1. Supported Pages & Initial Steps

- **All pages are supported with data.**
- Begin the process by initiating containment.

---

## 2. Assurance – Rogue & AWIPS Overview

**Overview Screenshots**

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image001.png)

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image003.png)

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image005.png)

---

## 3. Identifying Threats

Navigate to the **Threats** section.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image007.png)

### Selecting a Threat

- Select a threat from the list where the threat type is **Honeypot**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image009.png)

---

## 4. Starting Containment

- Go to **Actions** and select **Start Containment**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image011.png)

- Click on **Configuration Preview** to review containment settings.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image013.png)

- After starting containment, the threat status changes to **Informational**.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image015.png)

---

## 5. Managing Allowed List

You can add a device to the allowed list to modify its threat status:

1. In the **Assurance → Rogues & AWIPS → Threats** section, select the **MAC Address** of the device.

   ![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image017.png)
2. Under **Actions**, choose **Add to Allowed List**.

   ![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image019.png)

   ![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image021.png)
3. After adding to the allowed list, the **Threat Level** changes to **Potential** and the **Containment Status** updates to **Contained**.

   ![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image023.png)

   ![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image025.png)
4. The MAC address added will now be visible in the **Allowed List** section.

   ![A screenshot of a computer  Description automatically generated](../../images/assurance/img/awips-image027.png)

---

## Conclusion

By following the steps in this guide, you can efficiently identify, contain, and manage rogue threats using the Rogue & AWIPS system. This ensures improved network security and streamlined incident management.

---
