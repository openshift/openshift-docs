# About OpenShift on a single node

You can create a single-node cluster with standard installation methods. {product-title} on a single node is a specialized installation that requires the creation of a special ignition configuration ISO. The primary use case is for edge computing workloads, including intermittent connectivity, portable clouds, and 5G radio access networks (RAN) close to a base station. The major tradeoff with an installation on a single node is the lack of high availability.

<dl><dt><strong>❗ IMPORTANT</strong></dt><dd>

The use of OpenShiftSDN with {sno} is not supported. OVN-Kubernetes is the default network plugin for {sno} deployments.
</dd></dl>
