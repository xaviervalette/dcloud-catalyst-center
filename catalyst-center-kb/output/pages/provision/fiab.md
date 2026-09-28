---
title: "Fabric In a Box (FIAB)"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/fiab/
images: 45
links: 0
---

# Fabric In a Box (FIAB)

## Introduction

This demo guide provides step-by-step instructions for deploying Fabric In a Box (FIAB) and configuring Anycast Gateways using Cisco's network management interface. The guide walks you through:
- Navigating to the fabric site and configuring device roles
- Creating and verifying Anycast Gateways
- Attaching a Wireless SSID to Virtual Networks

Each step includes screenshots for visual reference, ensuring a smooth and successful demonstration.

---

## 1. Accessing the Fabric Site

**Step 1:**  
Navigate to **Main menu → Provision → Fabric Sites**. You will land on the following screen. Click on the desired fabric site's number.

![Screenshot](../../images/provision/img/fiab-image001.png)

**Step 2:**  
Click on the **London2** site.

![Screenshot](../../images/provision/img/fiab-image003.png)

**Step 3:**  
In the topology view, click on the device named **LDN2-C9300-FIAB.PseudoCo.com**.

![Screenshot](../../images/provision/img/fiab-image005_new.png)

The following screen will appear:

![Screenshot](../../images/provision/img/fiab-image007.png)

---

## 2. Configuring Device Roles in the Fabric Tab

**Step 4:**  
Within the **Fabric** tab, enable each device role in sequence:

- **Border Node:** Enter the required details and click **Add**.

![Screenshot](../../images/provision/img/fiab-image009.png)

- **Control Plane:** Select **LISP Pub / Sub** and click the **Add** button.

![Screenshot](../../images/provision/img/fiab-image011.png)

A new window will open:

![Screenshot](../../images/provision/img/fiab-image013.png)

- **Edge Node:** Enable the Edge Node role, but **do not click Add yet**.

![Screenshot](../../images/provision/img/fiab-image015.png)

- **Embedded Wireless LAN Controller:**  
  This step has sub-steps as shown in the screenshots below:
- The scope (e.g., London2 → 1st Floor) is selected automatically.

![Screenshot](../../images/provision/img/fiab-image017.png)

- Advanced options.

![Screenshot](../../images/provision/img/fiab-image019.png)

- Summary view.

![Screenshot](../../images/provision/img/fiab-image021.png)

After completing the above, click the **Add** button on the final step.

![Screenshot](../../images/provision/img/fiab-image023.png)

Then, click the **Deploy** button.

![Screenshot](../../images/provision/img/fiab-image025_new.png)

Follow the remaining prompts as shown:

![Screenshot](../../images/provision/img/fiab-image027.png)
![Screenshot](../../images/provision/img/fiab-image029.png)
![Screenshot](../../images/provision/img/fiab-image031.png)
![Screenshot](../../images/provision/img/fiab-image033.png)
![Screenshot](../../images/provision/img/fiab-image035.png)

Once the task is submitted, the roles will be attached to **LDN2-C9300-FIAB.PseudoCo.com** and the device icon will update accordingly.

![Screenshot](../../images/provision/img/fiab-image037_new.png)
![Screenshot](../../images/provision/img/fiab-image039_new.png)

---

## 3. Creating an Anycast Gateway

### Step 1: Initial Checks

Before starting, verify the following for the **VN\_Employees** virtual network:

- **Layer 3 Virtual Networks tab:**  
  Anycast Gateway count should be 0.

![Screenshot](../../images/provision/img/fiab-image041.png)

- **Layer 2 Virtual Networks tab:**  
  There should be no entry with VN\_Employees in the "Associated Layer 3 Virtual Network" column.

![Screenshot](../../images/provision/img/fiab-image043.png)

- **Anycast Gateway tab:**  
  No entry for VN\_Employees in the "Associated Layer 3 Virtual Network" column.

![Screenshot](../../images/provision/img/fiab-image045.png)

---

### Step 2: Create Anycast Gateway

- Click on **Create Anycast Gateways**.
- Select **VN\_Employees Virtual Network** using the "+" icon.

![Screenshot](../../images/provision/img/fiab-image047.png)
![Screenshot](../../images/provision/img/fiab-image049.png)

Click **Next**.

---

### Step 3: Configure Attributes

On the **Configuration Attributes** page, fill in the following:

- **IP Address Pool:** Select `LDN2_10.10.23.128_SDA_Employees [10.10.23.128/26]`
- **IP-Directed Broadcast:** Check this box
- **TCP MSS Adjustment:** Check and enter a value between 500–1440
- **VLAN Name:** Enter a name, e.g., `VLAN-VN_Employees`
- **VLAN ID:** 1120 (or any valid value)
- **Fabric-Enabled Wireless:** Check this box
- **Multiple IP-to-MAC Addresses:** Check this box

Leave other settings at default, then click **Next**.

![Screenshot](../../images/provision/img/fiab-image051.png)

---

### Step 4: Fabric Zone

- No data entry required in this section. Click **Next**.

![Screenshot](../../images/provision/img/fiab-image053.png)

---

### Step 5: Summary and Deployment

- Review the summary of your configuration and click **Next**.

![Screenshot](../../images/provision/img/fiab-image055.png)

---

### Step 6: Finalize Deployment

- Click **Deploy** to complete the workflow.

![Screenshot](../../images/provision/img/fiab-image057.png)
![Screenshot](../../images/provision/img/fiab-image059.png)
![A white background with text  Description automatically generated](data:image/png;base64...)

![Screenshot](../../images/provision/img/fiab-image061.png)
![Screenshot](../../images/provision/img/fiab-image063.png)

---

### Step 7: Review Results

After deployment, you will see a confirmation screen:

![Screenshot](../../images/provision/img/fiab-image065.png)

Click **View Anycast Gateways** to proceed.

---

### Step 8: Verify Anycast Gateway

You will be directed to the **Anycast Gateways** tab, where the newly created entry appears.

![Screenshot](../../images/provision/img/fiab-image067.png)

---

### Step 9: Verify Layer 2 Virtual Network Entry

Go to **Layer 2 Virtual Networks** to see the new entry with the values you created.

![Screenshot](../../images/provision/img/fiab-image069.png)

---

### Step 10: Confirm Anycast Gateway Count

On the **Layer 2 Virtual Networks** tab, confirm that the Anycast Gateway count has increased for **VN\_Employees**.

![Screenshot](../../images/provision/img/fiab-image071.png)

---

## 4. Wireless SSID Attachment to Virtual Networks

### Step 1: Access Wireless SSID Tab

Click on the **Wireless SSID** tab.

![Screenshot](../../images/provision/img/fiab-image073.png)

---

### Step 2: Deploy Wireless SSID

Select the values as shown in the screenshot, then click **Deploy** and follow the workflow.

![Screenshot](../../images/provision/img/fiab-image075.png)
![Screenshot](../../images/provision/img/fiab-image077.png)
![Screenshot](../../images/provision/img/fiab-image079.png)

---

### Step 3: Preview and Deploy

Review your configuration in the **Preview Configuration** step, then click **Deploy**.

![Screenshot](../../images/provision/img/fiab-image081.png)
![Screenshot](../../images/provision/img/fiab-image083.png)

After completion, you will see a confirmation screen with your selected values:

![Screenshot](../../images/provision/img/fiab-image085.png)
![Screenshot](../../images/provision/img/fiab-image087.png)

---

## Conclusion

You have now successfully completed the FIAB demo, including configuration of device roles, Anycast Gateway creation, and Wireless SSID attachment. Use this guide as a reference for future deployments and demonstrations.
