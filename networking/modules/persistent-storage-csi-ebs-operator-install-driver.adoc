// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc

[id="persistent-storage-csi-ebs-operator-install-driver_{context}"]
= Installing the AWS Elastic Block Store CSI driver

The AWS Elastic Block Store (EBS) Container Storage Interface (CSI) driver is a custom resource (CR) that enables you to create and mount AWS EBS persistent volumes.

The driver is not installed in {product-title} by default, and must be installed after the AWS EBS CSI Driver Operator has been installed.

.Prerequisites

* The AWS EBS CSI Driver Operator has been installed.
* You have access to the {product-title} web console.

.Procedure

To install the AWS EBS CSI driver from the web console, complete the following steps:

. Log in to the {product-title} web console.

. Navigate to *Operators* -> *Installed Operators*.

. Locate the *AWS EBS CSI Driver Operator* from the list and click on the Operator link.

. Create the driver:
.. From the *Details* tab, click *Create Instance*.

.. Optional: Select *YAML view* to make modifications, such as adding notations, to the driver object template.

.. Click *Create* to finalize.
+
[IMPORTANT]
====
Renaming the cluster and specifying a certain namespace are not supported functions.
====
