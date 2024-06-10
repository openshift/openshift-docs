// Module included in the following assemblies:
//
// * authentication/using-rbac.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="local-role-binding-commands_{context}"]
= Local role binding commands

When you manage a user or group's associated roles for local role bindings using the
following operations, a project may be specified with the `-n` flag. If it is
not specified, then the current project is used.

You can use the following commands for local RBAC management.

.Local role binding operations
[options="header"]
|===

|Command |Description

|`$ oc adm policy who-can _<verb>_ _<resource>_`
|Indicates which users can perform an action on a resource.

|`$ oc adm policy add-role-to-user _<role>_ _<username>_`
|Binds a specified role to specified users in the current project.

|`$ oc adm policy remove-role-from-user _<role>_ _<username>_`
|Removes a given role from specified users in the current project.

|`$ oc adm policy remove-user _<username>_`
|Removes specified users and all of their roles in the current project.

|`$ oc adm policy add-role-to-group _<role>_ _<groupname>_`
|Binds a given role to specified groups in the current project.

|`$ oc adm policy remove-role-from-group _<role>_ _<groupname>_`
|Removes a given role from specified groups in the current project.

|`$ oc adm policy remove-group _<groupname>_`
|Removes specified groups and all of their roles in the current project.

|===
