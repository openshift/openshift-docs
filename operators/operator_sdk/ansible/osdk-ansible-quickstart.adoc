:_mod-docs-content-type: ASSEMBLY
[id="osdk-ansible-quickstart"]
= Getting started with Operator SDK for Ansible-based Operators
include::_attributes/common-attributes.adoc[]
:context: osdk-ansible-quickstart

toc::[]

// This assembly is currently excluded from the OSD and ROSA docs, because it requires cluster-admin permissions.

The Operator SDK includes options for generating an Operator project that leverages existing Ansible playbooks and modules to deploy Kubernetes resources as a unified application, without having to write any Go code.

To demonstrate the basics of setting up and running an link:https://docs.ansible.com/ansible/latest/index.html[Ansible]-based Operator using tools and libraries provided by the Operator SDK, Operator developers can build an example Ansible-based Operator for Memcached, a distributed key-value store, and deploy it to a cluster.

include::modules/osdk-common-prereqs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../operators/operator_sdk/osdk-installing-cli.adoc#osdk-installing-cli[Installing the Operator SDK CLI]
* xref:../../../cli_reference/openshift_cli/getting-started-cli.adoc#getting-started-cli[Getting started with the OpenShift CLI]

include::modules/osdk-quickstart.adoc[leveloffset=+1]

[id="osdk-ansible-quickstart-next-steps"]
== Next steps

* See xref:../../../operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc#osdk-ansible-tutorial[Operator SDK tutorial for Ansible-based Operators] for a more in-depth walkthrough on building an Ansible-based Operator.
