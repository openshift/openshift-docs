:_mod-docs-content-type: ASSEMBLY
[id=creating-an-application-with-a-database]
= Creating an application with a database
include::_attributes/common-attributes.adoc[]
:context: creating-an-application-with-a-database

toc::[]

This example describes how to deploy and connect a database to a front-end application.

.Prerequisites

* `{odo-title}` is installed.
* `oc` client is installed.
* You have a running cluster. Developers can use link:https://access.redhat.com/documentation/en-us/red_hat_openshift_local/[{openshift-local-productname}] to deploy a local cluster quickly.
* The Service Catalog is installed and enabled on your cluster.
+
[NOTE]
====
Service Catalog is deprecated on {product-title} 4 and later.
====

include::modules/developer-cli-odo-creating-a-project.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deploying-the-front-end-component.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deploying-a-database-in-interactive-mode.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deploying-a-database-manually.adoc[leveloffset=+1]

include::modules/developer-cli-odo-connecting-the-database.adoc[leveloffset=+1]
