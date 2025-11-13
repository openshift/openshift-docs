// Module included in the following assemblies:
//
// * logging/nodes-edge-remote-workers.adoc

[id="nodes-edge-remote-workers-network_{context}"]
= Network separation with remote worker nodes

All nodes send heartbeats to the Kubernetes Controller Manager Operator (kube controller) in the {product-title} cluster every 10 seconds. If the cluster does not receive heartbeats from a node, {product-title} responds using several default mechanisms.
 
{product-title} is designed to be resilient to network partitions and other disruptions. You can mitigate some of the more common disruptions, such as interruptions from software upgrades, network splits, and routing issues. Mitigation strategies include ensuring that pods on remote worker nodes request the correct amount of CPU and memory resources, configuring an appropriate replication policy, using redundancy across zones, and using Pod Disruption Budgets on workloads. 

If the kube controller loses contact with a node after a configured period, the node controller on the control plane updates the node health to `Unhealthy` and marks the node `Ready` condition as `Unknown`. In response, the scheduler stops scheduling pods to that node. The on-premise node controller adds a `node.kubernetes.io/unreachable` taint with a `NoExecute` effect to the node and schedules pods on the node for eviction after five minutes, by default.  

If a workload controller, such as a `Deployment` object or `StatefulSet` object, is directing traffic to pods on the unhealthy node and other nodes can reach the cluster, {product-title} routes the traffic away from the pods on the node. Nodes that cannot reach the cluster do not get updated with the new traffic routing. As a result, the workloads on those nodes might continue to attempt to reach the unhealthy node.

You can mitigate the effects of connection loss by: 

* using daemon sets to create pods that tolerate the taints
* using static pods that automatically restart if a node goes down
* using Kubernetes zones to control pod eviction
* configuring pod tolerations to delay or avoid pod eviction
* configuring the kubelet to control the timing of when it marks nodes as unhealthy. 
