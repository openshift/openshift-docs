:_mod-docs-content-type: ASSEMBLY
[id="openshift-cli"]
= Creating and building an application using the CLI
include::_attributes/common-attributes.adoc[]
:context: openshift-cli

toc::[]

[id="openshift-cli-before-you-begin"]

== Before you begin

* Review xref:../cli_reference/openshift_cli/getting-started-cli.adoc#cli-about-cli_cli-developer-commands[About the OpenShift CLI].
* You must be able to access a running instance of {product-title}. If you do not have access, contact your cluster administrator.
* You must have the OpenShift CLI (`oc`) xref:../cli_reference/openshift_cli/getting-started-cli.adoc#installing-openshift-cli[downloaded and installed].

include::modules/getting-started-cli-login.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-login[oc login]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-logout[oc logout]

include::modules/getting-started-cli-creating-new-project.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-new-project[oc new-project]

include::modules/getting-started-cli-granting-permissions.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../authentication/understanding-authentication.adoc#understanding-authentication[Understanding authentication]
* xref:../authentication/using-rbac.adoc#authorization-overview_using-rbac[RBAC overview]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-policy-add-role-to-user[oc policy add-role-to-user]

include::modules/getting-started-cli-deploying-first-image.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-new-app[oc new-app]


include::modules/getting-started-cli-creating-route.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-create-route-edge[oc create route edge]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-get[oc get]


include::modules/getting-started-cli-examining-pod.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-describe[oc describe]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-get[oc get]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-label[oc label]
* xref:../cli_reference/openshift_cli/getting-started-cli.adoc#viewing-pods[Viewing pods]
* xref:../cli_reference/openshift_cli/getting-started-cli.adoc#viewing-pod-logs[Viewing pod logs]

include::modules/getting-started-cli-scaling-app.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-scale[oc scale]

include::modules/getting-started-cli-deploying-python-app.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-new-app[oc new-app]

include::modules/getting-started-cli-connecting-a-database.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-new-project[oc new-project]

include::modules/getting-started-cli-creating-secret.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-create-secret-generic[oc create secret generic]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-set-env[oc set env]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-rollout-status[oc rollout status]

include::modules/getting-started-cli-load-data-output.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-exec[oc exec]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-label[oc label]
* xref:../cli_reference/openshift_cli/developer-cli-commands.adoc#oc-get[oc get]
