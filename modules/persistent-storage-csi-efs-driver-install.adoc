// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/osd-persistent-storage-csi-aws-efs.adoc

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-csi-efs-driver-install_{context}"]
= Installing the {FeatureName} CSI Driver

ifdef::openshift-rosa[]
After installing the link:https://github.com/openshift/aws-efs-csi-driver-operator[{FeatureName} CSI Driver Operator] (a Red Hat operator) and configuring it with STS, you install the link:https://github.com/openshift/aws-efs-csi-driver[{FeatureName} CSI driver].
endif::openshift-rosa[]
ifdef::openshift-dedicated[]
After installing the {FeatureName} CSI Driver Operator, you install the {FeatureName} CSI Driver.
endif::openshift-dedicated[]

.Prerequisites
* Access to the {product-title} web console.

.Procedure

. Click *Administration* -> *CustomResourceDefinitions* -> *ClusterCSIDriver*.

. On the *Instances* tab, click *Create ClusterCSIDriver*.

. Use the following YAML file:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: ClusterCSIDriver
metadata:
    name: efs.csi.aws.com
spec:
  managementState: Managed
----

. Click *Create*.

. Wait for the following Conditions to change to a "True" status:
+

* AWSEFSDriverNodeServiceControllerAvailable

* AWSEFSDriverControllerServiceControllerAvailable