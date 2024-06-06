// Module included in the following assemblies:
//
// * authentication/using-rbac.adoc
// * post_installation_configuration/preparing-for-users.adoc

:_mod-docs-content-type: PROCEDURE
ifdef::openshift-enterprise,openshift-webscale,openshift-origin,openshift-dedicated,openshift-rosa[]
[id="creating-local-role_{context}"]
= Creating a local role

You can create a local role for a project and then bind it to a user.

.Procedure

. To create a local role for a project, run the following command:
+
[source,terminal]
----
$ oc create role <name> --verb=<verb> --resource=<resource> -n <project>
----
+
In this command, specify:
+
--
* `<name>`, the local role's name
* `<verb>`, a comma-separated list of the verbs to apply to the role
* `<resource>`, the resources that the role applies to
* `<project>`, the project name
--
+
For example, to create a local role that allows a user to view pods in the
`blue` project, run the following command:
+
[source,terminal]
----
$ oc create role podview --verb=get --resource=pod -n blue
----

. To bind the new role to a user, run the following command:
+
[source,terminal]
----
$ oc adm policy add-role-to-user podview user2 --role-namespace=blue -n blue
----
endif::[]
