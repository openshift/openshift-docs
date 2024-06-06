// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

:_mod-docs-content-type: PROCEDURE
[id="service-accounts-managing_{context}"]
= Creating service accounts

You can create a service account in a project and grant it permissions by
binding it to a role.

.Procedure

. Optional: To view the service accounts in the current project:
+
[source,terminal]
----
$ oc get sa
----
+
.Example output
[source,terminal]
----
NAME       SECRETS   AGE
builder    2         2d
default    2         2d
deployer   2         2d
----

. To create a new service account in the current project:
+
[source,terminal]
----
$ oc create sa <service_account_name> <1>
----
<1> To create a service account in a different project, specify `-n <project_name>`.
+
.Example output
[source,terminal]
----
serviceaccount "robot" created
----
+
[TIP]
====
You can alternatively apply the following YAML to create the service account:

[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <service_account_name>
  namespace: <current_project>
----
====

. Optional: View the secrets for the service account:
+
[source,terminal]
----
$ oc describe sa robot
----
+
.Example output
[source,terminal]
----
Name:                robot
Namespace:           project1
Labels:	             <none>
Annotations:	     <none>
Image pull secrets:  robot-dockercfg-qzbhb
Mountable secrets:   robot-dockercfg-qzbhb
Tokens:              robot-token-f4khf
Events:              <none>
----
