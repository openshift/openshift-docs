// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc

[id="machineset-vsphere-requirements-user-provisioned-machine-sets_{context}"]
= Minimum required vCenter privileges for compute machine set management

To manage compute machine sets in an {product-title} cluster on vCenter, you must use an account with privileges to read, create, and delete the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions.

If you cannot use an account with global administrative privileges, you must create roles to grant the minimum required privileges. The following table lists the minimum vCenter roles and privileges that are required to create, scale, and delete compute machine sets and to delete machines in your {product-title} cluster.

.Minimum vCenter roles and privileges required for compute machine set management
[%collapsible]
====
[cols="3a,3a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges

|vSphere vCenter
|Always
|
[%hardbreaks]
`InventoryService.Tagging.AttachTag`
`InventoryService.Tagging.CreateCategory`
`InventoryService.Tagging.CreateTag`
`InventoryService.Tagging.DeleteCategory`
`InventoryService.Tagging.DeleteTag`
`InventoryService.Tagging.EditCategory`
`InventoryService.Tagging.EditTag`
`Sessions.ValidateSession`
`StorageProfile.Update`^1^
`StorageProfile.View`^1^

|vSphere vCenter Cluster
|Always
|
[%hardbreaks]
`Resource.AssignVMToPool`

|vSphere Datastore
|Always
|
[%hardbreaks]
`Datastore.AllocateSpace`
`Datastore.Browse`

|vSphere Port Group
|Always
|`Network.Assign`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.Settings`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`

|vSphere vCenter Datacenter
|If the installation program creates the virtual machine folder
|
[%hardbreaks]
`Resource.AssignVMToPool`
`VirtualMachine.Provisioning.DeployTemplate`

3+a|
^1^ The `StorageProfile.Update` and `StorageProfile.View` permissions are required only for storage backends that use the Container Storage Interface (CSI).
|===
====

The following table details the permissions and propagation settings that are required for compute machine set management.

.Required permissions and propagation settings
[%collapsible]
====
[cols="3a,3a,3a,3a",options="header"]
|===
|vSphere object
|Folder type
|Propagate to children
|Permissions required

|vSphere vCenter
|Always
|Not required
|Listed required privileges

.2+|vSphere vCenter Datacenter
|Existing folder
|Not required
|`ReadOnly` permission

|Installation program creates the folder
|Required
|Listed required privileges

|vSphere vCenter Cluster
|Always
|Required
|Listed required privileges

|vSphere vCenter Datastore
|Always
|Not required
|Listed required privileges

|vSphere Switch
|Always
|Not required
|`ReadOnly` permission

|vSphere Port Group
|Always
|Not required
|Listed required privileges

|vSphere vCenter Virtual Machine Folder
|Existing folder
|Required
|Listed required privileges
|===
====

For more information about creating an account with only the required privileges, see link:https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5372F580-5C23-4E9C-8A4E-EF1B4DD9033E.html[vSphere Permissions and User Management Tasks] in the vSphere documentation.
