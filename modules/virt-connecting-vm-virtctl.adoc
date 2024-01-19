// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-consoles.adoc

ifeval::["{context}" == "vnc-console"]
:vnc-console:
:console: VNC console
endif::[]
ifeval::["{context}" == "serial-console"]
:serial-console:
:console: serial console
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="virt-connecting-vm-virtctl_{context}"]
= Connecting to the {console} by using virtctl

You can use the `virtctl` command line tool to connect to the {console} of a running virtual machine.

ifdef::vnc-console[]
[NOTE]
====
If you run the `virtctl vnc` command on a remote machine over an SSH connection, you must forward the X session to your local machine by running the `ssh` command with the `-X` or `-Y` flags.
====

.Prerequisites

* You must install the `virt-viewer` package.
endif::[]

.Procedure

. Run the following command to start the console session:
+
ifdef::serial-console[]
[source,terminal]
----
$ virtctl console <vm_name>
----

. Press `Ctrl+]` to end the console session.
endif::[]
ifdef::vnc-console[]
[source,terminal]
----
$ virtctl vnc <vm_name>
----

. If the connection fails, run the following command to collect
troubleshooting information:
+
[source,terminal]
----
$ virtctl vnc <vm_name> -v 4
----
endif::[]

ifeval::["{context}" == "vnc-console"]
:!console:
endif::[]
ifeval::["{context}" == "serial-console"]
:!console:
endif::[]