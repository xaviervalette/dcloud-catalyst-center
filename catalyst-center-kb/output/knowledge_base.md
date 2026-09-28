# Cisco Catalyst Center Instant Demo 3.2 — Base de connaissances

Source : https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/  
Pages : 68


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/ -->
## Cisco Catalyst Center 3.2.3 Instant Demo

### Authors

**Satpal Ranu**, Solution Engineer, satrana@cisco.com

**John Bartin**, Solution Engineer, jobartin@cisco.com

**Noah Funderburk**, Solution Engineer, nfunderb@cisco.com

(last updated: August 17, 2026)

### What's New

The AI Assistant is now live within the Catalyst Center environment and can be accessed by navigating to the [AI Assistant](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/scenarios/ai-assistant/) page under the Storylines section. It provides AI-powered responses, recommendations, and insights to help streamline network operations. The AI Assistant assists IT teams by identifying and resolving network issues, contributing to minimal downtime and enhanced network performance. To ensure an optimal experience, please follow the demo guide for all AI prompts, as this scenario is simulated within the Catalyst Center Instant Demo.

Guides for Role-Based Access Compliance (RBAC) and Rule Based Compliance are coming soon.

### Overview

Cisco Catalyst Center is a comprehensive network management solution with functionality that spans all aspects of modern network management, including design, discovery, policy, provisioning, predictive analytics, intelligent monitoring, visibility, and compliance. Catalyst Center includes built-in automation and simplified workflows to help ensure efficiency and consistency in operations.

- [Storylines](#storylines)  
  Explore purpose-driven use cases that bring together Catalyst Center capabilities to address common network operations and business needs.
- [Design](#design)  
  Learn how to architect and plan your network environment with Catalyst Center's powerful design tools.
- [Provision](#provision)  
  Discover how to quickly deploy and configure devices and services across your network.
- [Assurance](#assurance)  
  Gain insights into network health and performance through real-time monitoring and analytics.
- [Policy](#policy)  
  Explore how to define and enforce consistent network policies for enhanced security and compliance.

### Storylines

The Storylines section presents broader scenarios that bring together related Cisco Catalyst Center capabilities to address a complete network objective. These guides provide context for how platform functions work together in practical network operations.

**Key scenarios demonstrated in this section:**

- Planning and implementing an SD-Access fabric
- Using the AI Assistant tool to streamline network operations

### Design

The Design section of this Catalyst Center demo guides you through the foundational steps required to plan, configure, and standardize your network environment. This section covers everything from visualizing your network layout and assigning profiles to configuring core services, security, IP addressing, wireless design, automated device configuration, and image management. Whether you're building a new deployment or refining an existing one, these workflows help ensure your network is robust, secure, and scalable.

**Key tasks demonstrated in this section:**

- Visualizing the network hierarchy, floor maps, and wireless heat maps
- Creating and managing network profiles for consistent site configuration
- Defining service provider profiles for WAN connectivity and class of service
- Configuring essential network servers, including AAA, DHCP, DNS, SFTP, and NTP
- Managing device credentials globally and at the site level
- Setting up security and trust settings, including certificate revocation checks
- Assigning and exporting IP address pools for different locations and floors
- Configuring and reviewing wireless network SSIDs per site and floor
- Creating, editing, and applying CLI templates for device configuration
- Managing device operating system images and identifying "golden" image standards

### Provision

The Provision section of the Catalyst Center demo provides a comprehensive, hands-on walkthrough of how to onboard, configure, automate, and manage network devices within Cisco Catalyst Center. This section is designed to help users master every stage of the device lifecycle—from initial discovery and provisioning through advanced automation, policy application, and lifecycle management. Each workflow is presented with intuitive step-by-step instructions and visual references, empowering users to deploy, monitor, and maintain their network infrastructure with confidence and efficiency.

**Key tasks demonstrated in this section:**

- Viewing and filtering network devices in the Inventory page
- Accessing and exploring detailed device information
- Claiming and provisioning new switches and Wireless LAN Controllers (WLC) using Plug and Play (PnP)
- Automating network deployment and expansion with LAN Automation
- Configuring VLANs and ports in existing (brownfield) environments
- Enabling and disabling Application Visibility Control (CBAR) for traffic analytics and monitoring
- Managing software image upgrades and orchestrating device updates with Software Image Management (SWIM)
- Executing sequential and error-handling workflows for software image deployments

- Replacing faulty devices using Return Material Authorization (RMA) workflows and reviewing replacement history
- Monitoring deployment status, compliance, and progress throughout the provisioning lifecycle

### Assurance

The Assurance section of the Cisco Catalyst Center demo provides a comprehensive, hands-on exploration of Cisco's advanced monitoring, analytics, and troubleshooting capabilities. Designed for users seeking to maximize network reliability and performance, this section guides you through core dashboards, client and device visibility tools, AI-driven analytics, event correlation, and powerful remediation features. Whether monitoring health, resolving complex issues, or leveraging next-generation Wi-Fi insights, you’ll experience the full depth of Cisco’s Assurance innovation in a seamless, role-oriented workflow.

**Key tasks and highlights in this section:**

- Navigate and interpret the Network Health and Client Health dashboards
- Drill down to individual clients, users, and devices with Client360, User360, and Device360 views
- Leverage SSID Monitoring and detailed onboarding analytics
- Visualize network and client connectivity paths with Path Trace and topology tools
- Analyze application health, performance, and usage with App Health and Application 360
- Investigate issues and events using AI-driven anomaly detection and dynamic baselines
- Explore advanced analytics, including Event Analytics and Peer Comparison dashboards
- Assess power usage, PoE status, and energy savings across your network
- Monitor network services such as DNS and WAN health
- Deep-dive into Access Point performance, enhanced RRM, and Wi-Fi 6/6E/7 readiness

- Manage and remediate rogue devices and wireless threats with AWIPS and containment workflows

### Policy

This section of the Catalyst Center demo provides a comprehensive walkthrough of Cisco’s advanced policy capabilities for network security and performance management. Users will learn how to leverage AI-powered analytics, implement adaptive network controls, streamline endpoint grouping, manage group-based access policies, and optimize application quality of service. The demo is structured to guide users from foundational concepts to advanced policy enforcement, enabling efficient, secure, and intelligent network operations.

**Key Tasks Covered in This Section:**

- Navigate the AI Endpoint Analytics interface to detect spoofing and manage trust scores.
- Reset trust scores for endpoints flagged as suspicious.
- Apply Adaptive Network Control (ANC) policies to mitigate endpoint risks.
- Filter and identify endpoints based on trust score metrics.
- Restore network access by resetting trust scores after policy enforcement.
- Accept, modify, or reject AI-proposed endpoint groupings using Smart Grouping.
- Manage and organize endpoint types and hierarchies for streamlined policy application.
- Review and refine endpoint group proposals to match organizational requirements.
- View, create, and edit security groups and access contracts using GBAC.
- Establish and modify contract policies between user, device, and application groups.
- Leverage ISE profiles and StealthWatch host groups for enhanced security context.
- Monitor and manage existing policies and their enforcement status.
- Implement and analyze application-level Quality of Service (QoS) policies.
- Track deployment status and results of application QoS policies by device.
- Access and interpret queuing profiles to optimize network performance.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/home/start_here/ -->
### Environment

This demo is hosted on **dCloud**, but it is considered *Community Developed* and therefore **is not subject** to standard dCloud validation or support.

This demo is derived from an **actual demo lab** and leverages a **simulation engine** to demonstrate a broad range of features. It offers a consistent, scalable environment with **full administrative access** for comprehensive demonstrations. Please follow these recommendations so that you are not caught off-guard when using the demo in public.

- We recommend to use **Google Chrome** (or a browser using the standard Chromium engine) to avoid simulation errors or unexpected behaviors when navigating the demo.
- Consider this as a **prescriptive demo** with a limited set of screen simulations. Not all screens are simulated, so please **only perform** tasks that are in this guide or **practice before** using the demo.

### Credentials

The Catalyst SD-WAN Center will **automatically log in**. If it prompts for credentials, please use the following:

- Username: `demo`
- Password: `demo1234!`

### Reset The Demo

Simply log out of the session; this will reset all the changes you have made.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/home/try_new_homepage/ -->
## New Home Page

In the top-right corner, there is an option labeled "Try the new home page! BETA". This beta homepage provides a more detailed summary view of your network data, enabling faster assessment of overall network health and performance.

This new homepage experience in Catalyst Center 3.1 aims to improve operational efficiency and user engagement by combining detailed network insights with intuitive navigation and support features.

![Screenshot](images/home/img/try_new_homepage-image01.png)

![Screenshot](images/home/img/try_new_homepage-image02.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/scenarios/sda-fabric/ -->
### Step 1: Introductions

This guide is designed to clarify the steps involved in deploying Cisco SDA Fabric, covering everything from the initial planning phase through to full implementation.

Follow the guide to access the  [Catalyst Center Dashboard](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/home/start_here/).

### Step 2: Design

Before starting with Cisco SDA, ensure you fully understand your current network. Begin by assessing your existing network design, site hierarchy, and configuration settings to establish a solid foundation for deployment.

Explore the Network Hierarchy structure within Catalyst Center -  [Network Hierarchy](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/network_hierarchy/).

Explore the Network Server Settings -  [Network Settings](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/server_settings/).

Explore the pre-define device credentials -  [Device Credentials](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/device_credentials/).

Explore the IP Address Pools which is required during the LAN Automation and Fabric provisioning -  [IP Address Pools](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/ip_pools/).

### Step 3: Provision

Discover how to claim and provision network devices with Cisco Plug and Play (PnP). This includes claiming devices, assigning them to sites, configuring network settings, previewing and validating configurations, and finalizing the provisioning process.

[PnP - Claim and Provision the Catalyst C9300 switch](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/pnp/#claiming-and-provisioning-a-switch/)

Explore the LAN Automation process, including each step from initiating LAN Automation, selecting seed devices and interfaces, assigning IP address pools, monitoring progress, to stopping automation sessions.

[LAN Automation](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/lan_automation/)

This guide offers detailed, step-by-step instructions for enabling the Edge role on a C9300 switch through the Cisco Fabric Provisioning interface.

[Enable a Edge role on existing SDA Fabric infrastructure](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/fabric/)

This demo guide walks you through deploying Fabric In a Box (FIAB) and configuring Anycast Gateways. You will gain hands-on experience deploying a Border Node, Control Plane, Edge Node, and Embedded Wireless LAN Controller on a Catalyst 9300 switch.

[Deploy Fabric In a Box (FIAB)](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/fiab/)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/scenarios/ai-assistant/ -->
## AI Assistant

The AI Assistant in Cisco Catalyst Center is a conversational AI interface designed to optimize network management and facilitate troubleshooting. It provides AI-powered responses, recommendations, and insights to help streamline network operations. The AI Assistant assists IT teams by identifying and resolving network issues, contributing to minimal downtime and enhanced network performance.
To ensure an optimal experience, please follow the demo guide for all AI prompts, as this scenario is simulated within the Catalyst Center Instant Demo.

Since the AI Assistant is a simulated environment and supports only certain commands, please follow the guide below.

### Supported AI Prompts

**To ensure an optimal experience, please use only these commands for AI prompts, as this scenario is simulated within the Catalyst Center Instant Demo:**

1. Show the list of the switches
2. Classify these switches based on the level of PoE support they provide
3. Show the current PoE usage of switch c9300-24U
4. Show the list of clients with the worst health scores
5. Show details for GraceSmith-PC

**The following questions from the default drop-downs are also supported:**

#### Network Overview

Are there any critical issues?
How is a specific site doing? follow up question then enter "london 1".

#### Troubleshooting

Troubleshoot a specific client. For followup question then enter "grace smith".
Troubleshoot a specific access point. For followup question enter "CW9178I-LDN1-01".

#### Client & Device Insights

List any recent software upgrade status on my network devices.
Show me the busiest APs.

#### Policies & Configuration

How do I create and deploy a CLI template?


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/network_hierarchy/ -->
## Network Hierarchy in PseudoCo

### Introduction

This guide provides a step-by-step overview of how to use the **Network Hierarchy** feature in PseudoCo. It covers how to navigate the network hierarchy, visualize floor maps and heat maps, and interact with access points using both 2D and 3D views. The guide is designed to help users efficiently manage and visualize wireless network deployments across multiple sites and floors.

---

### Overview of Network Hierarchy

The Network Hierarchy feature allows you to view and manage the layout of your organization's network infrastructure. Floor maps and heat maps are available for all sites that have at least one access point assigned.

- **Navigation**:  
  Go to **Design** > **Network Hierarchy**.
- **Note**:  
  Floor maps and heat maps will only be displayed for sites with at least one assigned access point.

---

### Visualizing Floor Maps & Heat Maps

When viewing the network hierarchy, you can see detailed floor maps and heat maps for eligible sites. The following screenshots demonstrate these features:

![Screenshot](images/design/img/network-hierarchy-image001.png)

In the simulation, the following locations and floors have access points assigned:

- London1 building: 1st Floor & 2nd Floor

Below are sample screenshots from the simulation:

![Screenshot](images/design/img/network-hierarchy-image003.png)

![Screenshot](images/design/img/network-hierarchy-image005.png)

#### Example: London1, 2nd Floor

![Screenshot](images/design/img/network-hierarchy-image007.png)

![Screenshot](images/design/img/network-hierarchy-image009.png)

---

### Exploring 3D Map Views

- Switch to **3D view** to visualize the network in three dimensions.
- Toggle between different frequency bands (5GHz/6GHz and 2.4GHz) to observe how the heat map changes in 3D.

![Screenshot](images/design/img/network-hierarchy-image013.png)

---

### Interactive Map Walkthrough

- Move through the map to view access point positions and configurations.
- Experiment with different settings to see their effect on the network visualization.

![Screenshot](images/design/img/network-hierarchy-image015.png)

---

### Conclusion

The Network Hierarchy feature in PseudoCo offers powerful visualization tools for managing and optimizing your wireless network deployments. Use the floor and heat maps to gain insights and ensure optimal coverage for your environment.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/network_profiles/ -->
## Design - Network Profiles Guide

This guide provides a comprehensive, step-by-step overview of how to effectively use and manage Network Profiles within the **Design** module. It is intended for users who need to assign sites to network profiles or modify existing profile configurations. By following these instructions, you will learn the updated process for managing network profiles, ensuring a streamlined and efficient design workflow.

---

### Table of Contents

1. [Overview](#overview)
2. [Accessing Network Profiles](#accessing-network-profiles)
3. [Assigning a Site to a Network Profile](#assigning-a-site-to-a-network-profile)
4. [Editing a Network Profile](#editing-a-network-profile)
5. [Notes & Best Practices](#notes--best-practices)

---

### Overview

Network Profiles are fundamental for defining and applying consistent network configurations across multiple sites. They allow you to standardize settings, attach templates, and manage wireless SSIDs, ensuring uniformity and simplifying large-scale deployments. This guide will walk you through the key processes involved in managing these profiles.

---

### Accessing Network Profiles

To begin managing your network profiles, navigate to the **Design** section and select **Network Profiles**.

![Screenshot](images/design/img/network_profiles-image000.png)
![Screenshot](images/design/img/network_profiles-image0000.png)

---

### Assigning a Site to a Network Profile

Follow these steps to assign a site to an existing network profile:

1. Locate the desired network profile from the list.
2. Click **Assign Site** to link a site to your selected network profile.
   ![Screenshot](images/design/img/network_profiles-image001.png)
   ![Screenshot](images/design/img/network_profiles-image003.png)
3. From the dialog box, choose the desired site(s) and click the **Save** button.
   ![Screenshot](images/design/img/network_profiles-image004.png)
4. A success notification will appear, confirming the site assignment.
   ![Screenshot](images/design/img/network_profiles-image004_1.png)
5. The 'Sites' column for that profile will now display the updated number of assigned sites.
   ![Screenshot](images/design/img/network_profiles-image004_2.png)

---

---

### Notes & Best Practices

- Always adhere to your organization's established naming conventions when creating or editing network profiles to maintain consistency and clarity.
- Exercise caution when assigning sites to profiles to prevent potential misconfigurations across different clusters.
- Remember to **Save** all changes after editing a profile or assigning sites to ensure your updates are successfully applied.
- For specific configuration requirements or advanced settings, always refer to your cluster-specific documentation.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/sp_profiles/ -->
## Service Provider Profiles

This guide provides step-by-step instructions for creating and managing Service Provider (SP) profiles within the Design section of the platform. By following these steps, you will learn how to navigate to the Service Provider Profiles page, create new profiles, and manage class of service models for WAN providers.

---

### Part 1: Accessing and Managing Service Provider Profiles

#### Step 1: Navigate to Service Provider Profiles

1. On the Homepage, click the **Menu**.
2. Navigate to **Design > Service Provider Profiles**.

![Screenshot](images/design/img/sp_profiles-image001.png)

---

#### Step 2: Create or Manage a Service Provider Profile

- You can create a Service Provider (SP) profile that defines the class of service for a particular WAN provider.
- The platform allows you to define service models with 4, 5, 6, or 8 classes.

![Screenshot](images/design/img/sp_profiles-image003.png)

- Additionally, you have the option to **delete** or **reset** all changes to the profiles as needed.

---

### Notes

- Make sure to save your changes after creating or modifying a profile.
- Deleting or resetting changes is irreversible; proceed with caution.

---

**End of Guide**


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/server_settings/ -->
## Network Settings – Servers Tab

### Introduction

This demo guide provides step-by-step instructions for navigating and configuring network server settings in the **Design > Network Settings > Servers** tab. You will learn how to view and manage global and site-specific credentials, search and select sites, and configure essential network server features such as AAA, DHCP, DNS, SFTP, NTP, Stealthwatch Flow Destination, Time Zone, and Message of the Day. Screenshots are included to illustrate each step and enhance understanding.

---

### Step 1: Accessing Network Settings

From the Homepage menu, navigate to **Design > Network Settings**.

![Screenshot](images/design/img/server_settings-image001.png)

---

### Step 2: Viewing the Servers Tab

By default, the **Network Settings** page opens to the **Servers** tab.

> **Note:** In previous versions, this tab was named **Network**.

![Screenshot](images/design/img/server_settings-image003.png)

When the page opens, the global site credentials are displayed.

---

### Step 3: Viewing Site Credentials

On the left side of the page, select any site to view its specific credentials.

![Screenshot](images/design/img/server_settings-image005.png)

---

### Step 4: Searching and Selecting Sites

Use the search panel to find and select the desired sites quickly.

![Screenshot](images/design/img/server_settings-image007.png)

---

### Step 5: Configuring External Network Servers

- In the **AAA** tab, you can configure external network servers or endpoints.

![Screenshot](images/design/img/server_settings-image009.png)

- In the **DHCP** tab, specify one or more dedicated DHCP servers to manage client device networking configuration.

---

### Step 6: Configuring DNS, Image Distribution, and NTP

- In the **DNS** tab, configure your network’s domain name and specify DNS servers for hostname resolution.

![Screenshot](images/design/img/server_settings-image011.png)
![Screenshot](images/design/img/server_settings-image012.png)

- In the **Image Distribution** tab, select SFTP servers to act as image distribution servers.

  > Using a distributed SWIM architecture with strategically located SFTP servers helps support large-scale device software image upgrades and conserves WAN bandwidth.
- In the **NTP** tab, specify one or more NTP servers to facilitate system clock synchronization for your network.
- In the **Stealthwatch Flow Destination** tab, set the flow destination used to provision SSA on this site.

---

### Step 7: Time Zone and Message of the Day Configuration

- In the **Time Zone** tab, select the time zone that matches the physical location of the site.
  > The site time zone is used when scheduling device provisioning and updates.

![Screenshot](images/design/img/server_settings-image013.png)

- In the **Message of the Day** tab, customize the message that appears during login to routers, switches, and hubs.

---

### Summary

This guide covered how to navigate the **Servers** tab in Network Settings, view and manage site credentials, search for sites, and configure critical network server features including AAA, DHCP, DNS, SFTP, NTP, flow destinations, time zones, and the Message of the Day. For more details, refer to the screenshots provided at each step.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/device_credentials/ -->
## Managing Device Credentials in Network Settings

This guide walks you through the process of viewing, searching, and editing device credentials within the Cisco Design > Network Settings interface. By following these steps, you will learn how to navigate to the Device Credentials tab, view global and site-specific credentials, search for specific sites, and edit credentials as needed.

---

### Step 1: Access Network Settings

From the homepage menu, navigate to **Design > Network Settings**.

![Screenshot](images/design/img/device_credentials-image001.png)

---

### Step 2: Open the Device Credentials Tab

By default, the Network Settings page opens on the **Servers** tab. Switch to the **Device Credentials** tab.

When the Device Credentials tab opens, the global site credentials will be displayed.

![Screenshot](images/design/img/device_credentials-image003.png)

---

### Step 3: View Site Credentials

On the left side of the page, you can select any site to view its specific credentials.

![Screenshot](images/design/img/device_credentials-image005.png)

---

### Step 4: Search and Select Sites

Use the search panel to find specific sites. Select the desired sites from the search results to view their credentials.

![Screenshot](images/design/img/device_credentials-image007.png)

---

---

### Note

> The **Manage Credentials** button is currently disabled.

---

**End of Guide**


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/security_trust/ -->
## Security and Trust – Network Settings

This guide provides step-by-step instructions for navigating and configuring security and trust settings in the Cisco Design > Network Settings interface. You will learn how to access the Security and Trust tab, view and search site credentials, and configure revocation check options for selected sites. Screenshots are included to assist you throughout the process.

---

### Steps to Configure Security and Trust Settings

#### Step 1: Navigate to Network Settings

From the Homepage menu, go to **Design > Network Settings**.

![Screenshot](images/design/img/security_trust-image001.png)

---

#### Step 2: Access the Security and Trust Tab

By default, the Network Settings page opens on the **Servers** tab. Switch to the **Security and Trust** tab.

![Screenshot](images/design/img/security_trust-image003.png)

Once the tab is open, the global site credentials will be displayed.

---

#### Step 3: View Site Credentials

On the left side of the page, you can select any site to view its credentials.

![Screenshot](images/design/img/security_trust-image005.png)

---

#### Step 4: Search and Select Sites

Use the search panel to find specific sites. Select the desired sites from the list.

![Screenshot](images/design/img/security_trust-image007.png)

---

#### Step 5: Configure Revocation Check Options

After selecting one or more sites, navigate to the **Revocation Check** tab to view available options. Choose the required revocation check options and click **Save** to apply your changes.

![Screenshot](images/design/img/security_trust-image009.png)

---

### Summary

By following these steps, you can efficiently access, review, and configure security and trust settings for your network sites within the Cisco platform. Use the screenshots as visual references for each step to ensure a seamless experience.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/ip_pools/ -->
## IP Address Pools

### Introduction

This demo guide provides step-by-step instructions for accessing, viewing, and exporting IP address pools within the system. You'll learn how to navigate to specific locations, check IP pools for different floors, switch between IPv4 and IPv6 views, and export IP address pool details to an Excel file for further analysis. Screenshots are included at each step to assist you throughout the process.

---

### Steps

#### Step 1: Access the IP Address Pools

![Screenshot](images/design/img/ip_pools-image000.png)
Click on **IP Address Pools** in the main navigation menu.

![Screenshot](images/design/img/ip_pools-image001.png)

---

#### Step 2: Navigate to the Desired Location

- Go to **Global** → **Europe** → **England** → **London1**.
- Review the available IP pools for the following locations:
- 1st Floor
- 2nd Floor
- Ground Floor

![Screenshot](images/design/img/ip_pools-image003.png)

---

#### Step 3: View IP Versions

Click on the tabs for **IPv4 only** and **IPv6** to view address pools for each protocol version.

![Screenshot](images/design/img/ip_pools-image005.png)

![Screenshot](images/design/img/ip_pools-image007.png)

---

#### Step 4: Export IP Address Pool Data

1. At the site level, click on **Global**.
2. Click the **Export** button.

![Screenshot](images/design/img/ip_pools-image009.png)

---

#### Step 5: Save the Exported File

- After clicking the Export option, a **Save As** pop-up window will appear.
- Choose the destination folder on your PC where you want to save the file.

![Screenshot](images/design/img/ip_pools-image011.png)

---

#### Step 6: Review the Exported File

- Open the downloaded file.
- The exported file will display all details from the **IP Address Pool** tab in Excel format.

![Screenshot](images/design/img/ip_pools-image013.png)

---

### Conclusion

Following these steps, you can effectively navigate, review, and export IP address pools for specific locations and floors. Use the exported Excel file to analyze or share IP pool details as required.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/wireless_design/ -->
## Wireless Network Design

This guide provides step-by-step instructions for configuring wireless network settings using the **Design > Network Settings > Wireless** menu. You will learn how to navigate to the Wireless configuration section, select a specific location (London 1 Î±1st Floor), and view the available SSIDs. Follow this guide to familiarize yourself with the key features and interface elements involved in wireless network design.

---

### 1. Accessing Wireless Network Settings

- Navigate to **Design > Network Settings**.

![Screenshot](images/design/img/wireless_design-image001.png)

- Click on **Wireless** to open the wireless network settings page.

![Screenshot](images/design/img/wireless_design-image003.png)

---

### 2. Selecting a Location

- For demonstration purposes, select **London 1 > 1st Floor** from the available locations.

![Screenshot](images/design/img/wireless_design-image005.png)

---

### 3. Viewing SSIDs

1. Click on **SSIDs** in the navigation panel.
2. The SSIDs page will display all configured wireless network IDs for the selected location.

![Screenshot](images/design/img/wireless_design-image007.png)

---

### Summary

This guide outlined the basic steps to access and review wireless network settings and SSIDs for a specific location. Use this process as a foundation for further wireless configuration and management tasks.

---

> **Note:**  
> This document is periodically updated to reflect interface and workflow changes. Please ensure you are referring to the latest version for accurate instructions.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/cli_templates/ -->
## Cisco CLI Templates

### Introduction

This guide provides a step-by-step walkthrough of the Cisco CLI Templates interface. You will learn how to navigate to the CLI Templates section, use filters, view and manage templates, add new projects and devices, and edit existing templates. Visual aids are included throughout to help you understand each step in the process.

---

### Step 1: Navigating to CLI Templates

Using the hamburger menu, go to **Design > CLI Templates**.

![Screenshot](images/design/img/cli-templates-image001.png)

---

### Step 2: CLI Templates Landing Page

After navigation, you will arrive at the **CLI Templates** page.

![Screenshot](images/design/img/cli-templates-image003.png)

---

### Step 3: Using Filters

Filters are located on the left-hand side. Selecting a filter will display the corresponding templates on the right.

![Screenshot](images/design/img/cli-templates-image005.png)

---

### Step 4: Applying Multiple Filters

You can select multiple filters on the left. This will refine your results and show project-type templates on the right.

![Screenshot](images/design/img/cli-templates-image007.png)

---

### Step 5: Searching for Templates

You can search for specific templates or project names using the search bar above the filters.

![Screenshot](images/design/img/cli-templates-image009.png)

---

### Step 6: Viewing Template Details

Click on any template to view its details, such as **Templates**, **Variables**, **Simulation**, and **Provision Conflicts**.

![Screenshot](images/design/img/cli-templates-image011.png)

---

### Step 7: Template View and Properties

This is the main template view. Use the menu items to access related template properties.

![Screenshot](images/design/img/cli-templates-image013.png)

---

### Step 8: System Variables Assistant

View the **System Variables Assistant** for guidance on using variables in templates.

![Screenshot](images/design/img/cli-templates-image014.png)

---

### Step 9: Viewing Template History

Click the **Template History** icon to review the history of a template.

![Screenshot](images/design/img/cli-templates-image015.png)

---

### Step 10: Adding a Project or Template

Add a new project or template from this section.

![Screenshot](images/design/img/cli-templates-image019.png)

---

### Step 11: Creating a New Project

Enter the project name and description, then click **Continue** to proceed to template addition.

![Screenshot](images/design/img/cli-templates-image021.png)

---

### Step 12: Adding a Template to a Project

Once the project is added, you'll see its name at the top. Provide a template name, select the project, and choose the template type, language, and software type. To add a new template, select a project from the list and repeat the steps.

![Screenshot](images/design/img/cli-templates-image023.png)

---

#### Step 12A: Adding Device Details

Add device details as required.

![Screenshot](images/design/img/cli-templates-image025.png)

---

#### Step 12B: Selecting Devices

Choose "Switches and Hubs," select a device from the dropdown, and click **Add**.

![Screenshot](images/design/img/cli-templates-image027.png)

---

#### Step 12C: Confirming Added Devices

The added device family and specific devices will appear in the device type details section. Click **Continue**.

![Screenshot](images/design/img/cli-templates-image029.png)

---

### Step 13: Accessing the Template Page

You will now see the template page.

![Screenshot](images/design/img/cli-templates-image031.png)

---

#### Step 13A

![Screenshot](images/design/img/cli-templates-image033.png)

---

#### Step 13B: Saving and Committing Templates

Save and commit your template here. Click **CLI Template** in the top-left corner to return to the templates list.

![Screenshot](images/design/img/cli-templates-image035.png)

---

### Step 14: Reviewing Your Newly Created Template

Your new template will now appear in the list. The project name, template count, version, and commit state with dates are shown in the summary tab on the left.

![Screenshot](images/design/img/cli-templates-image037.png)

---

### Step 15: Editing Templates and Projects

Edit templates and projects from this section. The editing screens are the same as in Steps 11 and 12. Save your changes before exiting.

![Screenshot](images/design/img/cli-templates-image039.png)

---

### Conclusion

This guide has walked you through the process of navigating, filtering, creating, and editing CLI Templates within the Cisco interface. For further assistance, refer to Cisco's official documentation or support channels.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/design/image_mgmt/ -->
## Device Image Repository – Golden Image Use Case

### Introduction

This demo guide provides step-by-step instructions for using the **Image Repository** feature within the Assurance > Device workflow, specifically focusing on the "Golden Image" use case. You will learn how to identify and manage device images, use global site-level filtering, and recognize devices running the current recommended (golden) OS image. The guide is designed for clarity, with visuals to assist each step.

---

### Steps

#### Step 1: Accessing the Image Repository

Begin by navigating to the **Image Repository** section within the Assurance > Device area.

![Screenshot](images/design/img/image_mgmt-image001.png)

---

#### Step 2: Global Site-Level Filtering

- The image repository currently supports filtering at the **global site level** only.
- Other site levels are not supported at this time.
- Use the available filters to narrow down device types such as routers, wireless LAN controllers (WLCs), etc.

![Screenshot](images/design/img/image_mgmt-image003.png)

---

#### Step 3: Viewing Device Families

- Within the global site, available device family names are displayed in a table.
- Select a device family name to proceed to the next page, where you can review images specific to that family.

![Screenshot](images/design/img/image_mgmt-image005.png)

---

#### Step 4: Identifying Golden Image Versions

- For each device family, if there is one or more image version matching the current (recommended) version, it will be highlighted with a **golden star**.
- The golden star visually indicates that the device is running the designated golden image.

![Screenshot](images/design/img/image_mgmt-image007.png)

---

#### Step 5: Viewing Image Details

- Click on any image to view detailed information about that image version.

![Screenshot](images/design/img/image_mgmt-image009.png)

---

### Summary

This guide has outlined the process of navigating the Image Repository, filtering devices at the global site level, identifying device families, recognizing golden image versions, and accessing detailed image information. Use this workflow to maintain consistent and up-to-date device images across your network.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/inventory/ -->
## Catalyst Center Inventory Page

### Introduction

This demo guide provides an overview of the **Inventory Page** in Catalyst Center. You will learn how to view and filter devices within your environment using both basic and advanced filter options. This guide outlines the page layout, available filters, and key functionalities to help you efficiently navigate and utilize the Inventory Page.

---

### Inventory Page Overview

The **Inventory Page** displays all devices managed within your Catalyst Center.

![Screenshot](images/provision/img/inventory-image001.jpg)

![Screenshot](images/provision/img/inventory-image003.jpg)

#### Key Features

- **Device List:** View all devices currently provisioned in Catalyst Center.
- **Filters:** Access filters at the top and on the left side of the page to narrow down device listings.

---

### Using Filters

At the top of the Inventory Page, there are filter options to help you quickly find devices based on various criteria.

When you click on the text box labeled *"Click here to apply basic or advanced filters or view recently applied filters"*, you can:

- Apply basic or advanced filters to refine your device search.
- View a list of recently used filters for quick access.

As of **12/02/2024**, all filter functionalities are working as expected.

![Screenshot](images/provision/img/inventory-image005.jpg)

---

### Additional Page Views

You can further explore device details and filter options using the available interface panels.

![Screenshot](images/provision/img/inventory-image007.jpg)

---

### Summary

The Catalyst Center Inventory Page offers a comprehensive, user-friendly interface for managing and filtering devices. Utilize the filtering options to efficiently locate and manage your network inventory.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/device_details/ -->
## Device Details Page

### Introduction

This guide provides a comprehensive overview of the **Device Details Page** within the Inventory system. It outlines the various ways to access detailed information about a particular device, describes the features and functions available on the Device Details Page, and highlights the unique options available for specific device types such as Wireless LAN Controllers (WLC). This document is intended to help users efficiently navigate, utilize, and understand the Device Details Page for inventory management.

---

### Accessing the Device Details Page

The Device Details Page displays full information about a selected device. There are multiple ways to access this page. One common method is via the **Provision Inventory Page**.

![Screenshot](images/provision/img/device_details-image001_new.png)

#### Steps to Access Device Details:

1. **From the Inventory Page:**
2. Click on any device name in the inventory list.
3. A small pop-up will appear showing basic device information.
4. Within this pop-up, click the **"View Device details"** link.
5. This link opens a new browser tab and loads all the details for the selected device.

![Screenshot](images/provision/img/device_details-image003_new.png)

1. **Viewing More Details in the Pop-up:**
2. In the same pop-up, you can also click the **"Show more"** link.
3. This reveals additional details about the device directly in the pop-up window.

![Screenshot](images/provision/img/device_details-image005.png)

---

### Navigating the Device Details Page

- Each menu option on the Device Details Page should load relevant data (or an empty state if data is unavailable).
- The interface should **not** display loading icons or error pop-ups when navigating between menu options.

![Screenshot](images/provision/img/device_details-image007.png)

![Screenshot](images/provision/img/device_details-image009.png)

![Screenshot](images/provision/img/device_details-image011.png)

---

### Special Features for WLC Devices

For Wireless LAN Controller (WLC) devices, such as **LDN1-C9800-01.PseudoCo.com**, there is a dedicated tab called **"Wireless info"**. This tab provides comprehensive wireless-related details, including:

- Wireless Summary
- Redundancy Summary
- Health Parameters
- Additional Details

![Screenshot](images/provision/img/device_details-image013.png)

![Screenshot](images/provision/img/device_details-image015.png)

![Screenshot](images/provision/img/device_details-image017.png)

![Screenshot](images/provision/img/device_details-image019.png)

---

### Summary

The Device Details Page is designed to give users quick access to detailed device information and ensure a seamless experience when managing inventory. Make use of the different access methods and menu options to view all relevant device data, and utilize the special features available for WLC devices for enhanced wireless management.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/device-discovery/ -->
## Device Discovery and Provisioning Guide

This guide provides a comprehensive walkthrough of the device discovery, assignment, and provisioning processes within the platform. It outlines how to discover network devices, assign them to existing or newly created sites, and provision them for network integration. Additionally, this document covers the steps for creating new network hierarchy elements, such as areas, buildings, and floors, to organize your network infrastructure effectively.

---

### Navigating to the Tools & Discovery Page

To begin, navigate to the **Tools & Discovery** page. This is your central hub for managing device discovery operations.

![Screenshot](images/provision/img/device-discovery-image001.png)

---

### Discovery Actions

The Discovery page allows you to perform several key actions:

1. **Cloning Discovery**
2. **Rediscovery**
3. **Adding New Discovery**

---

#### Cloning a Discovery

To clone an existing discovery, follow these steps:

1. Ensure there is at least one existing discovery available.
2. On the Discovery Dashboard page, locate the desired discovery. Under the "Action" section, click on the **three dots** (`...`).

   ![Screenshot](images/provision/img/device-discovery-image002.png)
3. From the dropdown menu, click on **Copy and Edit**.

   ![Screenshot](images/provision/img/device-discovery-image003.png)
4. Review the discovery settings and click **Next** to continue.

   ![Screenshot](images/provision/img/device-discovery-image004.png)
5. Ensure the checkbox for CLI credentials is selected, then click **Next** to continue.

   ![Screenshot](images/provision/img/device-discovery-image005.png)
6. Select at least one SNMP credential, then click **Next** to continue.

   ![Screenshot](images/provision/img/device-discovery-image006.png)
7. Click **Next** to continue through the scheduling options.
   ***Note: Scheduling the job later is not supported for cloned discoveries.***

   ![Screenshot](images/provision/img/device-discovery-image007.png)
8. Click on **Start Discovery** to initiate the discovery process.

   ![Screenshot](images/provision/img/device-discovery-image008.png)
9. To view the discovered devices, click on the **View Discovery** link.

   ![Screenshot](images/provision/img/device-discovery-image009.png)
10. The discovered devices will be displayed on this page.

    ![Screenshot](images/provision/img/device-discovery-image010.png)

---

#### Re-Discovering Devices

You can re-discover devices using an existing discovery. This is useful for updating device information or finding new devices within the same scope.

1. On the Discovery Dashboard page, locate the existing discovery you wish to re-run. Under the "Action" section, click on the **three dots** (`...`) and select **Re-discover**.

   ![Screenshot](images/provision/img/device-discovery-image011.png)
2. Enter a task name for the re-discovery process, then click **Discover** to start.

   ![Screenshot](images/provision/img/device-discovery-image012.png)
3. The status of the re-discovery process will be displayed in the "Status" column, progressing from **Queued**, to **In Progress**, and finally to **Completed**.

   ![Screenshot](images/provision/img/device-discovery-image013.png)
   ![Screenshot](images/provision/img/device-discovery-image014.png)
   ![Screenshot](images/provision/img/device-discovery-image015.png)

---

#### Creating a New Discovery

The Discovery feature scans your network for devices and adds them to the inventory. You can discover devices using methods such as Link Layer Discovery Protocol (LLDP), CDP, CIDR, or an IP address range.

To start a new discovery:

1. Click on **Add Discovery**.

   ![Screenshot](images/provision/img/device-discovery-image016.png)
2. Select your preferred discovery method. For this demonstration, we are using an **IP address range** to discover devices. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image017.png)
3. Ensure the checkbox for CLI credentials is selected. SNMP Read & Write credentials are selected by default. Click **Next** to continue.

   ![Screenshot](images/provision/img/device-discovery-image005.png)
4. Select the Global NETCONF port, then click **Next** to continue.

   ![Screenshot](images/provision/img/device-discovery-image018.png)
5. Select the HTTP(S) Write credentials, then click **Next** to continue.

   ![Screenshot](images/provision/img/device-discovery-image019.png)
6. On the Schedule Job page, select **Now**, then click **Next** to continue.
   ***Note: Assigning devices to an existing site during the discovery process is not supported. This will be done in a subsequent step.***

   ![Screenshot](images/provision/img/device-discovery-image020.png)
7. Click on **Start Discovery** to begin the process.

   ![Screenshot](images/provision/img/device-discovery-image021.png)
8. Click on **View Discovery** to check the details of the discovery process and its results.

   ![Screenshot](images/provision/img/device-discovery-image022.png)
9. This page displays the devices that have been discovered. To return to the Discovery dashboard, click on the **All Discoveries** link.

   ![Screenshot](images/provision/img/device-discovery-image023.png)
   ![Screenshot](images/provision/img/device-discovery-image024.png)

---

### Assigning Discovered Devices to a Site

Newly discovered devices will appear in the Inventory page as "Unassigned". You can assign these devices to an existing site or a newly created one.

1. Navigate to **Provision -> Inventory**.
2. Filter the devices by "Unassigned" to easily locate them.

   ![Screenshot](images/provision/img/device-discovery-image025.png)
3. Select the newly discovered device and click **Assign**.

   ![Screenshot](images/provision/img/device-discovery-image026.png)
4. Choose a site for the device. For this demonstration, select **New York 1**. Click **Save** to proceed.
   *You can select an existing site or create a new site under* *Design -> Network Hierarchy* *before assigning the discovered device.*

   ![Screenshot](images/provision/img/device-discovery-image027.png)
   ![Screenshot](images/provision/img/device-discovery-image028.png)
5. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image029.png)
6. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image030.png)
7. Click on **Preview** to review the assignment details.

   ![Screenshot](images/provision/img/device-discovery-image031.png)
8. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image032.png)
9. Once the status changes to **Ready**, click on **Deploy** to apply the site assignment.

   ![Screenshot](images/provision/img/device-discovery-image033.png)
10. Click on **Submit** to finalize the site assignment.

    ![Screenshot](images/provision/img/device-discovery-image034.png)
11. Now, if you navigate back to Inventory, you will see that the new device is successfully assigned to the selected site.

    ![Screenshot](images/provision/img/device-discovery-image035.png)

---

### Provisioning a Discovered Device

After assigning a device to a site, the next step is to provision it.

1. Select the newly discovered switch in the Inventory.
2. Click on **Actions -> Provision -> Provision Device**.

   ![Screenshot](images/provision/img/device-discovery-image036.png)
3. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image037.png)
4. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image038.png)
5. Verify the details in the Summary section and click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image039.png)
6. Enter a Task Name if desired, or leave it as default and click **Apply** to continue the flow.

   ![Screenshot](images/provision/img/device-discovery-image040.png)
7. Click **Next** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image041.png)
8. When the status is **Ready**, click on **Deploy** to continue.

   ![Screenshot](images/provision/img/device-discovery-image042.png)
9. Enter a task name and click on **Submit** to proceed.

   ![Screenshot](images/provision/img/device-discovery-image043.png)
10. Once the process is complete, navigate to Inventory. You will see that the new switch has been successfully provisioned.

    ![Screenshot](images/provision/img/device-discovery-image044.png)

---

### Creating a New Site (Network Hierarchy)

You can provision discovered devices to a newly created site as well. The steps for creating a new site involve defining Areas, Buildings, and Floors within the network hierarchy.

#### Create New Site Elements

1. Navigate to **Design -> Network Hierarchy**.

   ![Screenshot](images/provision/img/device-discovery-image045.png)

#### Adding an Area

1. To add an Area, click on the **three dots** (`...`) next to "Global" or any other existing area.
2. Enter the Area name.

   ![Screenshot](images/provision/img/device-discovery-image046.png)
3. After entering the area name, click **Add**.

   ![Screenshot](images/provision/img/device-discovery-image047.png)

#### Adding a Building

1. To add a Building, click on the **three dots** (`...`) next to "Global" or any other area.
2. Click on **Add Building**.

   ![Screenshot](images/provision/img/device-discovery-image048.png)
3. Enter the building name and address of the building, then click **Add** to create the building.

   ![Screenshot](images/provision/img/device-discovery-image049.png)

#### Adding a Floor

1. To add a Floor for any building, click the **three dots** (`...`) next to the desired building.
2. Then, click **Add Floor**.

   ![Screenshot](images/provision/img/device-discovery-image050.png)
3. Enter the floor name and click on **Add** to create the floor.
   ***Note: Currently, adding a floor plan is not supported.***

   ![Screenshot](images/provision/img/device-discovery-image051.png)
4. Click on **Ok** to complete the floor creation.

   ![Screenshot](images/provision/img/device-discovery-image052.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/topology/ -->
## Topology View in Cisco Catalyst Center

This guide provides a step-by-step walkthrough of how to utilize the Topology View feature within Cisco Catalyst Center. The Topology View allows you to visualize your network devices, understand their interconnections, and quickly access detailed information about each component. By following these steps, demo users will learn how to navigate the topology, inspect links, view device details, and access device-specific pages.

### Step 1: Accessing the Inventory and Topology View

Navigate to the **Provision > Inventory** page. This page displays all devices managed by Cisco Catalyst Center.

![Screenshot](images/provision/img/topology-image001.jpg)

From the Inventory page, select the **Topology View** option to visualize the network topology of all your devices.

![Screenshot](images/provision/img/topology-image003.jpg)

### Step 2: Inspecting Physical Links

Clicking on any link between devices within the topology will highlight and display the physical connections. This helps in understanding the direct paths and interfaces connecting your network components.

![Screenshot](images/provision/img/topology-image005.jpg)

### Step 3: Viewing Device Details

Hover your mouse cursor over any device name in the topology view to quickly see its detailed information in a tooltip. This provides a summary of key device attributes without leaving the topology map.

![Screenshot](images/provision/img/topology-image007.jpg)

### Step 4: Collapsing the View

To simplify the topology visualization or to focus on specific sections, click the **Collapse All** button. This action will group devices and reduce visual clutter.

![Screenshot](images/provision/img/topology-image009.jpg)

### Step 5: Navigating to Device Details Page

Clicking on any device within the topology view will redirect you to its dedicated **Device Details** page. This page offers comprehensive information, configuration options, and monitoring capabilities for the selected device.

![Screenshot](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/topology/img/topology-image0011.jpg)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/pnp/ -->
## Cisco Plug and Play (PnP) Demo Guide

### Introduction

This guide provides step-by-step instructions for utilizing Cisco Plug and Play (PnP) to streamline the claiming and provisioning of network devices. By following this demo, users will learn how to efficiently onboard both Wireless LAN Controllers (WLCs) and switches, assign them to network sites, configure essential parameters, and deploy configurations. This process ensures a smooth and automated network setup, leveraging PnP for rapid device deployment. All screenshots and interface references are included to help you navigate the workflow smoothly.

---

### Table of Contents

1. [Claiming and Provisioning a WLC Device](#claiming-and-provisioning-a-wlc-device)
   - [Step 1: Claim PnP Device – WLC](#step-1-claim-pnp-device--wlc)
   - [Step 2: Assign Site](#step-2-assign-site)
   - [Step 3: Configure Device Details](#step-3-configure-device-details)
   - [Step 4: Preview Configuration](#step-4-preview-configuration)
   - [Step 5: Verify WLC in Inventory](#step-5-verify-wlc-in-inventory)
   - [Step 6: Provision Claimed Device](#step-6-provision-claimed-device)
2. [Claiming and Provisioning a Switch](#claiming-and-provisioning-a-switch)
   - [Step 1: Claim PnP Device – Switch](#step-1-claim-pnp-device--switch)
   - [Step 2: Assign Site](#step-2-assign-site-1)
   - [Step 3: Check Image and Templates](#step-3-check-image-and-templates)
   - [Step 4: Preview Configuration](#step-4-preview-configuration-1)
   - [Step 5: Verify Switch in Inventory](#step-5-verify-switch-in-inventory)
   - [Step 6: Provision Claimed Device](#step-6-provision-claimed-device-1)

---

### Claiming and Provisioning a WLC Device

#### Step 1: Claim PnP Device – WLC

1. Navigate to **Provision > Network Devices > Plug and Play**.

   ![Screenshot](images/provision/img/pnp-image001.png)
2. Select the **WLC** you want to claim. Click **Actions > Claim**.

   ![Screenshot](images/provision/img/pnp-image003.png)

---

#### Step 2: Assign Site

1. Assign the device to the desired site, e.g., `newyork1 / newyork1->1st floor`.

   ![Screenshot](images/provision/img/pnp-image005.png)

   Click **Assign** and then **Next** to continue.
2. ![Screenshot](images/provision/img/pnp-image007.png)

   Click **Assign** to configure required network details for the Catalyst WLC.

---

#### Step 3: Configure Device Details

Fill in the required network details for the Catalyst WLC as shown below:

- **IP Address:** 10.12.52.21
- **Subnet Mask:** 255.255.255.0
- **Gateway:** 10.12.52.1
- **Interface:** Ten 0/0/0
- **VLAN ID:** 12

  ![Screenshot](images/provision/img/pnp-image009.png)

  Click on **Save** to continue.

  ![Screenshot](images/provision/img/pnp-image011.png)

  The `WLC9800-PnP-Template` is being used in this workflow. Since the hostname is a variable in this template, you can enter the desired device name here, which will also be reflected in the inventory.

  Click **Next** to continue.

  ![Screenshot](images/provision/img/pnp-image013.png)

---

#### Step 4: Preview Configuration

1. Select the **Preview Configuration** option.

   ![Screenshot](images/provision/img/pnp-image015.png)
2. Verify that the hostname matches the device name used in this demo.

   ![Screenshot](images/provision/img/pnp-image017.png)
3. After claiming, the status will initially remain unchanged.
4. Click the **Refresh** button at the top of the table or wait 30 seconds for the status to auto-refresh.

   ![Screenshot](images/provision/img/pnp-image019.png)

---

#### Step 5: Verify WLC in Inventory

1. Navigate to **Provision > Inventory**.
2. Confirm that the WLC device has been added to the inventory.

   ![Screenshot](images/provision/img/pnp-image021.png)

---

#### Step 6: Provision Claimed Device

1. Select the claimed WLC device from the inventory.
2. Click **Actions > Provision > Provision device**.

   ![Screenshot](images/provision/img/pnp-image023.png)

   Review the details and click **Next** to continue.
   ![Screenshot](images/provision/img/pnp-image025.png)

   Enter the VLAN ID and click **Next** to continue.
   ![Screenshot](images/provision/img/pnp-image027.png)

   Click **Next** to continue.
   ![Screenshot](images/provision/img/pnp-image029.png)

   Click **Next** to continue.
   ![Screenshot](images/provision/img/pnp-image031.png)

   Click **Next** to continue.
   ![Screenshot](images/provision/img/pnp-image033.png)

   Click on **Apply** to proceed.
   ![Screenshot](images/provision/img/pnp-image034.png)

   Click on **Next** to continue.
   ![Screenshot](images/provision/img/pnp-image035.png)

   Click on **Deploy** to continue.
   ![Screenshot](images/provision/img/pnp-image039.png)

   The provisioning of the device will complete successfully, as indicated by the status.
   ![Screenshot](images/provision/img/pnp-image041.png)

---

### Claiming and Provisioning a Switch

#### Step 1: Claim PnP Device – Switch

1. Navigate to **Provision > Network Devices > Plug and Play**.

   ![Screenshot](images/provision/img/pnp-image043.png)
2. Select a switch to claim, Click **Actions > Claim**.

   ![Screenshot](images/provision/img/pnp-image045.png)

---

#### Step 2: Assign Site

1. Assign the switch to the appropriate site, e.g., `newyork1 / newyork1->1st floor`.

   ![Screenshot](images/provision/img/pnp-image047.png)
2. Click **Next** to continue.

   ![Screenshot](images/provision/img/pnp-image049.png)

---

#### Step 3: Check Image and Templates

1. Review the image and templates as prompted.
2. Click **Next** to proceed.

   ![Screenshot](images/provision/img/pnp-image051.png)
   3. Click on the device to check the template variables.

   ![Screenshot](images/provision/img/pnp-image053.png)
   4. Then check the hostname and stack. Then click **Next**.

   ![Screenshot](images/provision/img/pnp-image055.png)

---

#### Step 4: Preview Configuration

1. Select the **Preview Configuration** option.

   ![Screenshot](images/provision/img/pnp-image057.png)
2. Ensure the hostname matches the one specified in the earlier steps.

   ![Screenshot](images/provision/img/pnp-image059.png)
3. After claiming, the status will remain unchanged initially. Click **Refresh** at the top of the table or wait 30 seconds for an automatic refresh.

   ![Screenshot](images/provision/img/pnp-image061.png)

---

#### Step 5: Verify Switch in Inventory

1. Navigate to **Provision > Inventory**. Confirm the switch device appears in the inventory.

   ![Screenshot](images/provision/img/pnp-image063.png)

---

#### Step 6: Provision Claimed Device

1. In Inventory, select the newly claimed switch device. Click **Actions > Provision > Provision device**.

   ![Screenshot](images/provision/img/pnp-image065.png)
2. Check the details and click **Next**.

   ![Screenshot](images/provision/img/pnp-image067.png)
   ![Screenshot](images/provision/img/pnp-image069.png)
3. Continue through the wizard, clicking **Next** as needed.

   ![Screenshot](images/provision/img/pnp-image071.png)
   ![Screenshot](images/provision/img/pnp-image073.png)
4. Click **Apply**.

   ![Screenshot](images/provision/img/pnp-image075.png)
5. Click **Next**.

   ![Screenshot](images/provision/img/pnp-image077.png)
6. Ensure the status is **Ready**, then click **Deploy**.

   ![Screenshot](images/provision/img/pnp-image079.png)
7. Click **Submit**.

   ![Screenshot](images/provision/img/pnp-image081.png)
8. If a success notification appears, the device has been provisioned successfully.

---

### Notes

- Ensure all device details and hostnames are accurate during the claiming and provisioning steps.
- If device status does not update automatically, use the manual refresh function.
- Follow on-screen prompts closely, as interface steps may vary slightly depending on software version.

---

**End of Guide**


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/lan_automation/ -->
## LAN Automation Demo Guide

### Introduction

This guide provides a comprehensive overview and step-by-step instructions for utilizing Cisco's LAN Automation feature. LAN Automation is designed to simplify network operations by automating the deployment of new networks, freeing network administrators from time-consuming and repetitive configuration tasks. It ensures the creation of a standard, error-free Layer 3 routed access design by leveraging the IS-IS routing protocol. This document will walk you through initiating, managing, and stopping LAN Automation sessions for single and multiple sites.

### LAN Automation Workflow

#### Step 1: Accessing LAN Automation

To begin, navigate to the LAN Automation feature from the main menu:
**Provision -> Network devices -> LAN automation.**

This page displays all currently running or previously configured LAN Automation sessions. If no sessions are active or configured, the page will appear empty. To start a new session, click the **"Start LAN automation"** button.

![Screenshot](images/provision/img/lan_automation-image001.jpg)

![Screenshot](images/provision/img/lan_automation-image003.jpg)

![Screenshot](images/provision/img/lan_automation-image005.jpg)

#### Step 2: Selecting a Seed Device

In this step, you will select a seed device for your LAN Automation session. This is done by choosing a specific site or floor that contains network devices. For example, in the screenshot below, "London 1" is selected as the site, and "1st floor" is one of the floors within that building. The page will display the network devices assigned to the selected floor.

![Screenshot](images/provision/img/lan_automation-image007.jpg)

![Screenshot](images/provision/img/lan_automation-image009.jpg)

#### Step 3: Selecting Device Interfaces

Once the primary seed device is selected, you must choose the interfaces that will be used for LAN Automation. Click on **"Select Interfaces"** to open a pop-up window displaying the device's available interfaces.

![Screenshot](images/provision/img/lan_automation-image011.jpg)

![Screenshot](images/provision/img/lan_automation-image013.jpg)

#### Step 4: Adding Interfaces

From the interface list, select the interfaces with an "up" status. You can add an interface by clicking the **"plus"** symbol next to its name or by double-clicking the interface name. Selected interfaces will move to the right-side window. You can remove interfaces from the right-side window if needed. You can add multiple interfaces.

For this demo, select interfaces 37 and 38 from the list. After selecting the desired interfaces, click the **"Select"** button in the pop-up window.

![Screenshot](images/provision/img/lan_automation-image015.jpg)

![Screenshot](images/provision/img/lan_automation-image017.jpg)

#### Step 5: Proceed to Next Step

After selecting the interfaces, click the **"Next"** button to continue.

![Screenshot](images/provision/img/lan_automation-image019.jpg)

#### Step 6: Selecting the Principal IP Address Pool

On this screen, you need to select the Principal IP address pool. Choose the building that contains the relevant IP address pool; for instance, we are selecting the "London 1" building in this example. Once selected, click the **"Review"** button.

![Screenshot](images/provision/img/lan_automation-image021.jpg)

#### Step 7: Review and Start Automation

The review screen summarizes all the options you have selected in the previous steps. Carefully review these settings. Once you have confirmed that all selections are correct, click the **"Start"** button at the bottom of the page to initiate LAN Automation.

![Screenshot](images/provision/img/lan_automation-image023.jpg)

![Screenshot](images/provision/img/lan_automation-image025.jpg)

#### Step 8: Monitoring LAN Automation Progress

After starting LAN Automation, you will be redirected to the main LAN Automation page. Here, you will see a dashlet indicating the status of your session. Initially, it will be in an "Initialized" state, signifying that LAN Automation is in progress. Within a few seconds, the dashlet's status will update to "Seed Provisioned," then "In Progress," and finally "Completed" as the automation progresses.

![Screenshot](images/provision/img/lan_automation-image027.jpg)

#### Step 9: Starting LAN Automation for Multiple Sites

You can initiate LAN Automation for multiple sites simultaneously. To start another session, for example, for the "San Jose" site, click **"Start LAN Automation"** again.

The process for the second site is identical to the first:
\* Select the appropriate floor containing devices for the San Jose site.
\* Select the interfaces of the chosen device.
\* Select the IP address pool associated with the San Jose site.

![Screenshot](images/provision/img/lan_automation-image029.jpg)

#### Step 10: San Jose Site - Device Selection

![Screenshot](images/provision/img/lan_automation-image031.jpg)

#### Step 11: San Jose Site - Interface Selection

![Screenshot](images/provision/img/lan_automation-image033.jpg)

#### Step 12: San Jose Site - Interface Confirmation

![Screenshot](images/provision/img/lan_automation-image035.jpg)

#### Step 13: San Jose Site - IP Pool Selection

![Screenshot](images/provision/img/lan_automation-image037.jpg)

#### Step 14: Viewing LAN Automation Sessions and Devices

Once both LAN Automation sessions (e.g., London and San Jose) have been started, you can view their details in the sessions table on the main LAN Automation page.

![Screenshot](images/provision/img/lan_automation-image039.jpg)

Additionally, the "LAN automated devices" tab provides further insights. This tab includes sub-tabs for "Seed devices," "Provision," "Discovered," and "Error," allowing you to monitor the status of devices involved in the automation process.

![Screenshot](images/provision/img/lan_automation-image041.jpg)

![Screenshot](images/provision/img/lan_automation-image043.jpg)

![Screenshot](images/provision/img/lan_automation-image045.jpg)

![Screenshot](images/provision/img/lan_automation-image047.jpg)

#### Step 15: Stopping LAN Automation

To stop an active LAN Automation session, click the **"Stop LAN automation"** link within the corresponding dashlet. After a short period, that particular dashlet will disappear from the page, indicating the session has been terminated.

![Screenshot](images/provision/img/lan_automation-image049.jpg)

![Screenshot](images/provision/img/lan_automation-image051.jpg)

![Screenshot](images/provision/img/lan_automation-image053.jpg)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/avc/ -->
## Application Visibility (AVC) - Network Devices Enablement Guide

This guide provides step-by-step instructions for managing Application Visibility (AVC) settings on network devices within the Cisco platform. Specifically, it covers the processes for both disabling and enabling CBAR (Cisco Borderless Access Router) functionality on selected network devices. Following these steps will ensure proper configuration and deployment of AVC services.

### Provision > Services > Application Visibility > Network Devices Enablement

---

#### Part 1: Disable CBAR

This section details the procedure for disabling CBAR on selected network devices.

1. **Select Devices and Initiate Disable CBAR**
   Navigate to `Provision > Services > Application Visibility > Network Devices Enablement`. In the site devices table, which lists all available devices, select the CBAR method devices for which you wish to disable CBAR.
   Then, select the `CBAR` option and choose `disable CBAR on selected device`.

   ![Screenshot](images/provision/img/avc-image001.jpg)

   ![Screenshot](images/provision/img/avc-image003.jpg)

   A confirmation pop-up window will appear. To continue, select `Yes`.
2. **Enter Task Name and Apply**
   Another pop-up window will appear. Enter a descriptive `Task Name` and then select `Apply`.

   ![Screenshot](images/provision/img/avc-image005.jpg)
3. **Review Pending Operations and Device Compliance (Step 1 of Task)**
   The first step of the task will load, displaying `Pending Operations` and `Device Compliance` checks.
   Ensure both checks are successful and appear in green. Once confirmed, click `Next`.
   If desired, you can recheck the status by clicking the `Recheck` button.

   ![Screenshot](images/provision/img/avc-image007.jpg)
4. **Prepare Device Configuration File (Step 2 of Task)**
   The second step of the task will load. This step prepares the configuration files for the selected devices.
   The names of the selected devices will appear on the left side of the page. The status will remain `in-progress` until the configuration files are fully prepared.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](images/provision/img/avc-image009.png)
5. **Preview and Deploy Configuration (Step 3 of Task)**
   The third step of the task will load. In this step, the device's configuration files are loaded and previewed.
   To proceed, click `Deploy`.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](images/provision/img/avc-image011.jpg)
6. **Configure Deployment Timing and Submit**
   Upon clicking `Deploy`, a pop-up window will appear on the right side of the page. Here, you can edit the task name if needed.
   You can also select the task deployment timing: `Now` (immediate deployment) or `Later` (at a specified time).
   To continue, click `Submit`.

   ![Screenshot](images/provision/img/avc-image013.jpg)
7. **Task Creation and Status Update**
   After submitting the task, it will be created in the `Task` section. The page will then return to the `site devices table` where the process began.
   In the site devices table, the selected device's CBAR Deployment status will initially show as `In-Progress`.
   If you refresh the page, the selected device's CBAR deployment status will be displayed as `Not Deployed`.
   The device's CBAR deployment status is now disabled.

   ![Screenshot](images/provision/img/avc-image015.jpg)

   ![Screenshot](images/provision/img/avc-image017.jpg)

---

#### Part 2: Enable CBAR

This section details the procedure for enabling CBAR on selected network devices.

1. **Select Devices and Initiate Enable CBAR**
   Navigate to `Provision > Services > Application Visibility > Network Devices Enablement`. In the site devices table, which lists all available devices, select the CBAR method devices for which you wish to enable CBAR.
   Then, select the `CBAR` option and choose `enable CBAR on selected device`.

   ![Screenshot](images/provision/img/avc-image019.jpg)

   ![Screenshot](images/provision/img/avc-image021.jpg)

   A confirmation pop-up window will appear. To continue, select `Yes`.
2. **Confirm Enablement and Enter Task Name**
   A pop-up window will appear on the right side of the page. To continue, click `Next`.
   Another pop-up window will then load, displaying the selected device's name. To continue, click `Enable`.
   Finally, another pop-up window will appear. Enter a descriptive `Task Name` and then select `Apply`.

   ![Screenshot](images/provision/img/avc-image023.jpg)

   ![Screenshot](images/provision/img/avc-image025.jpg)

   ![Screenshot](images/provision/img/avc-image027.jpg)
3. **Review Pending Operations and Device Compliance (Step 1 of Task)**
   The first step of the task will load, displaying `Pending Operations` and `Device Compliance` checks.
   Ensure both checks are successful and appear in green. Once confirmed, click `Next`.
   If desired, you can recheck the status by clicking the `Recheck` button.

   ![Screenshot](images/provision/img/avc-image029.jpg)
4. **Prepare Device Configuration File (Step 2 of Task)**
   The second step of the task will load. This step prepares the configuration files for the selected devices.
   The names of the selected devices will appear on the left side of the page. The status will remain `in-progress` until the configuration files are fully prepared.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](images/provision/img/avc-image031.png)
5. **Preview and Deploy Configuration (Step 3 of Task)**
   The third step of the task will load. In this step, the device's configuration files are loaded and previewed.
   To proceed, click `Deploy`.
   You can refresh this step by clicking the `Refresh` button in the top-right corner of the page. You can also exit and preview the task later from this view.

   ![Screenshot](images/provision/img/avc-image033.jpg)
6. **Configure Deployment Timing and Submit**
   Upon clicking `Deploy`, a pop-up window will appear on the right side of the page. Here, you can edit the task name if needed.
   You can also select the task deployment timing: `Now` (immediate deployment) or `Later` (at a specified time).
   To continue, click `Submit`.

   ![Screenshot](images/provision/img/avc-image035.jpg)
7. **Task Creation and Status Update**
   After submitting the task, it will be created in the `Task` section. The page will then return to the `site devices table` where the process began.
   In the site devices table, the selected device's CBAR Deployment status will initially show as `In-Progress`.
   If you refresh the page, the selected device's CBAR deployment status will be displayed as `Completed`.
   The device's CBAR deployment status is now enabled.

   ![Screenshot](images/provision/img/avc-image037.jpg)

   ![Screenshot](images/provision/img/avc-image039.jpg)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim/ -->
## Software Image Management (SWIM) Demo Guide

### Introduction

This guide provides a step-by-step demonstration of the Software Image Management (SWIM) feature, designed to simplify and automate the process of updating software images on network devices. This document will walk you through a specific use case: updating the software image version for multiple Cisco Catalyst 9300 series switches. By following these instructions, you will learn how to select devices, initiate an update task, perform readiness checks, schedule distribution and activation, and monitor the update status.

### Use Case

Update software image version from `cat9k_iosxe.17.15.02.SPA.bin` to `cat9k_iosxe.17.15.03.SPA.bin` for `LDN1-C9300-DIST1.PseudoCo.com` & `LDN1-C9300-DIST2.PseudoCo.com` devices.

---

**Navigation:** `Provision -> Inventory`

![Screenshot](images/provision/img/swim-image001.jpg)

---

### Step 1: Select Software Images Focus

Navigate to the Inventory section and select **Software Images** from the Focus dropdown menu.

![Screenshot](images/provision/img/swim-image003.jpg)

---

### Step 2: Select Target Devices

Identify and select the devices for software image update: `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`.

![Screenshot](images/provision/img/swim-image005.jpg)

---

### Step 3: Initiate Software Image Management

From the **Action** menu, navigate to `Software Image > Software Image Management`. This action will redirect you to the Software Image Management Page.

![Screenshot](images/provision/img/swim-image007.jpg)

![Screenshot](images/provision/img/swim-image009.jpg)

![Screenshot](images/provision/img/swim-image011.jpg)

![Screenshot](images/provision/img/swim-image013.jpg)

On the Software Image Management page, re-select `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com` devices, then click **Update Devices**.

---

### Step 4: Name the Update Task

Enter a descriptive task name for the software update and click **Next**.

![Screenshot](images/provision/img/swim-image015.jpg)

---

### Step 5: Review Navigation Options

Review the navigation options available:
\* **Exit:** To cancel the software update task.
\* **Back:** To return to the previous step.
\* **Next:** To proceed to the next step.

Click **Next** to continue.

![Screenshot](images/provision/img/swim-image017.jpg)

---

### Step 6: Select Software Image Version

Select the desired software image version for the update. In this use case, select `cat9k_iosxe.17.15.03.SPA.bin`.

![Screenshot](images/provision/img/swim-image019.jpg)

---

### Step 7: Perform Readiness Check

Verify that `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com` are listed in the Device Activation Order. Click the **Update Readiness Report** link to initiate an **Image Update Readiness Check** and review the device readiness report.

![Screenshot](images/provision/img/swim-image021.jpg)

---

### Step 8: Review and Close Readiness Report

After reviewing the Image Update Readiness Check results, close the report (by clicking 'X' or 'Close') to proceed with the workflow.

![Screenshot](images/provision/img/swim-image023.jpg)

![Screenshot](images/provision/img/swim-image025.jpg)

---

### Step 9: Configure Schedule and Activation Options

Configure the scheduling and cleanup options:
\* For **Software Distribution**, select **Now**.
\* For **Software Activation**, ensure **After Distribution** is **enabled**.

*Note: The 'Software Activation Later' option is not supported for this use case.*

Click **Submit** to proceed to the Summary page.

![Screenshot](images/provision/img/swim-image027.jpg)

---

### Step 10: Confirm and Schedule Distribution

Review the summary of your software image update task. Click **Submit** to schedule the distribution.

![Screenshot](images/provision/img/swim-image029.jpg)

![Screenshot](images/provision/img/swim-image031.jpg)

---

### Step 11: Monitor Image Update Status

To view the progress of the image update, click the **Image update status** button.

![Screenshot](images/provision/img/swim-image033.jpg)

---

### Step 12: Observe Distribution In-Progress

The status for both C9300 devices will initially show as **Distribution In-progress**.

![Screenshot](images/provision/img/swim-image035.jpg)

---

### Step 13: Review Mixed Status Results

Observe the updated status: `LDN1-C9300-DIST1.PseudoCo.com` shows **Distribution Success** and **Activation In-progress**, while `LDN1-C9300-DIST2.PseudoCo.com` shows **Distribution failed**.

![Screenshot](images/provision/img/swim-image037.jpg)

---

### Step 14: Final Status Overview

The final status indicates that `LDN1-C9300-DIST1.PseudoCo.com` is **Device UpToDate** with the latest software image, while `LDN1-C9300-DIST2.PseudoCo.com` remains in a **Distribution Failure** state.

![Screenshot](images/provision/img/swim-image039.jpg)

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim-sequential/ -->
## SWIM Sequential Device Updates

This guide outlines the process of performing sequential software image updates on multiple network devices using the Software Image Management (SWIM) feature. By following these steps, you will learn how to select devices, initiate a sequential update task, verify readiness, schedule distribution and activation, and monitor the update status.

---

#### Navigation Path

Navigate to **Provision > Inventory** in the application interface.

![Screenshot](images/provision/img/swim-sequential-image001.jpg)

---

#### Step 1: Select Software Images Focus

From the **Focus** dropdown menu, select **Software Images**.

![Screenshot](images/provision/img/swim-sequential-image003.jpg)

---

#### Step 2: Select Target Devices

Identify and select the target devices for the update: **LDN1-C9300-DIST1.PseudoCo.com** and **LDN1-C9300-DIST2.PseudoCo.com**.

![Screenshot](images/provision/img/swim-sequential-image005.jpg)

---

#### Step 3: Initiate Software Image Management

Navigate to **Action > Software Image > Software Image Management**. This action will redirect you to the **Software Image Management Page**.

![Screenshot](images/provision/img/swim-sequential-image007.jpg)

On the **Software Image Management Page**, re-select **LDN1-C9300-DIST1.PseudoCo.com** and **LDN1-C9300-DIST2.PseudoCo.com**, then click **Update Devices**.

![Screenshot](images/provision/img/swim-sequential-image009.jpg)

![Screenshot](images/provision/img/swim-sequential-image011.jpg)

![Screenshot](images/provision/img/swim-sequential-image013.jpg)

---

#### Step 4: Enter Task Name

Enter a descriptive **Task Name** (e.g., "Sequential\_C9300\_Update") and click **Next**.

![Screenshot](images/provision/img/swim-sequential-image015.jpg)

---

#### Step 5: Review Navigation Options

Review the navigation options available on this screen:
\* Click **Exit** to cancel the software update task.
\* Click **Back** to return to the previous step.
\* Click **Next** to proceed to the next step.

![Screenshot](images/provision/img/swim-sequential-image017.jpg)

---

#### Step 6: Configure Sequential Update Order

In the **Device Activation Order** section, both **LDN1-C9300-DIST1.PseudoCo.com** and **LDN1-C9300-DIST2.PseudoCo.com** will be listed. Select both devices and click **Move to Sequential Update Order**.

![Screenshot](images/provision/img/swim-sequential-image019.jpg)

![Screenshot](images/provision/img/swim-sequential-image021.jpg)

![Screenshot](images/provision/img/swim-sequential-image023.jpg)

---

#### Step 7: Perform Image Update Readiness Check

Click the **Update Readiness Report** link. An **Image Update Readiness Check** popup will appear, displaying the respective Device Readiness Report. Review the report, then close the popup to continue with the workflow.

![Screenshot](images/provision/img/swim-sequential-image025.jpg)

![Screenshot](images/provision/img/swim-sequential-image027.jpg)

---

#### Step 8: Schedule Task and Clean Up

Configure the schedule for **Software Distribution** and **Software Activation**:
\* For **Software Distribution**, select **Now**.
\* For **Software Activation**, ensure **After Distribution** is **enabled**.

**Note:** The 'Software Activation Later' option is not supported for this use case.

Click **Submit** to proceed to the Summary page.

![Screenshot](images/provision/img/swim-sequential-image029.jpg)

---

#### Step 9: Confirm Scheduled Distribution

On the Summary page, click **Submit** to schedule the distribution.

![Screenshot](images/provision/img/swim-sequential-image031.jpg)

---

#### Step 10: View Image Update Status

To view the image update status, click the **Image update status** button.

![Screenshot](images/provision/img/swim-sequential-image033.jpg)

---

#### Step 11: Monitor Sequential Update Progress

Monitor the status of the devices as they progress through the sequential update:

- **Initial Status:** **LDN1-C9300-DIST1.PseudoCo.com** is in **Distribution In-progress** state, while **LDN1-C9300-DIST2.PseudoCo.com** is in a **Waiting** state.
  ![Screenshot](images/provision/img/swim-sequential-image035.jpg)
- **Distribution Progress:** **LDN1-C9300-DIST1.PseudoCo.com** is now **Successfully Distributed & Activation In-progress**, and **LDN1-C9300-DIST2.PseudoCo.com** remains in a **Waiting** state.
  ![Screenshot](images/provision/img/swim-sequential-image037.jpg)
- **Activation Progress:** **LDN1-C9300-DIST1.PseudoCo.com** is **Successfully Distributed & Activated**, and **LDN1-C9300-DIST2.PseudoCo.com** is now in **Activation In-progress**.
  ![Screenshot](images/provision/img/swim-sequential-image039.jpg)

---

#### Step 12: Observe Potential Failure Scenario

This image illustrates a scenario where **LDN1-C9300-DIST1.PseudoCo.com** is in **Distribution Success and Activation In-progress**, but **LDN1-C9300-DIST2.PseudoCo.com** has encountered a **Distribution failed** state.

![Screenshot](images/provision/img/swim-sequential-image041.jpg)

---

#### Step 13: Review Final Device Status

The final status indicates that **LDN1-C9300-DIST1.PseudoCo.com** is **Device UpToDate** with the latest software image version, while **LDN1-C9300-DIST2.PseudoCo.com** remains in **Distribution Failure**.

![Screenshot](images/provision/img/swim-sequential-image043.jpg)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim-error/ -->
## SWIM - Software Image Management Error Scenario Guide

This guide outlines the process of performing a Software Image Management (SWIM) update for network devices, specifically demonstrating an error scenario that can occur during the distribution phase. By following these steps, users will learn how to initiate a software image update, monitor its progress, and identify where an update might fail, providing valuable insights for troubleshooting and resolution.

---

### Initiating a Software Image Update Task

#### 1. Navigate to Inventory

Begin by navigating to the **Provision** section, then select **Inventory**.

![Screenshot](images/provision/img/swim-error-image001.jpg)

#### 2. Select Software Images Focus

From the Inventory page, set the **Focus** to **Software Images**.

![Screenshot](images/provision/img/swim-error-image003.jpg)

#### 3. Select Target Devices for Update

Identify the devices that require a software image update. For this demonstration, we will update two devices: `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`.

Select both devices as shown below.

![Screenshot](images/provision/img/swim-error-image005.jpg)

#### 4. Initiate Software Image Management Action

With the devices selected, click on **Action**, then navigate to **Software Image** and select **Software Image Management**.

![Screenshot](images/provision/img/swim-error-image007.jpg)

This action will redirect you to the **Software Image Management Page**.

![Screenshot](images/provision/img/swim-error-image009.jpg)

#### 5. Confirm Devices and Proceed to Update

On the Software Image Management page, re-select `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`. After confirming your selection, click the **Update Devices** button.

![Screenshot](images/provision/img/swim-error-image011.jpg)

![Screenshot](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/swim-error/img/swim-error-image013.jpg)

#### 6. Enter Task Name

Provide a descriptive name for your update task and then click **Next**.

![Screenshot](images/provision/img/swim-error-image015.jpg)

#### 7. Review Navigation Options

This step presents navigation options for the update wizard:
\* **Exit button:** Exits the software update task.
\* **Back button:** Returns to the previous step.
\* **Next button:** Proceeds to the next step.

Click **Next** to continue.

![Screenshot](images/provision/img/swim-error-image017.jpg)

#### 8. Select Software Image

Choose the desired software image for the update.

![Screenshot](images/provision/img/swim-error-image019.jpg)

#### 9. Verify Device Activation Order and Readiness

On this page, you will see the selected devices, `LDN1-C9300-DIST1.PseudoCo.com` and `LDN1-C9300-DIST2.PseudoCo.com`, listed under **Device Activation Order**. By default, the update flow is set to **Parallel Update Order**.

Click the **Update Readiness Report** link to view a pop-up with the **Image Update Readiness Check** for each device.

![Screenshot](images/provision/img/swim-error-image021.jpg)

#### 10. Review Image Update Readiness Report

Examine the readiness report for any potential issues. After reviewing, close the report by clicking the 'X' icon to continue with the workflow.

![Screenshot](images/provision/img/swim-error-image023.jpg)

![Screenshot](images/provision/img/swim-error-image025.jpg)

#### 11. Schedule Task and Clean Up

Configure the scheduling options for the software distribution and activation:
\* For **Software Distribution**, select **Now**.
\* For **Software Activation**, ensure **After Distribution** is **enabled**.

**Note:** The "Software Activation Later" option is not supported for this use case.

Click **Submit** to proceed to the Summary page.

![Screenshot](images/provision/img/swim-error-image027.jpg)

#### 12. Confirm and Submit Distribution

On the Summary page, review the task details. Click the **Submit Button** to schedule the distribution.

![Screenshot](images/provision/img/swim-error-image029.jpg)

### Monitoring and Troubleshooting the Update

#### 13. View Image Update Status

After submission, click the **Image update status** button to monitor the progress of your update task.

![Screenshot](images/provision/img/swim-error-image031.jpg)

#### 14. Observe Distribution In-Progress

Initially, the status for both C9300 devices will show as **Distribution In-progress**.

![Screenshot](images/provision/img/swim-error-image033.jpg)

#### 15. Identify Update Status: Success and Failure

As the update progresses, you will observe the status of each device. In this scenario:
\* `LDN1-C9300-DIST1.PseudoCo.com` proceeds to **Distribution Success and Activation In-progress**.
\* `LDN1-C9300-DIST2.PseudoCo.com` shows a **Distribution failed** state.

![Screenshot](images/provision/img/swim-error-image035.jpg)

#### 16. Investigate Failed Device Logs

To understand why `LDN1-C9300-DIST2.PseudoCo.com` failed, click on its device name. This action will display the **error logs** in a pop-up window.

![Screenshot](images/provision/img/swim-error-image037.jpg)

The error logs will indicate that the software image version update from `cat9k_iosxe.17.11.01.SPA.bin` to `cat9k_iosxe.17.12.01.SPA.bin` for `LDN1-C9300-DIST2.PseudoCo.com` has failed, with specific error details provided in the pop-up.

![Screenshot](images/provision/img/swim-error-image039.jpg)

![Screenshot](images/provision/img/swim-error-image041.jpg)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/rma/ -->
## RMA Device Replacement Usecase

This guide outlines the process for performing a Return Merchandise Authorization (RMA) device replacement within the platform. It details the steps required to identify an unreachable device, mark it for replacement, select a new device, and monitor the replacement process through to completion. This workflow ensures a smooth transition when replacing faulty network devices.

---

### Step 1: Navigate to Inventory

From the Homepage, click the **Menu** icon. Then, navigate to **Provision > Inventory**.

![Screenshot](images/provision/img/rma-image001.jpg)

### Step 2: Filter for Unreachable Devices

Once on the Inventory page, use the left sidebar to filter for **unreachable** devices. Additionally, change the focus of the page to **Device Replacement**. The table below will then display a list of all unreachable devices.

![Screenshot](images/provision/img/rma-image003.jpg)

### Step 3: Mark Device for Replacement

Select the device you wish to replace from the table. Click the **Actions** button above the table, then navigate to **Device Replacement > Mark for Replacement**.

![Screenshot](images/provision/img/rma-image005.jpg)

A confirmation prompt will appear asking to **Mark** or **Cancel**. Click **Mark**.

![Screenshot](images/provision/img/rma-image007.jpg)

### Step 4: Verify "Ready for Replacement" Status

The device's replacement status will now change to **"Ready for Replacement"**, indicating it is prepared for the replacement process.

![Screenshot](images/provision/img/rma-image009.jpg)

### Step 5: Initiate Device Replacement

Re-select the marked device. Click **Actions > Device Replacement > Replace Device**.

![Screenshot](images/provision/img/rma-image011.jpg)

### Step 6: Choose Replacement Device

The "Choose Replacement Device" page will appear. Select **Plug and Play** as the source. Then, choose one of the available devices from the table to use as the replacement. Click **Next**.

![Screenshot](images/provision/img/rma-image013.jpg)

### Step 7: Review Replacement Summary

A summary page will appear, displaying the details of both the faulty device and the selected replacement device. Review the information and click **Next**.

![Screenshot](images/provision/img/rma-image015.jpg)

### Step 8: Schedule Replacement

The "Schedule Replacement" page will appear. Click **Next** to proceed.

![Screenshot](images/provision/img/rma-image017.jpg)

### Step 9: Perform Initial Checks

The first step of the RMA use case will now perform initial checks. Once all operations are successful, click **Next**.

![Screenshot](images/provision/img/rma-image019.jpg)

### Step 10: Process Device List and Fetch Configuration

The second step of the use case will check the device list. Please wait for this process to complete.

Subsequently, the third step will fetch the configuration files for the devices. Once the status is in a **ready** state, click **Deploy**.

![Screenshot](images/provision/img/rma-image021.jpg)

### Step 11: Confirm Deployment

After clicking **Deploy**, a pop-up will appear asking you to submit the deployment. Click **Submit**.

![Screenshot](images/provision/img/rma-image023.jpg)

### Step 12: Monitor In-Progress Replacement

Once deployed, the device replacement process will begin. On the Inventory page, the faulty device's replacement status will change to **In-Progress**.

![Screenshot](images/provision/img/rma-image025.jpg)

### Step 13: View In-Progress Details and Onboarding Status

While the device replacement is **In-Progress**, you can click on the **In-Progress** status in the inventory to view detailed information, including the replacement status history and the tasks being executed.

![Screenshot](images/provision/img/rma-image027.jpg)

![Screenshot](images/provision/img/rma-image029.jpg)

![Screenshot](images/provision/img/rma-image031.jpg)

The history of tasks performed for the device replacement process will be displayed.

![Screenshot](images/provision/img/rma-image033.jpg)

Additionally, during the **In-Progress** state, navigating to **Provision > Plug and Play** will show the selected replacement device as **Onboarding**.

### Step 14: Verify Successful Replacement

After the device has been successfully replaced, its replacement status in the inventory will show as **NA**. The device details, such as IP Address and serial number, will be updated to reflect the new replacement device.

![Screenshot](images/provision/img/rma-image035.jpg)

Furthermore, after the replacement, if you navigate to **Provision > Plug and Play**, the selected replacement device will now show as **Provisioned**.

![Screenshot](images/provision/img/rma-image037.jpg)

### Step 15: Review Replacement History

To review the history of device replacements, navigate to **Actions > Device Replacement > Replacement History**. This will display a record of all replacement activities.

![Screenshot](images/provision/img/rma-image039.jpg)

Clicking on the replacement status of a specific device in the history will provide a detailed view of the tasks performed during its replacement process.

![Screenshot](images/provision/img/rma-image041.jpg)

![Screenshot](images/provision/img/rma-image043.jpg)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/overall-health/ -->
## Assurance – Overall Health: A Demo Guide

This guide provides a step-by-step walkthrough on how to access and interpret the Overall Health dashboard within Cisco DNA Center Assurance. This dashboard offers a comprehensive view of your network's health, including device status, client performance, network services, and site analytics, enabling quick identification and resolution of potential issues.

---

#### Step 1: Navigating to the Health Dashboard

![Screenshot](images/assurance/img/overall-health-image001.png)

From the Cisco DNA Center Homepage, navigate to the main menu. Select **Assurance** > **Dashboards** > **Health** tab.

#### Step 2: Overview and Filtering Options

![Screenshot](images/assurance/img/overall-health-image003.png)

Upon entering the Health tab, you will land on the **Overall Health** page. Here, you can filter the displayed data by selecting specific sites and adjusting the time range to focus on relevant periods.

#### Step 3: Monitoring Network Devices and Clients

![Screenshot](images/assurance/img/overall-health-image005.png)

The **Network Devices** section displays the total number of devices and their health status as a percentage. To delve deeper into device health details, click **View Network Health**.

Similarly, the **Wired Clients** and **Wireless Clients** tabs provide an overview of client performance. Click **View Client Health** for more in-depth client information.

#### Step 4: Reviewing Network Services Performance

![Screenshot](images/assurance/img/overall-health-image007.png)

The **Network Services** section presents an overview of the services provided, indicating their success and failure rates in percentage. For detailed insights into specific services, click the respective links: [View AAA Dashboard](https://localhost:7000/dna/assurance/dashboards/health/networkServices/aaa), [View DNS Dashboard](https://localhost:7000/dna/assurance/dashboards/health/networkServices/dns), [View DHCP Dashboard](https://localhost:7000/dna/assurance/dashboards/health/networkServices/dhcp).

#### Step 5: Analyzing Site-Level Performance

![Screenshot](images/assurance/img/overall-health-image009.png)

The **Site Analytics** tab offers insights into site-level performance. To explore detailed site analytics, click **View Site Analytics**.

#### Step 6: Identifying Top Issues

![Screenshot](images/assurance/img/overall-health-image011.png)

The **Top 10 Issue Types** section highlights the most frequent issues and their counts across the top 10 affected devices. To view all open issues, navigate to the Issues page by clicking **View Open Issues**.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/client-assurance/ -->
## Client Assurance

### Overview

This guide provides a step-by-step walkthrough of the **Client Assurance > Health (Client Tab)** dashboard, highlighting the key features and functionalities available for monitoring client health in your network. You will learn how to navigate the dashboard, utilize time-level filtering, explore wireless and wired client data, and interpret various metrics through detailed dashlets and tables. Each section provides screenshots and explanations to ensure a smooth and effective demo experience.

---

### Step 1: Access the Client Assurance Dashboard

![client-assurance-image001](images/assurance/img/client-assurance-image001.png)

---

### Step 2: Main Client Dashboard & Time-Level Filtering

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image003.png)

- The main dashboard graph can be filtered by time intervals: **24 hours**, **3 hours**, and **7 days**.
- Note: Currently, only global site-level filtering is supported. Filtering by other sites is not available.

---

### Step 3: Wireless and Wired Dashlets

#### Wireless Dashlet

The wireless dashlet includes two tabs:

1. **Latest**: Displays data from the last 5 minutes.
2. **Trend**: Displays data from the last 24 hours.

##### Latest Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image005.png)

Click on `View Details` under **Wireless Clients**

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image007.png)

- Clicking the **Active Client** section reveals detailed data about active clients below.

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image009.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image011.png)

##### Trend Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image013.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image015.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image017.png)

---

#### Wired Client Dashlet

##### Latest Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image019.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image021.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image023.png)

##### Trend Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image025.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image027.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image029.png)

---

### Step 4: Site Analytics Dashlet

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image031.png)

- Selecting **View Details** redirects you to the Site Analytics dashboard page.

![client-assurance-image033](images/assurance/img/client-assurance-image033.png)

---

### Step 5: Client Onboarding Times Dashlet

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image034.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image035.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image037.png)

![A screenshot of a graph  Description automatically generated](images/assurance/img/client-assurance-image039.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image041.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image043.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image045.png)

![client-assurance-image047](images/assurance/img/client-assurance-image047.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image049.png)

---

### Step 6: Connectivity Dashlet

#### Latest (5 Minutes Data)

![client-assurance-image051](images/assurance/img/client-assurance-image051.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image053.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image055.png)

---

### Step 7: Connectivity SNR Dashlet

#### Latest

![client-assurance-image060](images/assurance/img/client-assurance-image060.png)

![client-assurance-image061](images/assurance/img/client-assurance-image061.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image063.png)

---

### Step 8: Client Roaming Times

#### Latest (5 Minutes Data)

![client-assurance-image066](images/assurance/img/client-assurance-image066.png)

![client-assurance-image067](images/assurance/img/client-assurance-image067.png)

![client-assurance-image068](images/assurance/img/client-assurance-image068.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image069.png)

![client-assurance-image071](images/assurance/img/client-assurance-image071.png)

![client-assurance-image073](images/assurance/img/client-assurance-image073.png)

---

### Step 9: Client Count Per SSID

#### Latest (5 Minutes Data)

![client-assurance-image082](images/assurance/img/client-assurance-image082.png)

![client-assurance-image083](images/assurance/img/client-assurance-image083.png)

![client-assurance-image084](images/assurance/img/client-assurance-image084.png)

#### Trend (24 Hours Data)

- 24 hours of data will be loaded for trend analysis.

---

### Step 10: Connectivity Physical Link

#### Latest

![client-assurance-image085](images/assurance/img/client-assurance-image085.png)

![client-assurance-image086](images/assurance/img/client-assurance-image086.png)

#### Trend

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image087.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image088.png)

---

### Step 11: Client Table

![client-assurance-image089](images/assurance/img/client-assurance-image089.png)

- The client table is a core component of the client page.
- Features include type-wise filtering, overall health filtering, and other customizable filters.

---

### Step 12: Client Count Per Band

#### Latest

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image090.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image091.png)

---

### Step 13: Client Per Rate

#### Latest

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image094.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/client-assurance-image095.png)

---

### Conclusion

This guide has walked you through the key components of the Client Assurance dashboard, including how to interpret and utilize wireless and wired client data, site analytics, onboarding times, connectivity, SNR, and more. Use these insights to proactively monitor and optimize client health across your network.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/client360/ -->
## Cisco Assurance: Client 360 Page Demo Guide

This guide provides a comprehensive walkthrough of the Client 360 page within Cisco Assurance, a powerful tool designed to offer a holistic view of individual client health and performance. The Client 360 page consolidates critical information such as device health, issue details, event logs, and user data, enabling network administrators to efficiently monitor, troubleshoot, and understand client experiences. This document outlines the methods to access the Client 360 page and details the various sections and insights it provides.

### Accessing the Client 360 Page

There are two primary methods to navigate to the Client 360 page within Cisco Assurance:

#### Method 1: Via Assurance Health Dashboard

1. Navigate to **Assurance > Health**.
   ![Screenshot](images/assurance/img/client360-image001.png)
2. From the Dashboard, select the **Client Tab**.
3. Locate the desired client in the client table and select it. This action will automatically redirect you to the Client 360 page for that specific client.
   ![Screenshot](images/assurance/img/client360-image003.png)
   ![Screenshot](images/assurance/img/client360-image005.png)

#### Method 2: Using Global Search

1. Utilize the **Global search** bar, typically located at the top of the interface.
   ![Screenshot](images/assurance/img/client360-image007.png)
2. Enter the client's name into the search field.
   ![Screenshot](images/assurance/img/client360-image009.png)
3. From the search results, select the entry corresponding to the client's name (often labeled as "client 360"). This will redirect you to the Client 360 page.
   ![Screenshot](images/assurance/img/client360-image011.png)

### Client 360 Global Graph

Upon entering the Client 360 page, you will see a global graph providing an overview of the client's performance and activity. Hovering over specific points on this graph will display detailed information and metrics relevant to that particular time or event.
![Screenshot](images/assurance/img/client360-image013.png)

### Summary Dashlet

The Summary dashlet offers key insights into the client's onboarding, roaming, and connectivity status, providing a quick glance at their overall network experience.

![Screenshot](images/assurance/img/client360-image015.png)

#### 1. Onboarding Details

This section displays details related to the client's onboarding process. Click "View Details" to access a more granular breakdown of onboarding events.
![Screenshot](images/assurance/img/client360-image017.png)

- **Event Viewer**: Provides a chronological log of events related to the client's onboarding.
  ![Screenshot](images/assurance/img/client360-image019.png)
- **Impact Analysis**: Shows the potential impact of specific onboarding events on the client's experience.
  ![Screenshot](images/assurance/img/client360-image021.png)
- **Correlation**: Helps in understanding the correlation between different onboarding events and their outcomes.
  ![Screenshot](images/assurance/img/client360-image023.png)

#### 2. Roaming Details

This section covers the client's roaming activities, including transitions between access points. Click "View Details" to explore further.
![Screenshot](images/assurance/img/client360-image025.png)

- **Event Viewer**: Displays events specifically related to the client's roaming behavior.
  ![Screenshot](images/assurance/img/client360-image027.png)
- **Impact Analysis**: Assesses the impact of roaming events on the client's connectivity and performance.
  ![Screenshot](images/assurance/img/client360-image029.png)
- **Correlation**: Identifies correlations within roaming events to pinpoint potential issues or patterns.
  ![Screenshot](images/assurance/img/client360-image031.png)

#### 3. Connectivity Details

This section provides insights into the client's network connectivity, including critical metrics like Signal-to-Noise Ratio (SNR) and Received Signal Strength Indicator (RSSI).

##### SNR (Signal-to-Noise Ratio)

Click "View Details" to access detailed SNR information, which is crucial for assessing signal quality.
![Screenshot](images/assurance/img/client360-image033.png)

- **Event Viewer**: Shows events related to SNR fluctuations and thresholds.
  ![Screenshot](images/assurance/img/client360-image035.png)
- **Impact Analysis**: Analyzes the impact of SNR levels on the client's connection stability and performance.
  ![Screenshot](images/assurance/img/client360-image037.png)
- **Correlation**: Helps correlate SNR data with other network events to diagnose connectivity issues.
  ![Screenshot](images/assurance/img/client360-image039.png)

##### RSSI (Received Signal Strength Indicator)

Click "View Details" to access detailed RSSI information, indicating the strength of the client's received signal.
![Screenshot](images/assurance/img/client360-image041.png)

- **Event Viewer**: Displays events related to RSSI levels and changes.
  ![Screenshot](images/assurance/img/client360-image043.png)
- **Impact Analysis**: Assesses the impact of RSSI levels on the client's connection quality.
  ![Screenshot](images/assurance/img/client360-image045.png)
- **Correlation**: Identifies correlations within RSSI data to understand signal strength patterns.
  ![Screenshot](images/assurance/img/client360-image047.png)

### Issue Dashlet

This dashlet highlights any active or historical issues associated with the selected client. If the client is currently experiencing or has recently experienced network-related problems, they will be prominently displayed here for quick identification and action.
![Screenshot](images/assurance/img/client360-image049.png)

### Onboarding Dashlet

The Onboarding dashlet provides a clear view of the client's current connection status, showing which SSID the client is connected to and the specific device being used.
![Screenshot](images/assurance/img/client360-image051.png)

Clicking the **"View device 360"** button will seamlessly redirect you to the Device 360 page, offering more detailed information about the client's device itself.
![Screenshot](images/assurance/img/client360-image053.png)
![Screenshot](images/assurance/img/client360-image055.png)

### Event Viewer

This dedicated section provides a comprehensive, filterable view of all events associated with the client. It offers a chronological log of activities, changes, and alerts, which is invaluable for detailed troubleshooting and auditing.
![Screenshot](images/assurance/img/client360-image057.png)

### Application Experience

This section provides insights into the client's application performance and overall experience, helping to identify if network issues are impacting specific applications.
![Screenshot](images/assurance/img/client360-image059.png)

### Detailed Information

The Detailed Information section is organized into four distinct tabs, each providing in-depth data about various aspects of the client's configuration and performance.

#### Device Info

This tab displays comprehensive information about the client's device, including hardware details, operating system, and other relevant specifications.
![Screenshot](images/assurance/img/client360-image061.png)

#### Connectivity

This tab provides detailed statistics and parameters related to the client's network connectivity, such as IP address, MAC address, and connection duration.
![Screenshot](images/assurance/img/client360-image063.png)

#### RF (Radio Frequency)

This tab offers insights into the client's radio frequency performance and the surrounding RF environment, including channel utilization and interference levels.
![Screenshot](images/assurance/img/client360-image065.png)
![Screenshot](images/assurance/img/client360-image067.png)

#### User Defined Network

This tab shows information related to any user-defined network configurations or policies applied to the client.
![Screenshot](images/assurance/img/client360-image069.png)

### Special Client Cases

Certain clients may display additional or specific information based on their characteristics or device type.

#### Grace Smith - iPad

For the "Grace Smith-ipad" client, a unique downfall graph is displayed, illustrating specific performance trends or issues over time.
![Screenshot](images/assurance/img/client360-image071.png)

Additionally, for both "Grace Smith-ipad" and "Grace Smith Galaxy-S23" clients, detailed issue data is available within the Issue dashlet. For all other clients, this section will typically show "no data available."
![Screenshot](images/assurance/img/client360-image073.png)

#### Grace Smith - iPad and Grace Smith - MacBook: iOS Analytics

For "Grace Smith-iPad" and "Grace Smith-MacBook" clients, an extra tab named **"IOS Analytics"** will be present under the Detailed Information section. This tab provides specific analytical data tailored for iOS devices, offering deeper insights into their performance and behavior.
![Screenshot](images/assurance/img/client360-image075.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/user360/ -->
## User 360 Demo Guide

### Introduction

This guide provides a comprehensive walkthrough for demonstrating the User360 feature within the Assurance > Health dashboard. User360 offers a powerful, unified view of client information, encompassing connectivity details, user-specific issues, onboarding status, application usage, and insightful analytics. Follow these steps to effectively showcase User360's capabilities, including global user search, interface navigation, and understanding its various informational components (dashlets) and detailed views.

### Accessing and Navigating User360

#### Step 1: Accessing User360 Using Global Search

To begin, use the global search bar to locate a client. Enter the client's username, then select the desired user from the search results. This action will automatically open the User360 page for that client.

![Screenshot](images/assurance/img/user360-image001.png)

![Screenshot](images/assurance/img/user360-image003.png)

#### Step 2: Viewing the User360 Global Graph

Upon navigating to the User360 page, a global graph visually represents the selected user's connectivity and network associations.

![Screenshot](images/assurance/img/user360-image005.png)

Hover over any element within the graph to reveal detailed information about the user's network journey, including connected devices and associated access points.

![Screenshot](images/assurance/img/user360-image007.png)

#### Step 3: Reviewing the Summary Dashlet

The **Summary Dashlet** provides a high-level overview of the client's onboarding experience, roaming activity, and current connectivity status.

![Screenshot](images/assurance/img/user360-image009.png)

> **Note:** Currently, this section displays static data (identical for all clients) as development is ongoing. Future updates will provide dynamic, client-specific information.

For more granular details regarding Onboarding, Roaming, or Connectivity, click the respective "View Details" links. This will navigate you to the Event Viewer for further analysis.

![Screenshot](images/assurance/img/user360-image011.png)

![Screenshot](images/assurance/img/user360-image013.png)

![Screenshot](images/assurance/img/user360-image015.png)

![Screenshot](images/assurance/img/user360-image017.png)

#### Step 4: Checking the Issue Dashlet

The **Issue Dashlet** prominently displays any network or connectivity issues that the selected client is currently experiencing. This section is crucial for quickly identifying and addressing client-specific problems.

![Screenshot](images/assurance/img/user360-image019.png)

#### Step 5: Exploring the Onboarding Dashlet

The **Onboarding Dashlet** shows which SSID the client connected to and the device used during the onboarding process. Hover over elements for additional information, or click to be redirected to the Device360 page for a comprehensive view of the device.

![Screenshot](images/assurance/img/user360-image021.png)

![Screenshot](images/assurance/img/user360-image023.png)

#### Step 6: Reviewing the Event Viewer

The **Event Viewer** presents a chronological timeline of key events pertinent to the selected client, including onboarding attempts, authentication events, and connectivity changes. This view is invaluable for diagnosing issues and gaining a deeper understanding of the client's network experience.

![Screenshot](images/assurance/img/user360-image025.png)

#### Step 7: Application Dashlet

The **Application Dashlet** provides insights into the applications accessed by the user, detailing usage patterns and traffic. Utilize this information to understand user behavior and optimize network resource utilization.

![Screenshot](images/assurance/img/user360-image027.png)

#### Step 8: Examining Detailed Information

The **Detailed Information** section offers in-depth client data, categorized for easy analysis:

##### Device Info

Provides comprehensive details about the client device, such as its type, operating system, and manufacturer.

![Screenshot](images/assurance/img/user360-image029.png)

##### Connectivity

Displays information related to connection history, current signal strength, and associated access points.

![Screenshot](images/assurance/img/user360-image031.png)

##### RF (Radio Frequency)

Presents metrics related to wireless performance, signal quality, and potential interference.

![Screenshot](images/assurance/img/user360-image033.png)

##### IOS Analytics

Offers insights derived from Cisco IOS data analytics, focusing on user connectivity and performance.

![Screenshot](images/assurance/img/user360-image035.png)

##### User Defined Network

Shows custom network settings or user-specific configurations that may be applied.

![Screenshot](images/assurance/img/user360-image037.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/device360/ -->
```
## Device 360
```

### Introduction

This guide provides a step-by-step walkthrough for navigating and utilizing the Device 360 Page within Cisco Assurance. You will learn how to access device-specific details, interpret health and event data, use diagnostic tools, and view device topologies. The instructions include visuals and detailed steps to ensure you can confidently demonstrate the Device 360 Page's functionality across various device types, such as routers, access points, core/distribution/access devices, and wireless controllers.

---

### Step 1: Accessing the Health Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image001.png)

- From the Homepage, open the main menu.
- Navigate to **Assurance > Dashboards > Health** tab.

---

### Step 2: Opening the Network Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image003.png)

- The Health tab opens by default to the **Overall** view.
- Click the **Network** tab to switch the view.

---

### Step 3: Navigating to the Device 360 Page

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image005.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image007.png)

- In the **Network** tab, scroll down to the network devices table to find the device details.
- Click the desired **device name** to open its Device 360 Page.
- Alternatively, use the **global search** for the device name, and access the Device 360 Page from the search results.

---

### Step 4: Viewing Device Health and Details

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image009.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image011.png)
![device360-image013](images/assurance/img/device360-image013.png)

- The Device 360 Page provides an overview graph showing the device health score, issues, events, and telemetry status over time.
- Hover over any interval on the graph to view detailed information about health score, system plane, data plane, and event details.
- Device basic details are displayed below the graph. Click **View All Details** to open a pop-up with comprehensive device information.

---

### Step 5: Exploring Physical Neighbor Topology

![device360-image015](images/assurance/img/device360-image015.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image017.png)

- The **Physical Neighbor Topology** section visualizes the device's connection topology.
- Clicking on any device within the topology displays its basic details.

---

### Step 6: Using the Event Viewer Tab

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image019.png)

- The **Event Viewer** tab lists events handled by the device, with associated timestamps.
- Selecting an event opens its details in a pop-up on the right.
- Click **Go to Global Event Viewer** to navigate to **Assurance > Dashboard > Issues and Events > Events**.

---

### Step 7: Reviewing Device Details by Device Type

#### Routers

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image021.png)

- Shows **CPU**, **Memory**, and **Uptime** fields.

#### Access Points

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image023.png)

- Displays device information, availability, CPU, memory, and an AP to WLC Connectivity Chart.

#### Core, Distribution, and Access Devices

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image025.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image027.png)

- Shows **CPU**, **CPU Name**, **Memory**, **Reachability**, **Temperature**, and **Temperature Sensor Name**.

#### Wireless Controllers

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image029.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image031.png)

- Includes fields for **Availability**, **HA Redundancy**, **Client Count**, **CPU**, **CPU Name**, **Memory**, **Reachability**, **Temperature**, **Temperature Sensor Name**, **Monitored AP Count**, and **AP Licenses**.

---

### Step 8: Using the Tools Tab for Access Points

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image033.png)

- Access Points feature an **Extra Tools** tab in Device 360.

---

### Step 9: Using the Ping Tool

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image035.png)

- Select **Tools > Ping**.
- The output will be displayed in the right-side tab.

---

### Step 10: Using the Trace Route Tool

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image037.png)

- Select **Tools > Trace Route**.
- The output will be displayed in the right-side tab.

---

### Step 11: AP Data Collection

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image039.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image041.png)

- Select **Tools > AP Data Collection**.
- This action opens a new tab displaying Wireless LAN Controller (WLC) details.

---

### Step 12: AP Reboot

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image043.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image045.png)

- Select **Tools > AP Reboot**.
- A pop-up will appear; click **Reboot**.
- An **In Progress** pop-up will display. Click **OK**.
- After some time, a **Success** message appears.

---

### Step 13: Radio Reset

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image047.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image049.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image051.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image053.png)

- Select **Tools > Radio Reset**.
- A pop-up appears; select the radio and click **Reset**.
- An **In Progress** pop-up will display.
- Once complete, a **Success** pop-up confirms the reset.

---

### Step 14: Flash LED

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image055.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-image057.png)

- Select **Tools > Flash LED**.
- A pop-up appears; click **Enable**.
- A **Success** message will confirm the action.

---

**End of Guide**


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/device360-int/ -->
## Device 360

### Introduction

This guide provides a step-by-step walkthrough of the **Device 360** feature for three device types: Switch, Wireless LAN Controller (WLC), and Access Point (AP). It covers how to access device details and interface data in Cisco's Assurance Network platform, highlighting differences in available information for each device type. Follow the instructions below to successfully demonstrate Device 360 capabilities.

---

### Part 1: Switch Device

#### Navigation: Assurance → Health → Network

##### Step 1

Scroll down to the **Network Devices** table.

![device360-int-image001](images/assurance/img/device360-int-image001.png)

##### Step 2

Click on any device under **Device Name**.

![device360-int-image003](images/assurance/img/device360-int-image003.png)

This action opens the device details page.

##### Step 3

Scroll down to find the **Interfaces** tab.

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-int-image005.png)

##### Step 4

Click on **Interfaces**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-int-image007.png)

---

### Part 2: WLC Device

#### Navigation: Home Page

![device360-int-image009](images/assurance/img/device360-int-image009.png)

##### Step 1

Use the global search to select the `LDN1-C9800-01` device.

![device360-int-image011](images/assurance/img/device360-int-image011.png)

##### Step 2

Click on **Device 360**.

![device360-int-image013](images/assurance/img/device360-int-image013.png)

This opens the WLC Device 360 page.

##### Step 3

Scroll down to find the **Interfaces** tab.

![device360-int-image015](images/assurance/img/device360-int-image015.png)

##### Step 4

Click on **Interfaces**.

You will now see the WLC device interface data.

![A screenshot of a computer  Description automatically generated](images/assurance/img/device360-int-image019.png)

---

### Part 3: AP Device

#### Navigation: Assurance → Health → Network

##### Step 1

Go to the **Network Devices** table.

![device360-int-image021](images/assurance/img/device360-int-image021.png)

##### Step 2

Select the `C9120AXI-LDN1-3FFC` device.

![device360-int-image023](images/assurance/img/device360-int-image023.png)

> **Note:**  
> AP devices do not have an **Interfaces** tab or interface data.  
> Only Switch and WLC devices display interface data.

![device360-int-image025](images/assurance/img/device360-int-image025.png)

---

### Summary

- **Switches and WLC devices**: Provide detailed device and interface data via the Device 360 view.
- **AP devices**: Do not display interface data or the Interfaces tab.

Use this guide to quickly demonstrate the Device 360 interface and highlight the different views and data available for each device type.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/ssid-monitoring/ -->
## SSID Monitoring Settings in Assurance

### Introduction

This guide provides a step-by-step walkthrough of configuring and verifying SSID Monitoring Settings within Cisco's Assurance platform. You will learn how to navigate to the relevant settings, ensure proper configuration, and confirm that the SSID monitoring feature is functioning as expected. This process is demonstrated using data from the 211 cluster.

---

### Navigating to SSID Monitoring Settings

1. **Access Assurance Settings**
2. From the main dashboard, navigate to:  
   **Assurance** → **Settings** → **SSID Monitoring Settings**
3. **Verify Functionality**
4. Ensure that SSID Monitoring Settings are working as expected.
5. The current system configuration has been validated and is functioning correctly.

---

### Data Source

- The demonstration utilizes data specific to the 211 cluster.

---

### Reference Screenshot

The following image illustrates the SSID Monitoring Settings screen:

![ssid-monitoring-image001](images/assurance/img/ssid-monitoring-image001.png)

---

### Summary

This guide outlined the process for accessing and verifying SSID Monitoring Settings within Cisco Assurance. Proper configuration ensures effective monitoring of SSIDs and supports optimal network assurance operations.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/msteams/ -->
## Microsoft Teams 360 Demo Guide

This comprehensive demo guide provides a step-by-step walkthrough of the MS Teams 360 feature, designed to help you efficiently showcase its powerful capabilities. MS Teams 360 offers a holistic view of user experience and meeting performance within Microsoft Teams, enabling administrators and support staff to quickly diagnose and troubleshoot quality issues. By following these instructions, you will learn how to navigate the client 360-page, delve into detailed meeting and quality metrics, and interpret various performance graphs for audio, video, and content sharing.

---

### Step 1: Access the User 360 Page for the Target User

To begin your analysis, you will first need to locate the specific user whose Microsoft Teams performance you wish to investigate.

- Use the **Global Search** function, typically found at the top of the interface, to search for the target user. For example, type "Grace Smith" into the search bar.

  ![Screenshot](images/assurance/img/msteams-image001.png)
- From the search results, click on the user's name (e.g., "grace-smith") to open their dedicated User 360 page. This page provides an overview of the user's various activities and device usage.

  ![Screenshot](images/assurance/img/msteams-image003.png)
- On the User 360 page, select the relevant device associated with the user (e.g., "grace-smith-iphone"). This step is crucial for viewing device-specific insights and ensuring the data pertains to the correct endpoint used during the Teams meetings.

  ![Screenshot](images/assurance/img/msteams-image005.png)

---

### Step 2: Navigate to the MS Teams 360 Section

Once on the device-specific User 360 page, you can access the Microsoft Teams performance data.

- Click on the **MS Teams 360** option, usually located in a prominent section or tab on the page.
- This section will display a chronological list of recent Microsoft Teams meetings associated with the selected user and device, providing a quick overview of their meeting history.

  ![Screenshot](images/assurance/img/msteams-image007.png)

---

### Step 3: View Meeting Details and Audio Quality

To dive deeper into a specific meeting's performance, select it from the list.

- Click on the first meeting record in the list to open its detailed information panel. This panel provides a comprehensive breakdown of the meeting's performance metrics.

  ![Screenshot](images/assurance/img/msteams-image009.png)
- Review the **Audio Quality** metrics, paying close attention to the MS Teams Score and Packet Loss statistics. The MS Teams Score indicates overall audio quality, while Packet Loss can highlight network congestion or instability impacting voice clarity.
- Scroll down to examine additional performance graphs for this meeting, which offer visual representations of various audio parameters over time.

  ![Screenshot](images/assurance/img/msteams-image011.png)
- Continue scrolling to view more detailed graphs, which can help identify trends or specific moments of degradation in audio performance.

  ![Screenshot](images/assurance/img/msteams-image013.png)

---

### Step 4: Analyze Video Quality Metrics

Beyond audio, MS Teams 360 provides granular insights into video performance.

- Select the **Video Quality** tab or section within the meeting details.
- Review all available graphs and data visualizations related to video performance. These metrics typically include video clarity, latency, frame rate, and resolution, allowing you to identify issues such as pixelation, freezing, or delays.

  ![Screenshot](images/assurance/img/msteams-image015.png)
- Carefully examine the graphs to pinpoint any anomalies or drops in video quality, which could indicate bandwidth limitations, device performance issues, or network problems.

  ![Screenshot](images/assurance/img/msteams-image017.png)

---

### Step 5: Review Sharing Quality Metrics

Content sharing is a critical component of collaboration. This section helps assess its performance.

- Click on the **Share Quality** tab or section to view insights into content sharing performance during the meeting.
- Analyze all relevant graphs that display metrics related to sharing, such as delays in content updates, quality fluctuations, or interruptions. These insights can reveal if network conditions or application performance affected the ability to share screens or documents effectively.

  ![Screenshot](images/assurance/img/msteams-image019.png)
- Look for patterns in the graphs that might explain user complaints about shared content appearing blurry, laggy, or not updating in real-time.

  ![Screenshot](images/assurance/img/msteams-image021.png)

---

### Step 6: Exit the MS Teams 360 View

Once your analysis is complete, you can return to the previous view.

- After reviewing all necessary details and gathering your insights, close the current window or navigate back to return to the main User 360 interface. From there, you can proceed to analyze another user or device, or conclude your investigation.

  ![Screenshot](images/assurance/img/msteams-image023.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/webex/ -->
## Webex 360 Demo Guide

### Introduction

This guide provides a comprehensive, step-by-step walkthrough for demo users to navigate the Webex 360 interface. You will learn how to efficiently review meeting details and analyze media quality metrics for a specific user, focusing on audio, video, and content sharing performance in meetings held within the last 24 hours. This process is essential for troubleshooting and ensuring a high-quality Webex experience.

---

### Step 1: Accessing a User's Client 360 Profile

1. **Navigate to Global Search:** Start by navigating to the **Global Search** feature within your Webex environment.
2. **Search for the User:** Enter the demo user's name, `Grace Smith`, into the search bar.

![Screenshot](images/assurance/img/webex-image001.png)

1. **Open Client 360:** From the search results, select the appropriate user entry (e.g., `Grace.Smith-Galaxy on Host`) and click on **Client 360** to open their detailed profile.

![Screenshot](images/assurance/img/webex-image002.png)

---

### Step 2: Navigating to Webex 360

Once on the Client 360 page, locate and select the **Webex 360** tab. This action will redirect you to the specialized interface dedicated to meeting analytics and media quality insights.

![Screenshot](images/assurance/img/webex-image003.png)

---

### Step 3: Searching for the User within Webex 360

Within the Webex 360 dashboard, locate the user search area, which is typically identified by an email icon.

Enter the demo user's email address, `gracesmith@cisco.com`, to filter and display relevant meeting data for Grace Smith.

![Screenshot](images/assurance/img/webex-image004.png)

---

### Step 4: Displaying Recent Meeting Details

1. **Search Meetings:** Click the **Search Meetings** button to retrieve a list of all meetings associated with the specified user.

![Screenshot](images/assurance/img/webex-image005.png)

1. **Review Meeting List:** The platform will then display all meetings Grace Smith has participated in over the past 24 hours, allowing for immediate analysis.

![Screenshot](images/assurance/img/webex-image006.png)

---

### Step 5: Selecting a Specific Meeting for Analysis

From the displayed list of recent meetings, click on the first meeting entry to access its detailed media quality metrics.

![Screenshot](images/assurance/img/webex-image007.png)

---

### Step 6: Analyzing Audio Quality Metrics

1. **Review Audio Quality Graph:** Examine the **Audio Quality** graph, which provides insights into the audio performance during the meeting:
   - The **Application** line (green) indicates the audio quality as perceived by the Webex application itself.
   - The **Network** line (green or yellow) reflects the underlying network conditions. Pay attention if the line turns yellow towards the end, as this indicates minor network issues affecting audio.

![Screenshot](images/assurance/img/webex-image008.png)

1. **Examine Additional Audio Graphs:** Scroll down to review any supplementary audio-related graphs for a more comprehensive insight into overall audio performance.

![Screenshot](images/assurance/img/webex-image009.png)

![Screenshot](images/assurance/img/webex-image010.png)

---

### Step 7: Reviewing Video Quality Metrics

1. **Navigate to Video Quality:** Click on the **Video Quality** tab or section to shift your focus to video performance metrics.

![Screenshot](images/assurance/img/webex-image011.png)

1. **Study Video Quality Graph:** Carefully examine the **Video Quality** graph:
   - The **Application** line (green) should remain steady, indicating good video quality from the Webex application's perspective.
   - The **Network** line should also predominantly be green. Any yellow segments indicate brief degradations in network quality, especially if observed towards the meeting's conclusion.

![Screenshot](images/assurance/img/webex-image012.png)

1. **Examine Additional Video Graphs:** Scroll down to view supplementary video quality graphs for a more detailed analysis of video performance.

![Screenshot](images/assurance/img/webex-image013.png)

![Screenshot](images/assurance/img/webex-image014.png)

---

### Step 8: Checking Share Quality Metrics

1. **Navigate to Share Quality:** Navigate to the **Share Quality** tab or section to analyze screen sharing performance.

![Screenshot](images/assurance/img/webex-image015.png)

1. **Examine Share Quality Graph:** Examine the **Share Quality** graph, which illustrates the quality of content sharing:
   - The **Application** line (green) should indicate consistent performance in sharing.
   - A yellow **Network** line in the final minutes suggests a slight dip in network quality that may have impacted sharing.

![Screenshot](images/assurance/img/webex-image016.png)

1. **Review Additional Share Graphs:** Scroll further to view additional graphs related to sharing performance for a complete picture.

![Screenshot](images/assurance/img/webex-image017.png)

![Screenshot](images/assurance/img/webex-image018.png)

---

### Step 9: Concluding the Analysis

Once you have thoroughly reviewed all media quality metrics (audio, video, and sharing), simply close the Webex 360 window to complete the analysis process.

![Screenshot](images/assurance/img/webex-image019.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/app-health/ -->
## Cisco Assurance Dashboard: Applications Health Tab

### Introduction

This guide provides a step-by-step walkthrough for using the **Applications** tab within the **Health** section of the Cisco Assurance Dashboard. It covers navigation, data visualization, analysis of application health, and exploration of detailed application metrics, including ThousandEyes tests and device exporters. The guide is designed to help demo users efficiently understand and demonstrate the dashboard's key features and capabilities.

---

### Step 1: Navigate to the Health Tab

![app-health-image001](images/assurance/img/app-health-image001.png)

- From the homepage, open the main menu.
- Go to **Assurance > Dashboards > Health**.

---

### Step 2: Access the Applications Tab

![app-health-image003](images/assurance/img/app-health-image003.png)

- Once in the **Health** tab, the overall health page will appear.
- Click on the **Applications** tab to proceed.

---

### Step 3: Review Application Health Overview

![A screenshot of a computer  Description automatically generated](images/assurance/img/app-health-image005.png)

- The **Applications** tab displays a graph showing:
- Average throughput
- Application health
- ThousandEyes test results (in percentage)
- You can filter the graph by **site** and **time duration**.
- Navigation options allow you to move to the previous or next timestamps and reload to the current time.
- The **ThousandEyes Test Dashboard** summarizes:
- Number of tests run
- Active alerts from tests
- Number of agents running the tests

---

### Step 4: Explore the Applications Table

![A screenshot of a computer  Description automatically generated](images/assurance/img/app-health-image007.png)

- The applications table lists detailed information for each application.
- Clicking an application name takes you to the **Application 360** page for more in-depth details.

---

### Step 5: Application 360 Page

![A screenshot of a computer  Description automatically generated](images/assurance/img/app-health-image009.png)

- The **Application 360** page provides:
- A graph showing the application's health score over time
- Filters to adjust by **site** and **time duration**
- The average health score displayed below the graph

---

### Step 6: View Exporter Devices for the Application

![A screenshot of a computer  Description automatically generated](images/assurance/img/app-health-image011.png)

- The page lists exporter devices associated with the current application.
- Clicking an exporter’s name reveals:
- The device's **Applications Endpoints** under the table
- Two additional graphs related to exporter performance

![app-health-image013](images/assurance/img/app-health-image013.png)

![app-health-image015](images/assurance/img/app-health-image015.png)

![app-health-image017](images/assurance/img/app-health-image017.png)

![app-health-image019](images/assurance/img/app-health-image019.png)

![app-health-image021](images/assurance/img/app-health-image021.png)

---

### Step 7: Examine ThousandEyes Test Details

![app-health-image023](images/assurance/img/app-health-image023.png)

- The table provides expandable details for each test, as referenced in the **ThousandEyes Tests Dashboard**.

Click on **Office 365 login** to view Test details

![app-health-image024](images/assurance/img/app-health-image024.png)

The Test details will load in the new tab

![app-health-image025](images/assurance/img/app-health-image025.png)

---

### Conclusion

This guide has outlined the steps to navigate and utilize the **Applications** tab within the Cisco Assurance Health Dashboard. By following these instructions, users can effectively demonstrate how to access, analyze, and interpret application health metrics, test results, and related device data.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/event-analytics/ -->
## Cisco Catalyst Center: Event Analytics

### Introduction

This hands-on laboratory session introduces you to the powerful Event Analytics feature, designed to enhance network visibility and management efficiency. You'll learn how to monitor your network, detect behavioral changes, and correlate different event types for both wired and wireless devices.

This guide will walk you through:

- Navigating the Event Analytics dashboard
- Analyzing network events by domain and type
- Using analytics features to isolate relevant events during interesting time periods
- Accessing individual events for detailed insights
- Creating user-defined issues based on observed patterns

By the end of this demo, you'll be able to move from a global event overview down to the specifics of a single device or interface, improving your network troubleshooting and management workflow.

---

### What is Event Analytics?

**Event Analytics** is a feature introduced in Cisco Catalyst Center version 2.3.7, providing comprehensive network event visibility across wired and wireless domains. Unlike traditional systems that require predefined issue signatures, Event Analytics uses machine learning and AI to process network event data and detect anomalies—even when specific signatures are not defined. Innovative data visualization techniques help you quickly identify and investigate potential issues in real time.

#### Benefits

- Broad visibility across all network domains
- Real-time anomaly detection using AI and ML
- Streamlined investigation workflow from overview to detailed event analysis
- Ability to define and be notified of custom, user-defined issues

---

### Supported Event Types

| **Event Type** | **Wired** | **Wireless** |
| --- | --- | --- |
| Syslog | X | X |
| Reachability | X | X |
| Radio events |  | X |
| Client events | \* | X |

*Note: Wired client events will be added in a future release.*

#### Event Type Descriptions

- **Syslog:** Messages collected from switches, routers, and Wireless LAN Controllers (WLCs). By default, only metadata (message type, severity, mnemonic) is exported to the Cisco AI Cloud for privacy. Full text export requires explicit user consent.
- **Reachability:** Reflects changes in device status as monitored by Catalyst Center (e.g., device joins/disjoins, reachable, unreachable).
  - **REACHABLE:** Device is fully manageable
  - **PING\_REACHABLE:** Device responds to pings but is not fully manageable
  - **UNREACHABLE:** Device is offline
- **Radio events:** Includes channel changes, power adjustments, coverage hole detection, and radio resets (wireless only).
- **Client events:** Onboarding and roaming events for wireless clients. Wired client events to be added in a future release.

---

### Event Analytics Workflow

#### 1. Accessing the Dashboard

Navigate to the **Event Analytics** dashboard:

**Menu > Assurance > Issue and Events > Event Analytics - Preview**

![AI-Driven issues - Hamburger menu](images/assurance/img/event-analytics-image001.png)

Select the **Event Analytics - Preview** tab at the top:

## event analytics preview is missing

![AI-Driven issues - Issues menu](images/assurance/img/event-analytics-image003.png)

---

#### 2. Heatmap Overview

The **Heatmap** provides a visual overview of network event volumes by type and category for the selected time period.

![Event Analytics - Heatmap overview](images/assurance/img/event-analytics-image005.png)

- **Default View:** Last 24 hours, showing Syslog and Reachability events for all wired devices (switches and routers).
- **Customization:** Filter by location, extend the time period (up to 60 days), or switch between wired and wireless views.

**Interpreting the Heatmap:**

- Darker areas indicate higher event volumes.
- Each event category has its own color scale, making rare events (e.g., high-severity Syslog messages) easier to spot.

![Event Analytics - Heatmap scale](images/assurance/img/event-analytics-image007.png)

- **High severity** event spikes require immediate attention.
- Increases in **medium or low severity** events may indicate behavioral changes worth investigating.

**First Investigation Step:**
- Identify time periods with significant changes in event volume.
- Example: Observe dense Syslog message areas and increased reachability events within the same timeframe.

![Event Analytics - Correlation across different event types](images/assurance/img/event-analytics-image009.png)

---

#### 3. Time Selection and Analytics

**Note:** From this point, the Event Analytics workflow can only be followed via this lab guide due to demo system limitations.

##### Time Selection

The heatmap helps you pinpoint when significant event volume changes occur and provides initial correlation across event types.

- Click on a heatmap time bucket to restrict your analysis to that period.
- Adjust the selection using the selector bars.

Example: A 1-hour period (each block in 24-hour view represents 15 minutes).

![Heatmap time selection](images/assurance/img/event-analytics-image011.png)

After selection, summary info below each category updates to reflect the event count in the chosen timeframe.

---

#### 4. Card View: Show Analytics

Click **Show Analytics** to expand and view event summaries as cards, specific to each event type.

- **Syslog Cards:** Highlight highest severity events, highest volume, rare types, and those with volume changes.
- Identify **new events**—those that started near the end of the selected period.
- Also, see **top network devices** based on event volume.

![Heatmap card view](images/assurance/img/event-analytics-image013.png)

---

#### 5. Detailed Event View

Choose a card of interest (e.g., Highest Severity Events) and click **Show details** for an in-depth view.

##### a. Detailed Heatmap

Shows the evolution of top event types over the selected period. By default, shows the top 3 events (up to 5 selectable), sorted by card criteria.

![Detailed view - Events heatmap](images/assurance/img/event-analytics-image017.png)

##### b. Sankey Diagram

Visualizes the impact of specific event types by site and device.

![Detailed view - Sankey](images/assurance/img/event-analytics-image019.png)

- Interact with the diagram to see event distribution across sites/devices.
- Example: Spanning tree messages from two specific devices.

![Detailed view - Sankey select event type](images/assurance/img/event-analytics-image021.png)

- Select a device with the most events to view details:
  - Example: Top events are `SPANTREE-2-BLOCK_BPDUGUARD` and `PORT_SECURITY-2-PSECURE_VIOLATION`.

![Detailed view - Sankey select network device](images/assurance/img/event-analytics-image023.png)

##### c. Event Table

Displays individual events for full details. By default, shows events for the heatmap selection. Interact with the Sankey diagram to filter by event type, location, or device.

- Example: Focus on a device producing the most high-severity events—see that spanning tree and port security messages are tied to interfaces `Gi1/0/37` and `Gi1/0/38`.

![Table view - Select device](images/assurance/img/event-analytics-image025.png)
![Table view - Analyize events](images/assurance/img/event-analytics-image027.png)

**In just a few clicks, you can move from an overview to a specific device and interface affected by an issue.**

---

#### 6. Configuring User-Defined Issues

Event Analytics enables you to define custom issues based on identified patterns, even if they don't match known issue signatures.

- To be notified about similar future events, create a **user-defined issue** directly from the event table:

![User defined issue - link](images/assurance/img/event-analytics-image029.png)

- Confirm your choice in the prompt:

![User defined issue - confirm](images/assurance/img/event-analytics-image031.png)

- You'll be taken to Issue Settings to finalize the issue creation:

![User defined issue - create](images/assurance/img/event-analytics-image033.png)

- Specify matching patterns, issue priority, and notification settings:

![User defined issue - pattern](images/assurance/img/event-analytics-image035.png)

---

### Key Takeaways

- **Event Analytics** provides cross-domain visibility and supports multiple event types for both wired and wireless networks.
- Advanced analytics and visualization tools make it easy to detect and investigate significant network events, even without predefined issue triggers.
- Quickly correlate, isolate, and analyze events—then create custom notifications for ongoing monitoring.

**This concludes the exploration of the Event Analytics feature.**  
Continue with the next lab or explore additional use cases as needed.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/events/ -->
## Navigating the Assurance Dashboard – Issues and Events

### Introduction

This demo guide provides a step-by-step walkthrough of how to use the **Assurance > Dashboard > Issues and Events** feature, focusing specifically on the **Events** tab. You will learn how to access event data, filter and analyze events, and review detailed information for both devices and endpoints. This guide is designed to help users efficiently navigate and utilize the dashboard for effective event monitoring and troubleshooting.

---

### Step 1: Access the Issues and Events Dashboard

Navigate to the main menu on the homepage and select:

**Assurance > Dashboard > Issues and Events**

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image001.png)

---

### Step 2: Open the Events Tab

After entering the "Issues and Events" section of the dashboard, the default view is the **Issues** page. To access events:

- Click the **Events** tab in the top menu.

The Events page will now be displayed.

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image003.png)

On this page, you will see a graph illustrating the number of events that occurred on devices and endpoints during each time interval.

- **Filtering Options:**
- Filter event data by site and time duration.
- Use the navigation buttons on the right to view previous, next, or current time intervals.

---

### Step 3: Analyze Events by Time Interval

The graph provides a visual overview of event occurrences within specific intervals.

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image005.png)

Hover over or select a segment of the graph to view the number of events that occurred during a particular interval. Double click this segment to filter the events in the table.

---

### Step 4: View Detailed Event Table

Below the graph, a table presents detailed information for each event within the selected intervals.

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image007.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image009.png)

- **Filtering Options:**
- Filter events by device or endpoint.
- Further refine the view by device or endpoint type.

---

### Step 5: Review Event Details

For more information about a specific event:

- Click the event name in the table.
- A pop-up window will display detailed event information, including the event timeline from start to end with timestamps.

This functionality applies to both device and endpoint events.

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image011.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/events-image013.png)

---

### Summary

Following these steps, you can efficiently access, filter, and analyze events within the Assurance dashboard. This enables proactive monitoring and detailed investigation of issues affecting your network devices and endpoints.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/issues/ -->
## Cisco Assurance: Issues and Events

### Introduction

This guide provides a step-by-step walkthrough of the Cisco Assurance Issues and Events interface. You will learn how to:
- View and filter issues based on different time ranges
- Interpret issue tables and priority breakdowns
- Use AI-driven filtering
- Navigate and analyze specific common issues (such as device disconnections, wireless client failures, and more)
- Run machine reasoning and suggested actions to diagnose and resolve issues

All screenshots and image references are retained from the original guide to assist you visually in each step.

---

### Table of Contents

1. [Viewing Issues and Events](#viewing-issues-and-events)
   - 1.1 [Accessing the Issues Graph](#accessing-the-issues-graph)
   - 1.2 [Adjusting the Time Range](#adjusting-the-time-range)
2. [Understanding the Issues Table](#understanding-the-issues-table)
   - 2.1 [Records per Time Range](#records-per-time-range)
   - 2.2 [Priority Counts (P1–P4)](#priority-counts-p1p4)
   - 2.3 [AI-Driven Issue Filter](#ai-driven-issue-filter)
3. [Investigating Specific Issue Types](#investigating-specific-issue-types)
   - 3.1 [Interface Connecting Network Devices is Down](#interface-connecting-network-devices-is-down)
   - 3.2 [Layer 2 Loop Symptoms](#layer-2-loop-symptoms)
   - 3.3 [Switch Unreachable](#switch-unreachable)
   - 3.4 [Switch Power Failure](#switch-power-failure)
   - 3.5 [Fabric Devices Connectivity - ISE Server](#fabric-devices-connectivity---ise-server)
   - 3.6 [WLC Unreachable](#wlc-unreachable)
   - 3.7 [Fabric Devices Connectivity - Control Border Underlay](#fabric-devices-connectivity---control-border-underlay)
   - 3.8 [Wireless Client Connection Issues](#wireless-client-connection-issues)
   - 3.9 [StackWise Virtual Link Failure](#stackwise-virtual-link-failure)
   - 3.10 [Wireless Client - Excessive Association Failures](#wireless-client---excessive-association-failures)
   - 3.11 [Excessive Failures to Connect - High Deviation from Baseline](#excessive-failures-to-connect---high-deviation-from-baseline)

---

### 1. Viewing Issues and Events

#### 1.1 Accessing the Issues Graph

- Navigate to **Assurance → Issues and Events**.
- Go to the **Issues** section.
- By default, you will see the issues graph for the last 24 hours.

![Issues Graph - 24 Hours](images/assurance/img/issues-image001.png)

---

#### 1.2 Adjusting the Time Range

You can select various time ranges to view issues.

**Step 1: Select 3 Hours**

- Choose the **3 hours** time range and click **Apply**.

![3 Hours Time Range Option](images/assurance/img/issues-image003.png)

- The graph updates to display issues from the last 3 hours.

![Issues Graph - 3 Hours](images/assurance/img/issues-image005.png)

**Step 2: Select 7 Days**

- Choose the **7 days** time range and click **Apply**.

![7 Days Time Range Option](images/assurance/img/issues-image007.png)

- The graph updates to display issues from the last 7 days.

![Issues Graph - 7 Days](images/assurance/img/issues-image009.png)

---

### 2. Understanding the Issues Table

#### 2.1 Records per Time Range

The **Issues Table** updates based on the selected time range.

- **24 hours:** 15 records  
  ![Issues Table - 24 Hours](images/assurance/img/issues-image011.png)
- **3 hours:** 10 records  
  ![Issues Table - 3 Hours](images/assurance/img/issues-image013.png)
- **7 days:** 30 records  
  ![Issues Table - 7 Days](images/assurance/img/issues-image015.png)

---

#### 2.2 Priority Counts (P1–P4)

- The table shows issue priorities: P1, P2, P3, and P4.
- For example, in the **All** tab:  
  P1: 4, P2: 6, P3: 8, P4: 7 (Total: 25)

![Priority Count Overview](images/assurance/img/issues-image017.png)

- The sum of P1–P4 issues matches the total count in the Issues Table.

##### Viewing by Priority

- Click on **P1** to filter and confirm the count matches the table.
  ![P1 Issues](images/assurance/img/issues-image019.png)
- Click on **P2**, **P3**, and **P4** to view their respective issue counts.
- ![P2 Issues](images/assurance/img/issues-image021.png)
- ![P3 Issues](images/assurance/img/issues-image023.png)
- ![P4 Issues](images/assurance/img/issues-image025.png)

---

#### 2.3 AI-Driven Issue Filter

- Toggle the **AI Driven** switch to display only AI-driven issues and their counts.

![AI Driven Issue Filter](images/assurance/img/issues-image017.png)

- Navigate to **Assurance → Issues and Events → Issues** to see all issues in the table.

##### Issues Not Displayed in Table

If certain issues are not shown:

![Issues Not Displayed](images/assurance/img/issues-image029.png)

---

### 3. Investigating Specific Issue Types

This section provides a quick reference for analyzing and resolving various issues using the interface.

---

#### 3.1 Interface Connecting Network Devices is Down

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image031.png)
2.  
![Step 2](images/assurance/img/issues-image033.png)
3. Click **Run Machine Reasoning** to view Reasoning Activity and Conclusions.  
![Step 3](images/assurance/img/issues-image035.png)

---

#### 3.2 Layer 2 Loop Symptoms

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image037.png)
2.  
![Step 2](images/assurance/img/issues-image039.png)
3. Click **Root Cause Analysis**.  
![Step 3](images/assurance/img/issues-image041.png)
4. Click **Run Machine Reasoning**.  
![Step 4](images/assurance/img/issues-image043.png)

---

#### 3.3 Switch Unreachable

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image045.png)
2.  
![Step 2](images/assurance/img/issues-image047.png)

---

#### 3.4 Switch Power Failure

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image049.png)
2.  
![Step 2](images/assurance/img/issues-image051.png)
3.  
![Step 3](images/assurance/img/issues-image053.png)

> **Tip:** Change the Time Range from 24 hours to 7 days to see all issues.
> ![Change Time Range](images/assurance/img/issues-image055.png)

---

#### 3.5 Fabric Devices Connectivity - ISE Server

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image057.png)
2.  
![Step 2](images/assurance/img/issues-image059.png)
3. Click **Suggested Actions**.  
![Step 3](images/assurance/img/issues-image061.png)
4. Click **Run**.  
![Step 4](images/assurance/img/issues-image063.png)

---

#### 3.6 WLC Unreachable

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image065.png)
2.  
![Step 2](images/assurance/img/issues-image067.png)

---

#### 3.7 Fabric Devices Connectivity - Control Border Underlay

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image069.png)
2.  
![Step 2](images/assurance/img/issues-image071.png)
3. Click **Suggested Actions**.  
![Step 3](images/assurance/img/issues-image073.png)
4. Click **Run**.  
![Step 4](images/assurance/img/issues-image075.png)

---

#### 3.8 Wireless Client Connection Issues

##### A. Wireless Clients Took a Long Time to Connect - Failed Credentials

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image077.png)
2.  
![Step 2a](images/assurance/img/issues-image079.png)
![Step 2b](images/assurance/img/issues-image081.png)
3.  
![Step 3](images/assurance/img/issues-image083.png)
4.  
![Step 4a](images/assurance/img/issues-image085.png)
![Step 4b](images/assurance/img/issues-image087.png)
![Step 4c](images/assurance/img/issues-image089.png)
![Step 4d](images/assurance/img/issues-image091.png)

##### B. Wireless Clients Took a Long Time to Connect - WLC Failures

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image093.png)
2.  
![Step 2](images/assurance/img/issues-image095.png)
3.  
![Step 3](images/assurance/img/issues-image097.png)
4.  
![Step 4](images/assurance/img/issues-image099.png)
5.  
![Step 5](images/assurance/img/issues-image101.png)
6.  
![Step 6a](images/assurance/img/issues-image103.png)
![Step 6b](images/assurance/img/issues-image105.png)
7.  
![Step 7](images/assurance/img/issues-image107.png)

##### C. Wireless Clients Failed to Connect - Security Parameter Mismatch

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image109.png)
2.  
![Step 2](images/assurance/img/issues-image111.png)
3.  
![Step 3](images/assurance/img/issues-image113.png)
4.  
![Step 4](images/assurance/img/issues-image115.png)
5.  
![Step 5a](images/assurance/img/issues-image117.png)
![Step 5b](images/assurance/img/issues-image119.png)
6.  
![Step 6](images/assurance/img/issues-image121.png)

##### D. Wireless Clients Failed to Connect - AAA Server Rejected Clients

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image123.png)
2.  
![Step 2](images/assurance/img/issues-image125.png)
3.  
![Step 3](images/assurance/img/issues-image127.png)
4.  
![Step 4](images/assurance/img/issues-image129.png)
5.  
![Step 5a](images/assurance/img/issues-image131.png)
![Step 5b](images/assurance/img/issues-image133.png)
![Step 5c](images/assurance/img/issues-image135.png)
![Step 5d](images/assurance/img/issues-image137.png)

---

#### 3.9 StackWise Virtual Link Failure

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image139.png)
2.  
![Step 2a](images/assurance/img/issues-image141.png)
![Step 2b](images/assurance/img/issues-image143.png)
![Step 2c](images/assurance/img/issues-image145.png)
3.  
![Step 3](images/assurance/img/issues-image147.png)
4. Click **Run**. The issue moves to the **Running** stage, then to **Success**.

![Run Stage 1](images/assurance/img/issues-image149.png)
![Run Stage 2](images/assurance/img/issues-image151.png)
![Run Stage 3](images/assurance/img/issues-image153.png)
![Run Stage 4](images/assurance/img/issues-image155.png)
![Run Stage 5](images/assurance/img/issues-image157.png)
![Run Stage 6](images/assurance/img/issues-image159.png)

---

#### 3.10 Wireless Client - Excessive Association Failures

**Scenario:**  
Wireless client took a long time to connect (SSID: PseudoCo-Corp, AP: CW9166I-LDN1-01, Band: 2.4 GHz) due to excessive association failures.

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image161.png)
2.  
![Step 2](images/assurance/img/issues-image163.png)
3.  
![Step 3](images/assurance/img/issues-image165.png)

---

#### 3.11 Excessive Failures to Connect - High Deviation from Baseline

**Steps:**
1.  
![Step 1](images/assurance/img/issues-image167.png)
2.  
![Step 2](images/assurance/img/issues-image169.png)
3.  
![Step 3](images/assurance/img/issues-image171.png)
4.  
![Step 4a](images/assurance/img/issues-image173.png)
![Step 4b](images/assurance/img/issues-image175.png)
5.  
![Step 5](images/assurance/img/issues-image177.png)
6.  
![Step 6](images/assurance/img/issues-image179.png)
7.  
![Step 7](images/assurance/img/issues-image181.png)
8.  
![Step 8](images/assurance/img/issues-image183.png)
9.  
![Step 9](images/assurance/img/issues-image185.png)

---

### Conclusion

This guide is intended to help you confidently navigate the Cisco Assurance Issues and Events interface, interpret issue data, and leverage advanced features such as AI-driven insights and machine reasoning. For further support or advanced troubleshooting, refer to the official Cisco documentation or reach out to Cisco support.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/ai-issues/ -->
## AI-Driven Issues

### Introduction

This guide provides a hands-on walkthrough of the AI-Driven anomaly detection features in Cisco Catalyst Center Assurance. You'll learn how to interpret and respond to AI/ML-generated issues that help proactively identify, analyze, and resolve network anomalies. The guide covers the following:

- Overview of AI-driven issue detection and baselining
- Types of issues detected by AI/ML algorithms
- Step-by-step workflows to investigate and resolve various network anomalies
- How to use the Assurance Issue dashboard and its key features
- Practical use cases and interpretation of visualizations and metrics

Follow the steps to gain insight into how Cisco Catalyst Center leverages AI and ML to enhance network reliability and simplify troubleshooting.

---

### AI-Driven Issues Overview

In this lab session, you will explore the AI-Driven anomaly detection feature and learn how to utilize the issues generated by the AI/ML algorithm. The advanced baselining allows you to focus on the most relevant issues and provides detailed information to help you resolve identified anomalies.

This guide will walk you through a typical AI-Driven anomaly detection workflow:

- Get an overview of detected network issues, organized by location and category, using the Assurance Issue dashboard.
- Compare expected network performance (computed by the AI/ML baselining algorithm) with actual network performance when an anomaly is detected.
- Gain guidance to further understand the impacted clients and access points, as well as potential root causes.

---

### Benefits of AI-Driven Anomaly Detection

The AI-driven anomaly detection feature extends the range of issues available in *Cisco Catalyst Center Assurance*. It leverages Artificial Intelligence and Machine Learning (AI/ML) to model network performance, learning from past behavior and network conditions (such as client types, applications used, RF conditions, etc.).

Unlike traditional static thresholds, the AI/ML model generates a baseline defining the expected lower and upper bounds of a given KPI for each network entity. An anomaly is raised when the actual KPI falls outside these boundaries.

**Advantages of this approach:**

- Alerts are context-aware, considering past network behavior and current conditions.
- No manual configuration is required; baselines are automatically computed and continuously updated for each network entity.
- The system reduces false positives and ensures that only truly anomalous events trigger alerts.

To benefit from AI-Driven anomaly detection issues, ensure your network devices are discovered and managed by the *Cisco Catalyst Center* appliance and that the *Cisco AI Analytics* service is enabled. For setup details, see [Lab 8 - Service Operations](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/).

---

### AI-Driven Issue Types

The AI-Driven issue types in Cisco Catalyst Center version 2.3.7 are organized into two main categories:

- [Onboarding and Roaming](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab2_ai_driven_issues/#onboarding-and-roaming)
- [Throughput](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab2_ai_driven_issues/#throughput)

#### Onboarding and Roaming

This category focuses on Wireless LAN client connection and roaming events. AI/ML baselining is particularly beneficial for these use cases due to the many factors influencing onboarding and roaming performance, such as SSID security policy, building infrastructure, client types, and time-of-day traffic patterns.

| **Issue Type** | **Target KPI** | **Input Data** | **Entity Aggregation** |
| --- | --- | --- | --- |
| Excessive time to connect | Expected time to complete Wireless LAN onboarding | Successful attempts | WLC, SSID, and Building |
| Excessive failures to connect | Expected failure rate for Wireless LAN onboarding | Failed attempts | WLC, SSID, and Building |
| Excessive failures to roam | Expected failure rate for Wireless LAN roaming | Failed attempts | SSID, Source & Destination Building |
| Excessive time to Associate | Expected time to complete 802.11 (re)association | Successful attempts | SSID and Building |
| Excessive failures to Associate | Expected number of association failures | Failed attempts | SSID and Building |
| Excessive time to get Authenticated | Expected time to complete AAA authentication (802.1x/PSK) | Successful attempts | SSID and Building |
| Excessive failures to get Authenticated | Expected authentication failure rate (802.1x/PSK) | Failed attempts | AAA Server |
| Excessive time to get an IP Address | Expected time to complete IP address learning | Successful attempts | SSID and Building |
| Excessive failures to get an IP address | Expected IP address learning failure rate | Failed attempts | DHCP Server |

*Static thresholds are often too rigid for these scenarios; AI/ML models learn and adapt to your network’s unique patterns, ensuring accurate anomaly detection.*

---

#### Throughput

This category focuses on modeling application throughput for Wireless LAN clients. AI/ML baselining is crucial as throughput can vary greatly depending on factors such as client number, client types, applications used, and RF conditions.

| **Issue Type** | **Sample Applications** |
| --- | --- |
| Drop in total radio throughput | All |
| Drop in radio throughput for Cloud Applications | Office 365, Salesforce, Google Workspace, iCloud, etc. |
| Drop in radio throughput for Collaboration Apps | SIP, Webex, MS Teams, Slack, Facetime, etc. |
| Drop in radio throughput for Social Apps | Facebook, Instagram, LinkedIn, Twitter, etc. |
| Drop in radio throughput for Media Applications | YouTube, Netflix, Hulu, ESPN, etc. |

---

### Using the Assurance Issue Dashboard

The AI-driven issues are presented in the [Assurance Issue Dashboard](https://dcloud-dnac-inst-cl-lon.cisco.com/dna/assurance/dashboards/issues-events/issues/open). Access it from the main menu:

**Menu > Assurance > Issues and Events**

![AI-Driven issues - Hamburger menu](images/assurance/img/ai-issues-image001.png)

AI-Driven issues are easily recognized by the **AI** tag in front of the *Issue Type*. You can use the AI-Driven filter to view only these issues:

![AI-Driven issues - Dashboard view](images/assurance/img/ai-issues-image003.png)

The dashboard groups issues by type and shows a summary for the selected time period (optionally filtered by site), including issue count and last occurrence.

---

### Investigating AI-Driven Issues

To explore an AI-Driven issue, click on the issue type and select a specific issue. For example, select **Drop in total radio throughput**:

![AI-Driven issues - Select Cloud Application Throughput issue](images/assurance/img/ai-issues-image005.png)

#### AI-Issue Overview

When you open an AI-Driven issue, a summary displays key information about the anomaly detected by the AI/ML engine:

- Time and date of the anomaly
- Location
- Information about the affected AP and radio band
- Number of impacted clients

The **Problem Details** view presents the KPI chart:

- **Blue line:** Actual KPI values observed on the AP
- **Green band:** Predicted normal KPI value range (baseline)
- **Red bands:** Periods when the KPI was anomalous

![AI-Driven issues - Problem details](images/assurance/img/ai-issues-image007.png)

---

#### Impact Analysis

The issue overview refers to a specific radio, considering a variety of RF and traffic-related KPIs for the affected radio and associated clients.

Knowing that a traffic anomaly was detected helps you identify critical network areas where client experience is suffering. To get more details:

**Impact View Tabs:**

- **Impacted Clients:** Shows all clients connected to the affected radio during the anomaly, with RF summary and device classification. Clicking on a client’s MAC Address takes you to the Device 360 view; clicking on the Username opens the User 360 view.

![AI-Driven issues - Impacted clients](images/assurance/img/ai-issues-image009.png)

- **Device Breakout:** Displays throughput aggregated by device type, helping you identify traffic patterns by client type.

![Alt text](images/assurance/img/ai-issues-image011.png)

- **Applications by TX/RX:** Shows throughput for each application observed during the period and highlights those that experienced a drop.

![AI-Driven issues - Impacted Apps](images/assurance/img/ai-issues-image013.png)

---

#### Root Cause Analysis

Next, explore the **Root Cause Analysis** tab to review KPIs related to the affected radio. This helps you understand the network conditions at the time the anomaly was detected.

The system automatically highlights the most probable network causes by pre-selecting KPIs that are likely to explain the issue.

![AI-Driven throughput issue - Root Cause Analysis](images/assurance/img/ai-issues-image015.png)

For example, if there’s a significant throughput drop, you might observe an increase in clients with low RSSI (e.g., up to 80% of clients at less than -80 dBm RSSI), indicating degraded wireless connection quality.

You can add more KPIs to the analysis for additional context:

![AI-Driven throughput issue - Add KPIs to Root Cause Analysis view](images/assurance/img/ai-issues-image017.png)

---

### Key Takeaways

AI-Driven issues are powerful for detecting network anomalies, especially for KPIs where static thresholds or simple rules often result in high alert noise or missed events.

AI/ML techniques create dynamic baselines tailored to each network entity, using historical data and current network conditions to identify deviations.

---

### Step-by-Step Use Case Workflows

Below are example workflows for common AI-Driven issues. Each workflow includes all original images in their original positions.

---

#### Excessive Failures to Connect – High Deviation from Baseline

**Step 1:**

![ai-issues-image019](images/assurance/img/ai-issues-image019.png)

**Step 2:**

![ai-issues-image021](images/assurance/img/ai-issues-image021.png)

**Step 3:**

![ai-issues-image023](images/assurance/img/ai-issues-image023.png)

![ai-issues-image025](images/assurance/img/ai-issues-image025.png)

**Step 4:**

![ai-issues-image027](images/assurance/img/ai-issues-image027.png)

![ai-issues-image029](images/assurance/img/ai-issues-image029.png)

**Step 5:**

![ai-issues-image031](images/assurance/img/ai-issues-image031.png)

![ai-issues-image033](images/assurance/img/ai-issues-image033.png)

![ai-issues-image035](images/assurance/img/ai-issues-image035.png)

![ai-issues-image037](images/assurance/img/ai-issues-image037.png)

**Step 6:**

![ai-issues-image039](images/assurance/img/ai-issues-image039.png)

---

#### Excessive Time to Connect – High Deviation from Baseline

**Step 1:**

![ai-issues-image041](images/assurance/img/ai-issues-image041.png)

**Step 2:**

![ai-issues-image043](images/assurance/img/ai-issues-image043.png)

**Step 3:**

![ai-issues-image045](images/assurance/img/ai-issues-image045.png)

**Step 4:**

![ai-issues-image047](images/assurance/img/ai-issues-image047.png)

![ai-issues-image049](images/assurance/img/ai-issues-image049.png)

**Step 5:**

![ai-issues-image051](images/assurance/img/ai-issues-image051.png)

![ai-issues-image053](images/assurance/img/ai-issues-image053.png)
![ai-issues-image055](images/assurance/img/ai-issues-image055.png)
![ai-issues-image057](images/assurance/img/ai-issues-image057.png)

**Step 6:**

![ai-issues-image059](images/assurance/img/ai-issues-image059.png)

---

#### Excessive Time to Get an IP Address – High Deviation from Baseline

**Step 1:**

![ai-issues-image061](images/assurance/img/ai-issues-image061.png)

**Step 2:**

![ai-issues-image063](images/assurance/img/ai-issues-image063.png)

**Step 3:**

![ai-issues-image065](images/assurance/img/ai-issues-image065.png)

**Step 4:**

![ai-issues-image067](images/assurance/img/ai-issues-image067.png)

**Step 5:**

![ai-issues-image069](images/assurance/img/ai-issues-image069.png)

**Step 6:**

![ai-issues-image071](images/assurance/img/ai-issues-image071.png)

![ai-issues-image073](images/assurance/img/ai-issues-image073.png)

![ai-issues-image075](images/assurance/img/ai-issues-image075.png)

**Step 7:**

![ai-issues-image077](images/assurance/img/ai-issues-image077.png)

---

#### Drop in Radio Throughput for Cloud Applications

**Step 1:**

![ai-issues-image079](images/assurance/img/ai-issues-image079.png)

**Step 2:**

![ai-issues-image081](images/assurance/img/ai-issues-image081.png)

**Step 3:**

![ai-issues-image083](images/assurance/img/ai-issues-image083.png)

**Step 4:**

![ai-issues-image085](images/assurance/img/ai-issues-image085.png)
![ai-issues-image087](images/assurance/img/ai-issues-image087.png)
![ai-issues-image089](images/assurance/img/ai-issues-image089.png)

**Step 5:**

![ai-issues-image091](images/assurance/img/ai-issues-image091.png)

**Step 6:**

![ai-issues-image093](images/assurance/img/ai-issues-image093.png)

---

#### Drop in Total Radio Throughput

**Step 1:**

![ai-issues-image095](images/assurance/img/ai-issues-image095.png)

**Step 2:**

![ai-issues-image097](images/assurance/img/ai-issues-image097.png)

**Step 3:**

![ai-issues-image099](images/assurance/img/ai-issues-image099.png)

**Step 4:**

![ai-issues-image101](images/assurance/img/ai-issues-image101.png)

![ai-issues-image103](images/assurance/img/ai-issues-image103.png)

![ai-issues-image105](images/assurance/img/ai-issues-image105.png)

**Step 5:**

![ai-issues-image107](images/assurance/img/ai-issues-image107.png)

**Step 6:**

![ai-issues-image109](images/assurance/img/ai-issues-image109.png)

---

### Conclusion

With AI-Driven issues, Cisco Catalyst Center enables proactive, context-aware anomaly detection and guided troubleshooting. This demo guide equips you to leverage these features, improving both network reliability and user experience. Continue exploring other use cases and features to further enhance your operational capabilities.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/baselines/ -->
## AI-Driven Baseline Dashboard

### Introduction

Welcome to the AI-Driven Baseline Dashboard Demo Guide. This document will walk you through the key features and workflows of the Baseline Dashboard—a powerful tool designed to provide unparalleled visibility into your network’s performance. Using AI-driven analytics, the dashboard helps you identify problematic buildings, discover outliers, compare key performance indicators (KPIs), and perform deep dives to understand network impacts on clients and Access Points (APs).

In this lab, you will:

- Gain an overview of network performance across all buildings using beeswarm visualization.
- Identify interesting buildings based on AI-driven anomaly detection issues or outlier status.
- Compare expected versus actual behavior across multiple KPIs and WLANs.
- Drill into each entity and KPI to analyze the impact on clients and APs.

---

### Benefits

The Baseline Dashboard allows you to explore and analyze network performance by comparing expected and actual Wi-Fi KPI values across different buildings, SSIDs, and time periods.

Key benefits include:

- No manual configuration required—just ensure your devices are managed by the Cisco Catalyst Center appliance, are exporting telemetry data, and have Cisco AI Analytics enabled ([see Lab 8 - Service Operations](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/)).
- Extended visibility even when no anomalies are detected.
- Ability to identify both sudden changes (anomalies) and persistent behaviors.

*Note: This lab uses a pre-configured system, as baselines typically require about a week of data to become available.*

---

### Workflow Overview

The Baseline Dashboard workflow guides users through network data exploration, focusing on onboarding-related KPIs and their baselines:

- **Identify good, bad, or busy buildings at a glance.**
- **See the evolution of expected vs. actual KPI values** over time for an SSID within a building.
- **Compare baselines for different KPIs** for the same SSID within a selected building.
- **Compare baselines for the same KPI across different SSIDs** within a building.
- **Perform deeper analysis** using the detailed view.

---

### Getting Started

#### Accessing the Baseline Dashboard

1. Open the [Baseline Dashboard Page](https://dcloud-dnac-inst-cl-lon.cisco.com/dna/assurance/trends/baselines):  
   **Menu > Assurance > AI Network Analytics > Baselines**
2. Follow the steps below to explore the dashboard.

![Baseline Dashboard - Menu item](images/assurance/img/baselines-image001.png)

---

#### Time Selection

- By default, the dashboard displays data from the last 24 hours.
- To expand the time range, use the **Custom Range** selector.

![Baseline Dashboard default time selection](images/assurance/img/baselines-image002.png)
*Note: The end date selection is not available in the current version.*

---

### Building Overview and Selection

Get an overview of all buildings to select one for deeper investigation.

The default visualization is a **beeswarm plot**:

- Each circle represents a **building**.
- Circle size indicates average **client count** for the selected period—spot busy buildings easily.
- **Red circles**: At least one AI-driven issue detected in the time period.
- **Blue circles**: No issues detected.
- X-axis position: Average of the selected KPI (default is Onboarding Time), helping you spot good or bad performers.

![Baseline Dashboard Beeswarm view](images/assurance/img/baselines-image003.png)

#### What Makes a Building "Interesting"?

Examples:

- **A busy building with good performance but marked in red:**  
  Example: *LONDON 1*
- Position: Left-hand side (average onboarding time < 2 seconds)
- Red color: At least one AI-driven issue reported

![Baseline Dashboard - Building with issues](images/assurance/img/baselines-image004.png)

- **A building with consistently bad performance but no issues:**  
  Example: *SAN FRANCISCO 1*
- Right-hand side of the beeswarm (high onboarding time)
- Blue color: No issues—AI/ML considers the persistent poor performance as "normal"

![Baseline Dashboard - Building no issues outlier](images/assurance/img/baselines-image005.png)

The beeswarm chart is highly effective for quickly assessing network health, even in large deployments.

**Tip:** If you already know which building to analyze (e.g., after a user complaint), use the map or table view for quick selection.

![Baseline Dashboard map or list](images/assurance/img/baselines-image006.png)

---

### Exploring Building Baseline Views

#### Selecting a Building

*What building did you choose to analyze first?*

---

#### Example 1: Building with Issues (*LONDON 1*)

After clicking the red circle for *LONDON 1*, you’ll see the baseline view, displaying all onboarding KPIs for one SSID.

- Adjust KPIs, SSIDs, and WLCs using the dropdowns at the top.

![Baseline Building KPI SSID WLC selection](images/assurance/img/baselines-image007.png)

##### Single SSID View

- Track how predicted and actual KPIs change over time.
- See AI-driven issue reports and access details.
- Identify if anomalies affect single or multiple KPIs.

![Baseline Dashboard - Default baseline view, 1 SSID with issue](images/assurance/img/baselines-image008.png)

##### Multiple SSIDs View

- Different SSIDs may show very different "normal" behaviors.
- Add SSIDs from the dropdown to compare predicted ranges and actual values across SSIDs.

To add a second SSID (e.g., *PseudoCo-Corp*):
- Click the **SSID** menu, select **PseudoCo-Corp**.

![Baseline Building add SSID](images/assurance/img/baselines-image009.png)

The updated view allows you to see, for example, that only the *PseudoCo-Guest* SSID was affected by an issue, while *PseudoCo-Corp* behaved normally.

![Baseline Dashboard - Baseline view, 2 SSIDs](images/assurance/img/baselines-image010.png)

---

#### Example 2: Building with No Issues (*SAN FRANCISCO 1*)

Now, review the *SAN FRANCISCO 1* building, which had no issues but consistently high onboarding times.

- Click **Network Overview** (top-left) to return to the beeswarm, then select *SAN FRANCISCO 1*.
- Add the *PseudoCo-Corp* SSID as previously described.

![Baseline Building add SSID](images/assurance/img/baselines-image011.png)

Now compare both SSIDs in the same building.

![Baseline Building add SSID](images/assurance/img/baselines-image017.png)

Resulting view:

![Baseline Dashboard - Baseline view, 2 SSIDs no issues](images/assurance/img/baselines-image012.png)

---

### KPI Detailed View

Baselines in the detailed view are computed for each *entity* (usually aggregated by SSID and building).

To investigate further (e.g., *SAN FRANCISCO 1*, *PseudoCo-Corp* SSID):

- Click **View Details** next to the SSID name under the Onboarding Time KPI.

![Baseline Building add SSID](images/assurance/img/baselines-image014.png)

The **Detailed View** provides:

- Client count time series
- AP table: Onboarding KPIs and direct links to the AP360 page for each AP.

*Note: Client type is based on device classification from the Wireless LAN Controller (WLC). Unclassified devices are labeled as "Device".*

![Baseline Detailed View](images/assurance/img/baselines-image018.png)

---

### Key Takeaways

- **AI/ML-based baselining** is a powerful way to understand typical network behavior and manage large volumes of data.
- The algorithms adapt over time to learn what is "normal," reducing unnecessary alerts and focusing attention on significant issues.
- However, persistent poor performance may be normalized by the algorithms and not trigger alerts. Thus, the Baseline Dashboard is essential for maintaining visibility into both sudden and ongoing performance issues.

---

This concludes the exploration of the **Baselines Dashboard** feature.  
You can use the link below to proceed with the exploration of other use cases.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/heatmap/ -->
## Cisco Catalyst Center: Network Heatmap Page Demo Guide

This guide provides a comprehensive walkthrough of the Network Heatmap Page in Cisco Catalyst Center. This powerful visualization tool allows network administrators to monitor the health, performance, and coverage of both Access Points (APs) and Switches within their network. Learn how to leverage advanced filtering options and intuitive visual cues to quickly identify and troubleshoot network issues, optimize resource allocation, and ensure high-quality connectivity across your organization.

This demo guide is divided into two main parts:
\* **Part 1: Access Points** - Focuses on monitoring and filtering AP data.
\* **Part 2: Switches** - Focuses on monitoring and filtering Switch data.

---

### Part 1: Access Points

This section guides you through using the Network Heatmap to monitor and manage your Access Points.

#### Step 1: Navigate to Network Heatmap

- From the Homepage, click on the **Menu** and go to **Assurance > Network Heatmap**.

![Screenshot](images/assurance/img/heatmap-image001.png)

#### Step 2: Access and Filter Access Points Data

- The Network Heatmap will open directly to the Access Points page.
- Use the filter options to refine your view by **KPI** (Key Performance Indicator), **AP band** (e.g., 2.4GHz or 5GHz), and select whether to display **Average** or **Maximum** values in the **"View By"** menu.
- The filtered radio data for APs will display below according to your selections.

![Screenshot](images/assurance/img/heatmap-image002.png)

![Screenshot](images/assurance/img/heatmap-image003.png)

#### Step 3: Select and Highlight Specific Access Points

- Click on the **Select AP** option to view a list of all available Access Points.

![Screenshot](images/assurance/img/heatmap-image004.png)

- Choosing one or more APs will highlight the selected devices on the heatmap, making it easy to identify impacted APs.

![Screenshot](images/assurance/img/heatmap-image005.png)

#### Step 4: View AP Details on Hover

- Hover over any AP block in the heatmap to view detailed information, such as location, MAC address, radio band, and current KPI value.

![Screenshot](images/assurance/img/heatmap-image006.png)

#### Step 5: Filter Access Points by Location

- To focus on a specific area, click the **Location** filter.

![Screenshot](images/assurance/img/heatmap-image007.png)

- A pop-up window will appear with a searchable list of locations. Select your desired location, and the table will update to show APs in that area.

![Screenshot](images/assurance/img/heatmap-image008.png)

![Screenshot](images/assurance/img/heatmap-image009.png)

#### Step 6: Filter Access Points by Time Range

- Use the **Time Range** filter to view AP data for a specific month or day.

![Screenshot](images/assurance/img/heatmap-image010.png)

- The displayed information will update to reflect your chosen time frame, helping you analyze trends or recent issues.

![Screenshot](images/assurance/img/heatmap-image011.png)

---

### Part 2: Switches

This section guides you through using the Network Heatmap to monitor and manage your Switches.

#### Step 1: Access Switches in the Heatmap

- To view Switch data, click on the **Show** option and select **Switches**.

![Screenshot](images/assurance/img/heatmap-image012.png)

#### Step 2: Filter Switches by Sensor Type KPI and Family

- Use the **Sensor Type KPI** filter to refine the switch list based on specific performance metrics.

![Screenshot](images/assurance/img/heatmap-image013.png)

- You can further filter by **Switch Family** to focus on certain device models. The filtered switch details will be shown in the table below for easy review and analysis.

![Screenshot](images/assurance/img/heatmap-image014.png)

![Screenshot](images/assurance/img/heatmap-image015.png)

#### Step 3: Filter Switches by Name

- From the table, you can filter switches directly by their names to quickly locate specific devices.

![Screenshot](images/assurance/img/heatmap-image016.png)

#### Step 4: View Switch Details on Hover

- Hover over a switch block in the heatmap to display detailed information, such as location, serial number, device type, and more.

![Screenshot](images/assurance/img/heatmap-image017.png)

#### Step 5: Filter Switches by Location

- Click the **Location** filter at the top of the page.

![Screenshot](images/assurance/img/heatmap-image018.png)

- In the pop-up window, search for and select your desired location.

![Screenshot](images/assurance/img/heatmap-image019.png)

- The table below will update to display switches from the selected location for easy review.

![Screenshot](images/assurance/img/heatmap-image020.png)

#### Step 6: Filter Switches by Time Range

- Use the **Time Range** filter to view switch performance data for a particular month or day.
- This helps in tracking performance trends or diagnosing recent network events.

![Screenshot](images/assurance/img/heatmap-image021.png)

![Screenshot](images/assurance/img/heatmap-image022.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/site-analytics/ -->
## Site Analytics Demo Guide

### Introduction

This guide provides a comprehensive walkthrough for demonstrating the Site Analytics feature within AI Analytics. You will learn how to navigate through different site hierarchy levels—Global, Europe, England, and London 1—to access and interpret analytics data and graphical dashboards (dashlets). Each dashboard presents insights specific to its respective site level, offering a clear view of performance metrics. This guide will demonstrate how to load and review both data and graphical representations across all available dashlets at each hierarchy level, with annotated screenshots to aid in identification.

### Site Hierarchy Overview

The site hierarchy is organized as follows, allowing for granular analysis from a broad overview to specific locations:

- Global
- Europe (within Global)
- England (within Europe)
- London 1 (within England)

### Navigating Site Analytics

#### Step 1: Accessing the Health Dashboard

To begin, navigate to the **Assurance** section from the main menu and then select **Health** to access the related analytics dashboards.

![Screenshot](images/assurance/img/site-analytics-image001.png)

#### Step 2: Selecting Site Analytics

From the main navigation bar, click on **AI Analytics** and then choose **Site Analytics**. Verify that you are in the **Site Analytics** section by confirming the selection in the dropdown menu on the AI Analytics page.

![Screenshot](images/assurance/img/site-analytics-image003.png)

#### Step 3: Exploring Analytics at Each Site Hierarchy Level

This section details how to explore analytics data at each level of the defined site hierarchy.

##### Global Level Analytics

Select the **Global** level to view aggregated analytics data for all sites across the entire organization. This view provides high-level insights and overall trends.

![Screenshot](images/assurance/img/site-analytics-image005.png)

![Screenshot](images/assurance/img/site-analytics-image007.png)

##### Europe Region Analytics (Global/Europe)

Next, select the **Europe** region within the Global hierarchy. The dashboard will update to display analytics specifically for Europe, allowing you to focus on regional performance and metrics.

![Screenshot](images/assurance/img/site-analytics-image009.png)

![Screenshot](images/assurance/img/site-analytics-image011.png)

##### England Site Analytics (Global/Europe/England)

Drill down further by selecting **England** within the Europe region. The dashboard will now present detailed analytics relevant to the England site, enabling localized analysis.

![Screenshot](images/assurance/img/site-analytics-image013.png)

![Screenshot](images/assurance/img/site-analytics-image015.png)

##### London 1 Site Analytics (Global/Europe/England/London 1)

For the most granular view, select the **London 1** site within England. Here, you will see site-specific data and graphs, providing in-depth operational insights for London 1.

![Screenshot](images/assurance/img/site-analytics-image017.png)

![Screenshot](images/assurance/img/site-analytics-image019.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/peer-compare/ -->
## Cisco Assurance: Peer Comparison Demo Guide

**Introduction**

This guide provides a comprehensive walkthrough of the Peer Comparison feature within Cisco Assurance. Designed for network administrators and demo users, this feature allows you to effectively analyze and benchmark your network's performance against similar environments. By leveraging detailed Key Performance Indicator (KPI) filters, you can gain actionable insights to enhance network reliability, optimize user experience, and proactively address potential issues.

Throughout this guide, you will learn how to:
\* Navigate to the Peer Comparison dashboard.
\* Apply and interpret various KPI filters.
\* Utilize comparative metrics to identify trends and anomalies.

Let's begin exploring how to maximize the value of Cisco Assurance's Peer Comparison capabilities.

### Peer Comparison Walkthrough

#### Step 1: Navigate to Peer Comparison Dashboard

To access the Peer Comparison feature:

- From the Cisco Assurance platform, follow this navigation path:
  `Assurance -> Peer Comparison`
- This action will open the Peer Comparison dashboard, where you can begin assessing your network's performance relative to peer environments.

![Screenshot](images/assurance/img/peer-compare-image001.png)

#### Step 2: Using KPI Filters for Comparative Analysis

The Peer Comparison dashboard is equipped with several Key Performance Indicator (KPI) filters, enabling you to focus on specific aspects of network health and performance. For each selected KPI, you can view comparative metrics, identify performance trends, and spot anomalies across your network and peer networks.

To use the filters:

- Select the desired KPI from the dropdown list available on the Peer Comparison dashboard.

Below is an overview of each available KPI and how it can be utilized for effective comparative analysis:

---

##### KPI: RSSI (Received Signal Strength Indicator)

- **Purpose:** To compare the signal strength received by client devices across your network and peer networks.
- **Usage:** Apply the RSSI filter to identify areas with weak wireless coverage or potential connectivity issues. The dashboard visualizes signal distribution, helping you target improvements in wireless signal quality.

![Screenshot](images/assurance/img/peer-compare-image003.png)

![Screenshot](images/assurance/img/peer-compare-image005.png)

---

##### KPI: Cloud Apps Throughput

- **Purpose:** To analyze throughput and bandwidth usage specifically for cloud applications among your peers.
- **Usage:** Select this filter to benchmark cloud application performance, pinpoint potential bottlenecks, and ensure optimal bandwidth allocation for your critical cloud-based applications.

![Screenshot](images/assurance/img/peer-compare-image007.png)

![Screenshot](images/assurance/img/peer-compare-image009.png)

---

##### KPI: Interference

- **Purpose:** To assess and compare wireless interference levels that could degrade network quality.
- **Usage:** Use this KPI to detect sources of interference (such as neighboring networks or devices) and take proactive corrective measures to maintain signal integrity and improve network performance.

![Screenshot](images/assurance/img/peer-compare-image011.png)

![Screenshot](images/assurance/img/peer-compare-image013.png)

---

##### KPI: Onboarding Error Source

- **Purpose:** To identify the root causes of onboarding failures when client devices attempt to connect to the network.
- **Usage:** Filter by onboarding errors to uncover common issues preventing successful device connections and streamline troubleshooting processes for faster resolution.

![Screenshot](images/assurance/img/peer-compare-image015.png)

![Screenshot](images/assurance/img/peer-compare-image017.png)

---

##### KPI: Packet Failure Rate

- **Purpose:** To measure the rate of failed packets, which is crucial for evaluating overall network reliability.
- **Usage:** Analyze packet failure trends across your network and peer environments to detect reliability issues and take action to minimize data loss or retransmissions, ensuring a stable network.

![Screenshot](images/assurance/img/peer-compare-image019.png)

![Screenshot](images/assurance/img/peer-compare-image021.png)

---

##### KPI: Radio Resets

- **Purpose:** To monitor occurrences of radio resets, events that can significantly impact wireless stability and client connectivity.
- **Usage:** Track and compare radio reset events to identify problematic access points or recurring patterns that require further investigation and remediation.

![Screenshot](images/assurance/img/peer-compare-image023.png)

![Screenshot](images/assurance/img/peer-compare-image025.png)

---

##### KPI: Radio Throughput

- **Purpose:** To review radio throughput statistics, ensuring optimal data transfer rates across your wireless network.
- **Usage:** Use this filter to verify if wireless radios are delivering expected throughput and benchmark their performance against peer networks to identify areas for optimization.

![Screenshot](images/assurance/img/peer-compare-image027.png)

![Screenshot](images/assurance/img/peer-compare-image029.png)

---

##### KPI: Roaming Error Source

- **Purpose:** To analyze the specific causes of errors encountered during client roaming between access points.
- **Usage:** Compare roaming error sources to enhance seamless mobility for users and reduce disruptions as they move across different network areas, improving overall user experience.

![Screenshot](images/assurance/img/peer-compare-image031.png)

![Screenshot](images/assurance/img/peer-compare-image033.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/poe/ -->
## Cisco Assurance – Power over Ethernet (PoE)

### Introduction

This demo guide provides a comprehensive walkthrough of the Power over Ethernet (PoE) assurance features within the Cisco Assurance dashboard. The steps outlined will help you explore and understand key PoE metrics, visualizations, and insights, empowering you to assess power savings, device distribution, operational state, and more. Each section includes instructions and screenshots to help you navigate the Assurance > PoE path effectively.

---

### Step 1: Navigate to the PoE Dashboard

Begin by accessing the PoE dashboard directly:

- Go to: **Dashboard → Assurance → PoE**

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image001.png)

---

### Step 2: Explore PoE Dashboard Overview

Familiarize yourself with the main PoE dashboard view.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image003.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image005.png)

---

### Step 3: Review PoE Dashboard Dashlets

For each dashlet, click **View Details** to explore further insights. Ensure that the "Top Sites" and the count in the table below each dashlet match.

#### a) Estimated AP Power Savings

View estimated power savings for access points.

![poe-image007](images/assurance/img/poe-image007.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image009.png)

---

#### b) AP Power Save Mode Distribution (Latest)

Check the current distribution of AP power save modes.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image011.png)

##### Power Save Mode Trend

Analyze trends in AP power save mode over time.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image013.png)

![poe-image015](images/assurance/img/poe-image015.png)

![poe-image017](images/assurance/img/poe-image017.png)

---

#### c) PoE Operational State Distribution

Review the operational state distribution of PoE devices.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image019.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image021.png)

![poe-image023](images/assurance/img/poe-image023.png)

---

#### d) PoE Powered Device Distribution

Understand the distribution of devices powered via PoE.

![poe-image025](images/assurance/img/poe-image025.png)

![poe-image027](images/assurance/img/poe-image027.png)

![poe-image029](images/assurance/img/poe-image029.png)

---

#### e) PoE Insights

Access actionable insights related to PoE.

![poe-image031](images/assurance/img/poe-image031.png)

![poe-image033](images/assurance/img/poe-image033.png)

---

#### f) Power Allocation Load Distribution

See how power allocation is distributed across devices.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image035.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image037.png)

---

#### g) Power Usage

Monitor the total power usage across devices and time.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image039.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image041.png)

---

#### h) PoE Port Availability

Check available PoE ports in your network.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image043.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image045.png)

---

#### i) PoE AP Power Mode Distribution

Analyze the distribution of AP power modes.

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image047.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/poe-image049.png)

---

### Conclusion

This guide has taken you through the main features and visualizations available in the Assurance > PoE dashboard. By following these steps and reviewing the relevant metrics and trends, you can effectively monitor, analyze, and optimize PoE usage within your network.

For additional help or detailed feature explanations, refer to Cisco documentation or reach out to your Cisco representative.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/network-services/ -->
## Network Services Assurance - DNS Demo Guide

This demo guide provides a step-by-step walkthrough of how to access and interpret DNS (Domain Name System) network services assurance data within the Cisco dashboard. You will learn how to navigate to the DNS health overview, and then drill down into specific metrics such as DNS server latency and transaction details, enabling you to monitor and troubleshoot DNS performance effectively.

### Step 1: Navigating to DNS Network Services Assurance

To begin, navigate to the Network Services Assurance section for DNS. Follow this direct path within the dashboard:

`Dashboard` > `Assurance` > `Health` > `Network Services` > `DNS`

This path will lead you to the main DNS health overview page, where you can see a high-level summary of your DNS services and their current status.

![Screenshot](images/assurance/img/network-services-image001.png)

![Screenshot](images/assurance/img/network-services-image003.png)

![Screenshot](images/assurance/img/network-services-image005.png)

![Screenshot](images/assurance/img/network-services-image007.png)

### Step 2: Exploring DNS Server Details

From the DNS health overview, you can delve deeper into the performance metrics of individual DNS servers. To do this, click on any of the displayed DNS server entries or their associated "View Details" links.

This action will open a detailed view for the selected DNS server, providing more granular insights into its operation and performance.

![Screenshot](images/assurance/img/network-services-image009.png)

![Screenshot](images/assurance/img/network-services-image011.png)

#### DNS Server Latency

Within the detailed view of a specific DNS server, you will find a section dedicated to **DNS Server Latency**. This section displays critical metrics related to the response times of your DNS server, helping you identify potential bottlenecks or performance issues. High latency can indicate network congestion, server overload, or other underlying problems affecting DNS resolution.

![Screenshot](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/network-services/img/network-services-image0013.png)

![Screenshot](images/assurance/img/network-services-image015.png)

#### DNS Server Transactions

Further down in the detailed DNS server view, the **DNS Server Transactions** section provides insights into the volume and success rate of DNS queries handled by the server. This data is crucial for understanding the load on your DNS infrastructure and detecting anomalies in query patterns, such as a sudden drop in successful queries or an unexpected surge in traffic.

![Screenshot](images/assurance/img/network-services-image017.png)

![Screenshot](images/assurance/img/network-services-image019.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/ap-perf/ -->
## AP Performance Advisories

### Introduction

Welcome to the AP Performance Advisories demo guide. This document provides a step-by-step walkthrough of Cisco's AP Performance Advisory feature. You'll learn how to use AI/ML-driven insights to identify wireless Access Points (APs) that persistently deliver a poor client experience, understand root causes, and receive actionable recommendations to optimize your wireless network. The guide is structured to help you explore the feature’s workflow, analytics, and remediation guidance in a clear and concise manner.

---

### Table of Contents

1. [Overview](#overview)
2. [Benefits](#benefits)
3. [How the AP Performance Advisory Feature Works](#how-the-ap-performance-advisory-feature-works)
   - [Algorithm Steps](#algorithm-steps)
4. [Demo Workflow](#demo-workflow)
   - [Landing Page](#landing-page)
   - [Summary Page](#summary-page)
   - [Details Page](#details-page)
5. [Key Takeaways](#key-takeaways)
6. [Additional Use Case: High AP Density at 2.4GHz](#additional-use-case-high-ap-density-at-24ghz)

---

### Overview

The **AP Performance Advisory** feature leverages AI and ML to analyze wireless network data and surface APs or radios that consistently provide a poor client Quality of Experience (QoE). With up to four weeks of data considered, the system helps you quickly pinpoint and resolve performance issues by:

- Providing an overview of detected client experience issues, organized by root cause.
- Grouping problematic radios to help you understand common causes.
- Allowing you to drill down into individual radios for specific insights and guidance.

---

### Benefits

- **Proactive Issue Detection:** Automatically surface APs that consistently deliver suboptimal QoE.
- **Actionable Insights:** Receive clear diagnostics and remediation steps for identified issues.
- **Long-term Analytics:** Weekly-refreshed insights based on up to four weeks of data.
- **Minimal Setup:** No configuration is required beyond enabling controller telemetry and activating the Cisco AI Analytics cloud service (see [Lab 8 - Service Operations](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/)).

---

### How the AP Performance Advisory Feature Works

#### Algorithm Steps

1. **Focus on Top Radios:** Limits analysis to the most important radios, improving relevance and detection accuracy.
2. **Identify Underperforming Radios:** Analyzes KPIs (e.g., RSSI, SNR) against a global baseline per frequency band (2.4 GHz, 5 GHz, 6 GHz).

   ![Global Baselining](images/assurance/img/ap-perf-image001.png)
3. **Apply Unsupervised Learning:** Uses multi-dimensional clustering to group radios with similar issues.

   ![Clustering](images/assurance/img/ap-perf-image003.png)
4. **Apply Supervised Learning:** Uses decision trees to identify key explanatory features (e.g., interference, power, CPU usage).
5. **Root Cause Analysis:** Leverages SME knowledge and AI/ML findings to derive root causes.
6. **Detailed Visualization:** Presents insights through visualizations and tables for easy exploration.

---

### Demo Workflow

The AP Performance Advisory workflow is designed to provide progressively deeper insights:

#### Landing Page

Navigate to **Menu > Assurance > Trends and Insights**.

The landing page presents all discovered radios with potential client experience issues, grouped as cards by root cause and frequency band. Each card summarizes the root cause, number of radios affected, and the estimated number of impacted endpoints. The names of the top three impacted radios are shown as links for quick access to their details.

![AP Performance Advisories - Menu](images/assurance/img/ap-perf-image005.png)

![Landing Page](images/assurance/img/ap-perf-image007.png)

---

#### Summary Page

Click a card (for example, **High co-channel interference on 2.4 GHz**) to investigate further.

The summary page provides:

- A **Hero Bar** summarizing the root cause, number of radios, impacted buildings, and a quick link to the top impacted radio.

  ![ap-perf-image009](images/assurance/img/ap-perf-image009.png)
- **Analysis Charts** showing the distribution of explanatory KPIs supporting the root cause analysis, compared with reference radios.

  - The x-axis shows KPI value ranges.
  - The y-axis shows frequency of observations.
  - Only KPIs relevant to the root cause are shown.
- **Remediation Guidance:** For example, high co-channel interference can often be mitigated by:

  - Tuning Transmit Power Control (TPC) to lower radio transmission power.
  - Disabling lower datarates to reduce airtime usage.

These suggestions are provided in the UI alongside explanations of each KPI.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ap-perf-image011.png)

- A **Radio Table** listing all radios in the group, ordered by their impact rating (combining the number of impacted clients and magnitude of KPI deviation). The “Insight Details” column links to the details page for each radio.

![Radio section](images/assurance/img/ap-perf-image013.png)

---

#### Details Page

Click on a radio (e.g., **CW9166I-LDN1-05**) to see detailed analytics.

![Radio select](images/assurance/img/ap-perf-image015.png)

- The **Hero Bar** shows AP model, location, AP360 link, and impacted clients.

![Details Hero bar](images/assurance/img/ap-perf-image017.png)

- Below, you’ll find charts of client experience KPIs (e.g., RSSI, SNR, link speed, packet retries, packet failures) that were statistically significant for the selected radio.

![Context bar](images/assurance/img/ap-perf-image019.png)

##### Customizing KPI Views

You can add more KPIs for additional context by clicking the `+` button:

![Add KPI](images/assurance/img/ap-perf-image021.png)

For example, adding the **Speed** KPI can show that lower data rates are more common on the problematic radio, which can directly impact client experience.

![Speed KPI](images/assurance/img/ap-perf-image023.png)

##### Root Cause Analysis (RCA)

Below the KPI charts, root cause analysis charts display all anomalous KPIs for the individual radio. You may add even more KPIs (CPU/memory usage, model, image version, channel changes, etc.) using the `+` button.

![RCA](images/assurance/img/ap-perf-image025.png)

---

### Key Takeaways

- The **AP Performance Advisories** feature automates radio performance analytics and helps identify the most critical radios impacting client experience.
- It provides a streamlined way to target network optimizations, ensuring a consistently high-quality wireless experience.

---

### Additional Use Case: High AP Density at 2.4GHz

The following images illustrate another scenario—high AP density at 2.4GHz:

![A screenshot of a computer  Description automatically generated](images/assurance/img/ap-perf-image027.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/ap-perf-image029.png)

![A screenshot of a graph  Description automatically generated](images/assurance/img/ap-perf-image031.png)

---

**End of Guide**

Continue exploring other use cases as needed. For additional information, refer to the relevant Cisco documentation or follow the provided links.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/wifi6/ -->
## Wi-Fi 6 & Wi-Fi 6E

Welcome to the Wi-Fi 6 and Wi-Fi 6E Demo Guide. This document provides a structured walkthrough of the demo, highlighting key features, metrics, and visual insights into Wi-Fi 6 and Wi-Fi 6E deployments. You will find information on client and AP distributions, network readiness, airtime efficiency, and wireless latency, with clear indications of where to apply filters and interpret data trends. All images and charts are placed as in the original for seamless reference.

---

### Table of Contents

1. [Wi-Fi 6E Data](#wi-fi-6e-data)
2. [Assurance and Insights for Wi-Fi 6](#assurance-and-insights-for-wi-fi-6)
3. [Client Distribution by Capability](#client-distribution-by-capability)
4. [Network Readiness](#network-readiness)
5. [AP Distribution Protocol](#ap-distribution-protocol)
6. [Wireless Airtime Efficiency](#wireless-airtime-efficiency)
7. [Wireless Latency by Client Count](#wireless-latency-by-client-count)

---

### 1. Wi-Fi 6E Data

Explore the latest data and insights pertaining to Wi-Fi 6E deployments.

---

### 2. Assurance and Insights for Wi-Fi 6

Gain valuable assurance and operational insights for your Wi-Fi 6 environments.

![wifi6-image001](images/assurance/img/wifi6-image001.png)

![wifi6-image003](images/assurance/img/wifi6-image003.png)

---

### 3. Client Distribution by Capability

Understand how clients are distributed based on their Wi-Fi capabilities. This section helps to visualize the adoption and support for different Wi-Fi standards among connected devices.

![wifi6-image005](images/assurance/img/wifi6-image005.png)

![wifi6-image007](images/assurance/img/wifi6-image007.png)

---

### 4. Network Readiness

Evaluate your network’s readiness for Wi-Fi 6 and Wi-Fi 6E. You can apply filters to focus specifically on Wi-Fi 6E or Wi-Fi 6 data for deeper analysis.

![A screenshot of a network  Description automatically generated](images/assurance/img/wifi6-image009.png)

![A screenshot of a network  Description automatically generated](images/assurance/img/wifi6-image011.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/wifi6-image013.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/wifi6-image015.png)

---

### 5. AP Distribution Protocol

Analyze the distribution of Access Points (APs) by their protocol capabilities. This section is split into the latest data for both Wi-Fi 6E and Wi-Fi 6.

#### Latest: Wi-Fi 6E

![wifi6-image017](images/assurance/img/wifi6-image017.png)

#### Latest: Wi-Fi 6

![wifi6-image019](images/assurance/img/wifi6-image019.png)

##### Trend Analysis

Examine historical trends in AP protocol distribution.

![wifi6-image021](images/assurance/img/wifi6-image021.png)

---

### 6. Wireless Airtime Efficiency

Monitor how efficiently wireless airtime is being utilized. Filters are available for both the latest snapshot and historical trend views.

#### Latest

![wifi6-image023](images/assurance/img/wifi6-image023.png)

![wifi6-image025](images/assurance/img/wifi6-image025.png)

#### Trend

![wifi6-image027](images/assurance/img/wifi6-image027.png)

![wifi6-image029](images/assurance/img/wifi6-image029.png)

---

### 7. Wireless Latency by Client Count

Assess wireless latency metrics in relation to client count. Filters are available for both current and trend analyses.

#### Latest

![wifi6-image031](images/assurance/img/wifi6-image031.png)

![wifi6-image033](images/assurance/img/wifi6-image033.png)

#### Trend

![wifi6-image035](images/assurance/img/wifi6-image035.png)

![wifi6-image037](images/assurance/img/wifi6-image037.png)

---

### Notes

- All images and their placements are preserved as in the original guide.
- Filters can be applied in relevant sections (as indicated) to narrow down the data for Wi-Fi 6 or Wi-Fi 6E, and to toggle between latest and trend views.
- This guide is intended to support demo users in exploring and explaining Wi-Fi 6/6E features and metrics with clarity and confidence.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/wifi7/ -->
## Wi-Fi 7 Demo Guide: Showcasing Advanced Wireless Capabilities

### Introduction

This comprehensive demo guide provides a step-by-step walkthrough to showcase the key features of Wi-Fi 7 within the Cisco management interface. It focuses on demonstrating enhanced end-user device connectivity, efficient inventory management, and intuitive device topology visualization. Through user-focused scenarios, inventory exploration, and network health assurance tools, you will learn to highlight multi-band support, advanced device relationships, and the robust capabilities of Cisco's Wi-Fi 7 solutions. Screenshots are included throughout the guide to enhance understanding and facilitate your demonstration.

This guide covers three primary use cases:
\* **User 360 View:** Evaluate the connectivity and performance of devices associated with a specific user.
\* **Inventory Management:** Explore and manage Wi-Fi 7-enabled devices within your network.
\* **Device 360 Page & Physical Neighbor Topology:** Visualize device interactions and client distribution within your network.

---

### A) Use Case: Grace Smith (Wireless – User 360)

In this section, you will utilize the **User 360** feature to evaluate the connectivity and performance of devices associated with a sample user, Grace Smith. This provides a holistic view of the user's wireless experience across different devices and protocols, demonstrating Wi-Fi 7's impact on individual user performance.

#### 1. Accessing User 360 for Grace Smith

**Step 1:** Open your Webex environment and navigate to the **Global Search** feature.

![Screenshot](images/assurance/img/wifi7-image001.png)

**Step 2:** Enter "Grace Smith" in the search bar.

**Step 3:** In the search results, locate and select the **User** section for Grace Smith. Click on the **User 360** button to access detailed insights into her device connections.

![Screenshot](images/assurance/img/wifi7-image003.png)

#### 2. Reviewing Device Connectivity for Grace Smith's Devices

For each device owned by Grace Smith, follow the navigation path and review the key connectivity details to observe varying Wi-Fi protocols and frequencies in use.

##### A. Grace Smith – iPad

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-iPad`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 6
\* **Access Point:** CW9178I-LDN1-01
\* **Radio:** 1
\* **Frequency:** 5 GHz

![Screenshot](images/assurance/img/wifi7-image005.png)

![Screenshot](images/assurance/img/wifi7-image007.png)

##### B. Grace Smith – iPhone

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-iPhone`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 7
\* **Access Point:** CW9178I-LDN1-01
\* **Radios:** 0, 1, 3

![Screenshot](images/assurance/img/wifi7-image009.png)

![Screenshot](images/assurance/img/wifi7-image011.png)

##### C. Grace Smith – Galaxy

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-Galaxy`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 7
\* **Access Point:** CW9178I-LDN1-01
\* **Radios:** 0, 1, 3
\* **Frequencies:** 2.4 GHz, 5 GHz, 6 GHz

![Screenshot](images/assurance/img/wifi7-image013.png)

![Screenshot](images/assurance/img/wifi7-image015.png)

##### D. Grace Smith – MacBook Pro

**Navigation:** `Home Page` → `Global Search` → `Grace Smith` → `User 360` → `Grace.Smith-MacBook Pro`

**Connectivity Details:**
\* **Protocol:** Wi-Fi 7
\* **Access Point:** CW9178I-LDN1-01
\* **Radio:** 1
\* **Frequency:** 5 GHz

![Screenshot](images/assurance/img/wifi7-image017.png)

![Screenshot](images/assurance/img/wifi7-image020.png)

---

### B) Use Case: Inventory Management for Wi-Fi 7 Devices

This section demonstrates how to view and manage specific Wi-Fi 7 enabled devices within your network inventory, providing insights into their hardware, connectivity, and configuration settings.

![Screenshot](images/assurance/img/wifi7-image022.png)

#### 1. Navigating to Device Inventory

To access the inventory details for your Wi-Fi 7 devices:

- **Path:** `Provision` → `Inventory` → `[Select Device]`
- From the Inventory dashboard, locate the following devices to view their details:
  - CW9178I-LDN1-01
  - CW9176I-LDN1-02
  - CW9178I-LDN1-03
  - CW9178I-LDN1-04

![Screenshot](images/assurance/img/wifi7-image024.png)

#### 2. Viewing Individual Device Details

For each device listed above, follow these steps to access its specific information:

##### A. CW9178I-LDN1-01 Device Details

Click on the device name `CW9178I-LDN1-01`.

![Screenshot](images/assurance/img/wifi7-image026.png)

Select **View Device Details** to access hardware information, connectivity statistics, and configuration settings for this access point.

![Screenshot](images/assurance/img/wifi7-image028.png)

![Screenshot](images/assurance/img/wifi7-image030.png)

##### B. CW9176I-LDN1-02 Device Details

Click on the device name `CW9176I-LDN1-02` and select **View Device Details** to access its hardware information, connectivity statistics, and configuration settings.

![Screenshot](images/assurance/img/wifi7-image032.png)

![Screenshot](images/assurance/img/wifi7-image034.png)

##### C. CW9178I-LDN1-03 Device Details

Click on the device name `CW9178I-LDN1-03` and select **View Device Details** to access its hardware information, connectivity statistics, and configuration settings.

![Screenshot](images/assurance/img/wifi7-image036.png)

![Screenshot](images/assurance/img/wifi7-image038.png)

##### D. CW9178I-LDN1-04 Device Details

Click on the device name `CW9178I-LDN1-04` and select **View Device Details** to access its hardware information, connectivity statistics, and configuration settings.

![Screenshot](images/assurance/img/wifi7-image040.png)

![Screenshot](images/assurance/img/wifi7-image042.png)

---

### C) Use Case: Device 360 Page – Physical Neighbor Topology

This section guides you through visualizing the physical neighbor topology for a specific device, helping you analyze how devices and clients interact within your network and showcasing Wi-Fi 7's multi-band capabilities.

#### 1. Accessing Device 360 and Physical Neighbor Topology

You have two options to access the Device 360 page for `CW9178I-LDN1-01`:

- **Option 1:** Navigate to `Assurance` → `Health` → `Network` → `Network Device Table`. From the table, select `CW9178I-LDN1-01`.
- **Option 2:** Use the `Global Search` feature to find `CW9178I-LDN1-01`, then open its Device 360 Page directly from the search results.

![Screenshot](images/assurance/img/wifi7-image044.png)

![Screenshot](images/assurance/img/wifi7-image046.png)

#### 2. Analyzing Physical Neighbor Topology

Once on the Device 360 page, navigate to the **Physical Neighbor Topology** tab.

![Screenshot](images/assurance/img/wifi7-image048.png)

Observe the network map, which displays the `CW9178I-LDN1-01` device and its connected clients. This visualization helps you assess how Wi-Fi 7's multi-band capabilities and advanced client support impact network performance and client distribution across different frequency bands.

![Screenshot](images/assurance/img/wifi7-image050.png)

#### 3. Client Distribution by Frequency

Within the Physical Neighbor Topology, examine the client distribution across different frequency bands:

##### A. 6 GHz Clients

This view includes 1 non-MLO (Multi-Link Operation) client and 2 clients utilizing MLO links on the 6 GHz band, highlighting Wi-Fi 7's advanced capabilities.

![Screenshot](images/assurance/img/wifi7-image053.png)

##### B. 5 GHz Clients

This view includes 1 non-MLO client and 2 clients utilizing MLO links on the 5 GHz band, demonstrating efficient client management across frequencies.

![Screenshot](images/assurance/img/wifi7-image055.png)

![Screenshot](images/assurance/img/wifi7-image057.png)

![Screenshot](images/assurance/img/wifi7-image059.png)


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/ai-epa/ -->
## AI Endpoint Analytics Spoofing Detection

### Introduction

This guide provides detailed, step-by-step instructions for using AI Endpoint Analytics to detect spoofing, manage trust scores, apply Adaptive Network Control (ANC) policies, and organize endpoint hierarchies. The instructions below are designed to help users navigate the interface efficiently, understand core features, and demonstrate each capability with ease. All screenshots referenced are included in their respective steps for visual guidance.

---

### Table of Contents

1. [Reset Trust Score](#reset-trust-score)
2. [Apply ANC Policy](#apply-anc-policy)
3. [Manage Endpoint Hierarchy](#manage-endpoint-hierarchy)
4. [Other Supported Pages](#other-supported-pages)

---

### 1. Reset Trust Score

The Reset Trust Score feature allows you to update the trust score for endpoints identified as potentially spoofed.

Navigate to **Policy** 🡪 **AI Endpoint Analytics** in your dashboard.

![ai-epa-image001](images/policy/img/ai-epa-image001.png)

1. Ensure that all dashlets (dashboard widgets) are displaying data as expected.

   ![ai-epa-image003](images/policy/img/ai-epa-image003.png)
2. Go to the **Trust Score** tab by selecting "Low" from the Trust Score filter. This will automatically show endpoints with low trust scores.

   ![ai-epa-image005](images/policy/img/ai-epa-image005.png)
3. Locate an endpoint with a low trust score (for example, Trust Score = 1),then select **Reset Trust Score**

   ![ai-epa-image007](images/policy/img/ai-epa-image007.png)
4. In the confirmation popup, click **Reset** to confirm your action.

   ![ai-epa-image009](images/policy/img/ai-epa-image009.png)
5. Once reset, the endpoint’s Trust Score will automatically update to a value above 4

   ![ai-epa-image011](images/policy/img/ai-epa-image011.png)

---

### 2. Apply ANC Policy

Go to **Policy 🡪 AI Endpoint Analytics**

1. Select the desired endpoint and click **Apply ANC Policy**.

   ![ai-epa-image013](images/policy/img/ai-epa-image013.png)
2. In the popup, choose the appropriate policy from the dropdown menu and click **Apply**.

   ![ai-epa-image015](images/policy/img/ai-epa-image015.png)
3. The selected ANC (Adaptive Network Control) Policy will now be enforced on the chosen network endpoint.

   ![ai-epa-image017](images/policy/img/ai-epa-image017.png)

---

### 3. Manage Endpoint Hierarchy

1. Navigate to **Policy 🡪 AI Endpoint Analytics 🡪 Hierarchy**.

   ![ai-epa-image019](images/policy/img/ai-epa-image019.png)
2. In this section, you can create new endpoint types.

   Endpoints can be easily organized by dragging and dropping them into the desired endpoint types or hierarchy levels.

   ![ai-epa-image021](images/policy/img/ai-epa-image021.png)

---

### 4. Other Supported Pages

All other pages within the AI Endpoint Analytics interface are also supported with relevant data and functionality. Refer to the navigation menu for access to additional features.

---

### Notes

- Ensure you have the necessary permissions to reset trust scores and apply policies.
- All screenshots reflect the actual user interface at the time of writing.
- Follow your organization’s standard practices for policy application and endpoint management.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/anc/ -->
## Policy Endpoint Overview

This demo guide provides a step-by-step overview of using Adaptive Network Control (ANC) Policy with endpoints based on Trust Score in Cisco systems. You will learn how to identify endpoints with a low Trust Score, apply ANC policies, and reset Trust Scores as needed. Each stage is illustrated with screenshots for clarity.

---

### 1. AI Policy Endpoint Overview

Go to **Policy 🡪 AI Endpoint Analytics**

![anc-image001](images/policy/img/anc-image001.png)

This section presents a high-level view of policy endpoints. Here, you can monitor and manage endpoints within your network.

---

### 2. Selecting Endpoints with Low Trust Score

Click on the **Endpoint Inventory** tab.

After filtering or selecting endpoints with a Trust Score in the "Low (1-3)" range, you will see relevant endpoint details:

![Graphical user interface, application  Description automatically generated](images/policy/img/anc-image003.png)

Endpoints with a low Trust Score may require further investigation or remediation.

---

### 3. Applying the ANC Policy

Once the relevant endpoints are identified, you can apply an ANC Policy directly from the interface:

![Graphical user interface, application  Description automatically generated](images/policy/img/anc-image005.png)

Follow the prompts to select and enforce the desired policy on the selected endpoints.

![Graphical user interface, text, application  Description automatically generated](images/policy/img/anc-image007.png)

You will receive visual confirmation that the ANC Policy has been successfully applied.

![Graphical user interface, text, application  Description automatically generated](images/policy/img/anc-image009.png)

Detailed policy actions and their outcomes are displayed for each affected endpoint.

![Graphical user interface, text, application  Description automatically generated](images/policy/img/anc-image011.png)

---

### 4. Resetting the Trust Score

If necessary, you can reset the Trust Score for an endpoint after applying and verifying the ANC Policy:

![Graphical user interface, application  Description automatically generated](images/policy/img/anc-image013.png)

This action restores the Trust Score and allows normal network access, assuming the endpoint is deemed secure.

---

### Summary

- Begin with a Policy Endpoint overview to understand the current state.
- Filter and identify endpoints with a low Trust Score (1-3).
- Apply appropriate ANC Policies to mitigate risk.
- Reset Trust Scores as needed to restore endpoint status.

Use this guide as a reference to efficiently demonstrate the process of managing endpoint security using Cisco's ANC Policy features.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/epa-grouping/ -->
## AI Endpoint Analytics Smart Grouping

### Introduction

This demo guide provides a step-by-step walkthrough of the AI Endpoint Analytics Smart Grouping feature in Kronos. The process covers how to review, accept, modify, or reject AI-proposed endpoint grouping rules, and how these actions impact your group's configuration within the Endpoint Analytics dashboard. The guide is split into two main parts: accepting and reviewing Smart Grouping proposals, and rejecting groupings.

---

### Understanding Smart Grouping & AI Proposals

**Smart Grouping** uses AI to analyze endpoint data and propose new grouping rules. Within the **AI Proposals** section, you will find:
- **New rules/groups** discovered by Smart Grouping
- **Suggested modifications** for previously accepted rules
- **Suggestions to delete** previously accepted rules

Navigate to:  
`Policy > AI Endpoint Analytics`
![epa-grouping-image000](images/policy/img/epa-grouping-image000.png)

---

### Part 1: Accepting and Reviewing AI-Proposed Endpoint Groups

#### Step 1: Initial Endpoint Group Review

There will be two endpoint groups proposed by Smart Grouping.

![epa-grouping-image001](images/policy/img/epa-grouping-image001.png)

---

#### Step 2: Exploring Endpoint Group Details

You can review the details of each endpoint group by navigating through the available tabs: **Summary**, **Profile Rule**, and **Endpoints**.

![epa-grouping-image003](images/policy/img/epa-grouping-image003.png)

After reviewing, select **Next** to proceed.

---

#### Step 3: Filling Endpoint Group Details

Fill in all required fields for the endpoint group. Dropdown menus will appear as you type; it is acceptable to leave fields as null if necessary.

![epa-grouping-image005](images/policy/img/epa-grouping-image005.png)

---

#### Step 4: Reviewing or Saving Grouping Rules

At this stage, you have two options:
- **Review More Rules(s) for Profiling**: This will redirect you back to **Step 1** to review additional proposals.
- **Review Endpoint Inventory**: This will take you to the Profiling Rules Policy page, where your newly added group will appear.

![epa-grouping-image007](images/policy/img/epa-grouping-image007.png)
![epa-grouping-image009](images/policy/img/epa-grouping-image009.png)

Upon completing the addition, the new group will be listed on the Profiling Rules Policy page.

![epa-grouping-image011](images/policy/img/epa-grouping-image011.png)
![epa-grouping-image013](images/policy/img/epa-grouping-image013.png)

---

### Part 2: Rejecting AI-Proposed Endpoint Groups

#### Step 1: Reviewing the AI Proposal Count

On the **Overview** page, the AI Proposals dashlet will display the current count of pending proposals (e.g., reducing from 2 to 1 after an action).

![epa-grouping-image015](images/policy/img/epa-grouping-image015.png)

Select **Review** to proceed.

![epa-grouping-image017](images/policy/img/epa-grouping-image017.png)

There will now be one remaining endpoint group, and you can review its **Summary**, **Profile Rule**, and **Endpoints** tabs.

---

#### Step 2: Rejecting an Endpoint Group

To reject a proposed grouping:
- Select **Reject Grouping** at the bottom of the group details page.
- Choose the appropriate reason and submit.

![epa-grouping-image019](images/policy/img/epa-grouping-image019.png)

After submission, the endpoint group profile will be deleted from the list.

![epa-grouping-image021](images/policy/img/epa-grouping-image021.png)

Returning to the home page, the AI Proposal count should now be 0, indicating no pending proposals.

![epa-grouping-image023](images/policy/img/epa-grouping-image023.png)

---

### Conclusion

This guide has outlined the full lifecycle for reviewing, accepting, and rejecting AI-proposed endpoint groupings within the Kronos AI Endpoint Analytics platform. By following these steps, you can efficiently manage and refine your organization's endpoint groups using intelligent AI recommendations.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/feedback/ -->
![cisco-logo](images/feedback/img/cisco-logo.png)

Demo Guide Feedback

Your feedback helps us improve our demo guides. This survey focuses on the guide’s content and process to help us enhance the material.
Please do not include personal or support-related information. This survey will take approximately 2–3 minutes to complete.

**Introduction:** We’re looking for your impressions and insights to help us enhance the material.
Please don’t include personal or support-related information.

1) On a scale of 1 to 5, how clear and easy to understand was the demo guide? 1
 2
 3
 4
 5(1 = Not at all clear, 5 = Extremely clear)

2) To what extent did this guide help you achieve your intended task/objective? 1
 2
 3
 4
 5(1 = Not at all, 5 = Completely)

3) Would you recommend this guide to a colleague or peer? Yes
 NoBecause you selected **“No”**:Please tell us why:

4) Did you encounter any specific issues with the text, instructions, or steps? Yes
 NoBecause you selected **“Yes”**:Please describe the specific issues (include section/step numbers or unclear wording):

5) Any other comments, suggestions, or general feedback? (Optional)

6)
If you'd like us to follow up on your feedback or reported issues, please provide your email.
(Optional)

Submit feedback

Anonymous & aggregated — no personal data collected.

Note: This form is specifically for feedback on this demo guide. It is not intended for dCloud issues,
environment problems, or immediate demo support requests.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/awips/ -->
## Using Rogue & AWIPS for Threat Containment

### Introduction

This demo guide provides step-by-step instructions for utilizing the Rogue & AWIPS (Advanced Wireless Intrusion Prevention System) interface to identify, contain, and manage network threats—specifically focusing on handling Honeypot threats. You will learn how to initiate containment, review threat statuses, and manage allowed devices. All screenshots and UI steps are included for a seamless demo experience.

---

### 1. Supported Pages & Initial Steps

- **All pages are supported with data.**
- Begin the process by initiating containment.

---

### 2. Assurance – Rogue & AWIPS Overview

**Overview Screenshots**

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image001.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image003.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image005.png)

---

### 3. Identifying Threats

Navigate to the **Threats** section.

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image007.png)

#### Selecting a Threat

- Select a threat from the list where the threat type is **Honeypot**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image009.png)

---

### 4. Starting Containment

- Go to **Actions** and select **Start Containment**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image011.png)

- Click on **Configuration Preview** to review containment settings.

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image013.png)

- After starting containment, the threat status changes to **Informational**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image015.png)

---

### 5. Managing Allowed List

You can add a device to the allowed list to modify its threat status:

1. In the **Assurance → Rogues & AWIPS → Threats** section, select the **MAC Address** of the device.

   ![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image017.png)
2. Under **Actions**, choose **Add to Allowed List**.

   ![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image019.png)

   ![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image021.png)
3. After adding to the allowed list, the **Threat Level** changes to **Potential** and the **Containment Status** updates to **Contained**.

   ![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image023.png)

   ![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image025.png)
4. The MAC address added will now be visible in the **Allowed List** section.

   ![A screenshot of a computer  Description automatically generated](images/assurance/img/awips-image027.png)

---

### Conclusion

By following the steps in this guide, you can efficiently identify, contain, and manage rogue threats using the Rogue & AWIPS system. This ensures improved network security and streamlined incident management.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/enable-apps/ -->
## Enabling ThousandEyes Enterprise Agent App on Switches

### Introduction

This guide provides a step-by-step walkthrough for enabling the ThousandEyes Enterprise Agent App on Cisco switches. By following these instructions, you will learn how to initiate the workflow, configure settings, select sites and switches, provision the app, and manage IoT applications through the user interface. The guide includes screenshots to help illustrate each step for greater clarity.

---

### Steps to Enable ThousandEyes Enterprise Agent App

#### Step 1: Navigate to Enable Apps on Switches

From the main menu, go to **Workflows** and click on **Enable Apps on Switches**.

![Enable Apps on Switches Menu](images/assurance/img/enable-apps-image001.png)

---

#### Step 2: Start the Workflow

Click the **Let's do it** button to begin.

![Let's do it Button](images/assurance/img/enable-apps-image002.png)

---

#### Step 3: Enter Task Name

Enter a valid **Task name** and click the **Next** button to proceed.

![Enter Task Name](images/assurance/img/enable-apps-image003.png)

---

#### Step 4: Select App

Select **ThousandEyes Enterprise Agent App** and click **Next**.

![Select App](images/assurance/img/enable-apps-image004.png)

---

#### Step 5: Select Site

Choose the **site** where you want to enable the app.

![Select Site](images/assurance/img/enable-apps-image005.png)

- Click **Exit** to leave the task.
- Click **Back** to return to the previous step.
- Click **Next** to continue.

---

#### Step 6: Review Site Selection

![Review Site Selection](images/assurance/img/enable-apps-image006.png)

---

#### Step 7: Select Switch(es)

Select one or more **Switches** and click **Next**.

![Select Switch](images/assurance/img/enable-apps-image007.png)

---

#### Step 8: Confirm Switch Selection

![Confirm Switch Selection](images/assurance/img/enable-apps-image008.png)

---

#### Step 9: Configure App

In the **Configure App** window:

- Set the **VLAN** to `144`.
- Set the **Address Type** to `Dynamic`.
- Click **Next** to proceed.

![Configure App Settings 1](images/assurance/img/enable-apps-image009.png)
![Configure App Settings 2](images/assurance/img/enable-apps-image010.png)

---

#### Step 10: Download Summary and Provision

- Click **Download Summary** to download the summary CSV file.
- Click **Provision** to enable the app on the selected switch.

![Download Summary and Provision](images/assurance/img/enable-apps-image011.png)

---

#### Step 11: Provisioning Complete

The agent is now provisioned.

![Provisioning Complete](images/assurance/img/enable-apps-image012.png)

---

#### Step 12: View Details

Click the **View Details** link to open the details popup.

![View Details](images/assurance/img/enable-apps-image013.png)

---

#### Step 13: Manage IoT App

Click the **Manage IoT App** button to continue.

![Manage IoT App](images/assurance/img/enable-apps-image014.png)

---

#### Step 14: Select Hostname

Click on the **Hostname** to proceed further.

![Select Hostname](images/assurance/img/enable-apps-image015.png)

---

#### Step 15: Review Final Step

![Final Step](images/assurance/img/enable-apps-image016.png)

---

### Notes

- Ensure you have the appropriate permissions to perform these actions.
- If you encounter any issues, refer to your administrator or consult the Cisco support documentation.
- The images in this guide match the original locations for clarity and ease of reference.

---

**End of Guide**


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/enhanced-rrm/ -->
## AI Enhanced RRM

### Introduction

This guide provides step-by-step instructions for demonstrating the AI Enhanced Radio Resource Management (RRM) feature within Cisco Assurance α. You will learn how to launch the AI-Enhanced RRM deployment workflow, configure RF profiles, and verify that the enhanced RRM features and Dashlets are functioning as expected across all supported frequency bands (6GHz, 5GHz, 2.4GHz).

---

### Key Features

- Support for all Dashlets with data
- Operation across all three frequencies: 6GHz, 5GHz, and 2.4GHz
- Fully functional filters within Dashlets
- Both LATEST and TREND data available for all Dashlets

---

### Step-by-Step Instructions

#### 1. Accessing AI Enhanced RRM

Navigate to the Assurance α AI Enhanced RRM section.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image001.png)

---

#### 2. Launch Deployment Workflow

Click **Launch AI-Enhanced RRM Deployment Workflow**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image003.png)

---

#### 3. Task Configuration

- The **Task Name** will populate automatically.
- Click **Next**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image005.png)

---

#### 4. Device Provisioning

- Select **Enable Without Device Provisioning**.
- Click **Next**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image007.png)

---

#### 5. Site Selection

- Use the search bar to find and select **London1**.

![A screenshot of a chat  Description automatically generated](images/assurance/img/enhanced-rrm-image009.png)

![enhanced-rrm-image011](images/assurance/img/enhanced-rrm-image011.png)
![enhanced-rrm-image013](images/assurance/img/enhanced-rrm-image013.png)
![enhanced-rrm-image015](images/assurance/img/enhanced-rrm-image015.png)

---

#### 6. Continue to Profile Selection

Click **Next**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image017.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image019.png)

---

#### 7. RF Profile Selection

- Select an **AI RF Profile** from the dropdown menu.
- Optionally, click the add button (Ã ) to create a new RF Profile.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image021.png)

---

#### 8. Add or Edit RF Profile

- Enter the **Profile Name**.
- Adjust profile settings if needed.
- Click **Save**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image023.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image025.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image027.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image029.png)

---

#### 9. Review and Proceed

- Verify all details.
- Click **Next**.
- **Note:** The summary caption may not be displayed (# Issue).

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image031.png)

- **Issue:** "Preview and Deploy" is displayed instead of "Preview".

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image033.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image035.png)

---

#### 10. Export RF Profile Details

- Download the CSV file containing RF Profile details.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image037.png)

---

#### 11. Deploy Configuration

- Click **Deploy** to apply your configuration.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image039.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image041.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image043.png)

---

#### 12. View RF Profile List

- Click **See all RF Profile List** to navigate to the RF Profile tab in **Design α Network Settings**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image045.png)
![enhanced-rrm-image047](images/assurance/img/enhanced-rrm-image047.png)

---

### 13. Verify AI Enhanced RRM Dashlets

- Ensure all Dashlets load correctly and display the appropriate data for all frequencies.

![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image049.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image051.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image053.png)
![A graph of different colored bars  Description automatically generated with medium confidence](images/assurance/img/enhanced-rrm-image055.png)
![A screenshot of a graph  Description automatically generated](images/assurance/img/enhanced-rrm-image057.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/enhanced-rrm-image059.png)
![A screenshot of a graph  Description automatically generated](images/assurance/img/enhanced-rrm-image061.png)

---

### Notes and Known Issues

- The "Summary" caption may not display during the review step.
- The label "Preview and Deploy" may appear instead of just "Preview."
- All images are referenced as in the original documentation for clarity and context.

---

### Conclusion

This guide enables you to successfully demonstrate the AI Enhanced RRM feature, from workflow initiation through deployment and verification. For any issues not covered in this guide, please refer to the official documentation or support channels.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/event-analytics-use/ -->
## Cisco Catalyst Center: Event Analytics

### Introduction

This demo guide provides a step-by-step walkthrough of the **Event Analytics** feature in Cisco Catalyst Center (available since version 2.3.7). Event Analytics enables network administrators to effectively monitor their networks by detecting behavioral changes and correlating various event types across both wired and wireless devices. The guide covers:

- Navigating the Event Analytics dashboard
- Understanding the benefits and supported event types
- Using analytics to isolate and investigate relevant events
- Leveraging heatmaps and visualizations for rapid anomaly detection

By following this guide, you will gain hands-on experience in using Event Analytics for enhanced network visibility and management efficiency.

---

### 1. Overview of Event Analytics

#### What is Event Analytics?

Event Analytics is a feature designed to give network administrators unparalleled insights into all types of network events, regardless of whether a specific issue signature is defined. Unlike traditional network management systems, which depend on predefined signatures, Event Analytics leverages machine learning, artificial intelligence, and data visualization techniques to process event data continuously and highlight anomalies or potential issues in real time.

#### Key Benefits

- **Comprehensive Visibility:** Monitor both wired and wireless domains from a single dashboard.
- **Signature-Free Detection:** Detect issues without requiring pre-configured issue signatures.
- **Advanced Analytics:** Use AI/ML algorithms for deeper insights and faster anomaly detection.
- **Rich Visualizations:** Quickly move from a global view to detailed event analysis with just a few clicks.

---

### 2. Supported Event Types

Event Analytics supports a variety of network event types:

| Event Type | Wired | Wireless |
| --- | --- | --- |
| **Syslog** | X | X |
| **Reachability** | X | X |
| **Radio Events** |  | X |
| **Client Events** | \* | X |

> **Note:** Wired client events will be added in a future release.

#### Event Type Descriptions

- **Syslog:** Messages collected from switches, routers, and Wireless LAN Controllers (WLCs). By default, only metadata is exported to the Cisco AI Cloud to comply with [Cisco AI Analytics Privacy Policy](http://labguides-wil.s3-website.eu-central-1.amazonaws.com/labops-1399/lab8_service_ops/#data-privacy-and-security-considerations). Full text export requires explicit user consent.
- **Reachability:** Indicates changes in device reachability as monitored by Catalyst Center. Wireless AP reachability is reported by WLCs and triggered by JOIN/DISJOIN events. Statuses include:
- REACHABLE: Fully manageable
- PING\_REACHABLE: Pingable but not manageable
- UNREACHABLE: Offline
- **Radio Events:** Includes channel changes, transmission power changes (RRM), coverage hole detections, and radio resets.
- **Client Events:** Onboarding and roaming events for wireless clients (wired support coming soon).

---

### 3. Accessing the Event Analytics Dashboard

To access the Event Analytics dashboard, navigate to:

**Menu > Assurance > Issues and Events > Event Analytics - Preview**

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image001.png)

---

### 4. Using Event Analytics

#### 4.1 Heatmap Overview

The **Heatmap** provides a visual overview of the volume of network events, categorized by type and severity.

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image003.png)

- The default view shows the last 24 hours for syslog and reachability events on all wired devices.
- You can adjust the view by:
- Filtering by location
- Extending the time range (up to 60 days)
- Switching between wired and wireless domains

##### Interpreting the Heatmap

- Darker colors indicate higher event volumes.
- Each event type/category has its own color scale to make rare events (like high-severity syslog messages) more visible.
- Syslog events are grouped by severity: **High** (Sev. 1 & 2), **Medium** (3 & 4), **Low** (5 & 6).

---

### 5. Detailed Event Exploration

#### 5.1 Wired Events

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image005.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image007.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image009.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image011.png)

##### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image013.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image015.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image017.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image019.png)

##### Sub Graph: 2

![A screenshot of a computer screen  Description automatically generated](images/assurance/img/event-analytics-use-image021.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image023.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image025.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image027.png)

##### Sub Graph: 3

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image029.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image031.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image033.png)

> **Note:** If you see "unknown" displayed in a graph, it may indicate incomplete data or unsupported event types.

![event-analytics-use-image035](images/assurance/img/event-analytics-use-image035.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image037.png)

##### Sub Graph: 4

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image039.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image041.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image043.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image045.png)

##### Sub Graph: 5

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image047.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image049.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image051.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image053.png)

##### Sub Graph: 6

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image055.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image057.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image059.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image061.png)

##### Sub Graph: 7

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image063.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image065.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image067.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image069.png)

---

#### 5.2 Reachability Transitions

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image071.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image073.png)

##### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image075.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image077.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image079.png)

##### Sub Graph: 2

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image081.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image083.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image085.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image087.png)

---

#### 5.3 Client Onboardings

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image089.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image091.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image093.png)

##### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image095.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image097.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image099.png)

---

### 6. Wireless Event Analytics

[**Event Analytics**](https://localhost:7000/dna/assurance/dashboards/issues-events/events-analytics)

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image101.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image103.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image105.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image107.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image109.png)

##### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image111.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image113.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image115.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image117.png)

##### Sub Graph: 2

![A screenshot of a white paper with blue and red text  Description automatically generated](images/assurance/img/event-analytics-use-image119.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image121.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image123.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image125.png)

##### Sub Graph: 3

![A screenshot of a report  Description automatically generated](images/assurance/img/event-analytics-use-image127.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image129.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image131.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image133.png)

##### Sub Graph: 4

![A screen shot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image135.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image137.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image139.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image141.png)

##### Sub Graph: 5

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image143.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image145.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image147.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image149.png)

##### Sub Graph: 6

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image151.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image153.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image155.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image157.png)

##### Sub Graph: 7

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image159.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image161.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image163.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image165.png)

---

#### 6.1 Wireless Reachability Transitions

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image167.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image169.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image171.png)

##### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image173.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image175.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image177.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image179.png)

##### Sub Graph: 2

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image181.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image183.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image185.png)

---

#### 6.2 Radio Events

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image187.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image189.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image191.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image193.png)

##### Sub Graph: 1

![A screenshot of a data report  Description automatically generated](images/assurance/img/event-analytics-use-image195.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image197.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image199.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image201.png)

##### Sub Graph: 2

**Top APs by failure radio resets**

##### Sub Graph: 3

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image203.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image205.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image207.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image209.png)

##### Sub Graph: 4

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image211.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image213.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image215.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image217.png)

##### Sub Graph: 5

**Top APs by coverage hole detection events**

---

#### 6.3 Client Onboardings

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image219.png)
![A screen shot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image221.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image223.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image225.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image227.png)

##### Sub Graph: 1

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image229.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image231.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image233.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image235.png)

##### Sub Graph: 2

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image237.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image239.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image241.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image243.png)

##### Sub Graph: 3

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image245.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image247.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image249.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image251.png)

##### Sub Graph: 4

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image253.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image255.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image257.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image259.png)

##### Sub Graph: 5

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image261.png)
![A barcode on a computer screen  Description automatically generated](images/assurance/img/event-analytics-use-image263.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image265.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image267.png)

##### Sub Graph: 6

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image269.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image271.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image273.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image275.png)

##### Sub Graph: 7

![A screenshot of a computer  Description automatically generated](images/assurance/img/event-analytics-use-image277.png)

---

### Conclusion

This guide has walked you through the Event Analytics feature of Cisco Catalyst Center, highlighting how you can monitor your network efficiently, detect anomalies in real time, and drill down from a global to a granular event view. Event Analytics leverages advanced analytics and visualization to provide actionable insights, making network management more proactive and effective.

For additional details or questions, consult the Cisco Catalyst Center documentation or your network administrator.

---

*All image references and links remain as in the original document for continuity and accuracy.*


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/intelligent-capture-360/ -->
## Intelligent Capture Device360

### Introduction

This guide provides a step-by-step walkthrough for using the **Intelligent Capture Device360** feature. It covers two main areas: analyzing RF statistics and performing spectrum analysis for Cisco access points. The instructions and corresponding screenshots will help you efficiently monitor, troubleshoot, and optimize network performance using Device360.

---

### Part 1: RF Statistics

#### Step 1

On the homepage, click the **Menu**. Navigate to **Assurance > Health**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image001.png)

---

#### Step 2

Open the **Network** tab and filter the network device table to show only access points. Click on any access point to proceed.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image003.png)

---

#### Step 3

On the Access Point Device360 page, select **Intelligent Capture**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image005.png)

---

#### Step 4

Click the **RF Statistics** tab as shown below. Review the data displayed for the dashboards in the 1, 3, and 5 hour time ranges. Check the available radio types in the radio drop-down menu.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image007.png)

---

#### Step 5

Examine the data and graphs loaded in all the dashboards. Hover over the graphs to see individual values for each time range.

For the **Top Clients with Tx Failed Packets by SSID** dashboard, some access points may have data available. Also, check the SSID drop-down values in this dashboard.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image009.png)

---

### Part 2: Spectrum Analysis

#### Step 1

Select the **Spectrum Analysis** tab, then click **Start Spectrum Analysis**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image011.png)

---

#### Step 2

A pop-up window will appear. Click **Next** to continue.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image013.png)

---

#### Step 3

In Step 1, the system will perform initial checks. Once complete, click **Next**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image015.png)

---

#### Step 4

The wizard will advance to steps 2 and 3. Review the configurations to be deployed as shown in the screenshot. Ensure the status in the top-right corner is **Ready**. Click **Deploy**.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image017.png)

---

#### Step 5

A new pop-up will appear. Click **Submit** to continue.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image019.png)

---

#### Step 6

After a short wait, the spectrum analysis will begin and the graphs will load.

- Review the **Spectrum Analysis** and **Interference and Duty Cycle** graphs for the 2.4 GHz band.
- Check the data for time ranges of 1, 3, and 5 hours.
- Also review the graphs in the **Realtime FFT** range, as shown in the second image.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image021.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image023.png)

---

#### Step 7

Switch to the 5 GHz band.

- Review the **Spectrum Analysis** and **Interference and Duty Cycle** graphs.
- Check the graphs for the 1, 3, and 5 hour time ranges.
- Also review the **Realtime FFT** graphs as shown below.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image025.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image027.png)

---

#### Step 8

To end the spectrum analysis, click **Stop Spectrum Analysis** in the top-right corner of the dashboard.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image029.png)

---

#### Step 9

A pop-up window will appear. Click **Accept** to confirm and stop the spectrum analysis.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-360-image031.png)

---

### Notes

- Ensure you have the appropriate permissions to use these features.
- If data does not appear in some dashboards, verify the selected access point and time range.
- Hovering over graphs provides more detailed insights for each data point.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/intelligent-capture/ -->
## Intelligent Capture

### Overview

This guide provides a step-by-step walkthrough for demonstrating the **Intelligent Capture** feature within the Assurance > Health > Client 360 workflow. The guide covers two primary navigation scenarios for accessing Client 360, showcases how to use Intelligent Capture, and highlights the live floor-level heat map tracking functionality. Screenshots are included throughout to support each step and provide clear visual references.

---

### Table of Contents

1. [Accessing Client 360 via Assurance Dashboard](#accessing-client-360-via-assurance-dashboard)
2. [Accessing Client 360 via Global Search](#accessing-client-360-via-global-search)
3. [Floor-Level Heat Map & Live Tracking](#floor-level-heat-map--live-tracking)

---

### 1. Accessing Client 360 via Assurance Dashboard

**Navigation Path:**

`Assurance` → `Health` → `Dashboard` → `Client Tab` → `Client Table` → *Select Client* → **Client 360 Page** → **Intelligent Capture**

Follow these steps:

1. From the main menu, navigate to `Assurance`.
2. Select `Health` and then open the `Dashboard`.
3. Click on the `Client Tab` to view the client table.
4. In the client table, select the desired client.
5. You will be redirected to the Client 360 page, where the **Intelligent Capture** section is available.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image001.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image003.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image005.png)

---

### 2. Accessing Client 360 via Global Search

**Navigation Path:**

`Global Search` → *Search Client Name* → *Select Client (Client 360)* → **Client 360 Page** → **Intelligent Capture**

Follow these steps:

1. Use the `Global Search` function at the top of the interface.
2. Enter the client's name in the search bar.
3. Select the appropriate client entry labeled with `Client 360`.
4. You will be redirected to the Client 360 page, where the **Intelligent Capture** section is available.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image007.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image009.png)

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image011.png)

---

### 3. Floor-Level Heat Map & Live Tracking

**Feature Highlight:**

Within the Client 360 page, the **Floor-Level Heat Map** provides a live tracking use case. If the user or client moves to another floor, the heat map will reflect this in real time, visually tracking their current location.

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image013.png)

---

### Additional Visual Reference

![A screenshot of a computer  Description automatically generated](images/assurance/img/intelligent-capture-image015.png)

---

### Notes

- All screenshots are provided for step-by-step reference and should match the described actions.
- Ensure you have appropriate access permissions to navigate through the described dashboards and features.
- For any issues accessing features, contact your system administrator.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/iot-services-app/ -->
## IoT Services – App Hosting on Cisco Catalyst 9100 Series Access Points

### Introduction

This demo guide provides a step-by-step walkthrough for hosting applications on Cisco Catalyst 9100 Series Access Points using the Cisco DNA Center (DNAC) IoT Services. The process leverages the modular IOx framework, enabling developers to deploy Docker-style container applications directly onto access points. This allows seamless integration of third-party software and hardware, enhancing flexibility for various IoT use cases.

Follow the steps below to provision and manage an IoT application on your Cisco Catalyst 9100 series APs.

---

### Step-by-Step Instructions

#### Step 1: Navigate to IoT Services

From the main menu, go to **Provision > Services > IoT Services**.

---

#### Step 2: Access MeshConnect

Click the **MeshConnect** icon from the DNAC IoT Services page.

![iot-services-app-image001](images/assurance/img/iot-services-app-image001.png)

---

#### Step 3: Install the Application

On the application metadata page, click **Install**.

![iot-services-app-image002](images/assurance/img/iot-services-app-image002.png)
![iot-services-app-image003](images/assurance/img/iot-services-app-image003.png)

---

#### Step 4: Enter Task Name

Enter a valid task name and click the **Next** button to proceed.

---

#### Step 5: Navigation Options

![iot-services-app-image004](images/assurance/img/iot-services-app-image004.png)

- **Exit**: Cancel and exit the current task.
- **Back**: Return to the previous step.
- **Next**: Proceed to the next step.

---

#### Step 6: Continue Setup

![iot-services-app-image005](images/assurance/img/iot-services-app-image005.png)

---

#### Step 7: Select Access Point

![iot-services-app-image006](images/assurance/img/iot-services-app-image006.png)

Select one access point and click the **Next** button.

---

#### Step 8: Review Selection

![A white background with black text Description automatically generated](![iot-services-app-image007](images/assurance/img/iot-services-app-image007.png)

---

#### Step 9: Download Summary and Provision

![iot-services-app-image008](images/assurance/img/iot-services-app-image008.png)

- Click on the **Download Summary** link to download the summary CSV file.
- Click the **Provision** button to start provisioning.

---

#### Step 10: Monitor Provisioning Status

![A white background with blue and white text Description automatically generated](![iot-services-app-image009](images/assurance/img/iot-services-app-image009.png)

- The provisioning state will change from "In-Progress" to "Provisioned" after approximately 60 seconds.
- Click the **View Details** link to see the details popup.

![iot-services-app-image010](images/assurance/img/iot-services-app-image010.png)

![iot-services-app-image011](images/assurance/img/iot-services-app-image011.png)

---

#### Step 11: Manage the IoT App

![iot-services-app-image012](images/assurance/img/iot-services-app-image012.png)

Click the **Manage IoT App** button to proceed.

---

#### Step 12: Select Hostname

![iot-services-app-image013](images/assurance/img/iot-services-app-image013.png)

Click on the hostname to continue.

---

#### Step 13: Download App Logs

![iot-services-app-image014](images/assurance/img/iot-services-app-image014.png)
![iot-services-app-image015](images/assurance/img/iot-services-app-image015.png)

- To download the log file, select the access point and click the **App Logs** link.
- Select the desired log file from the dropdown menu and click **Download**.

---

#### Step 14: View Sample Log File

**Sample logs file:**

![iot-services-app-image016](images/assurance/img/iot-services-app-image016.png)

---

#### Step 15: View Details

![iot-services-app-image017](images/assurance/img/iot-services-app-image017.png)

Click the **View** icon in the Details section.

---

#### Step 16: Check Health Status

Click on **See Details** under the "Healthy" status. You can view both Error and Output information in the popup window.

![iot-services-app-image018](images/assurance/img/iot-services-app-image018.png)

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/network-health-use/ -->
## Cisco Assurance Dashboard

**Section: Network Health (Network Tab)**

---

### Introduction

This demo guide walks you through the **Network Health (Network Tab)** within the Cisco Assurance Dashboard. You will learn how to navigate and utilize key features for monitoring network device health, access point status, client counts, interference metrics, device reachability, and WAN link performance. Screenshots are provided for visual reference at every step to facilitate a seamless demo experience.

---

### Step-by-Step Guide

#### Step 1: Navigate to Network Health Dashboard

From the homepage, open the menu and navigate to:  
**Assurance > Dashboards > Health tab**

![network-health-use-image001](images/assurance/img/network-health-use-image001.png)

---

#### Step 2: Access the Network Tab

By default, the Health tab opens in the "Overall" view.  
Click on the **Network** tab to display network-specific data.

![network-health-use-image003](images/assurance/img/network-health-use-image003.png)

---

#### Step 3: Select Sites and Time Range

You can filter the dashboard data by site and time range.  
- Use the controls on the right of the chart to move to the previous or next timestamp, or reload to the current time.
- Toggle the **Telemetry Status** checkbox to include or exclude telemetry status on the graph.

![A screen shot of a computer  Description automatically generated](images/assurance/img/network-health-use-image005.png)

---

#### Step 4: View Network Devices Overview

The **Network Devices** tab displays:
- **Total Devices** (percentage view)
- **Latest**: Device data for the last 5 minutes
- **Trend**: Device data for the last 24 hours

![network-health-use-image007](images/assurance/img/network-health-use-image007.png)  
![network-health-use-image009](images/assurance/img/network-health-use-image009.png)

##### Network Devices (Latest Part)

Shows data from the last 5 minutes.  
- Click **View Details** to see expanded information.
- Click any device for a detailed breakdown.

![network-health-use-image011](images/assurance/img/network-health-use-image011.png)  
![network-health-use-image013](images/assurance/img/network-health-use-image013.png)  
![network-health-use-image015](images/assurance/img/network-health-use-image015.png)

You can filter results by **Device Type**, **Device Model**, and **Device OS**.  
After applying filters, a table displays detailed device parameters.

---

#### Step 5: Analyze Network Devices (Trend Part)

Shows device data trends over the last 24 hours.  
- Click **View Details** for more information.
- Click any device for detailed stats.

![network-health-use-image017](images/assurance/img/network-health-use-image017.png)  
![network-health-use-image019](images/assurance/img/network-health-use-image019.png)

Filtering options: **Device Type**, **Device Model**, and **Device OS**.  
Filtered data appears in a detailed table.

---

#### Step 6: Monitor Total APs Up/Down

##### Latest Part

Shows up/down AP device data for the last 5 minutes.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image021.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image023.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image025.png)

- Click **Latest** to see data for the last 5 minutes.
- Click **View Details** for expanded information.
- Click **Up** to view a table of devices currently up.

##### Trend Part

Shows up/down AP device data for the last 24 hours.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image027.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image029.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image031.png)

- Click **Trend** to view 24-hour trends.
- Click **View Details** to access more data.
- Click **Up** or select a time range for a filtered table of up devices.

---

#### Step 7: Identify Top N APs by Client Count

##### Latest Part

Displays the APs with the highest client counts in the last 5 minutes.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image033.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image035.png)

- Click **View Details** for a breakdown.
- Click any AP for tabular data related to that device.

##### Trend Part

Shows top APs by client count over the last 24 hours.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image037.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image039.png)

- Click **View Details** for additional data.
- Click any AP for detailed tabular information.

---

#### Step 8: Review Top N APs by High Interference

##### Latest Part

Displays APs with the highest interference in the last 5 minutes.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image041.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image043.png)

- Click **View Details** for more information.
- Filter by interference bands: **2.4GHz**, **5GHz**, or **6GHz**.
- Click any AP to view its details in a table.

##### Trend Part

Shows APs with high interference trends for the past 24 hours.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image045.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image047.png)

- Click **View Details** for expanded information.
- Filter by band as needed.
- Click any AP for tabular device data.

---

#### Step 9: Examine Network Devices (Latest and Trend Parts)

##### Latest Part

Displays device details for the last 5 minutes in a table.

![network-health-use-image049](images/assurance/img/network-health-use-image049.png)

- Filter by **Health** or **Device Type**.
- Multiple selections are allowed.

##### Trend Part

Shows detailed device data trends for the last 24 hours in table format.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image051.png)

- Filter by **Health** or **Device Type**.
- Multiple selections are allowed.

---

#### Step 10: Assess Network Devices Reachability

##### Latest Part

Displays reachability (reachable/unreachable) status for devices in the last 5 minutes.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image053.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image055.png)

- Click **View Details** for in-depth information.
- Filter by **Role** or **Location** (multiple selections supported).
- Results are shown in a table.

##### Trend Part

Shows device reachability trends over the past 24 hours.

![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image057.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/network-health-use-image059.png)

- Click **View Details** for expanded reachability data.
- Filter by **Role** or **Location** (multiple selections supported).
- Results are displayed in a table.

---

#### WAN Link Analysis

##### WAN Link Utilization

Monitor WAN link utilization with up-to-date graphical representations.

![network-health-use-image061](images/assurance/img/network-health-use-image061.png)  
![network-health-use-image063](images/assurance/img/network-health-use-image063.png)

##### WAN Link Availability

Track the availability of WAN links for reliability assessment.

![network-health-use-image065](images/assurance/img/network-health-use-image065.png)  
![network-health-use-image067](images/assurance/img/network-health-use-image067.png)

---

### Conclusion

This guide provided a structured walkthrough of the Network Health (Network Tab) features within the Cisco Assurance Dashboard. Use the steps and visual references to effectively demonstrate or evaluate your network’s health and performance.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/ota-sniffing/ -->
## OTA (Over-The-Air) Sniffing

### Introduction

This guide provides a step-by-step walkthrough for performing an Over-The-Air (OTA) Sniffing use case on Cisco access points. OTA Sniffing enables you to capture wireless packets directly from selected access points to analyze network activity and troubleshoot issues. The process covers accessing the device, configuring capture parameters, running and monitoring the capture, and downloading the resulting packet capture (PCAP) files. Follow each step carefully to successfully complete the OTA Sniffing workflow.

---

### Step 1: Access the Device 360 Page

To begin, navigate to the **Device 360** page for the desired access point. You can do this either through the global search or via the inventory page.

In this example, we use the global search to select the `CW9166-LDN1-01` access point.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image001.png)

---

### Step 2: Start the OTA Capture

Once on the Device 360 page, locate and click the **Run OTA Capture** button.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image002.png)

---

### Step 3: Select Access Points

After clicking **Run OTA Capture**, a left panel will appear. Select any two access points by clicking on their names. The selected access points will be displayed below the floor map. Click the **Next** button to proceed.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image003.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image004.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image005.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image006.png)

---

### Step 4: Configure Capture Parameters

For each selected access point, choose the **Band**, **Radio**, **Channel Width**, and **Channel** as required. Once configured, click the **Run** button. A popup will appear; click **OK** to confirm.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image007.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image008.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image009.png)

---

### Step 5: Apply Capture Settings

A confirmation popup will display. Click **Apply** to proceed.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image010.png)

---

### Step 6: Perform Initial Checks

The system will now perform initial checks. Once these checks are successful, click **Next** to continue.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image011.png)

---

### Step 7: Review Device Configuration and Deploy

- **Step 2:** The device configuration will be checked; the status will be shown as **In-progress**.
- **Step 3:** After the configuration checks are complete and successful, the **Deploy** button will become enabled. Click **Deploy** to move forward.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image012.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image013.png)

---

### Step 8: Submit and Run the Capture

After clicking **Deploy**, a deployment popup will appear. Click **Submit** to start the OTA Sniffing process.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image014.png)

---

### Step 9: Monitor Capture Progress

You will now see the **OTA Capture Progress** message next to the **Stop** link. The system will continue capturing packets until you manually stop the capture.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image015.png)

---

### Step 10: View Capture History

While the capture is running, clicking the **Download** link will display the previous history of OTA Captures.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image016.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image017.png)

---

### Step 11: Stop the Capture and Access Results

Press **Stop** to end the packet capture. After stopping, clicking the **Download** link will show two entries: one for the previous capture and one for the current capture.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image018.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image016.png)
![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image019.png)

---

### Step 12: Download the Capture File

Click the **Download** icon to save the PCAP file for analysis.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image020.png)

---

### Step 13: View OTA Sniffing Progress in Assurance

You can also track OTA Sniffing progress by navigating to **Assurance → Settings → Intelligent Capture Settings → OTA Sniffer Capture** tab.

![A screenshot of a computer  Description automatically generated](images/assurance/img/ota-sniffing-image021.png)

---

### Conclusion

You have now completed the OTA Sniffing workflow, from device selection to packet capture and downloading the PCAP file. These steps enable efficient wireless packet analysis for troubleshooting and assurance purposes.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/assurance/pathtrace/ -->
## Path Trace\_User360

### Overview

This guide provides a step-by-step walkthrough for using the **Path Trace\_User360** feature. The demo covers how to search for a user, navigate to the User 360 view, select a device, run a path trace between a device and a target (such as a camera), and interpret the resulting network topology, VLAN connections, and ACL status. This process helps users visualize network paths and validate connectivity or configuration issues.

---

### Steps

#### Step 1: Search for the User

On the Homepage, click the global search bar as shown in the first image below.  
Type **"grace"** in the search field, select **Grace Smith** from the users list, and then click **User 360** on the right side.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image001.png)  
![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image003.png)

---

#### Step 2: Select a Device

In the **Grace Smith User 360** view, click on any one of Grace Smith’s devices, as shown below.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image005.png)

---

#### Step 3: Access Path Trace Tool

Scroll down on the page to locate the **Path Trace** section within the Tools dashboard.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image007.png)

---

#### Step 4: Run Path Trace

Click **Run Path Trace**.  
A pop-up will appear on the right side. In this pop-up, both **Source** and **Destination** drop-down menus will display all available client IPs and device details.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image009.png)

---

#### Step 5: Set Source and Destination

- Leave the **Source** as it is (selected Grace Smith’s device IP).
- Set the **Destination** to **10.10.13.214** (Camera 1 IP).
- Click **Start** to initiate the path trace.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image011.png)

---

#### Step 6: View the Topology

The tool will display the network topology between the selected source and destination.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image013.png)

---

#### Step 7: Verify Source, Destination, and Network Details

In the topology view, confirm that the **Source** and **Destination** match your selections from the drop-down menus.  
Additionally, review the VLAN connections and ACL (Access Control List) status defined on the devices, as shown below.

![A screenshot of a computer  Description automatically generated](images/assurance/img/pathtrace-image015.png)

---

### Notes

- Ensure you have the necessary permissions to access User 360 and Path Trace features.
- If any device or user is not found during the search, verify spelling or consult your admin for access.
- The screenshots above illustrate each step for clarity; your interface may have minor visual differences based on your platform version.

---

This concludes the Path Trace\_User360 demo guide.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/gbac/ -->
## Cisco GBAC Policy Management Demo Guide

### Introduction

This guide provides a comprehensive, step-by-step walkthrough for demonstrating policy management using Cisco Group-Based Access Control (GBAC). It is designed for demo users to easily understand and navigate the key functionalities. The topics covered include configuring Security Groups, managing ISE Profiles, setting up StealthWatch Host Groups, and creating, editing, and managing access policies. By following the clear instructions and visual aids provided, users will learn how to view group details, establish and modify contract policies, and effectively control network access in a structured and efficient manner.

---

### Table of Contents

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

### 1. Overview - Security Group

To access Security Group settings, navigate to **Policy > Group-Based Access Control**.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image001.png)

Click on **Security Groups**.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image003.png)

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image005.png)

---

### 2. Viewing Group Details

To view the details of any group:

- **Select any group** from the list to display its details.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image007.png)

- **Select a group** from the left panel, as shown below:

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image009.png)
![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image011.png)

- The group details will be displayed. Use the **Outbound** and **Inbound** tabs to view respective details.

---

### 3. Editing and Creating Contract Policies

To edit or create a new contract policy:

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image008.png)
Click on **Guests** and then click on **Lighting**.

- **Select the group** (e.g., "Guest -> Lighting").
  ![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image012.png)

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image013.png)

- Click **Edit Contract Policy**.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image015.png)

- **Add a new contract** and click **Next**.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image017.png)

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image019.png)

- **Enter the contract name and description**, then click **Save**.

---

### 4. Overview - ISE Profiles

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image020.png)

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image021.png)

---

### 5. Overview - StealthWatch Host Groups

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image022.png)

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image023.png)

---

### 6. Policy Management

You can view and manage existing policies here:

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image025.png)

To create a new policy:

- Select the **Auditors -> HVAC** group, then click **Change Contract**.
  ![screenshot](images/policy/img/gbac-image026.png)

![screenshot](images/policy/img/gbac-image027.png)
\* Click on **Change Contract**

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image029.png)
\* Select the Contract and click on **Change**

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image031.png)
\* Click on **Save Now** to save

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image033.png)

> **Note:** After creation, please refresh the policy matrix. The color will update to reflect changes.

---

### 7. Editing Policy Contracts

To edit an existing policy (e.g., for Auditors -> HVAC), click on the policy you wish to edit.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image033.png)

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image037.png)

- Change the policy action from **PermitIP** to **DenyIP** as needed.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image039.png)

- Select **Deny IP**.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image041.png)

- Click on **Save Now**.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image035.png)

> **Note:** After editing, please refresh the policy matrix. The color will update to reflect changes.

---

### 8. Security Group and Access Contract

View security group and access contract details as follows:

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image045.png)
Click on **Create Security Group** to create a new Security Group.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image047.png)
Click on **Save Now** to save. The new security group will then be visible.

#### Access the contract information here:

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image048.png)
Click on **Create Access Contract** to create a new Access Contract.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image049.png)
Click on **Save Now** to save.

![A screenshot of a computer  Description automatically generated](images/policy/img/gbac-image051.png)
The newly created Access Contract will be visible in the list.

---

### 9. Conclusion

This demo guide has outlined the core steps for viewing, creating, and editing policies within Cisco GBAC, including managing security groups and access contracts. Refer to the screenshots at each stage for visual guidance. For further details, consult the official Cisco documentation or your system administrator.


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/policy/qos/ -->
## Application QoS

This guide provides a step-by-step walkthrough for demonstrating the Application Quality of Service (QoS) feature within Cisco DNA Center. It covers how to view and interpret application policies, check deployment status, and analyze device-specific results. The guide also references queuing profiles relevant to Application QoS. Follow the instructions below to ensure a smooth and informative demo experience.

---

### Table of Contents

1. [Accessing Application Policies](#accessing-application-policies)
2. [Viewing Deployment Status](#viewing-deployment-status)
3. [Analyzing Device Results](#analyzing-device-results)
4. [Exploring Queuing Profiles](#exploring-queuing-profiles)

---

### 1. Accessing Application Policies

Navigate to the Application QoS section to begin managing and reviewing policies.

- Go to **Policy → Application QoS** in the Cisco DNA Center dashboard.

![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image001.png)

Or access it directly via:  
[**Application Policies**](https://172.29.58.84/dna/policy/applicationQoS/application-qos)

---

### 2. Viewing Deployment Status

To check the status of your Application QoS policy deployments:

- On the Application Policies page, click on **Deployment Status**.

![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image003.png)

- After clicking, the **Policy AU slide** will appear, providing deployment insights.

![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image005.png)

---

### 3. Analyzing Device Results

Deployment status displays the outcome per device category:

- Click on the types of devices shown to filter the results below according to the number of devices in each category.

  - **Failed Devices:** If you select this option, it will display 0 records.

  ![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image007.png)

  - **Successful Devices:** Selecting this option will display 3 records.

  ![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image009.png)

  ![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image011.png)

  ![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image013.png)

  ![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image015.png)

---

### 4. Exploring Queuing Profiles

To further analyze queuing behavior for Application QoS:

- Visit [**Queuing Profiles**](https://172.29.58.84/dna/policy/applicationQoS/queueuing-profile) for more details.

![A screenshot of a computer  Description automatically generated](images/policy/img/qos-image017.png)

---

### Summary

This demo guide provided a structured overview of the Application QoS feature in Cisco DNA Center, including accessing policies, checking deployment status, interpreting results by device, and referencing queuing profiles. Use this guide as a reference to ensure a seamless and effective demonstration.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/brownfield_automation/ -->
## Brownfield Automation

This demo guide provides step-by-step instructions for configuring VLANs and ports in a campus brownfield automation scenario. The guide is structured into two main sections:

1. **VLAN Configuration**: How to filter switches and configure VLANs.
2. **Port Configuration**: How to edit and verify port settings.

Each step is illustrated with screenshots to help you follow along with the configuration process.

---

### 1. VLAN Configuration

#### Step 1

Navigate to the relevant section in your automation platform.

![Screenshot](images/provision/img/brownfield_automation-image001.png)

---

#### Step 2

Proceed to the next configuration screen.

![Screenshot](images/provision/img/brownfield_automation-image003.png)

---

#### Step 3

Filter the switches as needed to narrow down your selection.

![Screenshot](images/provision/img/brownfield_automation-image005.png)

---

#### Step 4

Go to the **View Details** page and enable the **Layer 2 Configuration** tab.

![Screenshot](images/provision/img/brownfield_automation-image007.png)

---

#### Step 5

Enable the first four "power butter" options as required by your setup.

![Screenshot](images/provision/img/brownfield_automation-image009.png)

---

#### Step 6

Continue to the next step in the configuration process.

![A screenshot of a computer  Description automatically generated](data:image/png;base64...)

---

#### Step 7: VLAN Configuration Steps

Follow the VLAN configuration steps as shown below.

![Screenshot](images/provision/img/brownfield_automation-image011.png)

![Screenshot](images/provision/img/brownfield_automation-image013.png)

![Screenshot](images/provision/img/brownfield_automation-image015.png)

![Screenshot](images/provision/img/brownfield_automation-image017.png)

![Screenshot](images/provision/img/brownfield_automation-image019.png)

![Screenshot](images/provision/img/brownfield_automation-image021.png)

![Screenshot](images/provision/img/brownfield_automation-image023.png)

![Screenshot](images/provision/img/brownfield_automation-image025.png)

![Screenshot](images/provision/img/brownfield_automation-image027.png)

![Screenshot](images/provision/img/brownfield_automation-image029.png)

---

### 2. Port Configuration

#### Step 1

Begin by selecting the port configuration section.

![Screenshot](images/provision/img/brownfield_automation-image031.png)

![Screenshot](images/provision/img/brownfield_automation-image033.png)

---

#### Step 2

Proceed to the next step in port configuration.

![Screenshot](images/provision/img/brownfield_automation-image035.png)

---

#### Step 3

Continue configuring the port settings.

![Screenshot](images/provision/img/brownfield_automation-image037.png)

![Screenshot](images/provision/img/brownfield_automation-image039.png)

---

#### Step 4

Advance to the next configuration screen.

![Screenshot](images/provision/img/brownfield_automation-image041.png)

---

#### Step 5

Edit the specific record you want to modify.

![Screenshot](images/provision/img/brownfield_automation-image043.png)

![Screenshot](images/provision/img/brownfield_automation-image045.png)

![Screenshot](images/provision/img/brownfield_automation-image047.png)

![Screenshot](images/provision/img/brownfield_automation-image049.png)

![Screenshot](images/provision/img/brownfield_automation-image051.png)

---

#### Step 6

Continue to the subsequent step.

![Screenshot](images/provision/img/brownfield_automation-image053.png)

![Screenshot](images/provision/img/brownfield_automation-image055.png)

---

#### Step 7

Make further adjustments as required.

![Screenshot](images/provision/img/brownfield_automation-image057.png)

---

#### Step 8

Follow the steps as shown.

![Screenshot](images/provision/img/brownfield_automation-image059.png)

---

#### Step 9

Proceed with additional port configuration.

![Screenshot](images/provision/img/brownfield_automation-image061.png)

---

#### Step 10

Continue to the next configuration step.

![Screenshot](images/provision/img/brownfield_automation-image063.png)

---

#### Step 11

Finalize the configuration.

![Screenshot](images/provision/img/brownfield_automation-image065.png)

---

#### Step 12: Verify Port Configuration

Check the port configuration table to verify that the record changes have been applied successfully.

![Screenshot](images/provision/img/brownfield_automation-image067.png)

![Screenshot](images/provision/img/brownfield_automation-image069.png)

---

### Conclusion

By following this guide, you will be able to efficiently configure VLANs and ports in a brownfield campus automation environment. Refer to the screenshots for visual assistance at each step. For further details or troubleshooting, consult the official documentation or support resources.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/fabric/ -->
## Enabling Edge Role for London1 – 2nd Floor Device

This guide provides step-by-step instructions for enabling the Edge role on a device located on the 2nd Floor of the London1 site using the Cisco Fabric Provisioning interface. You will learn how to navigate the site hierarchy, select the correct device, enable the Edge role, and deploy the configuration.

---

### Steps to Enable Edge Role

#### Step 1: Navigate to the London1 Site and 2nd Floor

- Go to **Provision** > **Fabric Sites**.
- Click on the **London1** site.
- Select **2nd Floor** from the "View Site Hierarchy" panel.

![Screenshot](images/provision/img/fabric-image001.png)

---

#### Step 2: Select the Device

- Click on the device icon labeled **LDN1-C9200-Edge3.pseudoco.com**.

---

#### Step 3: Enable the Edge Node Role

- On the device details page, enable the **Edge node** role for **LDN1-C9200-Edge3.pseudoco.com**.

![Screenshot](images/provision/img/fabric-image003.png)

---

#### Step 4: Add the Device

- Click the **Add** button to include this device as an Edge node.

---

#### Step 5: Deploy the Configuration

- Click the **Deploy** button to proceed with the configuration deployment.

![Screenshot](images/provision/img/fabric-image005.png)

---

#### Step 6: Apply the Configuration

- In the **Generate Config Preview** slider window, click the **Apply** button to finalize and apply the changes.

![Screenshot](images/provision/img/fabric-image007.png)

![Screenshot](images/provision/img/fabric-image009.png)

---

### Summary

By following these steps, you have successfully enabled the Edge role for the selected device on the 2nd Floor of the London1 site. This ensures the device participates in the fabric as an Edge node, enabling enhanced connectivity and management capabilities for your network.

---


---

<!-- source: https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/provision/fiab/ -->
## Fabric In a Box (FIAB)

### Introduction

This demo guide provides step-by-step instructions for deploying Fabric In a Box (FIAB) and configuring Anycast Gateways using Cisco's network management interface. The guide walks you through:
- Navigating to the fabric site and configuring device roles
- Creating and verifying Anycast Gateways
- Attaching a Wireless SSID to Virtual Networks

Each step includes screenshots for visual reference, ensuring a smooth and successful demonstration.

---

### 1. Accessing the Fabric Site

**Step 1:**  
Navigate to **Main menu → Provision → Fabric Sites**. You will land on the following screen. Click on the desired fabric site's number.

![Screenshot](images/provision/img/fiab-image001.png)

**Step 2:**  
Click on the **London2** site.

![Screenshot](images/provision/img/fiab-image003.png)

**Step 3:**  
In the topology view, click on the device named **LDN2-C9300-FIAB.PseudoCo.com**.

![Screenshot](images/provision/img/fiab-image005_new.png)

The following screen will appear:

![Screenshot](images/provision/img/fiab-image007.png)

---

### 2. Configuring Device Roles in the Fabric Tab

**Step 4:**  
Within the **Fabric** tab, enable each device role in sequence:

- **Border Node:** Enter the required details and click **Add**.

![Screenshot](images/provision/img/fiab-image009.png)

- **Control Plane:** Select **LISP Pub / Sub** and click the **Add** button.

![Screenshot](images/provision/img/fiab-image011.png)

A new window will open:

![Screenshot](images/provision/img/fiab-image013.png)

- **Edge Node:** Enable the Edge Node role, but **do not click Add yet**.

![Screenshot](images/provision/img/fiab-image015.png)

- **Embedded Wireless LAN Controller:**  
  This step has sub-steps as shown in the screenshots below:
- The scope (e.g., London2 → 1st Floor) is selected automatically.

![Screenshot](images/provision/img/fiab-image017.png)

- Advanced options.

![Screenshot](images/provision/img/fiab-image019.png)

- Summary view.

![Screenshot](images/provision/img/fiab-image021.png)

After completing the above, click the **Add** button on the final step.

![Screenshot](images/provision/img/fiab-image023.png)

Then, click the **Deploy** button.

![Screenshot](images/provision/img/fiab-image025_new.png)

Follow the remaining prompts as shown:

![Screenshot](images/provision/img/fiab-image027.png)
![Screenshot](images/provision/img/fiab-image029.png)
![Screenshot](images/provision/img/fiab-image031.png)
![Screenshot](images/provision/img/fiab-image033.png)
![Screenshot](images/provision/img/fiab-image035.png)

Once the task is submitted, the roles will be attached to **LDN2-C9300-FIAB.PseudoCo.com** and the device icon will update accordingly.

![Screenshot](images/provision/img/fiab-image037_new.png)
![Screenshot](images/provision/img/fiab-image039_new.png)

---

### 3. Creating an Anycast Gateway

#### Step 1: Initial Checks

Before starting, verify the following for the **VN\_Employees** virtual network:

- **Layer 3 Virtual Networks tab:**  
  Anycast Gateway count should be 0.

![Screenshot](images/provision/img/fiab-image041.png)

- **Layer 2 Virtual Networks tab:**  
  There should be no entry with VN\_Employees in the "Associated Layer 3 Virtual Network" column.

![Screenshot](images/provision/img/fiab-image043.png)

- **Anycast Gateway tab:**  
  No entry for VN\_Employees in the "Associated Layer 3 Virtual Network" column.

![Screenshot](images/provision/img/fiab-image045.png)

---

#### Step 2: Create Anycast Gateway

- Click on **Create Anycast Gateways**.
- Select **VN\_Employees Virtual Network** using the "+" icon.

![Screenshot](images/provision/img/fiab-image047.png)
![Screenshot](images/provision/img/fiab-image049.png)

Click **Next**.

---

#### Step 3: Configure Attributes

On the **Configuration Attributes** page, fill in the following:

- **IP Address Pool:** Select `LDN2_10.10.23.128_SDA_Employees [10.10.23.128/26]`
- **IP-Directed Broadcast:** Check this box
- **TCP MSS Adjustment:** Check and enter a value between 500–1440
- **VLAN Name:** Enter a name, e.g., `VLAN-VN_Employees`
- **VLAN ID:** 1120 (or any valid value)
- **Fabric-Enabled Wireless:** Check this box
- **Multiple IP-to-MAC Addresses:** Check this box

Leave other settings at default, then click **Next**.

![Screenshot](images/provision/img/fiab-image051.png)

---

#### Step 4: Fabric Zone

- No data entry required in this section. Click **Next**.

![Screenshot](images/provision/img/fiab-image053.png)

---

#### Step 5: Summary and Deployment

- Review the summary of your configuration and click **Next**.

![Screenshot](images/provision/img/fiab-image055.png)

---

#### Step 6: Finalize Deployment

- Click **Deploy** to complete the workflow.

![Screenshot](images/provision/img/fiab-image057.png)
![Screenshot](images/provision/img/fiab-image059.png)
![A white background with text  Description automatically generated](data:image/png;base64...)

![Screenshot](images/provision/img/fiab-image061.png)
![Screenshot](images/provision/img/fiab-image063.png)

---

#### Step 7: Review Results

After deployment, you will see a confirmation screen:

![Screenshot](images/provision/img/fiab-image065.png)

Click **View Anycast Gateways** to proceed.

---

#### Step 8: Verify Anycast Gateway

You will be directed to the **Anycast Gateways** tab, where the newly created entry appears.

![Screenshot](images/provision/img/fiab-image067.png)

---

#### Step 9: Verify Layer 2 Virtual Network Entry

Go to **Layer 2 Virtual Networks** to see the new entry with the values you created.

![Screenshot](images/provision/img/fiab-image069.png)

---

#### Step 10: Confirm Anycast Gateway Count

On the **Layer 2 Virtual Networks** tab, confirm that the Anycast Gateway count has increased for **VN\_Employees**.

![Screenshot](images/provision/img/fiab-image071.png)

---

### 4. Wireless SSID Attachment to Virtual Networks

#### Step 1: Access Wireless SSID Tab

Click on the **Wireless SSID** tab.

![Screenshot](images/provision/img/fiab-image073.png)

---

#### Step 2: Deploy Wireless SSID

Select the values as shown in the screenshot, then click **Deploy** and follow the workflow.

![Screenshot](images/provision/img/fiab-image075.png)
![Screenshot](images/provision/img/fiab-image077.png)
![Screenshot](images/provision/img/fiab-image079.png)

---

#### Step 3: Preview and Deploy

Review your configuration in the **Preview Configuration** step, then click **Deploy**.

![Screenshot](images/provision/img/fiab-image081.png)
![Screenshot](images/provision/img/fiab-image083.png)

After completion, you will see a confirmation screen with your selected values:

![Screenshot](images/provision/img/fiab-image085.png)
![Screenshot](images/provision/img/fiab-image087.png)

---

### Conclusion

You have now successfully completed the FIAB demo, including configuration of device roles, Anycast Gateway creation, and Wireless SSID attachment. Use this guide as a reference for future deployments and demonstrations.
