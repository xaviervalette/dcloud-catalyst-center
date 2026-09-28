---
title: "Cisco GBAC Policy Management Demo Guide"
section: policy
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/gbac/
images: 32
links: 0
---

# Cisco GBAC Policy Management Demo Guide

## Introduction

This guide provides a comprehensive, step-by-step walkthrough for demonstrating policy management using Cisco Group-Based Access Control (GBAC). It is designed for demo users to easily understand and navigate the key functionalities. The topics covered include configuring Security Groups, managing ISE Profiles, setting up StealthWatch Host Groups, and creating, editing, and managing access policies. By following the clear instructions and visual aids provided, users will learn how to view group details, establish and modify contract policies, and effectively control network access in a structured and efficient manner.

---

## Table of Contents

1. [Overview - Security Group](#overview---security-group)
2. [Viewing Group Details](#viewing-group-details)
3. [Editing and Creating Contract Policies](#editing-and-creating-contract-policies)
4. [Overview - ISE Profiles](#overview---ise-profiles)
5. [Overview - StealthWatch Host Groups](#overview---stealthwatch-host-groups)
6. [Policy Management](#policy-management)
7. [Editing Policy Contracts](#editing-policy-contracts)
8. [Security Group and Access Contract](#security-group-and-access-contract)
9. [Conclusion](#conclusion)

---

## 1. Overview - Security Group

To access Security Group settings, navigate to **Policy > Group-Based Access Control**.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image001.png)

Click on **Security Groups**.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image003.png)

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image005.png)

---

## 2. Viewing Group Details

To view the details of any group:

- **Select any group** from the list to display its details.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image007.png)

- **Select a group** from the left panel, as shown below:

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image009.png)
![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image011.png)

- The group details will be displayed. Use the **Outbound** and **Inbound** tabs to view respective details.

---

## 3. Editing and Creating Contract Policies

To edit or create a new contract policy:

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image008.png)
Click on **Guests** and then click on **Lighting**.

- **Select the group** (e.g., "Guest -> Lighting").
  ![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image012.png)

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image013.png)

- Click **Edit Contract Policy**.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image015.png)

- **Add a new contract** and click **Next**.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image017.png)

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image019.png)

- **Enter the contract name and description**, then click **Save**.

---

## 4. Overview - ISE Profiles

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image020.png)

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image021.png)

---

## 5. Overview - StealthWatch Host Groups

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image022.png)

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image023.png)

---

## 6. Policy Management

You can view and manage existing policies here:

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image025.png)

To create a new policy:

- Select the **Auditors -> HVAC** group, then click **Change Contract**.
  ![screenshot](../../images/policy/img/gbac-image026.png)

![screenshot](../../images/policy/img/gbac-image027.png)
\* Click on **Change Contract**

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image029.png)
\* Select the Contract and click on **Change**

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image031.png)
\* Click on **Save Now** to save

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image033.png)

> **Note:** After creation, please refresh the policy matrix. The color will update to reflect changes.

---

## 7. Editing Policy Contracts

To edit an existing policy (e.g., for Auditors -> HVAC), click on the policy you wish to edit.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image033.png)

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image037.png)

- Change the policy action from **PermitIP** to **DenyIP** as needed.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image039.png)

- Select **Deny IP**.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image041.png)

- Click on **Save Now**.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image035.png)

> **Note:** After editing, please refresh the policy matrix. The color will update to reflect changes.

---

## 8. Security Group and Access Contract

View security group and access contract details as follows:

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image045.png)
Click on **Create Security Group** to create a new Security Group.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image047.png)
Click on **Save Now** to save. The new security group will then be visible.

### Access the contract information here:

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image048.png)
Click on **Create Access Contract** to create a new Access Contract.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image049.png)
Click on **Save Now** to save.

![A screenshot of a computer  Description automatically generated](../../images/policy/img/gbac-image051.png)
The newly created Access Contract will be visible in the list.

---

## 9. Conclusion

This demo guide has outlined the core steps for viewing, creating, and editing policies within Cisco GBAC, including managing security groups and access contracts. Refer to the screenshots at each stage for visual guidance. For further details, consult the official Cisco documentation or your system administrator.
