// Module included in the following assemblies:
//
// * virt/monitoring/virt-monitoring-vm-health.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-defining-watchdog-device-vm"]
= Configuring a watchdog device for the virtual machine

You configure a watchdog device for the virtual machine (VM).

.Prerequisites

* The VM must have kernel support for an `i6300esb` watchdog device. {op-system-base-full} images support `i6300esb`.

.Procedure

. Create a `YAML` file with the following contents:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    kubevirt.io/vm: vm2-rhel84-watchdog
  name: <vm-name>
spec:
  running: false
  template:
    metadata:
      labels:
        kubevirt.io/vm: vm2-rhel84-watchdog
    spec:
      domain:
        devices:
          watchdog:
            name: <watchdog>
            i6300esb:
              action: "poweroff" <1>
# ...
----
<1> Specify `poweroff`, `reset`, or `shutdown`.
+
The example above configures the `i6300esb` watchdog device on a RHEL8 VM with the poweroff action and exposes the device as `/dev/watchdog`.
+
This device can now be used by the watchdog binary.

. Apply the YAML file to your cluster by running the following command:
+
[source,yaml]
----
$ oc apply -f <file_name>.yaml
----

.Verification

--
[IMPORTANT]
====
This procedure is provided for testing watchdog functionality only and must not be run on production machines.
====
--

. Run the following command to verify that the VM is connected to the watchdog device:
+
[source,terminal]
----
$ lspci | grep watchdog -i
----

. Run one of the following commands to confirm the watchdog is active:

* Trigger a kernel panic:
+
[source,terminal]
----
# echo c > /proc/sysrq-trigger
----

* Stop the watchdog service:
+
[source,terminal]
----
# pkill -9 watchdog
----
