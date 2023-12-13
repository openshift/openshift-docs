// Module included in the following assemblies:
//
// * virt/monitoring/virt-monitoring-vm-health.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-installing-watchdog-agent_{context}"]
= Installing the watchdog agent on the guest

You install the watchdog agent on the guest and start the `watchdog` service.

.Procedure

. Log in to the virtual machine as root user.

. Install the `watchdog` package and its dependencies:
+
[source,terminal]
----
# yum install watchdog
----

. Uncomment the following line in the `/etc/watchdog.conf` file and save the changes:
+
[source,terminal]
----
#watchdog-device = /dev/watchdog
----

. Enable the `watchdog` service to start on boot:

+
[source,terminal]
----
# systemctl enable --now watchdog.service
----
