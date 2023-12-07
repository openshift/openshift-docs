:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-osus"]
= Uninstalling the OpenShift Update Service from a cluster
include::_attributes/common-attributes.adoc[]
:context: uninstalling-osus

toc::[]

////
WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.
////

To remove a local copy of the OpenShift Update Service (OSUS) from your cluster, you must first delete the OSUS application and then uninstall the OSUS Operator.

[id="update-service-delete-service"]
== Deleting an OpenShift Update Service application

You can delete an OpenShift Update Service application by using the {product-title} web console or CLI.

// Deleting an OpenShift Update Service application by using the web console
include::modules/update-service-delete-service-web-console.adoc[leveloffset=+2]

// Deleting an OpenShift Update Service application by using the CLI
include::modules/update-service-delete-service-cli.adoc[leveloffset=+2]

[id="update-service-uninstall"]
== Uninstalling the OpenShift Update Service Operator

You can uninstall the OpenShift Update Service Operator by using the {product-title} web console or CLI.

// Uninstalling the OpenShift Update Service Operator by using the web console
include::modules/update-service-uninstall-web-console.adoc[leveloffset=+2]

// Uninstalling the OpenShift Update Service Operator by using the CLI
include::modules/update-service-uninstall-cli.adoc[leveloffset=+2]
