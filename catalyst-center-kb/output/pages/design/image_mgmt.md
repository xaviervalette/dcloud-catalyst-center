---
title: "Device Image Repository – Golden Image Use Case"
section: design
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/image_mgmt/
images: 5
links: 0
---

# Device Image Repository – Golden Image Use Case

## Introduction

This demo guide provides step-by-step instructions for using the **Image Repository** feature within the Assurance > Device workflow, specifically focusing on the "Golden Image" use case. You will learn how to identify and manage device images, use global site-level filtering, and recognize devices running the current recommended (golden) OS image. The guide is designed for clarity, with visuals to assist each step.

---

## Steps

### Step 1: Accessing the Image Repository

Begin by navigating to the **Image Repository** section within the Assurance > Device area.

![Screenshot](../../images/design/img/image_mgmt-image001.png)

---

### Step 2: Global Site-Level Filtering

- The image repository currently supports filtering at the **global site level** only.
- Other site levels are not supported at this time.
- Use the available filters to narrow down device types such as routers, wireless LAN controllers (WLCs), etc.

![Screenshot](../../images/design/img/image_mgmt-image003.png)

---

### Step 3: Viewing Device Families

- Within the global site, available device family names are displayed in a table.
- Select a device family name to proceed to the next page, where you can review images specific to that family.

![Screenshot](../../images/design/img/image_mgmt-image005.png)

---

### Step 4: Identifying Golden Image Versions

- For each device family, if there is one or more image version matching the current (recommended) version, it will be highlighted with a **golden star**.
- The golden star visually indicates that the device is running the designated golden image.

![Screenshot](../../images/design/img/image_mgmt-image007.png)

---

### Step 5: Viewing Image Details

- Click on any image to view detailed information about that image version.

![Screenshot](../../images/design/img/image_mgmt-image009.png)

---

## Summary

This guide has outlined the process of navigating the Image Repository, filtering devices at the global site level, identifying device families, recognizing golden image versions, and accessing detailed image information. Use this workflow to maintain consistent and up-to-date device images across your network.
