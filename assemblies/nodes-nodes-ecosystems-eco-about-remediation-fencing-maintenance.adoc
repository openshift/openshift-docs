:_mod-docs-content-type: ASSEMBLY
[id="about-remediation-fencing-maintenance"]
= About node remediation, fencing, and maintenance
include::_attributes/common-attributes.adoc[]
:context: about-node-remediation-fencing-maintenance

toc::[]

Hardware is imperfect and software contains bugs. When node-level failures, such as the kernel hangs or network interface controllers (NICs) fail, the work required from the cluster does not decrease, and workloads from affected nodes need to be restarted somewhere. However, some workloads, such as ReadWriteOnce (RWO) volumes and StatefulSets, might require at-most-one semantics.

Failures affecting these workloads risk data loss, corruption, or both. It is important to ensure that the node reaches a safe state, known as `fencing` before initiating recovery of the workload, known as `remediation` and ideally, recovery of the node also.

It is not always practical to depend on administrator intervention to confirm the true status of the nodes and workloads. To facilitate such intervention, {product-title} provides multiple components for the automation of failure detection, fencing and remediation.

[id="about-remediation-fencing-maintenance-snr"]
== Self Node Remediation

The Self Node Remediation Operator is an {product-title} add-on operator which implements an external system of fencing and remediation that reboots unhealthy nodes and deletes resources, such as, Pods and VolumeAttachments. The reboot ensures that the workloads are fenced, and the resource deletion accelerates the rescheduling of affected workloads. Unlike other external systems, Self Node Remediation does not require any management interface, like, for example, Intelligent Platform Management Interface (IPMI) or an API for node provisioning.

Self Node Remediation can be used by failure detection systems, like Machine Health Check or Node Health Check.

[id="about-remediation-fencing-maintenance-mhc"]
== Machine Health Check

Machine Health Check utilizes an {product-title} built-in failure detection, fencing and remediation system, which monitors the status of machines and the conditions of nodes. Machine Health Checks can be configured to trigger external fencing and remediation systems, like Self Node Remediation.

[id="about-remediation-fencing-maintenance-nhc"]
== Node Health Check

The Node Health Check Operator is an {product-title} add-on operator which implements a failure detection system that monitors node conditions. It does not have a built-in fencing or remediation system and so must be configured with an external system that provides such features. By default, it is configured to utilize the Self Node Remediation system.

[id="about-remediation-fencing-maintenance-node"]
== Node Maintenance

Administrators face situations where they need to interrupt the cluster, for example, replace a drive, RAM, or a NIC.

In advance of this maintenance, affected nodes should be cordoned and drained. When a node is cordoned, new workloads cannot be scheduled on that node. When a node is drained, to avoid or minimize downtime, workloads on the affected node are transferred to other nodes.

While this maintenance can be achieved using command line tools, the Node Maintenance Operator offers a declarative approach to achieve this by using a custom resource. When such a resource exists for a node, the operator cordons and drains the node until the resource is deleted.
