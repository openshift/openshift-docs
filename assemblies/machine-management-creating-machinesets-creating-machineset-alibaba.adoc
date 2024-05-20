:_mod-docs-content-type: ASSEMBLY
[id="creating-machineset-alibaba"]
= Creating a compute machine set on Alibaba Cloud
include::_attributes/common-attributes.adoc[]
:context: creating-machineset-alibaba

toc::[]

You can create a different compute machine set to serve a specific purpose in your {product-title} cluster on Alibaba Cloud. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI
include::modules/machine-user-provisioned-limitations.adoc[leveloffset=+1]

//Sample YAML for a compute machine set custom resource on Alibaba Cloud
include::modules/machineset-yaml-alibaba.adoc[leveloffset=+1]

//Machine set parameters for Alibaba Cloud usage statistics
include::modules/machineset-yaml-alibaba-usage-stats.adoc[leveloffset=+2]

//Creating a compute machine set
include::modules/machineset-creating.adoc[leveloffset=+1]
