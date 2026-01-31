// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-mesh.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-about-adding-projects-using-smmr_{context}"]
= About adding projects using the ServiceMeshMemberRoll resource

Using the `ServiceMeshMemberRoll` resource is the simplest way to add a project to a service mesh. To add a project, specify the project name in the `spec.members` field of the `ServiceMeshMemberRoll` resource. The `ServiceMeshMemberRoll` resource specifies which projects are controlled by the `ServiceMeshControlPlane` resource.

image::ossm-adding-project-using-smmr.png[Adding project using `ServiceMeshMemberRoll` resource image]

[NOTE]
====
Adding projects using this method requires the user to have the `update servicemeshmemberrolls` and the `update pods` privileges in the project that is being added.
====

* If you already have an application, workload, or service to add to the service mesh, see the following:
** Adding or removing projects from the mesh using the `ServiceMeshMemberRoll` resource with the web console
** Adding or removing projects from the mesh using the `ServiceMeshMemberRoll` resource with the CLI

* Alternatively, to install a sample application called Bookinfo and add it to a `ServiceMeshMemberRoll` resource, see the Bookinfo example application tutorial.
