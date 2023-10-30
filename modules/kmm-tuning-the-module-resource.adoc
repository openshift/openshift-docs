// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: PROCEDURE
[id="kmm-tuning-the-module-resource_{context}"]
= Tuning the Module resource

.Procedure

* Set `.spec.moduleLoader.container.modprobe.firmwarePath` in the `Module` custom resource (CR):
+
[source,yaml]
----
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: my-kmod
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: my-kmod  # Required

        firmwarePath: /firmware <1>
----
<1> Optional: Copies `/firmware/*` into `/var/lib/firmware/` on the node.
