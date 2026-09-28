---
title: "IoT Services – App Hosting on Cisco Catalyst 9100 Series Access Points"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/iot-services-app/
images: 18
links: 0
---

# IoT Services – App Hosting on Cisco Catalyst 9100 Series Access Points

## Introduction

This demo guide provides a step-by-step walkthrough for hosting applications on Cisco Catalyst 9100 Series Access Points using the Cisco DNA Center (DNAC) IoT Services. The process leverages the modular IOx framework, enabling developers to deploy Docker-style container applications directly onto access points. This allows seamless integration of third-party software and hardware, enhancing flexibility for various IoT use cases.

Follow the steps below to provision and manage an IoT application on your Cisco Catalyst 9100 series APs.

---

## Step-by-Step Instructions

### Step 1: Navigate to IoT Services

From the main menu, go to **Provision > Services > IoT Services**.

---

### Step 2: Access MeshConnect

Click the **MeshConnect** icon from the DNAC IoT Services page.

![iot-services-app-image001](../../images/assurance/img/iot-services-app-image001.png)

---

### Step 3: Install the Application

On the application metadata page, click **Install**.

![iot-services-app-image002](../../images/assurance/img/iot-services-app-image002.png)
![iot-services-app-image003](../../images/assurance/img/iot-services-app-image003.png)

---

### Step 4: Enter Task Name

Enter a valid task name and click the **Next** button to proceed.

---

### Step 5: Navigation Options

![iot-services-app-image004](../../images/assurance/img/iot-services-app-image004.png)

- **Exit**: Cancel and exit the current task.
- **Back**: Return to the previous step.
- **Next**: Proceed to the next step.

---

### Step 6: Continue Setup

![iot-services-app-image005](../../images/assurance/img/iot-services-app-image005.png)

---

### Step 7: Select Access Point

![iot-services-app-image006](../../images/assurance/img/iot-services-app-image006.png)

Select one access point and click the **Next** button.

---

### Step 8: Review Selection

![A white background with black text Description automatically generated](![iot-services-app-image007](../../images/assurance/img/iot-services-app-image007.png)

---

### Step 9: Download Summary and Provision

![iot-services-app-image008](../../images/assurance/img/iot-services-app-image008.png)

- Click on the **Download Summary** link to download the summary CSV file.
- Click the **Provision** button to start provisioning.

---

### Step 10: Monitor Provisioning Status

![A white background with blue and white text Description automatically generated](![iot-services-app-image009](../../images/assurance/img/iot-services-app-image009.png)

- The provisioning state will change from "In-Progress" to "Provisioned" after approximately 60 seconds.
- Click the **View Details** link to see the details popup.

![iot-services-app-image010](../../images/assurance/img/iot-services-app-image010.png)

![iot-services-app-image011](../../images/assurance/img/iot-services-app-image011.png)

---

### Step 11: Manage the IoT App

![iot-services-app-image012](../../images/assurance/img/iot-services-app-image012.png)

Click the **Manage IoT App** button to proceed.

---

### Step 12: Select Hostname

![iot-services-app-image013](../../images/assurance/img/iot-services-app-image013.png)

Click on the hostname to continue.

---

### Step 13: Download App Logs

![iot-services-app-image014](../../images/assurance/img/iot-services-app-image014.png)
![iot-services-app-image015](../../images/assurance/img/iot-services-app-image015.png)

- To download the log file, select the access point and click the **App Logs** link.
- Select the desired log file from the dropdown menu and click **Download**.

---

### Step 14: View Sample Log File

**Sample logs file:**

![iot-services-app-image016](../../images/assurance/img/iot-services-app-image016.png)

---

### Step 15: View Details

![iot-services-app-image017](../../images/assurance/img/iot-services-app-image017.png)

Click the **View** icon in the Details section.

---

### Step 16: Check Health Status

Click on **See Details** under the "Healthy" status. You can view both Error and Output information in the popup window.

![iot-services-app-image018](../../images/assurance/img/iot-services-app-image018.png)

---
