:_mod-docs-content-type: CONCEPT

[id="auto-reboot-during-argo-cd-sync-with-machine-configurations"]
= Issue: Auto-reboot during Argo CD sync with machine configurations

In the Red Hat OpenShift Container Platform, nodes are updated automatically through the Red Hat OpenShift Machine Config Operator (MCO). A Machine Config Operator (MCO) is a custom resource that is used by the cluster to manage the complete life cycle of its nodes.

When an MCO resource is created or updated in a cluster, the MCO picks up the update, performs the necessary changes to the selected nodes, and restarts the nodes gracefully by cordoning, draining, and rebooting those nodes. It handles everything from the kernel to the kubelet.

However, interactions between the MCO and the GitOps workflow can introduce major performance issues and other undesired behaviors. This section shows how to make the MCO and the Argo CD GitOps orchestration tool work well together.