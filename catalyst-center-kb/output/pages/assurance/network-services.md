---
title: "Network Services Assurance - DNS Demo Guide"
section: assurance
source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/network-services/
images: 10
links: 0
---

# Network Services Assurance - DNS Demo Guide

This demo guide provides a step-by-step walkthrough of how to access and interpret DNS (Domain Name System) network services assurance data within the Cisco dashboard. You will learn how to navigate to the DNS health overview, and then drill down into specific metrics such as DNS server latency and transaction details, enabling you to monitor and troubleshoot DNS performance effectively.

## Step 1: Navigating to DNS Network Services Assurance

To begin, navigate to the Network Services Assurance section for DNS. Follow this direct path within the dashboard:

`Dashboard` > `Assurance` > `Health` > `Network Services` > `DNS`

This path will lead you to the main DNS health overview page, where you can see a high-level summary of your DNS services and their current status.

![Screenshot](../../images/assurance/img/network-services-image001.png)

![Screenshot](../../images/assurance/img/network-services-image003.png)

![Screenshot](../../images/assurance/img/network-services-image005.png)

![Screenshot](../../images/assurance/img/network-services-image007.png)

## Step 2: Exploring DNS Server Details

From the DNS health overview, you can delve deeper into the performance metrics of individual DNS servers. To do this, click on any of the displayed DNS server entries or their associated "View Details" links.

This action will open a detailed view for the selected DNS server, providing more granular insights into its operation and performance.

![Screenshot](../../images/assurance/img/network-services-image009.png)

![Screenshot](../../images/assurance/img/network-services-image011.png)

### DNS Server Latency

Within the detailed view of a specific DNS server, you will find a section dedicated to **DNS Server Latency**. This section displays critical metrics related to the response times of your DNS server, helping you identify potential bottlenecks or performance issues. High latency can indicate network congestion, server overload, or other underlying problems affecting DNS resolution.

![Screenshot](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/network-services/img/network-services-image0013.png)

![Screenshot](../../images/assurance/img/network-services-image015.png)

### DNS Server Transactions

Further down in the detailed DNS server view, the **DNS Server Transactions** section provides insights into the volume and success rate of DNS queries handled by the server. This data is crucial for understanding the load on your DNS infrastructure and detecting anomalies in query patterns, such as a sudden drop in successful queries or an unexpected surge in traffic.

![Screenshot](../../images/assurance/img/network-services-image017.png)

![Screenshot](../../images/assurance/img/network-services-image019.png)
