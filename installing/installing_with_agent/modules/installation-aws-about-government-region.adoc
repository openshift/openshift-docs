// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc

ifeval::["{context}" == "installing-aws-government-region"]
:aws-gov:
endif::[]
ifeval::["{context}" == "installing-aws-secret-region"]
:aws-secret:
endif::[]

[id="installation-aws-about-gov-secret-region_{context}"]
ifdef::aws-gov[]
= AWS government regions
endif::aws-gov[]
ifdef::aws-secret[]
= AWS secret regions
endif::aws-secret[]

ifdef::aws-gov[]
{product-title} supports deploying a cluster to an link:https://aws.amazon.com/govcloud-us[AWS GovCloud (US)] region.
endif::aws-gov[]

ifdef::aws-gov[]
The following AWS GovCloud partitions are supported:

* `us-gov-east-1`
* `us-gov-west-1`
endif::aws-gov[]

ifdef::aws-secret[]
The following AWS secret partitions are supported:

* `us-isob-east-1` (SC2S)
* `us-iso-east-1` (C2S)

[NOTE]
====
The maximum supported MTU in an AWS SC2S and C2S Regions is not the same as
AWS commercial. For more information about configuring MTU during installation,
see the _Cluster Network Operator configuration object_ section in _Installing
a cluster on AWS with network customizations_
====
endif::aws-secret[]

ifeval::["{context}" == "installing-aws-government-region"]
:!aws-gov:
endif::[]
ifeval::["{context}" == "installing-aws-secret-region"]
:!aws-secret:
endif::[]
