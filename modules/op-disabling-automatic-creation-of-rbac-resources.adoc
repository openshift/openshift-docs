// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-disabling-automatic-creation-of-rbac-resources_{context}"]
= Disabling the automatic creation of RBAC resources

The default installation of the {pipelines-title} Operator creates multiple role-based access control (RBAC) resources for all namespaces in the cluster, except the namespaces matching the `^(openshift|kube)-*` regular expression pattern. Among these RBAC resources, the `pipelines-scc-rolebinding` security context constraint (SCC) role binding resource is a potential security issue, because the associated `pipelines-scc` SCC has the `RunAsAny` privilege.

To disable the automatic creation of cluster-wide RBAC resources after the {pipelines-title} Operator is installed, cluster administrators can set the `createRbacResource` parameter to `false` in the cluster-level `TektonConfig` custom resource (CR).

.Example `TektonConfig` CR
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  params:
  - name: createRbacResource
    value: "false"
...
----

[WARNING]
====
As a cluster administrator or an user with appropriate privileges, when you disable the automatic creation of RBAC resources for all namespaces, the default `ClusterTask` resource does not work. For the `ClusterTask` resource to function, you must create the RBAC resources manually for each intended namespace.
====

