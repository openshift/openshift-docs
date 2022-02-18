---
title: Overview of Egress Lockdown
description: Overview of Egress Lockdown for Azure Red Hat OpenShift Clusters
author: sayjadha
ms.author: #Required; Microsoft alias of author; optional team alias.
ms.service: azure-redhat-openshift
keywords: egress lockdown, aro cluster, aro, networking, openshift, red hat
ms.topic: conceptual
ms.service: azure-redhat-openshift
ms.date: 02/28/2022
---

# Overview of Egress Lockdown
Egress Lockdown provides access to necessary URLs and endpoints that the Azure Red Hat OpenShift (ARO) cluster needs to function effectively. For example, it ensures that you have access to URLs such as management.azure.com so that you can create additional worker nodes backed by Azure VMs even if the outbound (egress) traffic is restricted through some means, such as a firewall appliance.

Egress Lockdown takes a collection of domains necessary for an ARO cluster to function and proxies calls to these domains through the ARO service. The domains are region-specific and customers cannot configure them.

Egress Lockdown does not rely on customer internet access for the OpenShift services to work. If clusters want to reach any ARO service, the cluster traffic exits through an Azure Private Endpoint created within the cluster resource group where all the ARO resources are available. A well-known subset of domains (that the ARO clusters need to function) validates the destination of the cluster traffic. Finally, the traffic passes through the ARO service to connect to these URLs and endpoints.

## Enabling Egress Lockdown
Egress Lockdown relies on a TLS extension called SNI (Server Name Indication) to function. All the customer workloads that communicate with the well-known subset of domains must have SNI enabled on them. Egress lockdown is enabled by default for new cluster creation. However, to enable egress lockdown on existing clusters, you must have SNI enabled on the customer workloads. Please submit a support case to either [Microsoft Support](https://support.microsoft.com/en-us) or [Red Hat Support](https://www.redhat.com/en/services/support) for enabling egress lockdown on your existing clusters.

## Verifying that Egress Lockdown is enabled on a cluster
To verify if Egress Lockdown is enabled on a cluster, run the following command when you are logged into the ARO cluster:
  ```
  $ oc get cluster.aro.openshift.io cluster -o go-template='{{ if .spec.gatewayDomains }}{{ "Egress Lockdown Feature Enabled" }}{{ else }}{{ "Egress Lockdown Feature Disabled" }}{{ end }}{{ "\n" }}
  ```
Depending on whether egress lockdown is enabled or disabled, the command will display the output 'Egress Lockdown Feature Enabled' or 'Egress Lockdown Feature Disabled' respectively.
