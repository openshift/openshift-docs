:_mod-docs-content-type: ASSEMBLY
[id="osdk-java-quickstart"]
= Getting started with Operator SDK for Java-based Operators
include::_attributes/common-attributes.adoc[]
:context: osdk-java-quickstart
:FeatureName: Java-based Operator SDK
include::snippets/technology-preview.adoc[]

// This assembly is not included in the OSD and ROSA docs, because it is Tech Preview. However, once Java-based Operator SDK is GA, this assembly will still need to be excluded from OSD and ROSA if it continues to require cluster-admin permissions.

toc::[]

To demonstrate the basics of setting up and running a Java-based Operator using tools and libraries provided by the Operator SDK, Operator developers can build an example Java-based Operator for Memcached, a distributed key-value store, and deploy it to a cluster.

include::modules/osdk-common-prereqs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../operators/operator_sdk/osdk-installing-cli.adoc#osdk-installing-cli[Installing the Operator SDK CLI]
* xref:../../../cli_reference/openshift_cli/getting-started-cli.adoc#getting-started-cli[Getting started with the OpenShift CLI]

include::modules/osdk-quickstart.adoc[leveloffset=+1]

[id="next-steps_osdk-java-quickstart"]
== Next steps

* See xref:../../../operators/operator_sdk/java/osdk-java-tutorial.adoc#osdk-java-tutorial[Operator SDK tutorial for Java-based Operators] for a more in-depth walkthrough on building a Java-based Operator.
