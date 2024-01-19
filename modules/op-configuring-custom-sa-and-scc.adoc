// Module included in the following assemblies:
//
// * cicd/pipelines/unprivileged-building-of-container-images-using-buildah.adoc
:_mod-docs-content-type: PROCEDURE

[id="configuring-custom-sa-and-scc_{context}"]
= Configuring custom service account and security context constraint

The default `pipeline` SA allows using a user id outside of the namespace range. To reduce dependency on the default SA, you can define a custom SA and SCC with necessary cluster role and role bindings for the `build` user with user id `1000`.

[IMPORTANT]
====
At this time, enabling the `allowPrivilegeEscalation` setting is required for Buildah to run successfully in the container. With this setting, Buildah can leverage `SETUID` and `SETGID` capabilities when running as a non-root user.
====

.Procedure

* Create a custom SA and SCC with necessary cluster role and role bindings.
+
.Example: Custom SA and SCC for used id `1000`
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: pipelines-sa-userid-1000 # <1>
---
kind: SecurityContextConstraints
metadata:
  annotations:
  name: pipelines-scc-userid-1000 # <2>
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: true # <3>
allowPrivilegedContainer: false
allowedCapabilities: null
apiVersion: security.openshift.io/v1
defaultAddCapabilities: null
fsGroup:
  type: MustRunAs
groups:
- system:cluster-admins
priority: 10
readOnlyRootFilesystem: false
requiredDropCapabilities:
- MKNOD
- KILL
runAsUser: # <4>
  type: MustRunAs
  uid: 1000
seLinuxContext:
  type: MustRunAs
supplementalGroups:
  type: RunAsAny
users: []
volumes:
- configMap
- downwardAPI
- emptyDir
- persistentVolumeClaim
- projected
- secret
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pipelines-scc-userid-1000-clusterrole # <5>
rules:
- apiGroups:
  - security.openshift.io
  resourceNames:
  - pipelines-scc-userid-1000
  resources:
  - securitycontextconstraints
  verbs:
  - use
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pipelines-scc-userid-1000-rolebinding # <6>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: pipelines-scc-userid-1000-clusterrole
subjects:
- kind: ServiceAccount
  name: pipelines-sa-userid-1000
----

<1> Define a custom SA.

<2> Define a custom SCC created based on restricted privileges, with modified `runAsUser` field.

<3> At this time, enabling the `allowPrivilegeEscalation` setting is required for Buildah to run successfully in the container. With this setting, Buildah can leverage `SETUID` and `SETGID` capabilities when running as a non-root user.

<4> Restrict any pod that gets attached with the custom SCC through the custom SA to run as user id `1000`.

<5> Define a cluster role that uses the custom SCC.

<6> Bind the cluster role that uses the custom SCC to the custom SA.
