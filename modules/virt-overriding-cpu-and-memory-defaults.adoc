// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-cdi-for-namespace-resourcequota.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-overriding-cpu-and-memory-defaults_{context}"]
= Overriding CPU and memory defaults

Modify the default settings for CPU and memory requests and limits for your use case by adding the `spec.resourceRequirements.storageWorkloads` stanza to the `HyperConverged` custom resource (CR).

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Edit the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the `spec.resourceRequirements.storageWorkloads` stanza to the CR, setting the values based on your use case. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  resourceRequirements:
    storageWorkloads:
      limits:
        cpu: "500m"
        memory: "2Gi"
      requests:
        cpu: "250m"
        memory: "1Gi"
----

. Save and exit the editor to update the `HyperConverged` CR.
