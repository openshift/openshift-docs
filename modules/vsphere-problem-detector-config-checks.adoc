// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

:operator-name: vSphere Problem Detector Operator

[id="vsphere-problem-detector-config-checks_{context}"]
= Configuration checks run by the {operator-name}

The following tables identify the configuration checks that the {operator-name} runs. Some checks verify the configuration of the cluster. Other checks verify the configuration of each node in the cluster.

.Cluster configuration checks
[options="header",cols="20,80a"]
|===
|Name
|Description

|`CheckDefaultDatastore`
|Verifies that the default datastore name in the vSphere configuration is short enough for use with dynamic provisioning.

If this check fails, you can expect the following:

* `systemd` logs errors to the journal such as `Failed to set up mount unit: Invalid argument`.

* `systemd` does not unmount volumes if the virtual machine is shut down or rebooted without draining all the pods from the node.

If this check fails, reconfigure vSphere with a shorter name for the default datastore.

|`CheckFolderPermissions`
|Verifies the permission to list volumes in the default datastore. This permission is required to create volumes. The Operator verifies the permission by listing the `/` and `/kubevols` directories. The root directory must exist. It is acceptable if the `/kubevols` directory does not exist when the check runs. The `/kubevols` directory is created when the datastore is used with dynamic provisioning if the directory does not already exist.

If this check fails, review the required permissions for the vCenter account that was specified during the {product-title} installation.

|`CheckStorageClasses`
|Verifies the following:

* The fully qualified path to each persistent volume that is provisioned by this storage class is less than 255 characters.

* If a storage class uses a storage policy, the storage class must use one policy only and that policy must be defined.

|`CheckTaskPermissions`
|Verifies the permission to list recent tasks and datastores.

|`ClusterInfo`
|Collects the cluster version and UUID from vSphere vCenter.
|===

.Node configuration checks
[options="header",cols="20,80a"]
|===
|Name
|Description

|`CheckNodeDiskUUID`
|Verifies that all the vSphere virtual machines are configured with `disk.enableUUID=TRUE`.

If this check fails, see the link:https://access.redhat.com/solutions/4606201[How to check 'disk.EnableUUID' parameter from VM in vSphere] Red Hat Knowledgebase solution.

|`CheckNodeProviderID`
|Verifies that all nodes are configured with the `ProviderID` from vSphere vCenter. This check fails when the output from the following command does not include a provider ID for each node.

[source,terminal]
----
$ oc get nodes -o custom-columns=NAME:.metadata.name,PROVIDER_ID:.spec.providerID,UUID:.status.nodeInfo.systemUUID
----

If this check fails, refer to the vSphere product documentation for information about setting the provider ID for each node in the cluster.

|`CollectNodeESXiVersion`
|Reports the version of the ESXi hosts that run nodes.

|`CollectNodeHWVersion`
|Reports the virtual machine hardware version for a node.
|===

// Clear temporary attributes
:!operator-name:
