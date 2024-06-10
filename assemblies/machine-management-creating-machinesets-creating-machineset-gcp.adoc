:_mod-docs-content-type: ASSEMBLY
[id="creating-machineset-gcp"]
= Creating a compute machine set on GCP
include::_attributes/common-attributes.adoc[]
:context: creating-machineset-gcp

toc::[]

You can create a different compute machine set to serve a specific purpose in your {product-title} cluster on Google Cloud Platform (GCP). For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI
include::modules/machine-user-provisioned-limitations.adoc[leveloffset=+1]

//Sample YAML for a compute machine set custom resource on GCP
include::modules/machineset-yaml-gcp.adoc[leveloffset=+1]

//Creating a compute machine set
include::modules/machineset-creating.adoc[leveloffset=+1]

//Configuring persistent disk types by using compute machine sets
include::modules/machineset-gcp-pd-disk-types.adoc[leveloffset=+1]

//Configuring Confidential VM by using machine sets
include::modules/machineset-gcp-confidential-vm.adoc[leveloffset=+1]

//Machine sets that deploy machines as preemptible VM instances
include::modules/machineset-non-guaranteed-instance.adoc[leveloffset=+1]

//Creating preemptible VM instances by using compute machine sets
include::modules/machineset-creating-non-guaranteed-instances.adoc[leveloffset=+2]

//Configuring Shielded VM options by using machine sets
include::modules/machineset-gcp-shielded-vms.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* link:https://cloud.google.com/compute/shielded-vm/docs/shielded-vm[What is Shielded VM?]
** link:https://cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot[Secure Boot]
** link:https://cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm[Virtual Trusted Platform Module (vTPM)]
** link:https://cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring[Integrity monitoring]

//Enabling customer-managed encryption keys for a compute machine set
include::modules/machineset-gcp-enabling-customer-managed-encryption.adoc[leveloffset=+1]

//Enabling GPU support for a compute machine set
include::modules/machineset-gcp-enabling-gpu-support.adoc[leveloffset=+1]

//Adding a GPU node to a machine set (stesmith)
include::modules/nvidia-gpu-gcp-adding-a-gpu-node.adoc[leveloffset=+1]

//Deploying the Node Feature Discovery Operator (stesmith)
include::modules/nvidia-gpu-aws-deploying-the-node-feature-discovery-operator.adoc[leveloffset=+1]
