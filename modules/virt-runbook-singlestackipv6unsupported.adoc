// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-SingleStackIPv6Unsupported"]
= SingleStackIPv6Unsupported

[discrete]
[id="meaning-singlestackipv6unsupported"]
== Meaning

This alert fires when you install {VirtProductName} on a single stack
IPv6 cluster.

[discrete]
[id="impact-singlestackipv6unsupported"]
== Impact

You cannot create virtual machines.

[discrete]
[id="diagnosis-singlestackipv6unsupported"]
== Diagnosis

* Check the cluster network configuration by running the following command:
+
[,shell]
----
$ oc get network.config cluster -o yaml
----
+
The output displays only an IPv6 CIDR for the cluster network.
+
.Example output
+
[source,text]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: fd02::/48
    hostPrefix: 64
----

[discrete]
[id="mitigation-singlestackipv6unsupported"]
== Mitigation

Install {VirtProductName} on a single stack IPv4 cluster or on a
dual stack IPv4/IPv6 cluster.
