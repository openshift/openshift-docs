// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_rh/virt-creating-vms-from-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-vm-from-template_{context}"]
= Creating a VM from a template

You can create a virtual machine (VM) from a template with an available boot source by using the {product-title} web console.

Optional: You can customize template or VM parameters, such as data sources, cloud-init, or SSH keys, before you start the VM.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click *Boot source available* to filter templates with boot sources.
+
The catalog displays the default templates. Click *All Items* to view all available templates for your filters.

. Click a template tile to view its details.
. Click *Quick create VirtualMachine* to create a VM from the template.
+
Optional: Customize the template or VM parameters:

.. Click *Customize VirtualMachine*.
.. Expand *Storage* or *Optional parameters* to edit data source settings.
.. Click *Customize VirtualMachine parameters*.
+
The *Customize and create VirtualMachine* pane displays the *Overview*, *YAML*, *Scheduling*, *Environment*, *Network interfaces*, *Disks*, *Scripts*, and *Metadata* tabs.

.. Edit the parameters that must be set before the VM boots, such as cloud-init or a static SSH key.
.. Click *Create VirtualMachine*.
+
The *VirtualMachine details* page displays the provisioning status.
