// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-config-security_{context}"]
= Security

If your service mesh application is constructed with a complex array of microservices, you can use {SMProductName} to customize the security of the communication between those services. The infrastructure of {product-title} along with the traffic management features of {SMProductShortName} help you manage the complexity of your applications and secure microservices.

.Before you begin

If you have a project, add your project to the xref:../../service_mesh/v2x/installing-ossm.adoc#ossm-member-roll-modify_installing-ossm[`ServiceMeshMemberRoll` resource].

[NOTE]
====
After you add the namespace to the `ServiceMeshMemberRoll`, services or pods in that namespace will not be accessible to callers outside the service mesh.
====
