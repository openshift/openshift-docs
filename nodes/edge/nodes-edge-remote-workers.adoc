:_mod-docs-content-type: ASSEMBLY
:context: nodes-edge-remote-workers
[id="nodes-edge-remote-workers"]
= Using remote worker nodes at the network edge
include::_attributes/common-attributes.adoc[]

toc::[]


You can configure {product-title} clusters with nodes located at your network edge. In this topic, they are called _remote worker nodes_. A typical cluster with remote worker nodes combines on-premise master and worker nodes with worker nodes in other locations that connect to the cluster. This topic is intended to provide guidance on best practices for using remote worker nodes and does not contain specific configuration details.

There are multiple use cases across different industries, such as telecommunications, retail, manufacturing, and government, for using a deployment pattern with remote worker nodes. For example, you can separate and isolate your projects and workloads by combining the remote worker nodes into xref:../../nodes/edge/nodes-edge-remote-workers.adoc#nodes-edge-remote-workers-strategies-zones_nodes-edge-remote-workers[Kubernetes zones].

However, having remote worker nodes can introduce higher latency, intermittent loss of network connectivity, and other issues. Among the challenges in a cluster with remote worker node are:

* *Network separation*: The {product-title} control plane and the remote worker nodes must be able communicate with each other. Because of the distance between the control plane and the remote worker nodes, network issues could prevent this communication. See xref:../../nodes/edge/nodes-edge-remote-workers.adoc#nodes-edge-remote-workers-network_nodes-edge-remote-workers[Network separation with remote worker nodes] for information on how {product-title} responds to network separation and for methods to diminish the impact to your cluster.

* *Power outage*: Because the control plane and remote worker nodes are in separate locations, a power outage at the remote location or at any point between the two can negatively impact your cluster. See xref:../../nodes/edge/nodes-edge-remote-workers.adoc#nodes-edge-remote-workers-power_nodes-edge-remote-workers[Power loss on remote worker nodes] for information on how {product-title} responds to a node losing power and for methods to diminish the impact to your cluster.

* *Latency spikes or temporary reduction in throughput*: As with any network, any changes in network conditions between your cluster and the remote worker nodes can negatively impact your cluster. {product-title} offers multiple _worker latency profiles_ that let you control the reaction of the cluster to latency issues.

Note the following limitations when planning a cluster with remote worker nodes:

* {product-title} does not support remote worker nodes that use a different cloud provider than the on-premise cluster uses.

* Moving workloads from one Kubernetes zone to a different Kubernetes zone can be problematic due to system and environment issues, such as a specific type of memory not being available in a different zone.

* Proxies and firewalls can present additional limitations that are beyond the scope of this document. See the relevant {product-title} documentation for how to address such limitations, such as xref:../../installing/install_config/configuring-firewall.adoc#configuring-firewall[Configuring your firewall].

* You are responsible for configuring and maintaining L2/L3-level network connectivity between the control plane and the network-edge nodes.

include::modules/nodes-rwn_con_adding-remote-worker-nodes.adoc[leveloffset=+1]

.Additional resources

* xref:../../installing/installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#ipi-install-establishing-communication-between-subnets_ipi-install-installation-workflow[Establishing communications between subnets]

* xref:../../installing/installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#ipi-install-configuring-host-network-interfaces-for-subnets_ipi-install-installation-workflow[Configuring host network interfaces for subnets]

* xref:../../installing/installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#configure-network-components-to-run-on-the-control-plane_ipi-install-installation-workflow[Configuring network components to run on the control plane]


include::modules/nodes-edge-remote-workers-network.adoc[leveloffset=+1]

For more information on using these objects in a cluster with remote worker nodes, see xref:../../nodes/edge/nodes-edge-remote-workers.adoc#nodes-edge-remote-workers-strategies_nodes-edge-remote-workers[About remote worker node strategies].

include::modules/nodes-edge-remote-workers-power.adoc[leveloffset=+1]

For more information on using these objects in a cluster with remote worker nodes, see xref:../../nodes/edge/nodes-edge-remote-workers.adoc#nodes-edge-remote-workers-strategies_nodes-edge-remote-workers[About remote worker node strategies].

[id="nodes-edge-remote-workers-latency"]
== Latency spikes or temporary reduction in throughput to remote workers

include::snippets/worker-latency-profile-intro.adoc[]

.Additional resources

* xref:../../nodes/clusters/nodes-cluster-worker-latency-profiles.adoc#nodes-cluster-worker-latency-profiles[Improving cluster stability in high latency environments using worker latency profiles ]

include::modules/nodes-edge-remote-workers-strategies.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* For more information on Daemonesets, see xref:../../nodes/jobs/nodes-pods-daemonsets.adoc#nodes-pods-daemonsets[DaemonSets].

* For more information on  taints and tolerations, see xref:../../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations[Controlling pod placement using node taints].

* For more information on configuring `KubeletConfig` objects, see xref:../../post_installation_configuration/node-tasks.adoc#create-a-kubeletconfig-crd-to-edit-kubelet-parameters_post-install-node-tasks[Creating a KubeletConfig CRD].

* For more information on replica sets, see xref:../../applications/deployments/what-deployments-are.adoc#deployments-repliasets_what-deployments-are[ReplicaSets].

* For more information on deployments, see xref:../../applications/deployments/what-deployments-are.adoc#deployments-kube-deployments_what-deployments-are[Deployments].

* For more information on replication controllers, see xref:../../applications/deployments/what-deployments-are.adoc#deployments-replicationcontrollers_what-deployments-are[Replication controllers].

* For more information on the controller manager, see xref:../../operators/operator-reference.adoc#kube-controller-manager-operator_cluster-operators-ref[Kubernetes Controller Manager Operator].

