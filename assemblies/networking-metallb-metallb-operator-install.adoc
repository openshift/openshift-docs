:_mod-docs-content-type: ASSEMBLY
[id="metallb-operator-install"]
= Installing the MetalLB Operator
include::_attributes/common-attributes.adoc[]
:context: metallb-operator-install

toc::[]

As a cluster administrator, you can add the MetallB Operator so that the Operator can manage the lifecycle for an instance of MetalLB on your cluster.

MetalLB and IP failover are incompatible. If you configured IP failover for your cluster, perform the steps to xref:../../networking/configuring-ipfailover.adoc#nw-ipfailover-remove_configuring-ipfailover[remove IP failover] before you install the Operator.


// Install the Operator with console
include::modules/metallb-installing-using-web-console.adoc[leveloffset=+1]

// Install the Operator with CLI
include::modules/nw-metallb-installing-operator-cli.adoc[leveloffset=+1]

// Starting MetalLB on your cluster
include::modules/nw-metallb-operator-initial-config.adoc[leveloffset=+1]

// Deployment specifications for metallb CR
include::modules/nw-metallb-operator-deployment-specifications-for-metallb.adoc[leveloffset=+1]

// Deployment specs to limit speaker pods to specific nodes
include::modules/nw-metallb-operator-limit-speaker-to-nodes.adoc[leveloffset=+2]

// Deployment specs to set RuntimeClass
include::modules/nw-metallb-operator-setting-runtimeclass.adoc[leveloffset=+2]

// Deployment specs to set pod priority and pod affinity
include::modules/nw-metallb-operator-setting-pod-priority-affinity.adoc[leveloffset=+2]

// Deployment specs to set pod CPU limits
include::modules/nw-metallb-operator-setting-pod-CPU-limits.adoc[leveloffset=+2]



[role="_additional-resources"]
[id="additional-resources_metallb-operator-install"]
== Additional resources

* xref:../../nodes/scheduling/nodes-scheduler-node-selectors.adoc#nodes-scheduler-node-selectors[Placing pods on specific nodes using node selectors]
* xref:../../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations-about[Understanding taints and tolerations]
* xref:../../nodes/pods/nodes-pods-priority.adoc#nodes-pods-priority-about_nodes-pods-priority[Understanding pod priority]
* xref:../../nodes/scheduling/nodes-scheduler-pod-affinity.adoc#nodes-scheduler-pod-affinity-about_nodes-scheduler-pod-affinity[Understanding pod affinity]

[id="next-steps_{context}"]
== Next steps

* xref:../../networking/metallb/metallb-configure-address-pools.adoc#metallb-configure-address-pools[Configuring MetalLB address pools]
