// Module included in the following assemblies:
//
// * applications/projects/configuring-project-creation.adoc

:_mod-docs-content-type: CONCEPT
[id="about-project-creation_{context}"]
= About project creation

The {product-title} API server automatically provisions new projects based on
the project template that is identified by the `projectRequestTemplate`
parameter in the cluster's project configuration resource. If the parameter is
not defined, the API server creates a default template that creates a project
with the requested name, and assigns the requesting user to the `admin` role for
that project.

When a project request is submitted, the API substitutes the following
parameters into the template:

.Default project template parameters
[cols="4,8",options="header"]
|===
|Parameter |Description

|`PROJECT_NAME`
|The name of the project. Required.

|`PROJECT_DISPLAYNAME`
|The display name of the project. May be empty.

|`PROJECT_DESCRIPTION`
|The description of the project. May be empty.

|`PROJECT_ADMIN_USER`
|The user name of the administrating user.

|`PROJECT_REQUESTING_USER`
|The user name of the requesting user.
|===

Access to the API is granted to developers with the `self-provisioner` role and
the `self-provisioners` cluster role binding. This role is available to all
authenticated developers by default.
