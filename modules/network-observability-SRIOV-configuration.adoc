// Module included in the following assemblies:
//
// * network_observability/configuring-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="network-observability-SR-IOV-config_{context}"]
= Configuring monitoring for SR-IOV interface traffic
In order to collect traffic from a cluster with a Single Root I/O Virtualization (SR-IOV) device, you must set the `FlowCollector` `spec.agent.ebpf.privileged` field to `true`. Then, the eBPF agent monitors other network namespaces in addition to the host network namespaces, which are monitored by default. When a pod with a virtual functions (VF) interface is created, a new network namespace is created. With `SRIOVNetwork` policy `IPAM` configurations specified, the VF interface is migrated from the host network namespace to the pod network namespace.

.Prerequisites
* Access to an {product-title} cluster with a SR-IOV device.
* The `SRIOVNetwork` custom resource (CR) `spec.ipam` configuration must be set with an IP address from the range that the interface lists or from other plugins.

.Procedure
. In the web console, navigate to *Operators* -> *Installed Operators*.
. Under the *Provided APIs* heading for the *NetObserv Operator*, select *Flow Collector*.
. Select *cluster* and then select the *YAML* tab.
. Configure the `FlowCollector` custom resource. A sample configuration is as follows:
+
[id="network-observability-flowcollector-configuring-SRIOV-monitoring{context}"]
.Configure `FlowCollector` for SR-IOV monitoring
[source,yaml]
----
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: DIRECT
  agent:
    type: EBPF
    ebpf:
      privileged: true   <1>
----
<1> The `spec.agent.ebpf.privileged` field value must be set to `true` to enable SR-IOV monitoring.