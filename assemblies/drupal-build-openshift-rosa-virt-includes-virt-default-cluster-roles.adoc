// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

:_mod-docs-content-type: REFERENCE
[id="default-cluster-roles-for-virt_{context}"]
= Default cluster roles for {VirtProductName}

By using cluster role aggregation, {VirtProductName} extends the default {product-title} cluster roles to include permissions for accessing virtualization objects.

.{VirtProductName} cluster roles
[cols="1,1,4",options="header"]
|===
|Default cluster role
|{VirtProductName} cluster role
|{VirtProductName} cluster role description

.^| `view`
.^|`kubevirt.io:view`
| A user that can view all {VirtProductName} resources in the cluster but cannot create, delete, modify, or access them. For example, the user can see that a virtual machine (VM) is running but cannot shut it down or gain access to its console.

.^| `edit`
.^|`kubevirt.io:edit`
| A user that can modify all {VirtProductName} resources in the cluster. For example, the user can create VMs, access VM consoles, and delete VMs.

.^| `admin`
.^|`kubevirt.io:admin`
| A user that has full permissions to all {VirtProductName} resources, including the ability to delete collections of resources. The user can also view and modify the {VirtProductName} runtime configuration, which is located in the `HyperConverged` custom resource in the `openshift-cnv` namespace.
|===