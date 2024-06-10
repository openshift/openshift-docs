// Module included in the following assemblies:
//
// * virt/virt-architecture.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-hpp-operator_{context}"]
= About the Hostpath Provisioner (HPP) Operator

The HPP Operator, `hostpath-provisioner-operator`, deploys and manages the multi-node HPP and related resources.

image::cnv_components_hpp-operator.png[hpp-operator components]

.HPP Operator components
[cols="1,1"]
|===
|*Component* |*Description*

|`deployment/hpp-pool-hpp-csi-pvc-block-<worker_node_name>`
|Provides a worker for each node where the HPP is designated to run. The pods mount the specified backing storage on the node.

|`daemonset/hostpath-provisioner-csi`
|Implements the Container Storage Interface (CSI) driver interface of the HPP.

|`daemonset/hostpath-provisioner`
|Implements the legacy driver interface of the HPP.
|===
