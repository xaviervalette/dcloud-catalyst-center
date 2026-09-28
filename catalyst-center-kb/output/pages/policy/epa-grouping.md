---
title: "AI Endpoint Analytics Smart Grouping"
section: policy
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/epa-grouping/
images: 13
links: 0
---

# AI Endpoint Analytics Smart Grouping

## Introduction

This demo guide provides a step-by-step walkthrough of the AI Endpoint Analytics Smart Grouping feature in Kronos. The process covers how to review, accept, modify, or reject AI-proposed endpoint grouping rules, and how these actions impact your group's configuration within the Endpoint Analytics dashboard. The guide is split into two main parts: accepting and reviewing Smart Grouping proposals, and rejecting groupings.

---

## Understanding Smart Grouping & AI Proposals

**Smart Grouping** uses AI to analyze endpoint data and propose new grouping rules. Within the **AI Proposals** section, you will find:
- **New rules/groups** discovered by Smart Grouping
- **Suggested modifications** for previously accepted rules
- **Suggestions to delete** previously accepted rules

Navigate to:  
`Policy > AI Endpoint Analytics`
![epa-grouping-image000](../../images/policy/img/epa-grouping-image000.png)

---

## Part 1: Accepting and Reviewing AI-Proposed Endpoint Groups

### Step 1: Initial Endpoint Group Review

There will be two endpoint groups proposed by Smart Grouping.

![epa-grouping-image001](../../images/policy/img/epa-grouping-image001.png)

---

### Step 2: Exploring Endpoint Group Details

You can review the details of each endpoint group by navigating through the available tabs: **Summary**, **Profile Rule**, and **Endpoints**.

![epa-grouping-image003](../../images/policy/img/epa-grouping-image003.png)

After reviewing, select **Next** to proceed.

---

### Step 3: Filling Endpoint Group Details

Fill in all required fields for the endpoint group. Dropdown menus will appear as you type; it is acceptable to leave fields as null if necessary.

![epa-grouping-image005](../../images/policy/img/epa-grouping-image005.png)

---

### Step 4: Reviewing or Saving Grouping Rules

At this stage, you have two options:
- **Review More Rules(s) for Profiling**: This will redirect you back to **Step 1** to review additional proposals.
- **Review Endpoint Inventory**: This will take you to the Profiling Rules Policy page, where your newly added group will appear.

![epa-grouping-image007](../../images/policy/img/epa-grouping-image007.png)
![epa-grouping-image009](../../images/policy/img/epa-grouping-image009.png)

Upon completing the addition, the new group will be listed on the Profiling Rules Policy page.

![epa-grouping-image011](../../images/policy/img/epa-grouping-image011.png)
![epa-grouping-image013](../../images/policy/img/epa-grouping-image013.png)

---

## Part 2: Rejecting AI-Proposed Endpoint Groups

### Step 1: Reviewing the AI Proposal Count

On the **Overview** page, the AI Proposals dashlet will display the current count of pending proposals (e.g., reducing from 2 to 1 after an action).

![epa-grouping-image015](../../images/policy/img/epa-grouping-image015.png)

Select **Review** to proceed.

![epa-grouping-image017](../../images/policy/img/epa-grouping-image017.png)

There will now be one remaining endpoint group, and you can review its **Summary**, **Profile Rule**, and **Endpoints** tabs.

---

### Step 2: Rejecting an Endpoint Group

To reject a proposed grouping:
- Select **Reject Grouping** at the bottom of the group details page.
- Choose the appropriate reason and submit.

![epa-grouping-image019](../../images/policy/img/epa-grouping-image019.png)

After submission, the endpoint group profile will be deleted from the list.

![epa-grouping-image021](../../images/policy/img/epa-grouping-image021.png)

Returning to the home page, the AI Proposal count should now be 0, indicating no pending proposals.

![epa-grouping-image023](../../images/policy/img/epa-grouping-image023.png)

---

## Conclusion

This guide has outlined the full lifecycle for reviewing, accepting, and rejecting AI-proposed endpoint groupings within the Kronos AI Endpoint Analytics platform. By following these steps, you can efficiently manage and refine your organization's endpoint groups using intelligent AI recommendations.
