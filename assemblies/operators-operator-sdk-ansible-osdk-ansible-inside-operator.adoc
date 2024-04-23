:_mod-docs-content-type: ASSEMBLY
[id="osdk-ansible-inside-operator"]
= Using Ansible inside an Operator
include::_attributes/common-attributes.adoc[]
:context: osdk-ansible-inside-operator

toc::[]

After you are familiar with xref:../../../operators/operator_sdk/ansible/osdk-ansible-k8s-collection.adoc#osdk-ansible-k8s-collection[using the Kubernetes Collection for Ansible locally], you can trigger the same Ansible logic inside of an Operator when a custom resource (CR) changes. This example maps an Ansible role to a specific Kubernetes resource that the Operator watches. This mapping is done in the `watches.yaml` file.

include::modules/osdk-ansible-custom-resource-files.adoc[leveloffset=+1]
include::modules/osdk-ansible-inside-operator-local.adoc[leveloffset=+1]
include::modules/osdk-run-deployment.adoc[leveloffset=+1]
include::modules/osdk-ansible-inside-operator-logs.adoc[leveloffset=+1]
include::modules/osdk-ansible-inside-operator-logs-view.adoc[leveloffset=+2]
include::modules/osdk-ansible-inside-operator-logs-full-result.adoc[leveloffset=+2]
include::modules/osdk-ansible-inside-operator-logs-verbose.adoc[leveloffset=+2]
