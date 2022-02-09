// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-government-region.adoc

[id="installation-prereq-aws-private-cluster_{context}"]
= Installation requirements

Before you can install the cluster, you must:

* Provide an existing private AWS VPC and subnets to host the cluster.
+
Public zones are not supported in Route 53 in AWS GovCloud. As a result, clusters must be private when you deploy to an AWS government region.
* Manually create the installation configuration file (`install-config.yaml`).
