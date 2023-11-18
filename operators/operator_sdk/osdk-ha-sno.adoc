:_mod-docs-content-type: ASSEMBLY
[id="osdk-ha-sno"]
= High-availability or single-node cluster detection and support
include::_attributes/common-attributes.adoc[]
:context: osdk-ha-sno

toc::[]

// OSD/ROSA don't support single-node clusters, but these Operator authors still need to know how to handle this configuration for their Operators to work correctly in OCP.
ifdef::openshift-dedicated,openshift-rosa[]
To ensure that your Operator runs well on both high-availability (HA) and non-HA modes in OpenShift Container Platform clusters, you can use the Operator SDK to detect the cluster's infrastructure topology and set the resource requirements to fit the cluster's topology.
endif::openshift-dedicated,openshift-rosa[]

// Not using {product-title} here, because HA mode and non-HA mode are specific to OCP and should be spelled out this way in other distros.
An OpenShift Container Platform cluster can be configured in high-availability (HA) mode, which uses multiple nodes, or in non-HA mode, which uses a single node. A single-node cluster, also known as {sno}, is likely to have more conservative resource constraints. Therefore, it is important that Operators installed on a single-node cluster can adjust accordingly and still run well.

By accessing the cluster high-availability mode API provided in {product-title}, Operator authors can use the Operator SDK to enable their Operator to detect a cluster's infrastructure topology, either HA or non-HA mode. Custom Operator logic can be developed that uses the detected cluster topology to automatically switch the resource requirements, both for the Operator and for any Operands or workloads it manages, to a profile that best fits the topology.

include::modules/osdk-ha-sno-api.adoc[leveloffset=+1]
include::modules/osdk-ha-sno-api-examples.adoc[leveloffset=+1]
