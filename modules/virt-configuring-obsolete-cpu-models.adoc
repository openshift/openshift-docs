// Module included in the following assemblies:
//
// * virt/nodes/virt-managing-node-labeling-obsolete-cpu-models.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-obsolete-cpu-models_{context}"]
= Configuring obsolete CPU models

You can configure a list of obsolete CPU models by editing the `HyperConverged` custom resource (CR).

.Procedure

* Edit the `HyperConverged` custom resource, specifying the obsolete CPU models in the `obsoleteCPUs` array. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  obsoleteCPUs:
    cpuModels: <1>
      - "<obsolete_cpu_1>"
      - "<obsolete_cpu_2>"
    minCPUModel: "<minimum_cpu_model>" <2>
----
<1> Replace the example values in the `cpuModels` array with obsolete CPU models. Any value that you specify is added to a predefined list of obsolete CPU models. The predefined list is not visible in the CR.
<2> Replace this value with the minimum CPU model that you want to use for basic CPU features. If you do not specify a value, `Penryn` is used by default.
