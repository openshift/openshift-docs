// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-china.adoc

//Starting in 4.10, aws on arm64 is only supported for installation on custom, network custom, private clusters and VPC. This attribute excludes arm64 content from installing on gov regions. When government regions are supported on arm64, remove this ifdevel.
ifeval::["{context}" == "installing-aws-government-region"]
:aws-govcloud:
endif::[]
//Starting in 4.10, aws on arm64 is only supported for installation on custom, network custom, private clusters and VPC. This attribute excludes arm64 content from installing on secret regions. When secret regions are supported on arm64, remove this ifdevel.
ifeval::["{context}" == "installing-aws-secret-region"]
:aws-secret:
endif::[]
//Starting in 4.10, aws on arm64 is only supported for installation on custom, network custom, private clusters and VPC. This attribute excludes arm64 content from installing in china regions. When china regions are supported on arm64, remove this ifdevel.
ifeval::["{context}" == "installing-aws-china-region"]
:aws-china:
endif::[]

[id="installation-supported-aws-machine-types_{context}"]
= Supported AWS machine types

The following Amazon Web Services (AWS) instance types are supported with {product-title}.

.Machine types based on x86_64 architecture
[%collapsible]
====
[cols="2a,2a,2a,2a",options="header"]
|===

|Instance type
|Bootstrap
|Control plane
|Compute

|`i3.large`
|x
|
|

|`m4.large`
|
|
|x

|`m4.xlarge`
|
|x
|x

|`m4.2xlarge`
|
|x
|x

|`m4.4xlarge`
|
|x
|x

|`m4.10xlarge`
|
|x
|x

|`m4.16xlarge`
|
|x
|x

|`m5.large`
|
|
|x

|`m5.xlarge`
|
|x
|x

|`m5.2xlarge`
|
|x
|x

|`m5.4xlarge`
|
|x
|x

|`m5.8xlarge`
|
|x
|x

|`m5.12xlarge`
|
|x
|x

|`m5.16xlarge`
|
|x
|x

|`m5a.large`
|
|
|x

|`m5a.xlarge`
|
|x
|x

|`m5a.2xlarge`
|
|x
|x

|`m5a.4xlarge`
|
|x
|x

|`m5a.8xlarge`
|
|x
|x

|`m5a.12xlarge`
|
|x
|x

|`m5a.16xlarge`
|
|x
|x

|`m6i.large`
|
|
|x

|`m6i.xlarge`
|
|x
|x

|`m6i.2xlarge`
|
|x
|x

|`m6i.4xlarge`
|
|x
|x

|`m6i.8xlarge`
|
|x
|x

|`m6i.12xlarge`
|
|x
|x

|`m6i.16xlarge`
|
|x
|x

|`c4.2xlarge`
|
|x
|x

|`c4.4xlarge`
|
|x
|x

|`c4.8xlarge`
|
|x
|x

|`c5.xlarge`
|
|
|x

|`c5.2xlarge`
|
|x
|x

|`c5.4xlarge`
|
|x
|x

|`c5.9xlarge`
|
|x
|x

|`c5.12xlarge`
|
|x
|x

|`c5.18xlarge`
|
|x
|x

|`c5.24xlarge`
|
|x
|x

|`c5a.xlarge`
|
|
|x

|`c5a.2xlarge`
|
|x
|x

|`c5a.4xlarge`
|
|x
|x

|`c5a.8xlarge`
|
|x
|x

|`c5a.12xlarge`
|
|x
|x

|`c5a.16xlarge`
|
|x
|x

|`c5a.24xlarge`
|
|x
|x

|`r4.large`
|
|
|x

|`r4.xlarge`
|
|x
|x

|`r4.2xlarge`
|
|x
|x

|`r4.4xlarge`
|
|x
|x

|`r4.8xlarge`
|
|x
|x

|`r4.16xlarge`
|
|x
|x

|`r5.large`
|
|
|x

|`r5.xlarge`
|
|x
|x

|`r5.2xlarge`
|
|x
|x

|`r5.4xlarge`
|
|x
|x

|`r5.8xlarge`
|
|x
|x

|`r5.12xlarge`
|
|x
|x

|`r5.16xlarge`
|
|x
|x

|`r5.24xlarge`
|
|x
|x

|`r5a.large`
|
|
|x

|`r5a.xlarge`
|
|x
|x

|`r5a.2xlarge`
|
|x
|x

|`r5a.4xlarge`
|
|x
|x

|`r5a.8xlarge`
|
|x
|x

|`r5a.12xlarge`
|
|x
|x

|`r5a.16xlarge`
|
|x
|x

|`r5a.24xlarge`
|
|x
|x

|`t3.large`
|
|
|x

|`t3.xlarge`
|
|
|x

|`t3.2xlarge`
|
|
|x

|`t3a.large`
|
|
|x

|`t3a.xlarge`
|
|
|x

|`t3a.2xlarge`
|
|
|x

|===
====

ifndef::aws-govcloud,aws-secret,aws-china,openshift-origin,localzone[]
.Machine types based on arm64 architecture
[%collapsible]
====
[cols="2a,2a,2a,2a",options="header"]
|===

|Instance type
|Bootstrap
|Control plane
|Compute

|`m6g.large`
|x
|
|x

|`m6g.xlarge`
|
|x
|x

|`m6g.2xlarge`
|
|x
|x

|`m6g.4xlarge`
|
|x
|x

|`m6g.8xlarge`
|
|x
|x

|`m6g.12xlarge`
|
|x
|x

|`m6g.16xlarge`
|
|x
|x

|`c6g.large`
|x
|
|

|`c6g.xlarge`
|
|
|x

|`c6g.2xlarge`
|
|x
|x

|`c6g.4xlarge`
|
|x
|x

|`c6g.8xlarge`
|
|x
|x

|`c6g.12xlarge`
|
|x
|x

|`c6g.16xlarge`
|
|x
|x

|`c7g.large`
|x
|
|

|`c7g.xlarge`
|
|x
|x

|`c7g.2xlarge`
|
|x
|x

|`c7g.4xlarge`
|
|x
|x

|`c7g.8xlarge`
|
|x
|x

|`c7g.12xlarge`
|
|x
|x

|`c7g.16large`
|
|x
|x

|===
====
endif::[]

ifeval::["{context}" == "installing-restricted-networks-aws"]
:!aws-restricted-upi:
endif::[]
ifeval::["{context}" == "installing-aws-government-region"]
:!aws-govcloud:
endif::[]
ifeval::["{context}" == "installing-aws-secret-region"]
:!aws-secret:
endif::[]
ifeval::["{context}" == "installing-aws-china-region"]
:!aws-china:
endif::[]
