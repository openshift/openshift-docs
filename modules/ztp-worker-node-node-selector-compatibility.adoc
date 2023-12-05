// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-sno-additional-worker-node.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-additional-worker-node-selector-comp_{context}"]
= PTP and SR-IOV node selector compatibility

The PTP configuration resources and SR-IOV network node policies use `node-role.kubernetes.io/master: ""` as the node selector. If the additional worker nodes have the same NIC configuration as the control plane node, the policies used to configure the control plane node can be reused for the worker nodes. However, the node selector must be changed to select both node types, for example with the `"node-role.kubernetes.io/worker"` label.
