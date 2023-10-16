// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-certificate-rotation.adoc

[id="virt-troubleshooting-cert-rotation-parameters_{context}"]
= Troubleshooting certificate rotation parameters

Deleting one or more `certConfig` values causes them to revert to the default values, unless the default values conflict with one of the following conditions:

* The value of `ca.renewBefore` must be less than or equal to the value of `ca.duration`.

* The value of `server.duration` must be less than or equal to the value of `ca.duration`.

* The value of `server.renewBefore` must be less than or equal to the value of `server.duration`.


If the default values conflict with these conditions, you will receive an error.

If you remove the `server.duration` value in the following example, the default value of `24h0m0s` is greater than the value of `ca.duration`, conflicting with the specified conditions.

.Example
[source,yaml]
----
certConfig:
   ca:
     duration: 4h0m0s
     renewBefore: 1h0m0s
   server:
     duration: 4h0m0s
     renewBefore: 4h0m0s
----

This results in the following error message:

[source,terminal]
----
error: hyperconvergeds.hco.kubevirt.io "kubevirt-hyperconverged" could not be patched: admission webhook "validate-hco.kubevirt.io" denied the request: spec.certConfig: ca.duration is smaller than server.duration
----

The error message only mentions the first conflict. Review all certConfig values before you proceed.
