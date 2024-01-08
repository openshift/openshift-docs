// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-network-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="configuring-ovs-log-level-permanently_{context}"]
= Configuring the Open vSwitch log level permanently

For long-term changes to the Open vSwitch (OVS) log level, you can change the log level permanently.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a file, such as `99-change-ovs-loglevel.yaml`, with a `MachineConfig` object like the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master  <1>
  name: 99-change-ovs-loglevel
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
      - dropins:
        - contents: |
            [Service]
              ExecStartPost=-/usr/bin/ovs-appctl vlog/set syslog:dbg  <2>
              ExecReload=-/usr/bin/ovs-appctl vlog/set syslog:dbg
          name: 20-ovs-vswitchd-restart.conf
        name: ovs-vswitchd.service
----
<1> After you perform this procedure to configure control plane nodes, repeat the procedure and set the role to `worker` to configure worker nodes.
<2> Set the `syslog:<log_level>` value. Log levels are `off`, `emer`, `err`, `warn`, `info`, or `dbg`. Setting the value to `off` filters out all log messages.

. Apply the machine config:
+
[source,terminal]
----
$ oc apply -f 99-change-ovs-loglevel.yaml
----

ifdef::ign-config-version[]
:!ign-config-version:
endif::[]

