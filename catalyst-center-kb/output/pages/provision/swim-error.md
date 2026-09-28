---
title: "SWIM - Software Image Management Error Scenario Guide"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim-error/
images: 21
links: 0
---

# SWIM - Software Image Management Error Scenario Guide

This guide outlines the process of performing a Software Image Management (SWIM) update for network devices, specifically demonstrating an error scenario that can occur during the distribution phase. By following these steps, users will learn how to initiate a software image update, monitor its progress, and identify where an update might fail, providing valuable insights for troubleshooting and resolution.

---

## Initiating a Software Image Update Task

### 1. Navigate to Inventory

Begin by navigating to the **Provision** section, then select **Inventory**.

![Screenshot](../../images/provision/img/swim-error-image001.jpg)

### 2. Select Software Images Focus

From the Inventory page, set the **Focus** to **Software Images**.

![Screenshot](../../images/provision/img/swim-error-image003.jpg)

### 3. Select Target Devices for Update

Identify the devices that require a software image update. For this demonstration, we will update two devices: `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`.

Select both devices as shown below.

![Screenshot](../../images/provision/img/swim-error-image005.jpg)

### 4. Initiate Software Image Management Action

With the devices selected, click on **Action**, then navigate to **Software Image** and select **Software Image Management**.

![Screenshot](../../images/provision/img/swim-error-image007.jpg)

This action will redirect you to the **Software Image Management Page**.

![Screenshot](../../images/provision/img/swim-error-image009.jpg)

### 5. Confirm Devices and Proceed to Update

On the Software Image Management page, re-select `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`. After confirming your selection, click the **Update Devices** button.

![Screenshot](../../images/provision/img/swim-error-image011.jpg)

![Screenshot](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim-error/img/swim-error-image013.jpg)

### 6. Enter Task Name

Provide a descriptive name for your update task and then click **Next**.

![Screenshot](../../images/provision/img/swim-error-image015.jpg)

### 7. Review Navigation Options

This step presents navigation options for the update wizard:
\* **Exit button:** Exits the software update task.
\* **Back button:** Returns to the previous step.
\* **Next button:** Proceeds to the next step.

Click **Next** to continue.

![Screenshot](../../images/provision/img/swim-error-image017.jpg)

### 8. Select Software Image

Choose the desired software image for the update.

![Screenshot](../../images/provision/img/swim-error-image019.jpg)

### 9. Verify Device Activation Order and Readiness

On this page, you will see the selected devices, `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`, listed under **Device Activation Order**. By default, the update flow is set to **Parallel Update Order**.

Click the **Update Readiness Report** link to view a pop-up with the **Image Update Readiness Check** for each device.

![Screenshot](../../images/provision/img/swim-error-image021.jpg)

### 10. Review Image Update Readiness Report

Examine the readiness report for any potential issues. After reviewing, close the report by clicking the 'X' icon to continue with the workflow.

![Screenshot](../../images/provision/img/swim-error-image023.jpg)

![Screenshot](../../images/provision/img/swim-error-image025.jpg)

### 11. Schedule Task and Clean Up

Configure the scheduling options for the software distribution and activation:
\* For **Software Distribution**, select **Now**.
\* For **Software Activation**, ensure **After Distribution** is **enabled**.

**Note:** The "Software Activation Later" option is not supported for this use case.

Click **Submit** to proceed to the Summary page.

![Screenshot](../../images/provision/img/swim-error-image027.jpg)

### 12. Confirm and Submit Distribution

On the Summary page, review the task details. Click the **Submit Button** to schedule the distribution.

![Screenshot](../../images/provision/img/swim-error-image029.jpg)

## Monitoring and Troubleshooting the Update

### 13. View Image Update Status

After submission, click the **Image update status** button to monitor the progress of your update task.

![Screenshot](../../images/provision/img/swim-error-image031.jpg)

### 14. Observe Distribution In-Progress

Initially, the status for both C9300 devices will show as **Distribution In-progress**.

![Screenshot](../../images/provision/img/swim-error-image033.jpg)

### 15. Identify Update Status: Success and Failure

As the update progresses, you will observe the status of each device. In this scenario:
\* `LDN1-C9300-DIST1.PseudoCo.com` proceeds to **Distribution Success and Activation In-progress**.
\* `LDN1-C9300-DIST2.PseudoCo.com` shows a **Distribution failed** state.

![Screenshot](../../images/provision/img/swim-error-image035.jpg)

### 16. Investigate Failed Device Logs

To understand why `LDN1-C9300-DIST2.PseudoCo.com` failed, click on its device name. This action will display the **error logs** in a pop-up window.

![Screenshot](../../images/provision/img/swim-error-image037.jpg)

The error logs will indicate that the software image version update from `cat9k_iosxe.17.11.01.SPA.bin` to `cat9k_iosxe.17.12.01.SPA.bin` for `LDN1-C9300-DIST2.PseudoCo.com` has failed, with specific error details provided in the pop-up.

![Screenshot](../../images/provision/img/swim-error-image039.jpg)

![Screenshot](../../images/provision/img/swim-error-image041.jpg)
