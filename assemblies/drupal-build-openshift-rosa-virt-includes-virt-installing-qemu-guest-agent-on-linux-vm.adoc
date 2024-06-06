// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-installing-qemu-guest-agent-on-linux-vm_{context}"]
= Installing the QEMU guest agent on a Linux VM

The `qemu-guest-agent` is widely available and available by default in {op-system-base-full} virtual machines (VMs). Install the agent and start the service.

[NOTE]
====
To create snapshots of an online (Running state) VM with the highest integrity, install the QEMU guest agent.

The QEMU guest agent takes a consistent snapshot by attempting to quiesce the VM file system as much as possible, depending on the system workload. This ensures that in-flight I/O is written to the disk before the snapshot is taken. If the guest agent is not present, quiescing is not possible and a best-effort snapshot is taken. The conditions under which the snapshot was taken are reflected in the snapshot indications that are displayed in the web console or CLI.
====

.Procedure

. Log in to the VM by using a console or SSH.

. Install the QEMU guest agent by running the following command:
+
[source,terminal]
----
$ yum install -y qemu-guest-agent
----

. Ensure the service is persistent and start it:
+
[source,terminal]
----
$ systemctl enable --now qemu-guest-agent
----

.Verification
* Run the following command to verify that `AgentConnected` is listed in the VM spec:

+
[source,terminal]
----
$ oc get vm <vm_name>
----