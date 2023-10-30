// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/osd-persistent-storage-csi-aws-efs.adoc

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-csi-olm-operator-install_{context}"]
= Installing the {FeatureName} CSI Driver Operator

The link:https://github.com/openshift/aws-efs-csi-driver-operator[AWS EFS CSI Driver Operator] (a Red Hat operator) is not installed in {product-title} by default. Use the following procedure to install and configure the {FeatureName} CSI Driver Operator in your cluster.

.Prerequisites
* Access to the {product-title} web console.

.Procedure
To install the {FeatureName} CSI Driver Operator from the web console:

. Log in to the web console.

. Install the {FeatureName} CSI Operator:

.. Click *Operators* -> *OperatorHub*.

.. Locate the {FeatureName} CSI Operator by typing *{FeatureName} CSI* in the filter box.

.. Click the *{FeatureName} CSI Driver Operator* button.
+
[IMPORTANT]
====
Be sure to select the *{FeatureName} CSI Driver Operator* and not the *{FeatureName} Operator*. The *{FeatureName} Operator* is a community Operator and is not supported by Red Hat.
====

.. On the *{FeatureName} CSI Driver Operator* page, click *Install*.

.. On the *Install Operator* page, ensure that:
+
ifdef::openshift-rosa,openshift-enterprise[]
* If you are using {FeatureName} with AWS Secure Token Service (STS), in the *role ARN* field, enter the ARN role copied from the last step of the _Obtaining a role Amazon Resource Name for Security Token Service_ procedure.
endif::[]
* *All namespaces on the cluster (default)* is selected.
* *Installed Namespace* is set to *openshift-cluster-csi-drivers*.

.. Click *Install*.
+
After the installation finishes, the {FeatureName} CSI Operator is listed in the *Installed Operators* section of the web console.

.Next steps
