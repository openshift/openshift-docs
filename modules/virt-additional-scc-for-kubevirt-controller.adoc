// Module included in the following assemblies:
//
// * virt/virt-security-policies.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-additional-scc-for-kubevirt-controller_{context}"]
= Additional SCCs and permissions for the kubevirt-controller service account

Security context constraints (SCCs) control permissions for pods. These permissions include actions that a pod, a collection of containers, can perform and what resources it can access. You can use SCCs to define a set of conditions that a pod must run with to be accepted into the system.

The `virt-controller` is a cluster controller that creates the `virt-launcher` pods for virtual machines in the cluster. These pods are granted permissions by the `kubevirt-controller` service account.

The `kubevirt-controller` service account is granted additional SCCs and Linux capabilities so that it can create `virt-launcher` pods with the appropriate permissions. These extended permissions allow virtual machines to use {VirtProductName} features that are beyond the scope of typical pods.

The `kubevirt-controller` service account is granted the following SCCs:

* `scc.AllowHostDirVolumePlugin = true` +
This allows virtual machines to use the hostpath volume plugin.

* `scc.AllowPrivilegedContainer = false` +
This ensures the virt-launcher pod is not run as a privileged container.

* `scc.AllowedCapabilities = []corev1.Capability{"SYS_NICE", "NET_BIND_SERVICE"}`

** `SYS_NICE` allows setting the CPU affinity.
** `NET_BIND_SERVICE` allows DHCP and Slirp operations.

.Viewing the SCC and RBAC definitions for the kubevirt-controller

You can view the `SecurityContextConstraints` definition for the `kubevirt-controller` by using the `oc` tool:

[source,terminal]
----
$ oc get scc kubevirt-controller -o yaml
----

You can view the RBAC definition for the `kubevirt-controller` clusterrole by using the `oc` tool:

[source,terminal]
----
$ oc get clusterrole kubevirt-controller -o yaml
----
