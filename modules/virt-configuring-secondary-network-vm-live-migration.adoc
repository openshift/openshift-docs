// Module included in the following assemblies:
//
// * virt/vm_networking/virt-dedicated-network-live-migration.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-secondary-network-vm-live-migration_{context}"]
= Configuring a dedicated secondary network for live migration

To configure a dedicated secondary network for live migration, you must first create a bridge network attachment definition (NAD) by using the CLI. Then, you add the name of the `NetworkAttachmentDefinition` object to the `HyperConverged` custom resource (CR).

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You logged in to the cluster as a user with the `cluster-admin` role.
* Each node has at least two Network Interface Cards (NICs).
* The NICs for live migration are connected to the same VLAN.

.Procedure

. Create a `NetworkAttachmentDefinition` manifest according to the following example:
+
.Example configuration file
[source,yaml,subs="attributes+"]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: my-secondary-network <1>
  namespace: {CNVNamespace} <2>
spec:
  config: '{
    "cniVersion": "0.3.1",
    "name": "migration-bridge",
    "type": "macvlan",
    "master": "eth1", <2>
    "mode": "bridge",
    "ipam": {
      "type": "whereabouts", <3>
      "range": "10.200.5.0/24" <4>
    }
  }'
----
<1> Specify the name of the `NetworkAttachmentDefinition` object.
<2> Specify the name of the NIC to be used for live migration.
<3> Specify the name of the CNI plugin that provides the network for the NAD.
<4> Specify an IP address range for the secondary network. This range must not overlap the IP addresses of the main network.

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the name of the `NetworkAttachmentDefinition` object to the `spec.liveMigrationConfig` stanza of the `HyperConverged` CR:
+
.Example `HyperConverged` manifest
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  liveMigrationConfig:
    completionTimeoutPerGiB: 800
    network: <network> <1>
    parallelMigrationsPerCluster: 5
    parallelOutboundMigrationsPerNode: 2
    progressTimeout: 150
# ...
----
<1> Specify the name of the Multus `NetworkAttachmentDefinition` object to be used for live migrations.

. Save your changes and exit the editor. The `virt-handler` pods restart and connect to the secondary network.

.Verification

* When the node that the virtual machine runs on is placed into maintenance mode, the VM automatically migrates to another node in the cluster. You can verify that the migration occurred over the secondary network and not the default pod network by checking the target IP address in the virtual machine instance (VMI) metadata.
+
[source,terminal]
----
$ oc get vmi <vmi_name> -o jsonpath='{.status.migrationState.targetNodeAddress}'
----
