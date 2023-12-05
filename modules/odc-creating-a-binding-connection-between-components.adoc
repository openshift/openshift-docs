// Module included in the following assemblies:
//
// * applications/connecting_applications_to_services/odc-connecting-an-application-to-a-service-using-the-developer-perspective.adoc

:_mod-docs-content-type: PROCEDURE
[id="odc-creating-a-binding-connection-between-components_{context}"]
= Creating a binding connection between components

You can create a binding connection with Operator-backed components, as demonstrated in the following example, which uses a PostgreSQL Database service and a Spring PetClinic sample application. To create a binding connection with a service that the PostgreSQL Database Operator backs, you must first add the Red Hat-provided PostgreSQL Database Operator to the *OperatorHub*, and then install the Operator. The PostreSQL Database Operator then creates and manages the Database resource, which exposes the binding data in secrets, config maps, status, and spec attributes.

.Prerequisites

* You created and deployed a Spring PetClinic sample application in the *Developer* perspective.
* You installed {servicebinding-title} from the *OperatorHub*.
* You installed the *Crunchy Postgres for Kubernetes* Operator from the OperatorHub in the `v5` *Update* channel.
* You created a *PostgresCluster* resource in the *Developer* perspective, which resulted in a Crunchy PostgreSQL database instance with the following components: `hippo-backup`, `hippo-instance`, `hippo-repo-host`, and `hippo-pgbouncer`.

.Procedure

. In the *Developer* perspective, switch to the relevant project, for example, `my-petclinic`.
. In the *Topology* view, hover over the Spring PetClinic sample application to see a dangling arrow on the node.
. Drag and drop the arrow onto the *hippo* database icon in the Postgres Cluster to make a binding connection with the Spring PetClinic sample application.

. In the *Create Service Binding* dialog, keep the default name or add a different name for the service binding, and then click *Create*.
+
.Service Binding dialog
image::odc-sbc-modal.png[]
. Optional: If there is difficulty in making a binding connection using the Topology view, go to *+Add* -> *YAML* -> *Import YAML*.
. Optional: In the YAML editor, add the `ServiceBinding` resource:
+
[source,YAML]
----
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
    name: spring-petclinic-pgcluster
    namespace: my-petclinic
spec:
    services:
    - group: postgres-operator.crunchydata.com
      version: v1beta1
      kind: PostgresCluster
      name: hippo
    application:
      name: spring-petclinic
      group: apps
      version: v1
      resource: deployments
----
+
A service binding request is created and a binding connection is created through a `ServiceBinding` resource. When the database service connection request succeeds, the application is redeployed and the connection is established.
+
.Binding connector
image::odc-binding-connector.png[]
+
[TIP]
====
You can also use the context menu by dragging the dangling arrow to add and create a binding connection to an operator-backed service.

.Context menu to create binding connection
image::odc_context_operator.png[]
====

. In the navigation menu, click *Topology*. The spring-petclinic deployment in the Topology view includes an Open URL link to view its web page.

. Click the *Open URL* link.

You can now view the Spring PetClinic sample application remotely to confirm that the application is now connected to the database service and that the data has been successfully projected to the application from the Crunchy PostgreSQL database service.

The Service Binding Operator has successfully created a working connection between the application and the database service.