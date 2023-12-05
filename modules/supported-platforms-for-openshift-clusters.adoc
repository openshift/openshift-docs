// Module included in the following assemblies:
//
// * architecture/architecture-installation.adoc
// * installing/index.adoc

:_mod-docs-content-type: REFERENCE
[id="supported-platforms-for-openshift-clusters_{context}"]
= Supported platforms for {product-title} clusters

In {product-title} {product-version}, you can install a cluster that uses installer-provisioned infrastructure on the following platforms:

* Alibaba Cloud
* Amazon Web Services (AWS)
* Bare metal
* Google Cloud Platform (GCP)
* {ibm-cloud-name}
* Microsoft Azure
* Microsoft Azure Stack Hub
* Nutanix
* {rh-openstack-first}
** The latest {product-title} release supports both the latest {rh-openstack} long-life release and intermediate release. For complete {rh-openstack} release compatibility, see the link:https://access.redhat.com/articles/4679401[{product-title} on {rh-openstack} support matrix].
* VMware vSphere

For these clusters, all machines, including the computer that you run the installation process on, must have direct internet access to pull images for platform containers and provide telemetry data to Red Hat.

[IMPORTANT]
====
After installation, the following changes are not supported:

* Mixing cloud provider platforms.
* Mixing cloud provider components. For example, using a persistent storage framework from a another platform on the platform where you installed the cluster.
====

In {product-title} {product-version}, you can install a cluster that uses user-provisioned infrastructure on the following platforms:

* AWS
* Azure
* Azure Stack Hub
* Bare metal
* GCP
* {ibm-power-name}
* {ibm-z-name} or {ibm-linuxone-name}
* {rh-openstack}
** The latest {product-title} release supports both the latest {rh-openstack} long-life release and intermediate release. For complete {rh-openstack} release compatibility, see the link:https://access.redhat.com/articles/4679401[{product-title} on {rh-openstack} support matrix].
* VMware Cloud on AWS
* VMware vSphere

Depending on the supported cases for the platform, you can perform installations on user-provisioned infrastructure, so that you can run machines with full internet access, place your cluster behind a proxy, or perform a disconnected installation.

In a disconnected installation, you can download the images that are required to install a cluster, place them in a mirror registry, and use that data to install your cluster. While you require internet access to pull images for platform containers, with a disconnected installation on vSphere or bare metal infrastructure, your cluster machines do not require direct internet access.

The link:https://access.redhat.com/articles/4128421[OpenShift Container Platform 4.x Tested Integrations] page contains details about integration testing for different platforms.
