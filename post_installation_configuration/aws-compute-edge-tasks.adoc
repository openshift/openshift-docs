:_mod-docs-content-type: ASSEMBLY
[id="aws-compute-edge-tasks"]
= AWS Local Zone tasks
include::_attributes/common-attributes.adoc[]
:context: aws-compute-edge-tasks

toc::[]

After installing {product-title} on Amazon Web Services (AWS), you can further configure AWS Local Zones and an edge compute pool, so that you can expand and customize your cluster to meet your needs.

// Extend existing clusters to use AWS Local Zones
include::modules/post-install-edge-aws-extend-cluster.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* For more information about AWS Local Zones, the supported instances types, and services, see link:https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/[AWS Local Zones features] in the AWS documentation.


// About the Edge Compute Pool
include::modules/edge-machine-pools-aws-local-zones.adoc[leveloffset=+2]

[id="post-install-extend-existing-to-local-zones-mtu"]
=== Changing the Cluster Network MTU to support AWS Local Zones subnets

You might need to change the maximum transmission unit (MTU) value for the cluster
network so that your cluster infrastructure can support Local Zone subnets.

// About the cluster MTU
include::modules/nw-cluster-mtu-change-about.adoc[leveloffset=+3]

// Changing the cluster MTU
include::modules/nw-cluster-mtu-change.adoc[leveloffset=+3]

// Opting in to AWS Local Zones
include::modules/installation-aws-add-local-zone-locations.adoc[leveloffset=+2]

// Extend existing clusters to use AWS Local Zones
include::modules/post-install-existing-local-zone-subnet.adoc[leveloffset=+2]

// Creating a subnet in AWS Local Zones
include::modules/installation-creating-aws-subnet-localzone.adoc[leveloffset=+3]

// CloudFormation template for the subnet that uses AWS Local Zones
include::modules/installation-cloudformation-subnet-localzone.adoc[leveloffset=+3]

// Creating a machine set manifest for AWS Local Zones node
include::modules/post-install-edge-aws-extend-machineset.adoc[leveloffset=+2]

// Sample YAML for a compute machine set custom resource on AWS
include::modules/machineset-yaml-aws.adoc[leveloffset=+3]

// Creating a compute machine set
include::modules/machineset-creating.adoc[leveloffset=+3]

[role="_additional-resources"]
.Additional resources

* xref:../installing/installing_aws/installing-aws-localzone.adoc#installing-aws-localzone[Installing a cluster on AWS with worker nodes on AWS Local Zones]

// Creating user workloads in AWS Local Zones
include::modules/installation-extend-edge-nodes-aws-local-zones.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../installing/installing_aws/installing-aws-localzone.adoc#installing-aws-localzone[Installing a cluster on AWS with worker nodes on AWS Local Zones]

* xref:../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations[Understanding taints and tolerations]

.Next steps

* Optional: Use the AWS Load Balancer (ALB) Operator to expose a pod from a targeted edge worker node to services that run inside of a Local Zone subnet from a public network.
See xref:../networking/aws_load_balancer_operator/install-aws-load-balancer-operator.adoc#nw-installing-aws-load-balancer-operator_aws-load-balancer-operator[Installing the AWS Load Balancer Operator].