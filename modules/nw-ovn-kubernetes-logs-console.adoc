// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ovn-kubernetes-logs-console_{context}"]
= Viewing the OVN-Kubernetes logs using the web console

You can view the logs for each of the pods in the `ovnkube-master` and `ovnkube-node` pods in the web console.

.Prerequisites

* Access to the OpenShift CLI (`oc`).

.Procedure

. In the {product-title} console, navigate to *Workloads* -> *Pods* or navigate to the pod through the resource you want to investigate.

. Select the `openshift-ovn-kubernetes` project from the drop-down menu.

. Click the name of the pod you want to investigate.

. Click *Logs*. By default for the `ovnkube-master` the logs associated with the `northd` container are displayed.

. Use the down-down menu to select logs for each container in turn.