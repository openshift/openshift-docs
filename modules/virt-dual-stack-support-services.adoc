// Module included in the following assemblies:
//
// * virt/vm_networking/virt-exposing-vm-with-service.adoc


:_mod-docs-content-type: REFERENCE
[id="virt-dual-stack-support-services_{context}"]
= Dual-stack support

If IPv4 and IPv6 dual-stack networking is enabled for your cluster, you can create a service that uses IPv4, IPv6, or both, by defining the `spec.ipFamilyPolicy` and the `spec.ipFamilies` fields in the `Service` object.

The `spec.ipFamilyPolicy` field can be set to one of the following values:

SingleStack:: The control plane assigns a cluster IP address for the service based on the first configured service cluster IP range.

PreferDualStack:: The control plane assigns both IPv4 and IPv6 cluster IP addresses for the service on clusters that have dual-stack configured.

RequireDualStack:: This option fails for clusters that do not have dual-stack networking enabled. For clusters that have dual-stack configured, the behavior is the same as when the value is set to `PreferDualStack`. The control plane allocates cluster IP addresses from both IPv4 and IPv6 address ranges.

You can define which IP family to use for single-stack or define the order of IP families for dual-stack by setting the `spec.ipFamilies` field to one of the following array values:

* `[IPv4]`
* `[IPv6]`
* `[IPv4, IPv6]`
* `[IPv6, IPv4]`
