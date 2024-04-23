:_mod-docs-content-type: ASSEMBLY
[id="virt-security-policies"]
= Security policies
include::_attributes/common-attributes.adoc[]
:context: virt-security-policies

toc::[]

Learn about {VirtProductName} security and authorization.

.Key points
* {VirtProductName} adheres to the `restricted` link:https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted[Kubernetes pod security standards] profile, which aims to enforce the current best practices for pod security.
* Virtual machine (VM) workloads run as unprivileged pods.
* xref:../../authentication/managing-security-context-constraints.adoc#security-context-constraints-about_configuring-internal-oauth[Security context constraints] (SCCs) are defined for the `kubevirt-controller` service account.
* TLS certificates for {VirtProductName} components are renewed and rotated automatically.

include::modules/virt-about-workload-security.adoc[leveloffset=+1]

include::modules/virt-automatic-certificates-renewal.adoc[leveloffset=+1]

[id="authorization_virt-security-policies"]
== Authorization

{VirtProductName} uses xref:../../authentication/using-rbac.adoc#using-rbac[role-based access control] (RBAC) to define permissions for human users and service accounts. The permissions defined for service accounts control the actions that {VirtProductName} components can perform.

You can also use RBAC roles to manage user access to virtualization features. For example, an administrator can create an RBAC role that provides the permissions required to launch a virtual machine. The administrator can then restrict access by binding the role to specific users.

include::modules/virt-default-cluster-roles.adoc[leveloffset=+2]

include::modules/virt-storage-rbac-roles.adoc[leveloffset=+2]

include::modules/virt-additional-scc-for-kubevirt-controller.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* xref:../../authentication/managing-security-context-constraints.adoc#security-context-constraints-about_configuring-internal-oauth[Managing security context constraints]
* xref:../../authentication/using-rbac.adoc#using-rbac[Using RBAC to define and apply permissions]
* xref:../../authentication/using-rbac.adoc#creating-cluster-role_using-rbac[Creating a cluster role]
* xref:../../authentication/using-rbac.adoc#cluster-role-binding-commands_using-rbac[Cluster role binding commands]
* xref:../../virt/storage/virt-enabling-user-permissions-to-clone-datavolumes.adoc#virt-enabling-user-permissions-to-clone-datavolumes[Enabling user permissions to clone data volumes across namespaces]

