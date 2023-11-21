// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-service-virtctl_{context}"]
= Creating a service by using virtctl

You can create a service for a virtual machine (VM) by using the `virtctl` command line tool.

.Prerequisites

* You installed the `virtctl` command line tool.
* You configured the cluster network to support the service.
* The environment where you installed `virtctl` has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable.

.Procedure

* Create a service by running the following command:
+
[source,terminal]
----
$ virtctl expose vm <vm_name> --name <service_name> --type <service_type> --port <port> <1>
----
<1> Specify the `ClusterIP`, `NodePort`, or `LoadBalancer` service type.
+
.Example
+
[source,terminal]
----
$ virtctl expose vm example-vm --name example-service --type NodePort --port 22
----

.Verification

* Verify the service by running the following command:
+
[source,terminal]
----
$ oc get service
----