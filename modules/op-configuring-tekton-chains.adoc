// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: CONCEPT
[id="configuring-tekton-chains_{context}"]
= Configuring {tekton-chains}

The {pipelines-title} Operator installs {tekton-chains} by default. You can configure {tekton-chains} by modifying the `TektonConfig` custom resource; the Operator automatically applies the changes that you make in this custom resource.

To edit the custom resource, use the following command:

[source,terminal]
----
$ oc edit TektonConfig config
----

The custom resource includes a `chain:` array. You can add any supported configuration parameters to this array, as shown in the following example:

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  addon: {}
  chain:
    artifacts.taskrun.format: tekton
  config: {}
----
