// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc


[id="csi-driver-daemonset_{context}"]
= CSI driver daemon set

The CSI driver daemon set runs a pod on every node that allows
{product-title} to mount storage provided by the CSI driver to the node
and use it in user workloads (pods) as persistent volumes (PVs). The pod
with the CSI driver installed contains the following containers:

* A CSI driver registrar, which registers the CSI driver into the
`openshift-node` service running on the node. The `openshift-node` process
running on the node then directly connects with the CSI driver using the
UNIX Domain Socket available on the node.
* A CSI driver.

The CSI driver deployed on the node should have as few credentials to the
storage back end as possible. {product-title} will only use the node plugin
set of CSI calls such as `NodePublish`/`NodeUnpublish` and
`NodeStage`/`NodeUnstage`, if these calls are implemented.
