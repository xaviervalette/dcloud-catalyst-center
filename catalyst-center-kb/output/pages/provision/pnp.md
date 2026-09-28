---
title: "Cisco Plug and Play (PnP) Demo Guide"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/pnp/
images: 41
links: 0
---

# Cisco Plug and Play (PnP) Demo Guide

## Introduction

This guide provides step-by-step instructions for utilizing Cisco Plug and Play (PnP) to streamline the claiming and provisioning of network devices. By following this demo, users will learn how to efficiently onboard both Wireless LAN Controllers (WLCs) and switches, assign them to network sites, configure essential parameters, and deploy configurations. This process ensures a smooth and automated network setup, leveraging PnP for rapid device deployment. All screenshots and interface references are included to help you navigate the workflow smoothly.

---

## Table of Contents

1. [Claiming and Provisioning a WLC Device](#claiming-and-provisioning-a-wlc-device)
   - [Step 1: Claim PnP Device – WLC](#step-1-claim-pnp-device--wlc)
   - [Step 2: Assign Site](#step-2-assign-site)
   - [Step 3: Configure Device Details](#step-3-configure-device-details)
   - [Step 4: Preview Configuration](#step-4-preview-configuration)
   - [Step 5: Verify WLC in Inventory](#step-5-verify-wlc-in-inventory)
   - [Step 6: Provision Claimed Device](#step-6-provision-claimed-device)
2. [Claiming and Provisioning a Switch](#claiming-and-provisioning-a-switch)
   - [Step 1: Claim PnP Device – Switch](#step-1-claim-pnp-device--switch)
   - [Step 2: Assign Site](#step-2-assign-site-1)
   - [Step 3: Check Image and Templates](#step-3-check-image-and-templates)
   - [Step 4: Preview Configuration](#step-4-preview-configuration-1)
   - [Step 5: Verify Switch in Inventory](#step-5-verify-switch-in-inventory)
   - [Step 6: Provision Claimed Device](#step-6-provision-claimed-device-1)

---

## Claiming and Provisioning a WLC Device

### Step 1: Claim PnP Device – WLC

1. Navigate to **Provision > Network Devices > Plug and Play**.

   ![Screenshot](../../images/provision/img/pnp-image001.png)
2. Select the **WLC** you want to claim. Click **Actions > Claim**.

   ![Screenshot](../../images/provision/img/pnp-image003.png)

---

### Step 2: Assign Site

1. Assign the device to the desired site, e.g., `newyork1 / newyork1->1st floor`.

   ![Screenshot](../../images/provision/img/pnp-image005.png)

   Click **Assign** and then **Next** to continue.
2. ![Screenshot](../../images/provision/img/pnp-image007.png)

   Click **Assign** to configure required network details for the Catalyst WLC.

---

### Step 3: Configure Device Details

Fill in the required network details for the Catalyst WLC as shown below:

- **IP Address:** 10.12.52.21
- **Subnet Mask:** 255.255.255.0
- **Gateway:** 10.12.52.1
- **Interface:** Ten 0/0/0
- **VLAN ID:** 12

  ![Screenshot](../../images/provision/img/pnp-image009.png)

  Click on **Save** to continue.

  ![Screenshot](../../images/provision/img/pnp-image011.png)

  The `WLC9800-PnP-Template` is being used in this workflow. Since the hostname is a variable in this template, you can enter the desired device name here, which will also be reflected in the inventory.

  Click **Next** to continue.

  ![Screenshot](../../images/provision/img/pnp-image013.png)

---

### Step 4: Preview Configuration

1. Select the **Preview Configuration** option.

   ![Screenshot](../../images/provision/img/pnp-image015.png)
2. Verify that the hostname matches the device name used in this demo.

   ![Screenshot](../../images/provision/img/pnp-image017.png)
3. After claiming, the status will initially remain unchanged.
4. Click the **Refresh** button at the top of the table or wait 30 seconds for the status to auto-refresh.

   ![Screenshot](../../images/provision/img/pnp-image019.png)

---

### Step 5: Verify WLC in Inventory

1. Navigate to **Provision > Inventory**.
2. Confirm that the WLC device has been added to the inventory.

   ![Screenshot](../../images/provision/img/pnp-image021.png)

---

### Step 6: Provision Claimed Device

1. Select the claimed WLC device from the inventory.
2. Click **Actions > Provision > Provision device**.

   ![Screenshot](../../images/provision/img/pnp-image023.png)

   Review the details and click **Next** to continue.
   ![Screenshot](../../images/provision/img/pnp-image025.png)

   Enter the VLAN ID and click **Next** to continue.
   ![Screenshot](../../images/provision/img/pnp-image027.png)

   Click **Next** to continue.
   ![Screenshot](../../images/provision/img/pnp-image029.png)

   Click **Next** to continue.
   ![Screenshot](../../images/provision/img/pnp-image031.png)

   Click **Next** to continue.
   ![Screenshot](../../images/provision/img/pnp-image033.png)

   Click on **Apply** to proceed.
   ![Screenshot](../../images/provision/img/pnp-image034.png)

   Click on **Next** to continue.
   ![Screenshot](../../images/provision/img/pnp-image035.png)

   Click on **Deploy** to continue.
   ![Screenshot](../../images/provision/img/pnp-image039.png)

   The provisioning of the device will complete successfully, as indicated by the status.
   ![Screenshot](../../images/provision/img/pnp-image041.png)

---

## Claiming and Provisioning a Switch

### Step 1: Claim PnP Device – Switch

1. Navigate to **Provision > Network Devices > Plug and Play**.

   ![Screenshot](../../images/provision/img/pnp-image043.png)
2. Select a switch to claim, Click **Actions > Claim**.

   ![Screenshot](../../images/provision/img/pnp-image045.png)

---

### Step 2: Assign Site

1. Assign the switch to the appropriate site, e.g., `newyork1 / newyork1->1st floor`.

   ![Screenshot](../../images/provision/img/pnp-image047.png)
2. Click **Next** to continue.

   ![Screenshot](../../images/provision/img/pnp-image049.png)

---

### Step 3: Check Image and Templates

1. Review the image and templates as prompted.
2. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/pnp-image051.png)
   3. Click on the device to check the template variables.

   ![Screenshot](../../images/provision/img/pnp-image053.png)
   4. Then check the hostname and stack. Then click **Next**.

   ![Screenshot](../../images/provision/img/pnp-image055.png)

---

### Step 4: Preview Configuration

1. Select the **Preview Configuration** option.

   ![Screenshot](../../images/provision/img/pnp-image057.png)
2. Ensure the hostname matches the one specified in the earlier steps.

   ![Screenshot](../../images/provision/img/pnp-image059.png)
3. After claiming, the status will remain unchanged initially. Click **Refresh** at the top of the table or wait 30 seconds for an automatic refresh.

   ![Screenshot](../../images/provision/img/pnp-image061.png)

---

### Step 5: Verify Switch in Inventory

1. Navigate to **Provision > Inventory**. Confirm the switch device appears in the inventory.

   ![Screenshot](../../images/provision/img/pnp-image063.png)

---

### Step 6: Provision Claimed Device

1. In Inventory, select the newly claimed switch device. Click **Actions > Provision > Provision device**.

   ![Screenshot](../../images/provision/img/pnp-image065.png)
2. Check the details and click **Next**.

   ![Screenshot](../../images/provision/img/pnp-image067.png)
   ![Screenshot](../../images/provision/img/pnp-image069.png)
3. Continue through the wizard, clicking **Next** as needed.

   ![Screenshot](../../images/provision/img/pnp-image071.png)
   ![Screenshot](../../images/provision/img/pnp-image073.png)
4. Click **Apply**.

   ![Screenshot](../../images/provision/img/pnp-image075.png)
5. Click **Next**.

   ![Screenshot](../../images/provision/img/pnp-image077.png)
6. Ensure the status is **Ready**, then click **Deploy**.

   ![Screenshot](../../images/provision/img/pnp-image079.png)
7. Click **Submit**.

   ![Screenshot](../../images/provision/img/pnp-image081.png)
8. If a success notification appears, the device has been provisioned successfully.

---

## Notes

- Ensure all device details and hostnames are accurate during the claiming and provisioning steps.
- If device status does not update automatically, use the manual refresh function.
- Follow on-screen prompts closely, as interface steps may vary slightly depending on software version.

---

**End of Guide**
