---
title: "Application Visibility (AVC) - Network Devices Enablement Guide"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/avc/
images: 20
links: 0
---

# Application Visibility (AVC) - Network Devices Enablement Guide

This guide provides step-by-step instructions for managing Application Visibility (AVC) settings on network devices within the Cisco platform. Specifically, it covers the processes for both disabling and enabling CBAR (Cisco Borderless Access Router) functionality on selected network devices. Following these steps will ensure proper configuration and deployment of AVC services.

## Provision > Services > Application Visibility > Network Devices Enablement

---

### Part 1: Disable CBAR

This section details the procedure for disabling CBAR on selected network devices.

1. **Select Devices and Initiate Disable CBAR**
   Navigate to `Provision > Services > Application Visibility > Network Devices Enablement`. In the site devices table, which lists all available devices, select the CBAR method devices for which you wish to disable CBAR.
   Then, select the `CBAR` option and choose `disable CBAR on selected device`.

   ![Screenshot](../../images/provision/img/avc-image001.jpg)

   ![Screenshot](../../images/provision/img/avc-image003.jpg)

   A confirmation pop-up window will appear. To continue, select `Yes`.
2. **Enter Task Name and Apply**
   Another pop-up window will appear. Enter a descriptive `Task Name` and then select `Apply`.

   ![Screenshot](../../images/provision/img/avc-image005.jpg)
3. **Review Pending Operations and Device Compliance (Step 1 of Task)**
   The first step of the task will load, displaying `Pending Operations` and `Device Compliance` checks.
   Ensure both checks are successful and appear in green. Once confirmed, click `Next`.
   If desired, you can recheck the status by clicking the `Recheck` button.

   ![Screenshot](../../images/provision/img/avc-image007.jpg)
4. **Prepare Device Configuration File (Step 2 of Task)**
   The second step of the task will load. This step prepares the configuration files for the selected devices.
   The names of the selected devices will appear on the left side of the page. The status will remain `in-progress` until the configuration files are fully prepared.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](../../images/provision/img/avc-image009.png)
5. **Preview and Deploy Configuration (Step 3 of Task)**
   The third step of the task will load. In this step, the device's configuration files are loaded and previewed.
   To proceed, click `Deploy`.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](../../images/provision/img/avc-image011.jpg)
6. **Configure Deployment Timing and Submit**
   Upon clicking `Deploy`, a pop-up window will appear on the right side of the page. Here, you can edit the task name if needed.
   You can also select the task deployment timing: `Now` (immediate deployment) or `Later` (at a specified time).
   To continue, click `Submit`.

   ![Screenshot](../../images/provision/img/avc-image013.jpg)
7. **Task Creation and Status Update**
   After submitting the task, it will be created in the `Task` section. The page will then return to the `site devices table` where the process began.
   In the site devices table, the selected device's CBAR Deployment status will initially show as `In-Progress`.
   If you refresh the page, the selected device's CBAR deployment status will be displayed as `Not Deployed`.
   The device's CBAR deployment status is now disabled.

   ![Screenshot](../../images/provision/img/avc-image015.jpg)

   ![Screenshot](../../images/provision/img/avc-image017.jpg)

---

### Part 2: Enable CBAR

This section details the procedure for enabling CBAR on selected network devices.

1. **Select Devices and Initiate Enable CBAR**
   Navigate to `Provision > Services > Application Visibility > Network Devices Enablement`. In the site devices table, which lists all available devices, select the CBAR method devices for which you wish to enable CBAR.
   Then, select the `CBAR` option and choose `enable CBAR on selected device`.

   ![Screenshot](../../images/provision/img/avc-image019.jpg)

   ![Screenshot](../../images/provision/img/avc-image021.jpg)

   A confirmation pop-up window will appear. To continue, select `Yes`.
2. **Confirm Enablement and Enter Task Name**
   A pop-up window will appear on the right side of the page. To continue, click `Next`.
   Another pop-up window will then load, displaying the selected device's name. To continue, click `Enable`.
   Finally, another pop-up window will appear. Enter a descriptive `Task Name` and then select `Apply`.

   ![Screenshot](../../images/provision/img/avc-image023.jpg)

   ![Screenshot](../../images/provision/img/avc-image025.jpg)

   ![Screenshot](../../images/provision/img/avc-image027.jpg)
3. **Review Pending Operations and Device Compliance (Step 1 of Task)**
   The first step of the task will load, displaying `Pending Operations` and `Device Compliance` checks.
   Ensure both checks are successful and appear in green. Once confirmed, click `Next`.
   If desired, you can recheck the status by clicking the `Recheck` button.

   ![Screenshot](../../images/provision/img/avc-image029.jpg)
4. **Prepare Device Configuration File (Step 2 of Task)**
   The second step of the task will load. This step prepares the configuration files for the selected devices.
   The names of the selected devices will appear on the left side of the page. The status will remain `in-progress` until the configuration files are fully prepared.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](../../images/provision/img/avc-image031.png)
5. **Preview and Deploy Configuration (Step 3 of Task)**
   The third step of the task will load. In this step, the device's configuration files are loaded and previewed.
   To proceed, click `Deploy`.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](../../images/provision/img/avc-image033.jpg)
6. **Configure Deployment Timing and Submit**
   Upon clicking `Deploy`, a pop-up window will appear on the right side of the page. Here, you can edit the task name if needed.
   You can also select the task deployment timing: `Now` (immediate deployment) or `Later` (at a specified time).
   To continue, click `Submit`.

   ![Screenshot](../../images/provision/img/avc-image035.jpg)
7. **Task Creation and Status Update**
   After submitting the task, it will be created in the `Task` section. The page will then return to the `site devices table` where the process began.
   In the site devices table, the selected device's CBAR Deployment status will initially show as `In-Progress`.
   If you refresh the page, the selected device's CBAR deployment status will be displayed as `Completed`.
   The device's CBAR deployment status is now enabled.

   ![Screenshot](../../images/provision/img/avc-image037.jpg)

   ![Screenshot](../../images/provision/img/avc-image039.jpg)
