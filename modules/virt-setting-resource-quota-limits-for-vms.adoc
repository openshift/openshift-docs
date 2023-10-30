// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-working-with-resource-quotas-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-setting-resource-quota-limits-for-vms_{context}"]
= Setting resource quota limits for virtual machines

Resource quotas that only use requests automatically work with virtual machines (VMs). If your resource quota uses limits, you must manually set resource limits on VMs. Resource limits must be at least 100 MiB larger than resource requests.

.Procedure

. Set limits for a VM by editing the `VirtualMachine` manifest. For example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: with-limits
spec:
  running: false
  template:
    spec:
      domain:
# ...
        resources:
          requests:
            memory: 128Mi
          limits:
            memory: 256Mi  <1>
----
<1> This configuration is supported because the `limits.memory` value is at least `100Mi` larger than the `requests.memory` value.

. Save the `VirtualMachine` manifest.
