---
title: "RMA Device Replacement Usecase"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/rma/
images: 22
links: 0
---

# RMA Device Replacement Usecase

This guide outlines the process for performing a Return Merchandise Authorization (RMA) device replacement within the platform. It details the steps required to identify an unreachable device, mark it for replacement, select a new device, and monitor the replacement process through to completion. This workflow ensures a smooth transition when replacing faulty network devices.

---

## Step 1: Navigate to Inventory

From the Homepage, click the **Menu** icon. Then, navigate to **Provision > Inventory**.

![Screenshot](../../images/provision/img/rma-image001.jpg)

## Step 2: Filter for Unreachable Devices

Once on the Inventory page, use the left sidebar to filter for **unreachable** devices. Additionally, change the focus of the page to **Device Replacement**. The table below will then display a list of all unreachable devices.

![Screenshot](../../images/provision/img/rma-image003.jpg)

## Step 3: Mark Device for Replacement

Select the device you wish to replace from the table. Click the **Actions** button above the table, then navigate to **Device Replacement > Mark for Replacement**.

![Screenshot](../../images/provision/img/rma-image005.jpg)

A confirmation prompt will appear asking to **Mark** or **Cancel**. Click **Mark**.

![Screenshot](../../images/provision/img/rma-image007.jpg)

## Step 4: Verify "Ready for Replacement" Status

The device's replacement status will now change to **"Ready for Replacement"**, indicating it is prepared for the replacement process.

![Screenshot](../../images/provision/img/rma-image009.jpg)

## Step 5: Initiate Device Replacement

Re-select the marked device. Click **Actions > Device Replacement > Replace Device**.

![Screenshot](../../images/provision/img/rma-image011.jpg)

## Step 6: Choose Replacement Device

The "Choose Replacement Device" page will appear. Select **Plug and Play** as the source. Then, choose one of the available devices from the table to use as the replacement. Click **Next**.

![Screenshot](../../images/provision/img/rma-image013.jpg)

## Step 7: Review Replacement Summary

A summary page will appear, displaying the details of both the faulty device and the selected replacement device. Review the information and click **Next**.

![Screenshot](../../images/provision/img/rma-image015.jpg)

## Step 8: Schedule Replacement

The "Schedule Replacement" page will appear. Click **Next** to proceed.

![Screenshot](../../images/provision/img/rma-image017.jpg)

## Step 9: Perform Initial Checks

The first step of the RMA use case will now perform initial checks. Once all operations are successful, click **Next**.

![Screenshot](../../images/provision/img/rma-image019.jpg)

## Step 10: Process Device List and Fetch Configuration

The second step of the use case will check the device list. Please wait for this process to complete.

Subsequently, the third step will fetch the configuration files for the devices. Once the status is in a **ready** state, click **Deploy**.

![Screenshot](../../images/provision/img/rma-image021.jpg)

## Step 11: Confirm Deployment

After clicking **Deploy**, a pop-up will appear asking you to submit the deployment. Click **Submit**.

![Screenshot](../../images/provision/img/rma-image023.jpg)

## Step 12: Monitor In-Progress Replacement

Once deployed, the device replacement process will begin. On the Inventory page, the faulty device's replacement status will change to **In-Progress**.

![Screenshot](../../images/provision/img/rma-image025.jpg)

## Step 13: View In-Progress Details and Onboarding Status

While the device replacement is **In-Progress**, you can click on the **In-Progress** status in the inventory to view detailed information, including the replacement status history and the tasks being executed.

![Screenshot](../../images/provision/img/rma-image027.jpg)

![Screenshot](../../images/provision/img/rma-image029.jpg)

![Screenshot](../../images/provision/img/rma-image031.jpg)

The history of tasks performed for the device replacement process will be displayed.

![Screenshot](../../images/provision/img/rma-image033.jpg)

Additionally, during the **In-Progress** state, navigating to **Provision > Plug and Play** will show the selected replacement device as **Onboarding**.

## Step 14: Verify Successful Replacement

After the device has been successfully replaced, its replacement status in the inventory will show as **NA**. The device details, such as IP Address and serial number, will be updated to reflect the new replacement device.

![Screenshot](../../images/provision/img/rma-image035.jpg)

Furthermore, after the replacement, if you navigate to **Provision > Plug and Play**, the selected replacement device will now show as **Provisioned**.

![Screenshot](../../images/provision/img/rma-image037.jpg)

## Step 15: Review Replacement History

To review the history of device replacements, navigate to **Actions > Device Replacement > Replacement History**. This will display a record of all replacement activities.

![Screenshot](../../images/provision/img/rma-image039.jpg)

Clicking on the replacement status of a specific device in the history will provide a detailed view of the tasks performed during its replacement process.

![Screenshot](../../images/provision/img/rma-image041.jpg)

![Screenshot](../../images/provision/img/rma-image043.jpg)
