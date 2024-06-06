// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-managing-vms-openshift-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deploying-ssp_{context}"]
= Deploying the Scheduling, Scale, and Performance (SSP) resources

The SSP Operator example Tekton Tasks and Pipelines are not deployed by default when you install {VirtProductName}. To deploy the SSP Operator's Tekton resources, enable the `deployTektonTaskResources` feature gate in the `HyperConverged` custom resource (CR).

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Set the `spec.featureGates.deployTektonTaskResources` field to `true`.
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: kubevirt-hyperconverged
spec:
  tektonPipelinesNamespace: <user_namespace> <1>
  featureGates:
    deployTektonTaskResources: true <2>
# ...
----
<1> The namespace where the pipelines are to be run.
<2> The feature gate to be enabled to deploy Tekton resources by SSP operator.
+
[NOTE]
====
The tasks and example pipelines remain available even if you disable the feature gate later.
====

. Save your changes and exit the editor.
