:_mod-docs-content-type: PROCEDURE
[id="odc-using-the-developer-catalog-to-add-services-or-components_{context}"]
= Using the Developer Catalog to add services or components to your application

You use the Developer Catalog to deploy applications and services based on Operator backed services such as Databases, Builder Images, and Helm Charts. The Developer Catalog contains a collection of application components, services, event sources, or source-to-image builders that you can add to your project. Cluster administrators can customize the content made available in the catalog.

.Procedure

. In the *Developer* perspective, navigate to the *+Add* view and from the *Developer Catalog* tile, click *All Services* to view all the available services in the *Developer Catalog*.
. Under *All Services*, select the kind of service or the component you need to add to your project. For this example, select *Databases* to list all the database services and then click *MariaDB* to see the details for the service.
+
. Click *Instantiate Template* to see an automatically populated template with details for the *MariaDB* service, and then click *Create* to create and view the MariaDB service in the *Topology* view.
+
.MariaDB in Topology
image::odc_devcatalog_toplogy.png[]
