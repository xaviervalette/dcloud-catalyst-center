---
title: "Design - Network Profiles Guide"
section: design
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/network_profiles/
images: 7
links: 0
---

# Design - Network Profiles Guide

This guide provides a comprehensive, step-by-step overview of how to effectively use and manage Network Profiles within the **Design** module. It is intended for users who need to assign sites to network profiles or modify existing profile configurations. By following these instructions, you will learn the updated process for managing network profiles, ensuring a streamlined and efficient design workflow.

---

## Table of Contents

1. [Overview](#overview)
2. [Accessing Network Profiles](#accessing-network-profiles)
3. [Assigning a Site to a Network Profile](#assigning-a-site-to-a-network-profile)
4. [Editing a Network Profile](#editing-a-network-profile)
5. [Notes & Best Practices](#notes--best-practices)

---

## Overview

Network Profiles are fundamental for defining and applying consistent network configurations across multiple sites. They allow you to standardize settings, attach templates, and manage wireless SSIDs, ensuring uniformity and simplifying large-scale deployments. This guide will walk you through the key processes involved in managing these profiles.

---

## Accessing Network Profiles

To begin managing your network profiles, navigate to the **Design** section and select **Network Profiles**.

![Screenshot](../../images/design/img/network_profiles-image000.png)
![Screenshot](../../images/design/img/network_profiles-image0000.png)

---

## Assigning a Site to a Network Profile

Follow these steps to assign a site to an existing network profile:

1. Locate the desired network profile from the list.
2. Click **Assign Site** to link a site to your selected network profile.
   ![Screenshot](../../images/design/img/network_profiles-image001.png)
   ![Screenshot](../../images/design/img/network_profiles-image003.png)
3. From the dialog box, choose the desired site(s) and click the **Save** button.
   ![Screenshot](../../images/design/img/network_profiles-image004.png)
4. A success notification will appear, confirming the site assignment.
   ![Screenshot](../../images/design/img/network_profiles-image004_1.png)
5. The 'Sites' column for that profile will now display the updated number of assigned sites.
   ![Screenshot](../../images/design/img/network_profiles-image004_2.png)

---

---

## Notes & Best Practices

- Always adhere to your organization's established naming conventions when creating or editing network profiles to maintain consistency and clarity.
- Exercise caution when assigning sites to profiles to prevent potential misconfigurations across different clusters.
- Remember to **Save** all changes after editing a profile or assigning sites to ensure your updates are successfully applied.
- For specific configuration requirements or advanced settings, always refer to your cluster-specific documentation.
