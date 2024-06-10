// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-windows-vm_{context}"]
= Creating a Windows VM

You can create a Windows virtual machine (VM) by uploading a Windows image to a persistent volume claim (PVC) and then cloning the PVC when you create a VM by using the {product-title} web console.

.Prerequisites

* You created a Windows installation DVD or USB with the Windows Media Creation Tool. See link:https://www.microsoft.com/en-us/software-download/windows10%20[Create Windows 10 installation media] in the Microsoft documentation.
* You created an `autounattend.xml` answer file. See link:https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs[Answer files (unattend.xml)] in the Microsoft documentation.

.Procedure

. Upload the Windows image as a new PVC:

.. Navigate to *Storage* -> *PersistentVolumeClaims* in the web console.
.. Click *Create PersistentVolumeClaim* -> *With Data upload form*.
.. Browse to the Windows image and select it.
.. Enter the PVC name, select the storage class and size and then click *Upload*.
+
The Windows image is uploaded to a PVC.

. Configure a new VM by cloning the uploaded PVC:

.. Navigate to *Virtualization* -> *Catalog*.
.. Select a Windows template tile and click *Customize VirtualMachine*.
.. Select *Clone (clone PVC)* from the *Disk source* list.
.. Select the PVC project, the Windows image PVC, and the disk size.

. Apply the answer file to the VM:

.. Click *Customize VirtualMachine parameters*.
.. On the *Sysprep* section of the *Scripts* tab, click *Edit*.
.. Browse to the `autounattend.xml` answer file and click *Save*.

. Set the run strategy of the VM:

.. Clear *Start this VirtualMachine after creation* so that the VM does not start immediately.
.. Click *Create VirtualMachine*.
.. On the *YAML* tab, replace `running:false` with `runStrategy: RerunOnFailure` and click *Save*.

. Click the options menu {kebab} and select *Start*.
+
The VM boots from the `sysprep` disk containing the `autounattend.xml` answer file.
