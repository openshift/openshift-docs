# Requirements for installing OpenShift on a single node

Installing {product-title} on a single node alleviates some of the requirements for high availability and large scale clusters. However, you must address the following requirements:

* **Administration host:** You must have a computer to prepare the ISO, to create the USB boot drive, and to monitor the installation.
* **CPU Architecture:** Installing {product-title} on a single node supports `x86_64` and `arm64` CPU architectures.
* **Supported platforms:** Installing {product-title} on a single node is supported on bare metal, vSphere, AWS, Red Hat OpenStack, and {rh-virtualization-first} platforms.
* **Production-grade server:** Installing {product-title} on a single node requires a server with sufficient resources to run {product-title} services and a production workload.

  **Minimum resource requirements**

  |====
  |Profile|vCPU|Memory|Storage
  |Minimum|8 vCPU cores|16GB of RAM| 120GB
  |====

  <dl><dt><strong>📌 NOTE</strong></dt><dd>

  * One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or hyperthreading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio:

    (threads per core × cores) × sockets = vCPUs
  * Adding Operators during the installation process might increase the minimum resource requirements.
  </dd></dl>

  The server must have a Baseboard Management Controller (BMC) when booting with virtual media. 
* **Networking:** The server must have access to the internet or access to a local registry if it is not connected to a routable network. The server must have a DHCP reservation or a static IP address for the Kubernetes API, ingress route, and cluster node domain names. You must configure the DNS to resolve the IP address to each of the following fully qualified domain names (FQDN):

  **Required DNS records**

  |====
  |Usage|FQDN|Description
  |Kubernetes API|`api.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record. This record must be resolvable by clients external to the cluster.
  |Internal API|`api-int.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record when creating the ISO manually. This record must be resolvable by nodes within the cluster.
  |Ingress route|`*.apps.<cluster_name>.<base_domain>`| Add a wildcard DNS A/AAAA or CNAME record that targets the node. This record must be resolvable by clients external to the cluster.
  |====

  Without persistent IP addresses, communications between the `apiserver` and `etcd` might fail.
