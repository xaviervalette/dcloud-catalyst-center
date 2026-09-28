---
title: "Path Trace_User360"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/pathtrace/
images: 8
links: 0
---

# Path Trace\_User360

## Overview

This guide provides a step-by-step walkthrough for using the **Path Trace\_User360** feature. The demo covers how to search for a user, navigate to the User 360 view, select a device, run a path trace between a device and a target (such as a camera), and interpret the resulting network topology, VLAN connections, and ACL status. This process helps users visualize network paths and validate connectivity or configuration issues.

---

## Steps

### Step 1: Search for the User

On the Homepage, click the global search bar as shown in the first image below.  
Type **"grace"** in the search field, select **Grace Smith** from the users list, and then click **User 360** on the right side.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image001.png)  
![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image003.png)

---

### Step 2: Select a Device

In the **Grace Smith User 360** view, click on any one of Grace Smith’s devices, as shown below.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image005.png)

---

### Step 3: Access Path Trace Tool

Scroll down on the page to locate the **Path Trace** section within the Tools dashboard.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image007.png)

---

### Step 4: Run Path Trace

Click **Run Path Trace**.  
A pop-up will appear on the right side. In this pop-up, both **Source** and **Destination** drop-down menus will display all available client IPs and device details.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image009.png)

---

### Step 5: Set Source and Destination

- Leave the **Source** as it is (selected Grace Smith’s device IP).
- Set the **Destination** to **10.10.13.214** (Camera 1 IP).
- Click **Start** to initiate the path trace.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image011.png)

---

### Step 6: View the Topology

The tool will display the network topology between the selected source and destination.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image013.png)

---

### Step 7: Verify Source, Destination, and Network Details

In the topology view, confirm that the **Source** and **Destination** match your selections from the drop-down menus.  
Additionally, review the VLAN connections and ACL (Access Control List) status defined on the devices, as shown below.

![A screenshot of a computer  Description automatically generated](../../images/assurance/img/pathtrace-image015.png)

---

## Notes

- Ensure you have the necessary permissions to access User 360 and Path Trace features.
- If any device or user is not found during the search, verify spelling or consult your admin for access.
- The screenshots above illustrate each step for clarity; your interface may have minor visual differences based on your platform version.

---

This concludes the Path Trace\_User360 demo guide.
