:_mod-docs-content-type: ASSEMBLY
[id="serverless-functions-getting-started"]
= Getting started with functions
:context: serverless-functions-getting-started
include::_attributes/common-attributes.adoc[]

toc::[]

Function lifecycle management includes creating, building, and deploying a function. Optionally, you can also test a deployed function by invoking it. You can do all of these operations on {ServerlessProductName} using the `kn func` tool.

[id="prerequisites_serverless-functions-getting-started"]
== Prerequisites

Before you can complete the following procedures, you must ensure that you have completed all of the prerequisite tasks in xref:../../serverless/functions/serverless-functions-setup.adoc#serverless-functions-setup[Setting up {FunctionsProductName}].

include::modules/serverless-create-func-kn.adoc[leveloffset=+1]
include::modules/serverless-kn-func-run.adoc[leveloffset=+1]
include::modules/serverless-build-func-kn.adoc[leveloffset=+1]
include::modules/serverless-deploy-func-kn.adoc[leveloffset=+1]
include::modules/serverless-kn-func-invoke.adoc[leveloffset=+1]
include::modules/serverless-kn-func-delete.adoc[leveloffset=+1]

ifdef::openshift-enterprise[]
[id="additional-resources_serverless-functions-getting-started"]
[role="_additional-resources"]
== Additional resources
* xref:../../registry/securing-exposing-registry.adoc#securing-exposing-registry[Exposing a default registry manually]
* link:https://plugins.jetbrains.com/plugin/16476-knative\--serverless-functions-by-red-hat[Marketplace page for the Intellij Knative plugin]
* link:https://marketplace.visualstudio.com/items?itemName=redhat.vscode-knative&utm_source=VSCode.pro&utm_campaign=AhmadAwais[Marketplace page for the Visual Studio Code Knative plugin]
* xref:../../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-creating-applications-using-the-developer-perspective[Creating applications using the Developer perspective]
// This Additional resource applies only to OCP, but not to OSD nor ROSA.
endif::[]

[id="next-steps_serverless-functions-getting-started"]
== Next steps

* See xref:../../serverless/functions/serverless-functions-eventing.adoc#serverless-functions-eventing[Using functions with Knative Eventing]
