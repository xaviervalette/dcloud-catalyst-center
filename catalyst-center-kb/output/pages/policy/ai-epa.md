---
title: "AI Endpoint Analytics Spoofing Detection"
section: policy
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/ai-epa/
images: 11
links: 0
---

# AI Endpoint Analytics Spoofing Detection

## Introduction

This guide provides detailed, step-by-step instructions for using AI Endpoint Analytics to detect spoofing, manage trust scores, apply Adaptive Network Control (ANC) policies, and organize endpoint hierarchies. The instructions below are designed to help users navigate the interface efficiently, understand core features, and demonstrate each capability with ease. All screenshots referenced are included in their respective steps for visual guidance.

---

## Table of Contents

1. [Reset Trust Score](#reset-trust-score)
2. [Apply ANC Policy](#apply-anc-policy)
3. [Manage Endpoint Hierarchy](#manage-endpoint-hierarchy)
4. [Other Supported Pages](#other-supported-pages)

---

## 1. Reset Trust Score

The Reset Trust Score feature allows you to update the trust score for endpoints identified as potentially spoofed.

Navigate to **Policy** 🡪 **AI Endpoint Analytics** in your dashboard.

![ai-epa-image001](../../images/policy/img/ai-epa-image001.png)

1. Ensure that all dashlets (dashboard widgets) are displaying data as expected.

   ![ai-epa-image003](../../images/policy/img/ai-epa-image003.png)
2. Go to the **Trust Score** tab by selecting "Low" from the Trust Score filter. This will automatically show endpoints with low trust scores.

   ![ai-epa-image005](../../images/policy/img/ai-epa-image005.png)
3. Locate an endpoint with a low trust score (for example, Trust Score = 1),then select **Reset Trust Score**

   ![ai-epa-image007](../../images/policy/img/ai-epa-image007.png)
4. In the confirmation popup, click **Reset** to confirm your action.

   ![ai-epa-image009](../../images/policy/img/ai-epa-image009.png)
5. Once reset, the endpoint’s Trust Score will automatically update to a value above 4

   ![ai-epa-image011](../../images/policy/img/ai-epa-image011.png)

---

## 2. Apply ANC Policy

Go to **Policy 🡪 AI Endpoint Analytics**

1. Select the desired endpoint and click **Apply ANC Policy**.

   ![ai-epa-image013](../../images/policy/img/ai-epa-image013.png)
2. In the popup, choose the appropriate policy from the dropdown menu and click **Apply**.

   ![ai-epa-image015](../../images/policy/img/ai-epa-image015.png)
3. The selected ANC (Adaptive Network Control) Policy will now be enforced on the chosen network endpoint.

   ![ai-epa-image017](../../images/policy/img/ai-epa-image017.png)

---

## 3. Manage Endpoint Hierarchy

1. Navigate to **Policy 🡪 AI Endpoint Analytics 🡪 Hierarchy**.

   ![ai-epa-image019](../../images/policy/img/ai-epa-image019.png)
2. In this section, you can create new endpoint types.

   Endpoints can be easily organized by dragging and dropping them into the desired endpoint types or hierarchy levels.

   ![ai-epa-image021](../../images/policy/img/ai-epa-image021.png)

---

## 4. Other Supported Pages

All other pages within the AI Endpoint Analytics interface are also supported with relevant data and functionality. Refer to the navigation menu for access to additional features.

---

## Notes

- Ensure you have the necessary permissions to reset trust scores and apply policies.
- All screenshots reflect the actual user interface at the time of writing.
- Follow your organization’s standard practices for policy application and endpoint management.

---
