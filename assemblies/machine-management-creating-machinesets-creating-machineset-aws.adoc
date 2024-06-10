:_mod-docs-content-type: ASSEMBLY
[id="creating-machineset-aws"]
= Creating a compute machine set on AWS
include::_attributes/common-attributes.adoc[]
:context: creating-machineset-aws

toc::[]

You can create a different compute machine set to serve a specific purpose in your {product-title} cluster on Amazon Web Services (AWS). For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI
include::modules/machine-user-provisioned-limitations.adoc[leveloffset=+1]

//Sample YAML for a compute machine set custom resource on AWS
include::modules/machineset-yaml-aws.adoc[leveloffset=+1]

//Creating a compute machine set
include::modules/machineset-creating.adoc[leveloffset=+1]

//Assigning machines to placement groups by using machine sets
include::modules/machineset-aws-existing-placement-group.adoc[leveloffset=+1]

//Machine sets that enable the Amazon EC2 Instance Metadata Service
include::modules/machineset-imds-options.adoc[leveloffset=+1]

//Creating machines that use the Amazon EC2 Instance Metadata Service
include::modules/machineset-creating-imds-options.adoc[leveloffset=+2]

//Machine sets that deploy machines as Dedicated Instances
include::modules/machineset-dedicated-instances.adoc[leveloffset=+1]

//Creating Dedicated Instances by using machine sets
include::modules/machineset-creating-dedicated-instances.adoc[leveloffset=+2]

//Machine sets that deploy machines as Spot Instances
include::modules/machineset-non-guaranteed-instance.adoc[leveloffset=+1]

//Creating Spot Instances by using compute machine sets
include::modules/machineset-creating-non-guaranteed-instances.adoc[leveloffset=+2]

//Adding a GPU node to a machine set (stesmith)
include::modules/nvidia-gpu-aws-adding-a-gpu-node.adoc[leveloffset=+1]

//Deploying the Node Feature Discovery Operator (stesmith)
include::modules/nvidia-gpu-aws-deploying-the-node-feature-discovery-operator.adoc[leveloffset=+1]
