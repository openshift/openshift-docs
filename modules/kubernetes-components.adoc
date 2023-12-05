// Module included in the following assemblies:
//
// * getting_started/kubernetes-overview.adoc

:_mod-docs-content-type: REFERENCE
[id="kubernetes-components_{context}"]
= Kubernetes components

.Kubernetes components
[cols="1,2",options="header"]
|===
|Component |Purpose

|`kube-proxy`
|Runs on every node in the cluster and maintains the network traffic between the Kubernetes resources.

|`kube-controller-manager`
|Governs the state of the cluster.

|`kube-scheduler`
|Allocates pods to nodes.

|`etcd`
|Stores cluster data.

|`kube-apiserver`
|Validates and configures data for the API objects.

|`kubelet`
|Runs on nodes and reads the container manifests. Ensures that the defined containers have started and are running.

|`kubectl`
|Allows you to define how you want to run workloads. Use the `kubectl` command to interact with the `kube-apiserver`.

|Node
|Node is a physical machine or a VM in a Kubernetes cluster. The control plane manages every node and schedules pods across the nodes in the Kubernetes cluster.

|container runtime
|container runtime runs containers on a host operating system. You must install a container runtime on each node so that pods can run on the node.

|Persistent storage
|Stores the data even after the device is shut down. Kubernetes uses persistent volumes to store the application data.

|`container-registry`
|Stores and accesses the container images.

|Pod
|The pod is the smallest logical unit in Kubernetes. A pod contains one or more containers to run in a worker node.
|===
