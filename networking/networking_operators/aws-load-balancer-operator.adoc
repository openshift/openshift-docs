:_mod-docs-content-type: ASSEMBLY
[id="aws-load-balancer"]
= AWS Load Balancer Operator
include::_attributes/common-attributes.adoc[]
:context: aws-load-balancer-operator

toc::[]


The AWS Load Balancer Operator (ALBO) is an Operator supported by Red{nbsp}Hat that users can optionally install on SRE-managed
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
{product-title} (ROSA)
endif::openshift-rosa[]
clusters. The ALBO manages the lifecycle of the AWS-managed AWS Load Balancer Controller (ALBC) that provisions AWS Elastic Load Balancing v2 (ELBv2) services for applications running in
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
clusters.

include::modules/aws-installing-an-aws-load-balancer-operator.adoc[leveloffset=+1]
include::modules/aws-uninstalling-an-aws-load-balancer-operator.adoc[leveloffset=+1]