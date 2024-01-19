:_mod-docs-content-type: ASSEMBLY
[id="cli-osdk-install"]
= Installing the Operator SDK CLI
include::_attributes/common-attributes.adoc[]
:context: cli-osdk-install

toc::[]

The Operator SDK provides a command-line interface (CLI) tool that Operator developers can use to build, test, and deploy an Operator. You can install the Operator SDK CLI on your workstation so that you are prepared to start authoring your own Operators.

Operator authors with cluster administrator access to a Kubernetes-based cluster, such as {product-title}, can use the Operator SDK CLI to develop their own Operators based on Go, Ansible, Java, or Helm. link:https://kubebuilder.io/[Kubebuilder] is embedded into the Operator SDK as the scaffolding solution for Go-based Operators, which means existing Kubebuilder projects can be used as is with the Operator SDK and continue to work.
ifndef::openshift-rosa,openshift-dedicated[]
See xref:../../operators/operator_sdk/osdk-about.adoc#osdk-about[Developing Operators] for full documentation on the Operator SDK.

[NOTE]
====
{product-title} {product-version} supports Operator SDK {osdk_ver}.
====
endif::openshift-rosa,openshift-dedicated[]

include::modules/osdk-installing-cli-linux-macos.adoc[leveloffset=+1]

include::modules/osdk-installing-cli-macos.adoc[leveloffset=+1]