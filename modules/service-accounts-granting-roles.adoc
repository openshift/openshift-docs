// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-granting-roles_{context}"]
= Examples of granting roles to service accounts

You can grant roles to service accounts in the same way that you grant roles
to a regular user account.

* You can modify the service accounts for the current project. For example, to add
the `view` role to the `robot` service account in the `top-secret` project:
+
[source,terminal]
----
$ oc policy add-role-to-user view system:serviceaccount:top-secret:robot
----
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: view
  namespace: top-secret
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: view
subjects:
- kind: ServiceAccount
  name: robot
  namespace: top-secret
----
====

* You can also grant access to a specific service account in a project. For
example, from the project to which the service account belongs, use
the `-z` flag and specify the `<service_account_name>`

+
[source,terminal]
----
$ oc policy add-role-to-user <role_name> -z <service_account_name>
----
+
[IMPORTANT]
====
If you want to grant access to a specific service account in a project, use the
`-z` flag. Using this flag helps prevent typos and ensures that access
is granted to only the specified service account.
====
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: <rolebinding_name>
  namespace: <current_project_name>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: <role_name>
subjects:
- kind: ServiceAccount
  name: <service_account_name>
  namespace: <current_project_name>
----
====

* To modify a different namespace, you can use the `-n` option to indicate the
project namespace it applies to, as shown in the following examples.

** For example, to allow all service accounts in all projects to view resources in
the `my-project` project:
+
[source,terminal]
----
$ oc policy add-role-to-group view system:serviceaccounts -n my-project
----
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: view
  namespace: my-project
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: view
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:serviceaccounts
----
====

** To allow all service accounts in the `managers` project to edit resources in the
`my-project` project:
+
[source,terminal]
----
$ oc policy add-role-to-group edit system:serviceaccounts:managers -n my-project
----
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: edit
  namespace: my-project
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: edit
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:serviceaccounts:managers
----
====
