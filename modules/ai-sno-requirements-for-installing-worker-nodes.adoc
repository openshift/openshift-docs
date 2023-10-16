// This is included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="ai-sno-requirements-for-installing-worker-nodes_{context}"]
= Requirements for installing {sno} worker nodes

To install a {sno} worker node, you must address the following requirements:

* *Administration host:* You must have a computer to prepare the ISO and to monitor the installation.

* *Production-grade server:* Installing {sno} worker nodes requires a server with sufficient resources to run {product-title} services and a production workload.
+
.Minimum resource requirements
[options="header"]
|====

|Profile|vCPU|Memory|Storage

|Minimum|2 vCPU cores|8GB of RAM| 100GB

|====
+
[NOTE]
====
One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or hyperthreading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio:

(threads per core × cores) × sockets = vCPUs
====
+
The server must have a Baseboard Management Controller (BMC) when booting with virtual media.

* *Networking:* The worker node server must have access to the internet or access to a local registry if it is not connected to a routable network. The worker node server must have a DHCP reservation or a static IP address and be able to access the {sno} cluster Kubernetes API, ingress route, and cluster node domain names. You must configure the DNS to resolve the IP address to each of the following fully qualified domain names (FQDN) for the {sno} cluster:
+
.Required DNS records
[options="header"]
|====

|Usage|FQDN|Description

|Kubernetes API|`api.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record. This record must be resolvable by clients external to the cluster.

|Internal API|`api-int.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record when creating the ISO manually. This record must be resolvable by nodes within the cluster.

|Ingress route|`*.apps.<cluster_name>.<base_domain>`| Add a wildcard DNS A/AAAA or CNAME record that targets the node. This record must be resolvable by clients external to the cluster.

|====
+
Without persistent IP addresses, communications between the `apiserver` and `etcd` might fail.
