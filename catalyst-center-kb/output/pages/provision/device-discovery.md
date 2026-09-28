---
title: "Device Discovery and Provisioning Guide"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/device-discovery/
images: 53
links: 0
---

# Device Discovery and Provisioning Guide

This guide provides a comprehensive walkthrough of the device discovery, assignment, and provisioning processes within the platform. It outlines how to discover network devices, assign them to existing or newly created sites, and provision them for network integration. Additionally, this document covers the steps for creating new network hierarchy elements, such as areas, buildings, and floors, to organize your network infrastructure effectively.

---

## Navigating to the Tools & Discovery Page

To begin, navigate to the **Tools & Discovery** page. This is your central hub for managing device discovery operations.

![Screenshot](../../images/provision/img/device-discovery-image001.png)

---

## Discovery Actions

The Discovery page allows you to perform several key actions:

1. **Cloning Discovery**
2. **Rediscovery**
3. **Adding New Discovery**

---

### Cloning a Discovery

To clone an existing discovery, follow these steps:

1. Ensure there is at least one existing discovery available.
2. On the Discovery Dashboard page, locate the desired discovery. Under the "Action" section, click on the **three dots** (`...`).

   ![Screenshot](../../images/provision/img/device-discovery-image002.png)
3. From the dropdown menu, click on **Copy and Edit**.

   ![Screenshot](../../images/provision/img/device-discovery-image003.png)
4. Review the discovery settings and click **Next** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image004.png)
5. Ensure the checkbox for CLI credentials is selected, then click **Next** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image005.png)
6. Select at least one SNMP credential, then click **Next** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image006.png)
7. Click **Next** to continue through the scheduling options.
   ***Note: Scheduling the job later is not supported for cloned discoveries.***

   ![Screenshot](../../images/provision/img/device-discovery-image007.png)
8. Click on **Start Discovery** to initiate the discovery process.

   ![Screenshot](../../images/provision/img/device-discovery-image008.png)
9. To view the discovered devices, click on the **View Discovery** link.

   ![Screenshot](../../images/provision/img/device-discovery-image009.png)
10. The discovered devices will be displayed on this page.

    ![Screenshot](../../images/provision/img/device-discovery-image010.png)

---

### Re-Discovering Devices

You can re-discover devices using an existing discovery. This is useful for updating device information or finding new devices within the same scope.

1. On the Discovery Dashboard page, locate the existing discovery you wish to re-run. Under the "Action" section, click on the **three dots** (`...`) and select **Re-discover**.

   ![Screenshot](../../images/provision/img/device-discovery-image011.png)
2. Enter a task name for the re-discovery process, then click **Discover** to start.

   ![Screenshot](../../images/provision/img/device-discovery-image012.png)
3. The status of the re-discovery process will be displayed in the "Status" column, progressing from **Queued**, to **In Progress**, and finally to **Completed**.

   ![Screenshot](../../images/provision/img/device-discovery-image013.png)
   ![Screenshot](../../images/provision/img/device-discovery-image014.png)
   ![Screenshot](../../images/provision/img/device-discovery-image015.png)

---

### Creating a New Discovery

The Discovery feature scans your network for devices and adds them to the inventory. You can discover devices using methods such as Link Layer Discovery Protocol (LLDP), CDP, CIDR, or an IP address range.

To start a new discovery:

1. Click on **Add Discovery**.

   ![Screenshot](../../images/provision/img/device-discovery-image016.png)
2. Select your preferred discovery method. For this demonstration, we are using an **IP address range** to discover devices. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image017.png)
3. Ensure the checkbox for CLI credentials is selected. SNMP Read & Write credentials are selected by default. Click **Next** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image005.png)
4. Select the Global NETCONF port, then click **Next** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image018.png)
5. Select the HTTP(S) Write credentials, then click **Next** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image019.png)
6. On the Schedule Job page, select **Now**, then click **Next** to continue.
   ***Note: Assigning devices to an existing site during the discovery process is not supported. This will be done in a subsequent step.***

   ![Screenshot](../../images/provision/img/device-discovery-image020.png)
7. Click on **Start Discovery** to begin the process.

   ![Screenshot](../../images/provision/img/device-discovery-image021.png)
8. Click on **View Discovery** to check the details of the discovery process and its results.

   ![Screenshot](../../images/provision/img/device-discovery-image022.png)
9. This page displays the devices that have been discovered. To return to the Discovery dashboard, click on the **All Discoveries** link.

   ![Screenshot](../../images/provision/img/device-discovery-image023.png)
   ![Screenshot](../../images/provision/img/device-discovery-image024.png)

---

## Assigning Discovered Devices to a Site

Newly discovered devices will appear in the Inventory page as "Unassigned". You can assign these devices to an existing site or a newly created one.

1. Navigate to **Provision -> Inventory**.
2. Filter the devices by "Unassigned" to easily locate them.

   ![Screenshot](../../images/provision/img/device-discovery-image025.png)
3. Select the newly discovered device and click **Assign**.

   ![Screenshot](../../images/provision/img/device-discovery-image026.png)
4. Choose a site for the device. For this demonstration, select **New York 1**. Click **Save** to proceed.
   *You can select an existing site or create a new site under* *Design -> Network Hierarchy* *before assigning the discovered device.*

   ![Screenshot](../../images/provision/img/device-discovery-image027.png)
   ![Screenshot](../../images/provision/img/device-discovery-image028.png)
5. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image029.png)
6. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image030.png)
7. Click on **Preview** to review the assignment details.

   ![Screenshot](../../images/provision/img/device-discovery-image031.png)
8. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image032.png)
9. Once the status changes to **Ready**, click on **Deploy** to apply the site assignment.

   ![Screenshot](../../images/provision/img/device-discovery-image033.png)
10. Click on **Submit** to finalize the site assignment.

    ![Screenshot](../../images/provision/img/device-discovery-image034.png)
11. Now, if you navigate back to Inventory, you will see that the new device is successfully assigned to the selected site.

    ![Screenshot](../../images/provision/img/device-discovery-image035.png)

---

## Provisioning a Discovered Device

After assigning a device to a site, the next step is to provision it.

1. Select the newly discovered switch in the Inventory.
2. Click on **Actions -> Provision -> Provision Device**.

   ![Screenshot](../../images/provision/img/device-discovery-image036.png)
3. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image037.png)
4. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image038.png)
5. Verify the details in the Summary section and click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image039.png)
6. Enter a Task Name if desired, or leave it as default and click **Apply** to continue the flow.

   ![Screenshot](../../images/provision/img/device-discovery-image040.png)
7. Click **Next** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image041.png)
8. When the status is **Ready**, click on **Deploy** to continue.

   ![Screenshot](../../images/provision/img/device-discovery-image042.png)
9. Enter a task name and click on **Submit** to proceed.

   ![Screenshot](../../images/provision/img/device-discovery-image043.png)
10. Once the process is complete, navigate to Inventory. You will see that the new switch has been successfully provisioned.

    ![Screenshot](../../images/provision/img/device-discovery-image044.png)

---

## Creating a New Site (Network Hierarchy)

You can provision discovered devices to a newly created site as well. The steps for creating a new site involve defining Areas, Buildings, and Floors within the network hierarchy.

### Create New Site Elements

1. Navigate to **Design -> Network Hierarchy**.

   ![Screenshot](../../images/provision/img/device-discovery-image045.png)

### Adding an Area

1. To add an Area, click on the **three dots** (`...`) next to "Global" or any other existing area.
2. Enter the Area name.

   ![Screenshot](../../images/provision/img/device-discovery-image046.png)
3. After entering the area name, click **Add**.

   ![Screenshot](../../images/provision/img/device-discovery-image047.png)

### Adding a Building

1. To add a Building, click on the **three dots** (`...`) next to "Global" or any other area.
2. Click on **Add Building**.

   ![Screenshot](../../images/provision/img/device-discovery-image048.png)
3. Enter the building name and address of the building, then click **Add** to create the building.

   ![Screenshot](../../images/provision/img/device-discovery-image049.png)

### Adding a Floor

1. To add a Floor for any building, click the **three dots** (`...`) next to the desired building.
2. Then, click **Add Floor**.

   ![Screenshot](../../images/provision/img/device-discovery-image050.png)
3. Enter the floor name and click on **Add** to create the floor.
   ***Note: Currently, adding a floor plan is not supported.***

   ![Screenshot](../../images/provision/img/device-discovery-image051.png)
4. Click on **Ok** to complete the floor creation.

   ![Screenshot](../../images/provision/img/device-discovery-image052.png)
