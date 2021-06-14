// Module included in the following assemblies:
//
// * logging/nodes-edge-remote-workers.adoc

[id="nodes-edge-remote-workers-power_{context}"]
= Power loss on remote worker nodes

If a remote worker node loses power or restarts ungracefully, {product-title} responds using several default mechanisms. 

If the Kubernetes Controller Manager Operator (kube controller) loses contact with a node after a configured period, the control plane updates the node health to `Unhealthy` and marks the node `Ready` condition as `Unknown`. In response, the scheduler stops scheduling pods to that node.  The on-premise node controller adds a `node.kubernetes.io/unreachable` taint with a `NoExecute` effect to the node and schedules pods on the node for eviction after five minutes, by default.

On the node, the pods must be restarted when the node recovers power and reconnects with the control plane.

[NOTE]
====
If you want the pods to restart immediately upon restart, use static pods.
====

After the node restarts, the kubelet also restarts and attempts to restart the pods that were scheduled on the node. If the connection to the control plane takes longer than the default five minutes, the control plane cannot update the node health and remove the `node.kubernetes.io/unreachable` taint. On the node, the kubelet terminates any running pods. When these conditions are cleared, the scheduler can start scheduling pods to that node. 

You can mitigate the effects of power loss by: 

* using daemon sets to create pods that tolerate the taints
* using static pods that automatically restart with a node
* configuring pods tolerations to delay or avoid pod eviction
* configuring the kubelet to control the timing of when the node controller marks nodes as unhealthy. 

