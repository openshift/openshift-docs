:_mod-docs-content-type: ASSEMBLY
[id="osdk-ansible-tutorial"]
= Operator SDK tutorial for Ansible-based Operators
include::_attributes/common-attributes.adoc[]
:context: osdk-ansible-tutorial

toc::[]

Operator developers can take advantage of link:https://docs.ansible.com/ansible/latest/index.html[Ansible] support in the Operator SDK to build an example Ansible-based Operator for Memcached, a distributed key-value store, and manage its lifecycle. This tutorial walks through the following process:

* Create a Memcached deployment
* Ensure that the deployment size is the same as specified by the `Memcached` custom resource (CR) spec
* Update the `Memcached` CR status using the status writer with the names of the `memcached` pods

This process is accomplished by using two centerpieces of the Operator Framework:

Operator SDK:: The `operator-sdk` CLI tool and `controller-runtime` library API

Operator Lifecycle Manager (OLM):: Installation, upgrade, and role-based access control (RBAC) of Operators on a cluster

ifndef::openshift-dedicated,openshift-rosa[]
[NOTE]
====
This tutorial goes into greater detail than xref:../../../operators/operator_sdk/ansible/osdk-ansible-quickstart.adoc#osdk-ansible-quickstart[Getting started with Operator SDK for Ansible-based Operators].
====
endif::openshift-dedicated,openshift-rosa[]

// The "Getting started" quickstarts require cluster-admin and are therefore only available in OCP.
ifdef::openshift-dedicated,openshift-rosa[]
[NOTE]
====
This tutorial goes into greater detail than link:https://access.redhat.com/documentation/en-us/openshift_container_platform/4.13/html-single/operators/index#osdk-ansible-quickstart[Getting started with Operator SDK for Ansible-based Operators] in the OpenShift Container Platform documentation.
====
endif::openshift-dedicated,openshift-rosa[]

include::modules/osdk-common-prereqs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../operators/operator_sdk/osdk-installing-cli.adoc#osdk-installing-cli[Installing the Operator SDK CLI]
* xref:../../../cli_reference/openshift_cli/getting-started-cli.adoc#getting-started-cli[Getting started with the OpenShift CLI]

include::modules/osdk-create-project.adoc[leveloffset=+1]
include::modules/osdk-project-file.adoc[leveloffset=+2]

include::modules/osdk-ansible-create-api.adoc[leveloffset=+1]
include::modules/osdk-ansible-modify-manager.adoc[leveloffset=+1]

include::modules/osdk-run-proxy.adoc[leveloffset=+1]

include::modules/osdk-run-operator.adoc[leveloffset=+1]

ifdef::openshift-dedicated,openshift-rosa[]
[role="_additional-resources"]
.Additional resources
* link:https://access.redhat.com/documentation/en-us/openshift_container_platform/4.13/html-single/operators/index#osdk-run-locally_osdk-ansible-tutorial[Running locally outside the cluster] (OpenShift Container Platform documentation)
* link:https://access.redhat.com/documentation/en-us/openshift_container_platform/4.13/html-single/operators/index#osdk-run-deployment_osdk-ansible-tutorial[Running as a deployment on the cluster] (OpenShift Container Platform documentation)
endif::openshift-dedicated,openshift-rosa[]

// In OSD/ROSA, the only applicable option for running the Operator is to bundle and deploy with OLM.
ifndef::openshift-dedicated,openshift-rosa[]
include::modules/osdk-run-locally.adoc[leveloffset=+2]
include::modules/osdk-run-deployment.adoc[leveloffset=+2]
endif::openshift-dedicated,openshift-rosa[]

[id="osdk-bundle-deploy-olm_{context}"]
=== Bundling an Operator and deploying with Operator Lifecycle Manager

include::modules/osdk-bundle-operator.adoc[leveloffset=+3]
include::modules/osdk-deploy-olm.adoc[leveloffset=+3]

include::modules/osdk-create-cr.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="osdk-ansible-tutorial-addtl-resources"]
== Additional resources

* See xref:../../../operators/operator_sdk/ansible/osdk-ansible-project-layout.adoc#osdk-ansible-project-layout[Project layout for Ansible-based Operators] to learn about the directory structures created by the Operator SDK.
ifndef::openshift-dedicated,openshift-rosa[]
* If a xref:../../../networking/enable-cluster-wide-proxy.adoc#enable-cluster-wide-proxy[cluster-wide egress proxy is configured], cluster administrators can xref:../../../operators/admin/olm-configuring-proxy-support.adoc#olm-configuring-proxy-support[override the proxy settings or inject a custom CA certificate] for specific Operators running on Operator Lifecycle Manager (OLM).
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* If a xref:../../../networking/configuring-cluster-wide-proxy.adoc#configuring-a-cluster-wide-proxy[cluster-wide egress proxy is configured], administrators with the `dedicated-admin` role can xref:../../../operators/admin/olm-configuring-proxy-support.adoc#olm-configuring-proxy-support[override the proxy settings or inject a custom CA certificate] for specific Operators running on Operator Lifecycle Manager (OLM).
endif::openshift-dedicated,openshift-rosa[]
