// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-tekton-chains-using-pipelines-operator_{context}"]
= Installing {tekton-chains} using the {pipelines-title} Operator

Cluster administrators can use the `TektonChain` custom resource (CR) to install and manage {tekton-chains}.

[NOTE]
====
{tekton-chains} is an optional component of {pipelines-title}. Currently, you cannot install it using the `TektonConfig` CR.
====

[discrete]
.Prerequisites
* Ensure that the {pipelines-title} Operator is installed in the `openshift-pipelines` namespace on your cluster.

[discrete]
.Procedure

. Create the `TektonChain` CR for your {product-title} cluster.
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonChain
metadata:
  name: chain
spec:
  targetNamespace: openshift-pipelines
----

. Apply the `TektonChain` CR.
+
[source,terminal]
----
$ oc apply -f TektonChain.yaml <1>
----
+
<1> Substitute with the file name of the `TektonChain` CR.

. Check the status of the installation.
+
[source,terminal]
----
$ oc get tektonchains.operator.tekton.dev
----


