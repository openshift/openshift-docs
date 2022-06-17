// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc

[id="private-clusters-about-azure_{context}"]
= Private clusters in Azure

To create a private cluster on Microsoft Azure, you must provide an existing private VNet and subnets to host the cluster. The installation program must also be able to resolve the DNS records that the cluster requires. The installation program configures the Ingress Operator and API server for only internal traffic.

Depending how your network connects to the private VNET, you might need to use a DNS forwarder to resolve the cluster's private DNS records. The cluster's machines use `168.63.129.16` internally for DNS resolution. For more information, see link:https://docs.microsoft.com/en-us/azure/dns/private-dns-overview[What is Azure Private DNS?] and link:https://docs.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16[What is IP address 168.63.129.16?] in the Azure documentation.

The cluster still requires access to internet to access the Azure APIs.

The following items are not required or created when you install a private cluster:

* A `BaseDomainResourceGroup`, since the cluster does not create public records
* Public IP addresses
* Public DNS records
* Public endpoints

 The cluster is configured so that the Operators do not create public records for the cluster and all cluster machines are placed in the private subnets that you specify.

[id="private-clusters-limitations-azure_{context}"]
== Limitations

Private clusters on Azure are subject to only the limitations that are associated with the use of an existing VNet.


////
Is this also valid in Azure?

The ability to add public functionality to a private cluster is limited.

* You cannot make the Kubernetes API endpoints public after installation without taking additional actions, including creating public subnets in the VNet for each availability zone in use, creating a public load balancer, and configuring the control plane security groups to allow traffic from the internet on 6443 (Kubernetes API port).
////
