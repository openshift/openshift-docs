:_mod-docs-content-type: ASSEMBLY
[id="osdk-helm-quickstart"]
= Getting started with Operator SDK for Helm-based Operators
include::_attributes/common-attributes.adoc[]
:context: osdk-helm-quickstart

toc::[]

// This assembly is currently excluded from the OSD and ROSA docs, because it requires cluster-admin permissions.

The Operator SDK includes options for generating an Operator project that leverages existing link:https://helm.sh/docs/[Helm] charts to deploy Kubernetes resources as a unified application, without having to write any Go code.

To demonstrate the basics of setting up and running an link:https://helm.sh/docs/[Helm]-based Operator using tools and libraries provided by the Operator SDK, Operator developers can build an example Helm-based Operator for Nginx and deploy it to a cluster.

include::modules/osdk-common-prereqs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../operators/operator_sdk/osdk-installing-cli.adoc#osdk-installing-cli[Installing the Operator SDK CLI]
* xref:../../../cli_reference/openshift_cli/getting-started-cli.adoc#getting-started-cli[Getting started with the OpenShift CLI]

include::modules/osdk-quickstart.adoc[leveloffset=+1]

[id="osdk-helm-quickstart-next-steps"]
== Next steps

* See xref:../../../operators/operator_sdk/helm/osdk-helm-tutorial.adoc#osdk-helm-tutorial[Operator SDK tutorial for Helm-based Operators] for a more in-depth walkthrough on building a Helm-based Operator.
