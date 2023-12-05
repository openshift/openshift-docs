// Module included in the following assemblies:
//
// * networking/configuring-cluster-wide-proxy.adoc

:_mod-docs-content-type: CONCEPT
[id="configuring-a-proxy-during-installation-ocm_{context}"]
= Configuring a proxy during installation using {cluster-manager}

If you are installing
ifdef::openshift-dedicated[]
an {product-title}
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
a {product-title} (ROSA)
endif::openshift-rosa[]
cluster into an existing Virtual Private Cloud (VPC), you can use {cluster-manager-first} to enable a cluster-wide HTTP or HTTPS proxy during installation.
ifdef::openshift-dedicated[]
You can enable a proxy only for clusters that use the Customer Cloud Subscription (CCS) model.
endif::openshift-dedicated[]

Prior to the installation, you must verify that the proxy is accessible from the VPC that the cluster is being installed into. The proxy must also be accessible from the private subnets of the VPC.

ifdef::openshift-dedicated[]
For detailed steps to configure a cluster-wide proxy during installation by using {cluster-manager}, see _Creating a cluster on AWS with CCS_ or _Creating a cluster on GCP with CCS_.
endif::openshift-dedicated[]

ifdef::openshift-rosa[]
For detailed steps to configure a cluster-wide proxy during installation by using {cluster-manager}, see _Creating a cluster with customizations by using OpenShift Cluster Manager_.
endif::openshift-rosa[]
