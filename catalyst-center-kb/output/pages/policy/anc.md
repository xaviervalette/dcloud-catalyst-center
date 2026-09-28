---
title: "Policy Endpoint Overview"
section: policy
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/anc/
images: 7
links: 0
---

# Policy Endpoint Overview

This demo guide provides a step-by-step overview of using Adaptive Network Control (ANC) Policy with endpoints based on Trust Score in Cisco systems. You will learn how to identify endpoints with a low Trust Score, apply ANC policies, and reset Trust Scores as needed. Each stage is illustrated with screenshots for clarity.

---

## 1. AI Policy Endpoint Overview

Go to **Policy 🡪 AI Endpoint Analytics**

![anc-image001](../../images/policy/img/anc-image001.png)

This section presents a high-level view of policy endpoints. Here, you can monitor and manage endpoints within your network.

---

## 2. Selecting Endpoints with Low Trust Score

Click on the **Endpoint Inventory** tab.

After filtering or selecting endpoints with a Trust Score in the "Low (1-3)" range, you will see relevant endpoint details:

![Graphical user interface, application  Description automatically generated](../../images/policy/img/anc-image003.png)

Endpoints with a low Trust Score may require further investigation or remediation.

---

## 3. Applying the ANC Policy

Once the relevant endpoints are identified, you can apply an ANC Policy directly from the interface:

![Graphical user interface, application  Description automatically generated](../../images/policy/img/anc-image005.png)

Follow the prompts to select and enforce the desired policy on the selected endpoints.

![Graphical user interface, text, application  Description automatically generated](../../images/policy/img/anc-image007.png)

You will receive visual confirmation that the ANC Policy has been successfully applied.

![Graphical user interface, text, application  Description automatically generated](../../images/policy/img/anc-image009.png)

Detailed policy actions and their outcomes are displayed for each affected endpoint.

![Graphical user interface, text, application  Description automatically generated](../../images/policy/img/anc-image011.png)

---

## 4. Resetting the Trust Score

If necessary, you can reset the Trust Score for an endpoint after applying and verifying the ANC Policy:

![Graphical user interface, application  Description automatically generated](../../images/policy/img/anc-image013.png)

This action restores the Trust Score and allows normal network access, assuming the endpoint is deemed secure.

---

## Summary

- Begin with a Policy Endpoint overview to understand the current state.
- Filter and identify endpoints with a low Trust Score (1-3).
- Apply appropriate ANC Policies to mitigate risk.
- Reset Trust Scores as needed to restore endpoint status.

Use this guide as a reference to efficiently demonstrate the process of managing endpoint security using Cisco's ANC Policy features.

---
