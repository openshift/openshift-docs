:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id='creating-a-multicomponent-application-with-odo']
= Creating a multicomponent application with `{odo-title}`
:context: creating-a-multicomponent-application-with-odo

toc::[]

`{odo-title}` allows you to create a multicomponent application, modify it, and link its components in an easy and automated way.

This example describes how to deploy a multicomponent application - a shooter game. The application consists of a front-end Node.js component and a back-end Java component.

.Prerequisites

* `{odo-title}` is installed.
* You have a running cluster. Developers can use link:https://access.redhat.com/documentation/en-us/red_hat_openshift_local/[{openshift-local-productname}] to deploy a local cluster quickly.
* Maven is installed.

include::modules/developer-cli-odo-creating-a-project.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deploying-the-back-end-component.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deploying-the-front-end-component.adoc[leveloffset=+1]

include::modules/developer-cli-odo-linking-both-components.adoc[leveloffset=+1]

include::modules/developer-cli-odo-exposing-the-components-to-the-public.adoc[leveloffset=+1]

include::modules/developer-cli-odo-modifying-the-running-application.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deleting-an-application.adoc[leveloffset=+1]
