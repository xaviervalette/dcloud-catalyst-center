---
title: "Software Image Management (SWIM) Demo Guide"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim/
images: 20
links: 0
---

# Software Image Management (SWIM) Demo Guide

## Introduction

This guide provides a step-by-step demonstration of the Software Image Management (SWIM) feature, designed to simplify and automate the process of updating software images on network devices. This document will walk you through a specific use case: updating the software image version for multiple Cisco Catalyst 9300 series switches. By following these instructions, you will learn how to select devices, initiate an update task, perform readiness checks, schedule distribution and activation, and monitor the update status.

## Use Case

Update software image version from `cat9k_iosxe.17.15.02.SPA.bin` to `cat9k_iosxe.17.15.03.SPA.bin` for `LDN1-C9300-DIST1.PseudoCo.com` & `LDN1-C9300-DIST2.PseudoCo.com` devices.

---

**Navigation:** `Provision -> Inventory`

![Screenshot](../../images/provision/img/swim-image001.jpg)

---

## Step 1: Select Software Images Focus

Navigate to the Inventory section and select **Software Images** from the Focus dropdown menu.

![Screenshot](../../images/provision/img/swim-image003.jpg)

---

## Step 2: Select Target Devices

Identify and select the devices for software image update: `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`.

![Screenshot](../../images/provision/img/swim-image005.jpg)

---

## Step 3: Initiate Software Image Management

From the **Action** menu, navigate to `Software Image > Software Image Management`. This action will redirect you to the Software Image Management Page.

![Screenshot](../../images/provision/img/swim-image007.jpg)

![Screenshot](../../images/provision/img/swim-image009.jpg)

![Screenshot](../../images/provision/img/swim-image011.jpg)

![Screenshot](../../images/provision/img/swim-image013.jpg)

On the Software Image Management page, re-select `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com` devices, then click **Update Devices**.

---

## Step 4: Name the Update Task

Enter a descriptive task name for the software update and click **Next**.

![Screenshot](../../images/provision/img/swim-image015.jpg)

---

## Step 5: Review Navigation Options

Review the navigation options available:
\* **Exit:** To cancel the software update task.
\* **Back:** To return to the previous step.
\* **Next:** To proceed to the next step.

Click **Next** to continue.

![Screenshot](../../images/provision/img/swim-image017.jpg)

---

## Step 6: Select Software Image Version

Select the desired software image version for the update. In this use case, select `cat9k_iosxe.17.15.03.SPA.bin`.

![Screenshot](../../images/provision/img/swim-image019.jpg)

---

## Step 7: Perform Readiness Check

Verify that `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com` are listed in the Device Activation Order. Click the **Update Readiness Report** link to initiate an **Image Update Readiness Check** and review the device readiness report.

![Screenshot](../../images/provision/img/swim-image021.jpg)

---

## Step 8: Review and Close Readiness Report

After reviewing the Image Update Readiness Check results, close the report (by clicking 'X' or 'Close') to proceed with the workflow.

![Screenshot](../../images/provision/img/swim-image023.jpg)

![Screenshot](../../images/provision/img/swim-image025.jpg)

---

## Step 9: Configure Schedule and Activation Options

Configure the scheduling and cleanup options:
\* For **Software Distribution**, select **Now**.
\* For **Software Activation**, ensure **After Distribution** is **enabled**.

*Note: The 'Software Activation Later' option is not supported for this use case.*

Click **Submit** to proceed to the Summary page.

![Screenshot](../../images/provision/img/swim-image027.jpg)

---

## Step 10: Confirm and Schedule Distribution

Review the summary of your software image update task. Click **Submit** to schedule the distribution.

![Screenshot](../../images/provision/img/swim-image029.jpg)

![Screenshot](../../images/provision/img/swim-image031.jpg)

---

## Step 11: Monitor Image Update Status

To view the progress of the image update, click the **Image update status** button.

![Screenshot](../../images/provision/img/swim-image033.jpg)

---

## Step 12: Observe Distribution In-Progress

The status for both C9300 devices will initially show as **Distribution In-progress**.

![Screenshot](../../images/provision/img/swim-image035.jpg)

---

## Step 13: Review Mixed Status Results

Observe the updated status: `LDN1-C9300-DIST1.PseudoCo.com` shows **Distribution Success** and **Activation In-progress**, while `LDN1-C9300-DIST2.PseudoCo.com` shows **Distribution failed**.

![Screenshot](../../images/provision/img/swim-image037.jpg)

---

## Step 14: Final Status Overview

The final status indicates that `LDN1-C9300-DIST1.PseudoCo.com` is **Device UpToDate** with the latest software image, while `LDN1-C9300-DIST2.PseudoCo.com` remains in a **Distribution Failure** state.

![Screenshot](../../images/provision/img/swim-image039.jpg)

---
