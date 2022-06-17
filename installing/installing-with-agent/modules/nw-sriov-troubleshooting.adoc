// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-device.adoc

[id="nw-sriov-troubleshooting_{context}"]
= Troubleshooting SR-IOV configuration

After following the procedure to configure an SR-IOV network device, the following sections address some error conditions.

To display the state of nodes, run the following command:

[source,terminal]
----
$ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name>
----

where: `<node_name>` specifies the name of a node with an SR-IOV network device.

.Error output: Cannot allocate memory
[source,terminal]
----
"lastSyncError": "write /sys/bus/pci/devices/0000:3b:00.1/sriov_numvfs: cannot allocate memory"
----

When a node indicates that it cannot allocate memory, check the following items:

* Confirm that global SR-IOV settings are enabled in the BIOS for the node.

* Confirm that VT-d is enabled in the BIOS for the node.
