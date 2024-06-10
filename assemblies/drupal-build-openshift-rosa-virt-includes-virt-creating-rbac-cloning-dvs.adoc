// Module included in the following assemblies:
//
// * virt/storage/virt-enabling-user-permissions-to-clone-datavolumes.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-rbac-cloning-dvs_{context}"]
= Creating RBAC resources for cloning data volumes

Create a new cluster role that enables permissions for all actions for the `datavolumes` resource.

.Prerequisites

* You must have cluster admin privileges.

.Procedure

. Create a `ClusterRole` manifest:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: <datavolume-cloner> <1>
rules:
- apiGroups: ["cdi.kubevirt.io"]
  resources: ["datavolumes/source"]
  verbs: ["*"]
----
<1> Unique name for the cluster role.

. Create the cluster role in the cluster:
+
[source,terminal]
----
$ oc create -f <datavolume-cloner.yaml> <1>
----
<1> The file name of the `ClusterRole` manifest created in the previous step.

. Create a `RoleBinding` manifest that applies to both the source and destination namespaces and references
the cluster role created in the previous step.
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: <allow-clone-to-user> <1>
  namespace: <Source namespace> <2>
subjects:
- kind: ServiceAccount
  name: default
  namespace: <Destination namespace> <3>
roleRef:
  kind: ClusterRole
  name: datavolume-cloner <4>
  apiGroup: rbac.authorization.k8s.io
----
<1> Unique name for the role binding.
<2> The namespace for the source data volume.
<3> The namespace to which the data volume is cloned.
<4> The name of the cluster role created in the previous step.

. Create the role binding in the cluster:
+
[source,terminal]
----
$ oc create -f <datavolume-cloner.yaml> <1>
----
<1> The file name of the `RoleBinding` manifest created in the previous step.
