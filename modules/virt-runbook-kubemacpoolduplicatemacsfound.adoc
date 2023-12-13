// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubeMacPoolDuplicateMacsFound"]
= KubeMacPoolDuplicateMacsFound

[discrete]
[id="meaning-kubemacpoolduplicatemacsfound"]
== Meaning

This alert fires when `KubeMacPool` detects duplicate MAC addresses.

`KubeMacPool` is responsible for allocating MAC addresses and preventing MAC
address conflicts. When `KubeMacPool` starts, it scans the cluster for the MAC
addresses of virtual machines (VMs) in managed namespaces.

[discrete]
[id="impact-kubemacpoolduplicatemacsfound"]
== Impact

Duplicate MAC addresses on the same LAN might cause network issues.

[discrete]
[id="diagnosis-kubemacpoolduplicatemacsfound"]
== Diagnosis

. Obtain the namespace and the name of the `kubemacpool-mac-controller` pod:
+
[source,terminal]
----
$ oc get pod -A -l control-plane=mac-controller-manager --no-headers \
  -o custom-columns=":metadata.namespace,:metadata.name"
----

. Obtain the duplicate MAC addresses from the `kubemacpool-mac-controller`
logs:
+
[source,terminal]
----
$ oc logs -n <namespace> <kubemacpool_mac_controller> | \
  grep "already allocated"
----
+
.Example output
+
[source,text]
----
mac address 02:00:ff:ff:ff:ff already allocated to
vm/kubemacpool-test/testvm, br1,
conflict with: vm/kubemacpool-test/testvm2, br1
----

[discrete]
[id="mitigation-kubemacpoolduplicatemacsfound"]
== Mitigation

. Update the VMs to remove the duplicate MAC addresses.
. Restart the `kubemacpool-mac-controller` pod:
+
[source,terminal]
----
$ oc delete pod -n <namespace> <kubemacpool_mac_controller>
----
