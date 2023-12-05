// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-cluster-config_{context}"]
= Configuring the cluster resolver

You can change the default kind and namespace for the cluster resolver, or limit the namespaces that the cluster resolver can use.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
+
. In the `TektonConfig` custom resource, edit the `pipeline.cluster-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    cluster-resolver-config:
      default-kind: pipeline # <1>
      default-namespace: namespace1 # <2>
      allowed-namespaces: namespace1, namespace2 # <3>
      blocked-namespaces: namespace3, namespace4 # <4>
----
<1> The default resource kind to fetch, if not specified in parameters.
<2> The default namespace for fetching resources, if not specified in parameters.
<3> A comma-separated list of namespaces that the resolver is allowed to access. If this key is not defined, all namespaces are allowed.
<4> An optional comma-separated list of namespaces which the resolver is blocked from accessing. If this key is not defined, all namespaces are allowed.
