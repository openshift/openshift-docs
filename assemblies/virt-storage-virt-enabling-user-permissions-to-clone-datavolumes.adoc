:_mod-docs-content-type: ASSEMBLY
[id="virt-enabling-user-permissions-to-clone-datavolumes"]
= Enabling user permissions to clone data volumes across namespaces
include::_attributes/common-attributes.adoc[]
:context: virt-enabling-user-permissions-to-clone-datavolumes

toc::[]

The isolating nature of namespaces means that users cannot by default
clone resources between namespaces.

To enable a user to clone a virtual machine to another namespace, a
user with the `cluster-admin` role must create a new cluster role. Bind
this cluster role to a user to enable them to clone virtual machines
to the destination namespace.

include::modules/virt-creating-rbac-cloning-dvs.adoc[leveloffset=+1]
