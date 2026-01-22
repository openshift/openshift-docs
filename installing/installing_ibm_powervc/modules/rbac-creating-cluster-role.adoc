// Module included in the following assemblies:
//
// * authentication/using-rbac.adoc
// * post_installation_configuration/preparing-for-users.adoc

:_mod-docs-content-type: PROCEDURE
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
[id="creating-cluster-role_{context}"]
= Creating a cluster role

You can create a cluster role.

.Procedure

. To create a cluster role, run the following command:
+
[source,terminal]
----
$ oc create clusterrole <name> --verb=<verb> --resource=<resource>
----
+
In this command, specify:
+
--
* `<name>`, the local role's name
* `<verb>`, a comma-separated list of the verbs to apply to the role
* `<resource>`, the resources that the role applies to
--
+
For example, to create a cluster role that allows a user to view pods, run the
following command:
+
[source,terminal]
----
$ oc create clusterrole podviewonly --verb=get --resource=pod
----
endif::[]
