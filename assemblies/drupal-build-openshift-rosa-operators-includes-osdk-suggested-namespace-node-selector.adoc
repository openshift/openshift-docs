// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-suggested-namespace-default-node_{context}"]
= Setting a suggested namespace with default node selector

Some Operators expect to run only on control plane nodes, which can be done by setting a `nodeSelector` in the `Pod` spec by the Operator itself.

To avoid getting duplicated and potentially conflicting cluster-wide default `nodeSelector`, you can set a default node selector on the namespace where the Operator runs. The default node selector will take precedence over the cluster default so the cluster default will not be applied to the pods in the Operators namespace.

When adding the Operator to a cluster using OperatorHub, the web console auto-populates the suggested namespace for the
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrator
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
installer
endif::openshift-dedicated,openshift-rosa[]
during the installation process. The suggested namespace is created using the namespace manifest in YAML which is included in the cluster service version (CSV).

.Procedure

* In your CSV, set the `operatorframework.io/suggested-namespace-template` with a manifest for a `Namespace` object. The following sample is a manifest for an example `Namespace` with the namespace default node selector specified:
+
[source,yaml]
----
metadata:
  annotations:
    operatorframework.io/suggested-namespace-template: <1>
      {
        "apiVersion": "v1",
        "kind": "Namespace",
        "metadata": {
          "name": "vertical-pod-autoscaler-suggested-template",
          "annotations": {
            "openshift.io/node-selector": ""
          }
        }
      }
----
<1> Set your suggested namespace.
+
[NOTE]
====
If both `suggested-namespace` and `suggested-namespace-template` annotations are present in the CSV, `suggested-namespace-template` should take precedence.
====