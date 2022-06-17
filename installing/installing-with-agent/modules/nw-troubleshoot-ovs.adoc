[id="nw-troubleshoot-ovs_{context}"]
= Troubleshooting Open vSwitch issues

To troubleshoot some Open vSwitch (OVS) issues, you might need to configure the log level to include more information.

If you modify the log level on a node temporarily, be aware that you can receive log messages from the machine config daemon on the node like the following example:

[source,terminal]
----
E0514 12:47:17.998892    2281 daemon.go:1350] content mismatch for file /etc/systemd/system/ovs-vswitchd.service: [Unit]
----

To avoid the log messages related to the mismatch, revert the log level change after you complete your troubleshooting.

