:_mod-docs-content-type: ASSEMBLY
:telco-core:
[id="telco-ran-rds-overview"]
= {rds-caps} {product-version} use model overview
:context: ran-core-design-overview
include::_attributes/common-attributes.adoc[]

toc::[]

The {rds-caps} reference design specification (RDS) describes a platform that supports large-scale telco applications including control plane functions such as signaling and aggregation. It also includes some centralized data plane functions, for example, user plane functions (UPF). These functions generally require scalability, complex networking support, resilient software-defined storage, and support performance requirements that are less stringent and constrained than far-edge deployments like RAN.

.Telco core use model architecture
image:473_OpenShift_Telco_Core_Reference_arch_1123.png[Use model architecture]

The networking prerequisites for {rds} functions are diverse and encompass an array of networking attributes and performance benchmarks. IPv6 is mandatory, with dual-stack configurations being prevalent. Certain functions demand maximum throughput and transaction rates, necessitating user plane networking support such as DPDK. Other functions adhere to conventional cloud-native patterns and can use solutions such as OVN-K, kernel networking, and load balancing.

{rds-caps} clusters are configured as standard three control plane clusters with worker nodes configured with the stock non real-time (RT) kernel. To support workloads with varying networking and performance requirements, worker nodes are segmented using `MachineConfigPool` CRs. For example, this is done to separate non-user data plane nodes from high-throughput nodes. To support the required telco operational features, the clusters have a standard set of Operator Lifecycle Manager (OLM) Day 2 Operators installed.

include::modules/telco-core-ref-design-baseline-model.adoc[leveloffset=+1]

include::modules/telco-core-ref-eng-usecase-model.adoc[leveloffset=+2]

include::modules/telco-core-ref-application-workloads.adoc[leveloffset=+2]

:!telco-core:

