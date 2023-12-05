// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

:_mod-docs-content-type: PROCEDURE
[id="ibm-z-boost-networking-performance-with-rfs_{context}"]
= Boost networking performance with Receive Flow Steering

Receive Flow Steering (RFS) extends Receive Packet Steering (RPS) by further reducing network latency. RFS is technically based on RPS, and improves the efficiency of packet processing by increasing the CPU cache hit rate. RFS achieves this, and in addition considers queue length, by determining the most convenient CPU for computation so that cache hits are more likely to occur within the CPU. Thus, the CPU cache is invalidated less and requires fewer cycles to rebuild the cache. This can help reduce packet processing run time.

[id="use-the-mco-to-activate-rfs_{context}"]
== Use the Machine Config Operator (MCO) to activate RFS

.Procedure

. Copy the following MCO sample profile into a YAML file. For example, `enable-rfs.yaml`:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 50-enable-rfs
spec:
  config:
    ignition:
      version: 2.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=US-ASCII,%23%20turn%20on%20Receive%20Flow%20Steering%20%28RFS%29%20for%20all%20network%20interfaces%0ASUBSYSTEM%3D%3D%22net%22%2C%20ACTION%3D%3D%22add%22%2C%20RUN%7Bprogram%7D%2B%3D%22/bin/bash%20-c%20%27for%20x%20in%20/sys/%24DEVPATH/queues/rx-%2A%3B%20do%20echo%208192%20%3E%20%24x/rps_flow_cnt%3B%20%20done%27%22%0A
        filesystem: root
        mode: 0644
        path: /etc/udev/rules.d/70-persistent-net.rules
      - contents:
          source: data:text/plain;charset=US-ASCII,%23%20define%20sock%20flow%20enbtried%20for%20%20Receive%20Flow%20Steering%20%28RFS%29%0Anet.core.rps_sock_flow_entries%3D8192%0A
        filesystem: root
        mode: 0644
        path: /etc/sysctl.d/95-enable-rps.conf
----

. Create the MCO profile:
+
[source,terminal]
----
$ oc create -f enable-rfs.yaml
----

. Verify that an entry named `50-enable-rfs` is listed:
+
[source,terminal]
----
$ oc get mc
----

. To deactivate, enter:
+
[source,terminal]
----
$ oc delete mc 50-enable-rfs
----

