// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-bundles-config_{context}"]
= Configuring the bundles resolver

You can change the default service account name and the default kind for pulling resources from a Tekton bundle by configuring the bundles resolver.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
+
. In the `TektonConfig` custom resource, edit the `pipeline.bundles-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    bundles-resolver-config:
      default-service-account: pipelines # <1>
      default-kind: task # <2>
----
<1> The default service account name to use for bundle requests.
<2> The default layer kind in the bundle image.
