:_mod-docs-content-type: CONCEPT
[id="ovn-kubernetes-logical-architecture-con_{context}"]
= OVN-Kubernetes logical architecture

OVN is a network virtualization solution. It creates logical switches and routers. These switches and routers are interconnected to create any network topologies. When you run `ovnkube-trace` with the log level set to 2 or 5 the OVN-Kubernetes logical components are exposed. The following diagram shows how the routers and switches are connected in {product-title}.

.OVN-Kubernetes router and switch components
image::299_OpenShift_OVN-Kubernetes_arch_1023_2.png[OVN-Kubernetes logical architecture]

The key components involved in packet processing are:

Gateway routers:: Gateway routers sometimes called L3 gateway routers, are typically used between the distributed routers and the physical network. Gateway routers including their logical patch ports are bound to a physical location (not distributed), or chassis. The patch ports on this router are known as l3gateway ports in the ovn-southbound database (`ovn-sbdb`).

Distributed logical routers:: Distributed logical routers and the logical switches behind them, to which virtual machines and containers attach, effectively reside on each hypervisor.

Join local switch:: Join local switches are used to connect the distributed router and gateway routers. It reduces the number of IP addresses needed on the distributed router.

Logical switches with patch ports:: Logical switches with patch ports are used to virtualize the network stack. They connect remote logical ports through tunnels.

Logical switches with localnet ports:: Logical switches with localnet ports are used to connect OVN to the physical network. They connect remote logical ports by bridging the packets to directly connected physical L2 segments using localnet ports.

Patch ports:: Patch ports represent connectivity between logical switches and logical routers and between peer logical routers. A single connection has a pair of patch ports at each such point of connectivity, one on each side.

l3gateway ports:: l3gateway ports are the port binding entries in the `ovn-sbdb` for logical patch ports used in the gateway routers. They are called l3gateway ports rather than patch ports just to portray the fact that these ports are bound to a chassis just like the gateway router itself.
localnet ports:: localnet ports are present on the bridged logical switches that allows a connection to a locally accessible network from each `ovn-controller` instance. This helps model the direct connectivity to the physical network from the logical switches. A logical switch can only have a single localnet port attached to it.