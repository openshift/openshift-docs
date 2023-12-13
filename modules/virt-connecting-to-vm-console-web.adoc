// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-consoles.adoc

ifeval::["{context}" == "vnc-console"]
:vnc-console:
:console: VNC console
:console-menu: VNC console
endif::[]
ifeval::["{context}" == "serial-console"]
:serial-console:
:console: serial console
:console-menu: Serial console
endif::[]
ifeval::["{context}" == "desktop-viewer"]
:desktop-viewer:
:console: desktop viewer
:console-menu: Desktop viewer
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="virt-connecting-to-vm-console-web_{context}"]
= Connecting to the {console} by using the web console

ifdef::vnc-console,serial-console[]
You can connect to the {console} of a virtual machine (VM) by using the {product-title} web console.
endif::[]
ifdef::desktop-viewer[]
You can connect to the {console} of a Windows virtual machine (VM) by using the {product-title} web console.
endif::[]

ifdef::vnc-console[]
[NOTE]
====
If you connect to a Windows VM with a vGPU assigned as a mediated device, you can switch between the default display and the vGPU display.
====
endif::[]

ifdef::desktop-viewer[]
.Prerequisites

* You installed the QEMU guest agent on the Windows VM.
* You have an RDP client installed.
endif::[]

.Procedure

. On the *Virtualization* -> *VirtualMachines* page, click a VM to open the *VirtualMachine details* page.
. Click the *Console* tab. The VNC console session starts automatically.
ifdef::desktop-viewer,serial-console[]
. Click *Disconnect* to end the VNC console session. Otherwise, the VNC console session continues to run in the background.
. Select *{console-menu}* from the console list.
endif::[]
ifdef::desktop-viewer[]
. Click *Create RDP Service* to open the *RDP Service* dialog.
. Select *Expose RDP Service* and click *Save* to create a node port service.
. Click *Launch Remote Desktop* to download an `.rdp` file and launch the {console}.
endif::[]
ifdef::vnc-console[]
. Optional: To switch to the vGPU display of a Windows VM, select *Ctl + Alt + 2* from the *Send key* list.
+
* Select *Ctl + Alt + 1* from the *Send key* list to restore the default display.
endif::[]
ifdef::vnc-console,serial-console[]
. To end the console session, click outside the console pane and then click *Disconnect*.
endif::[]

ifeval::["{context}" == "vnc-console"]
:console!:
:console-menu!:
endif::[]
ifeval::["{context}" == "serial-console"]
:console!:
:console-menu!:
endif::[]
ifeval::["{context}" == "desktop-viewer"]
:console!:
:console-menu!:
endif::[]
