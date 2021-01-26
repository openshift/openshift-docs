// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

:operator-name: vSphere Problem Detector Operator

[id="vsphere-problem-detector-operator-metrics_{context}"]
= Metrics for the {operator-name}

The {operator-name} exposes the following metrics for use by the {product-title} monitoring stack.

.Metrics exposed by the {operator-name}
[cols="2a,8a",options="header"]
|===
|Name |Description

|`vsphere_cluster_check_total`
|Cumulative number of cluster-level checks that the {operator-name} performed. This count includes both successes and failures.

|`vsphere_cluster_check_errors`
|Number of failed cluster-level checks that the {operator-name} performed. For example, a value of `1` indicates that one cluster-level check failed.

|`vsphere_esxi_version_total`
|Number of ESXi hosts with a specific version. Be aware that if a host runs more than one node, the host is counted only once.

|`vsphere_node_check_total`
|Cumulative number of node-level checks that the {operator-name} performed. This count includes both successes and failures.

|`vsphere_node_check_errors`
|Number of failed node-level checks that the {operator-name} performed. For example, a value of `1` indicates that one node-level check failed.

|`vsphere_node_hw_version_total`
|Number of vSphere nodes with a specific hardware version.

|`vsphere_vcenter_info`
|Information about the vSphere vCenter Server.
|===

// Clear temporary attributes
:!operator-name:
