// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
//
:_mod-docs-content-type: REFERENCE
[id="osd-aws-vpc-required-resources_{context}"]
= Amazon VPC Requirements for non-PrivateLink ROSA clusters

To create an Amazon VPC, You must have the following:

* An internet gateway,
* A NAT gateway,
* Private and public subnets that have internet connectivity provided to install required components.

You must have at least one single private and public subnet for Single-AZ clusters, and you need at least three private and public subnets for Multi-AZ clusters.