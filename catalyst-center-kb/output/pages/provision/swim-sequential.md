---
title: "SWIM Sequential Device Updates"
section: provision
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim-sequential/
images: 22
links: 0
---

# SWIM Sequential Device Updates

This guide outlines the process of performing sequential software image updates on multiple network devices using the Software Image Management (SWIM) feature. By following these steps, you will learn how to select devices, initiate a sequential update task, verify readiness, schedule distribution and activation, and monitor the update status.

---

### Navigation Path

Navigate to **Provision > Inventory** in the application interface.

![Screenshot](../../images/provision/img/swim-sequential-image001.jpg)

---

### Step 1: Select Software Images Focus

From the **Focus** dropdown menu, select **Software Images**.

![Screenshot](../../images/provision/img/swim-sequential-image003.jpg)

---

### Step 2: Select Target Devices

Identify and select the target devices for the update: **LDN1-C9300-DIST1.PseudoCo.com** and **LDN1-C9300-DIST2.PseudoCo.com**.

![Screenshot](../../images/provision/img/swim-sequential-image005.jpg)

---

### Step 3: Initiate Software Image Management

Navigate to **Action > Software Image > Software Image Management**. This action will redirect you to the **Software Image Management Page**.

![Screenshot](../../images/provision/img/swim-sequential-image007.jpg)

On the **Software Image Management Page**, re-select **LDN1-C9300-DIST1.PseudoCo.com** and **LDN1-C9300-DIST2.PseudoCo.com**, then click **Update Devices**.

![Screenshot](../../images/provision/img/swim-sequential-image009.jpg)

![Screenshot](../../images/provision/img/swim-sequential-image011.jpg)

![Screenshot](../../images/provision/img/swim-sequential-image013.jpg)

---

### Step 4: Enter Task Name

Enter a descriptive **Task Name** (e.g., "Sequential\_C9300\_Update") and click **Next**.

![Screenshot](../../images/provision/img/swim-sequential-image015.jpg)

---

### Step 5: Review Navigation Options

Review the navigation options available on this screen:
\* Click **Exit** to cancel the software update task.
\* Click **Back** to return to the previous step.
\* Click **Next** to proceed to the next step.

![Screenshot](../../images/provision/img/swim-sequential-image017.jpg)

---

### Step 6: Configure Sequential Update Order

In the **Device Activation Order** section, both **LDN1-C9300-DIST1.PseudoCo.com** and **LDN1-C9300-DIST2.PseudoCo.com** will be listed. Select both devices and click **Move to Sequential Update Order**.

![Screenshot](../../images/provision/img/swim-sequential-image019.jpg)

![Screenshot](../../images/provision/img/swim-sequential-image021.jpg)

![Screenshot](../../images/provision/img/swim-sequential-image023.jpg)

---

### Step 7: Perform Image Update Readiness Check

Click the **Update Readiness Report** link. An **Image Update Readiness Check** popup will appear, displaying the respective Device Readiness Report. Review the report, then close the popup to continue with the workflow.

![Screenshot](../../images/provision/img/swim-sequential-image025.jpg)

![Screenshot](../../images/provision/img/swim-sequential-image027.jpg)

---

### Step 8: Schedule Task and Clean Up

Configure the schedule for **Software Distribution** and **Software Activation**:
\* For **Software Distribution**, select **Now**.
\* For **Software Activation**, ensure **After Distribution** is **enabled**.

**Note:** The 'Software Activation Later' option is not supported for this use case.

Click **Submit** to proceed to the Summary page.

![Screenshot](../../images/provision/img/swim-sequential-image029.jpg)

---

### Step 9: Confirm Scheduled Distribution

On the Summary page, click **Submit** to schedule the distribution.

![Screenshot](../../images/provision/img/swim-sequential-image031.jpg)

---

### Step 10: View Image Update Status

To view the image update status, click the **Image update status** button.

![Screenshot](../../images/provision/img/swim-sequential-image033.jpg)

---

### Step 11: Monitor Sequential Update Progress

Monitor the status of the devices as they progress through the sequential update:

- **Initial Status:** **LDN1-C9300-DIST1.PseudoCo.com** is in **Distribution In-progress** state, while **LDN1-C9300-DIST2.PseudoCo.com** is in a **Waiting** state.
  ![Screenshot](../../images/provision/img/swim-sequential-image035.jpg)
- **Distribution Progress:** **LDN1-C9300-DIST1.PseudoCo.com** is now **Successfully Distributed & Activation In-progress**, and **LDN1-C9300-DIST2.PseudoCo.com** remains in a **Waiting** state.
  ![Screenshot](../../images/provision/img/swim-sequential-image037.jpg)
- **Activation Progress:** **LDN1-C9300-DIST1.PseudoCo.com** is **Successfully Distributed & Activated**, and **LDN1-C9300-DIST2.PseudoCo.com** is now in **Activation In-progress**.
  ![Screenshot](../../images/provision/img/swim-sequential-image039.jpg)

---

### Step 12: Observe Potential Failure Scenario

This image illustrates a scenario where **LDN1-C9300-DIST1.PseudoCo.com** is in **Distribution Success and Activation In-progress**, but **LDN1-C9300-DIST2.PseudoCo.com** has encountered a **Distribution failed** state.

![Screenshot](../../images/provision/img/swim-sequential-image041.jpg)

---

### Step 13: Review Final Device Status

The final status indicates that **LDN1-C9300-DIST1.PseudoCo.com** is **Device UpToDate** with the latest software image version, while **LDN1-C9300-DIST2.PseudoCo.com** remains in **Distribution Failure**.

![Screenshot](../../images/provision/img/swim-sequential-image043.jpg)
