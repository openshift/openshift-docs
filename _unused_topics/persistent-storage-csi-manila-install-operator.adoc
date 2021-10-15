// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc

[id="persistent-storage-csi-manila-install-operator_{context}"]
= Installing the Manila CSI Driver Operator

The Manila Container Storage Interface (CSI) Driver Operator is not installed in {product-title} by default. Use the following procedure to install and configure this Operator to enable the OpenStack Manila CSI driver in your cluster.

.Prerequisites
* You have access to the {product-title} web console.
* The underlying {rh-openstack-first} infrastructure cloud deploys Manila serving NFS shares.

.Procedure

To install the Manila CSI Driver Operator from the web console, follow these steps:

. Log in to the {product-title} web console.

. Navigate to *Operators* -> *OperatorHub*.

. Type *Manila CSI Driver Operator* into the filter box to locate the Operator.

. Click *Install*.

. On the *Install Operator* page, select *openshift-manila-csi-driver-operator* from the *Installed Namespace* drop-down menu.

. Adjust the values for *Update Channel* and *Approval Strategy* to the values that you want. The only supported *Installation Mode* is *All namespaces on the cluster*.

. Click *Install*.

Once finished, the Manila CSI Driver Operator is listed in the *Installed Operators* section of the web console.
