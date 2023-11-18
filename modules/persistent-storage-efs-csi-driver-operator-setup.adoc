// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/osd-persistent-storage-csi-aws-efs.adoc

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-efs-csi-driver-operator-setup_{context}"]
= Setting up the {FeatureName} CSI Driver Operator

. Install the link:https://github.com/openshift/aws-efs-csi-driver-operator[{FeatureName} CSI Driver Operator] (a Red Hat operator).

ifdef::openshift-rosa[]
. If you are using Amazon Elastic File Storage (Amazon EFS) with AWS Secure Token Service (STS), configure the https://github.com/openshift/aws-efs-csi-driver[{FeatureName} CSI driver] with STS.
endif::openshift-rosa[]

ifdef::openshift-rosa,openshift-enterprise[]
. If you are using {FeatureName} with AWS Secure Token Service (STS), obtain a role Amazon Resource Name (ARN) for STS. This is required for installing the {FeatureName} CSI Driver Operator.
endif::[]

. Install the {FeatureName} CSI Driver Operator.

. Install the {FeatureName} CSI Driver.
