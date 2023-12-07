:_mod-docs-content-type: ASSEMBLY
[id="osdk-golang-quickstart"]
= Getting started with Operator SDK for Go-based Operators
include::_attributes/common-attributes.adoc[]
:context: osdk-golang-quickstart

toc::[]

// This assembly is currently excluded from the OSD and ROSA docs, because it requires cluster-admin permissions.

To demonstrate the basics of setting up and running a Go-based Operator using tools and libraries provided by the Operator SDK, Operator developers can build an example Go-based Operator for Memcached, a distributed key-value store, and deploy it to a cluster.

include::modules/osdk-common-prereqs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../operators/operator_sdk/osdk-installing-cli.adoc#osdk-installing-cli[Installing the Operator SDK CLI]
* xref:../../../cli_reference/openshift_cli/getting-started-cli.adoc#getting-started-cli[Getting started with the OpenShift CLI]

include::modules/osdk-quickstart.adoc[leveloffset=+1]

[id="osdk-golang-quickstart-next-steps"]
== Next steps

* See xref:../../../operators/operator_sdk/golang/osdk-golang-tutorial.adoc#osdk-golang-tutorial[Operator SDK tutorial for Go-based Operators] for a more in-depth walkthrough on building a Go-based Operator.
