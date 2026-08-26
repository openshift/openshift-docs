:_mod-docs-content-type: PROCEDURE
[id='op-running-pipeline-and-task-run-pods-with-privileged-security-context']
= Running pipeline run and task run pods with privileged security context
:context: op-running-pipeline-and-task-run-pods-with-privileged-security-context


.Procedure

To run a pod (resulting from pipeline run or task run) with the `privileged` security context, do the following modifications:

* Configure the associated user account or service account to have an explicit SCC. You can perform the configuration using any of the following methods:
** Run the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user <scc-name> -z <service-account-name>
----
** Alternatively, modify the YAML files for `RoleBinding`, and `Role` or `ClusterRole`:

+
.Example `RoleBinding` object
[source,yaml,subs="attributes+"]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: service-account-name <1>
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: pipelines-scc-clusterrole <2>
subjects:
- kind: ServiceAccount
  name: pipeline
  namespace: default
----
<1> Substitute with an appropriate service account name.
<2> Substitute with an appropriate cluster role based on the role binding you use.

+
.Example `ClusterRole` object
[source,yaml,subs="attributes+"]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pipelines-scc-clusterrole <1>
rules:
- apiGroups:
  - security.openshift.io
  resourceNames:
  - nonroot
  resources:
  - securitycontextconstraints
  verbs:
  - use
----
<1> Substitute with an appropriate cluster role based on the role binding you use.

+
[NOTE]
====
As a best practice, create a copy of the default YAML files and make changes in the duplicate file.
====
+

* If you do not use the `vfs` storage driver, configure the service account associated with the task run or the pipeline run to have a privileged SCC, and set the security context as `privileged: true`.
