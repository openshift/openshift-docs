// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-core-ref-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-security_{context}"]
= Security

New in this release::

* DPDK applications that need to inject traffic to the kernel can run in non-privileged pods with the help of the TAP CNI plugin. Furthermore, in this 4.14 release that ability to create a MAC-VLAN, IP-VLAN, and VLAN subinterface based on a master interface in a container namespace is generally available.

Description::

Telco operators are security conscious and require clusters to be hardened against multiple attack vectors. Within {product-title}, there is no single component or feature responsible for securing a cluster. This section provides details of security-oriented features and configuration for the use models covered in this specification.

* **SecurityContextConstraints**: All workload pods should be run with restricted-v2 or restricted SCC.
* **Seccomp**: All pods should be run with the `RuntimeDefault` (or stronger) seccomp profile.
* **Rootless DPDK pods**: Many user-plane networking (DPDK) CNFs require pods to run with root privileges. With this feature, a conformant DPDK pod can be run without requiring root privileges.
* **Storage**: The storage network should be isolated and non-routable to other cluster networks. See the "Storage" section for additional details.

Limits and requirements::

* Rootless DPDK pods requires the following additional configuration steps:
** Configure the TAP plugin with the `container_t` SELinux context.
** Enable the `container_use_devices` SELinux boolean on the hosts.

Engineering considerations::

* For rootless DPDK pod support, the SELinux boolean `container_use_devices` must be enabled on the host for the TAP device to be created. This introduces a security risk that is acceptable for short to mid-term use. Other solutions will be explored.