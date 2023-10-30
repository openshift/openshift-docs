// Module included in the following assemblies:
//
// * nodes/nodes/eco-node-health-check-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="control-plane-fencing-node-health-check-operator_{context}"]
= Control plane fencing

In earlier releases, you could enable Self Node Remediation and Node Health Check on worker nodes. In the event of node failure, you can now also follow remediation strategies on control plane nodes.

Do not use the same `NodeHealthCheck` CR for worker nodes and control plane nodes. Grouping worker nodes and control plane nodes together can result in incorrect evaluation of the minimum healthy node count, and cause unexpected or missing remediations. This is because of the way the Node Health Check Operator handles control plane nodes. You should group the control plane nodes in their own group and the worker nodes in their own group. If required, you can also create multiple groups of worker nodes.

Considerations for remediation strategies:

* Avoid Node Health Check configurations that involve multiple configurations overlapping the same nodes because they can result in unexpected behavior. This suggestion applies to both worker and control plane nodes.
* The Node Health Check Operator implements a hardcoded limitation of remediating a maximum of one control plane node at a time. Multiple control plane nodes should not be remediated at the same time.
