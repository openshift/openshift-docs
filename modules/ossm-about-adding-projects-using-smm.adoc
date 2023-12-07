// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-mesh.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-about-adding-projects-using-smm_{context}"]
= About adding projects using the ServiceMeshMember resource

A `ServiceMeshMember` resource provides a way to add a project to a service mesh without modifying the `ServiceMeshMemberRoll` resource. To add a project, create a `ServiceMeshMember` resource in the project that you want to add to the service mesh. When the {SMProductShortName} Operator processes the `ServiceMeshMember` object, the project appears in the `status.members` list of the `ServiceMeshMemberRoll` resource. Then, the services that reside in the project are made available to the mesh.

image::ossm-adding-project-using-smm.png[Adding project using `ServiceMeshMember` resource image]

The mesh administrator must grant each mesh user permission to reference the `ServiceMeshControlPlane` resource in the `ServiceMeshMember` resource. With this permission in place, a mesh user can add a project to a mesh even when that user does not have direct access rights for the service mesh project or the `ServiceMeshMemberRoll` resource. For more information, see Creating the {SMProductName} members.