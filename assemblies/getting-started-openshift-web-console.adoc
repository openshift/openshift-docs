:_mod-docs-content-type: ASSEMBLY
[id="openshift-web-console"]
= Creating and building an application using the web console
include::_attributes/common-attributes.adoc[]
:context: openshift-web-console

toc::[]

[id="openshift-web-console-before-you-begin"]

== Before you begin
* Review xref:../web_console/web-console.adoc#web-console-overview[Accessing the web console].
* You must be able to access a running instance of {product-title}. If you do not have access, contact your cluster administrator.

include::modules/getting-started-web-console-login.adoc[leveloffset=+1]

include::modules/getting-started-web-console-creating-new-project.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../authentication/using-rbac.adoc#default-roles_using-rbac[Default cluster roles]
* xref:../applications/projects/working-with-projects.adoc#viewing-a-project-using-the-web-console_projects[Viewing a project using the web console]
* xref:../applications/projects/working-with-projects.adoc#odc-providing-project-permissions-using-developer-perspective_projects[Providing access permissions to your project using the Developer perspective]
* xref:../applications/projects/working-with-projects.adoc#deleting-a-project-using-the-web-console_projects[Deleting a project using the web console]

include::modules/getting-started-web-console-granting-permissions.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../authentication/understanding-authentication.adoc#rbac-users_understanding-authentication[Understanding authentication]
* xref:../authentication/using-rbac.adoc#authorization-overview_using-rbac[RBAC overview]

include::modules/getting-started-web-console-deploying-first-image.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc[Creating applications using the Developer perspective]
* xref:../applications/projects/working-with-projects.adoc#viewing-a-project-using-the-web-console_projects[Viewing a project using the web console]
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-viewing-application-topology_viewing-application-composition-using-topology-view[Viewing the topology of your application]
* xref:../applications/projects/working-with-projects.adoc#deleting-a-project-using-the-web-console_projects[Deleting a project using the web console]

include::modules/getting-started-web-console-examining-pod.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-interacting-with-applications-and-components_viewing-application-composition-using-topology-view[Interacting with applications and components]
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-scaling-application-pods-and-checking-builds-and-routes_viewing-application-composition-using-topology-view[Scaling application pods and checking builds and routes]
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-labels-and-annotations-used-for-topology-view_viewing-application-composition-using-topology-view[Labels and annotations used for the Topology view]

include::modules/getting-started-web-console-scaling-app.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../scalability_and_performance/recommended-performance-scale-practices/recommended-control-plane-practices.adoc#recommended-scale-practices_cluster-scaling[Recommended practices for scaling the cluster]
* xref:../nodes/pods/nodes-pods-autoscaling.adoc#nodes-pods-autoscaling-about_nodes-pods-autoscaling[Understanding horizontal pod autoscalers]
* xref:../nodes/pods/nodes-pods-vertical-autoscaler.adoc#nodes-pods-vertical-autoscaler-about_nodes-pods-vertical-autoscaler[About the Vertical Pod Autoscaler Operator]

include::modules/getting-started-web-console-deploying-python-app.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-adding-services-to-your-application_viewing-application-composition-using-topology-view[Adding services to your application]
* xref:../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-importing-codebase-from-git-to-create-application_odc-creating-applications-using-developer-perspective[Importing a codebase from Git to create an application]
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-viewing-application-topology_viewing-application-composition-using-topology-view[Viewing the topology of your application]
* xref:../applications/projects/working-with-projects.adoc#odc-providing-project-permissions-using-developer-perspective_projects[Providing access permissions to your project using the Developer perspective]
* xref:../applications/projects/working-with-projects.adoc#deleting-a-project-using-the-web-console_projects[Deleting a project using the web console]

include::modules/getting-started-web-console-connecting-a-database.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-adding-services-to-your-application_viewing-application-composition-using-topology-view[Adding services to your application]
* xref:../applications/projects/working-with-projects.adoc#viewing-a-project-using-the-web-console_projects[Viewing a project using the web console]
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-viewing-application-topology_viewing-application-composition-using-topology-view[Viewing the topology of your application]
* xref:../applications/projects/working-with-projects.adoc#odc-providing-project-permissions-using-developer-perspective_projects[Providing access permissions to your project using the Developer perspective]
* xref:../applications/projects/working-with-projects.adoc#deleting-a-project-using-the-web-console_projects[Deleting a project using the web console]

include::modules/getting-started-web-console-creating-secret.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../nodes/pods/nodes-pods-secrets.adoc#nodes-pods-secrets-about_nodes-pods-secrets[Understanding secrets]

include::modules/getting-started-web-console-load-data-output.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../applications/projects/working-with-projects.adoc#odc-providing-project-permissions-using-developer-perspective_projects[Providing access permissions to your project using the Developer perspective]
* xref:../applications/odc-viewing-application-composition-using-topology-view.adoc#odc-labels-and-annotations-used-for-topology-view_viewing-application-composition-using-topology-view[Labels and annotations used for the Topology view]
