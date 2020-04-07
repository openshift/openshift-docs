// Module included in the following assemblies:
//
// * nodes/nodes-nodes-resources-configuring.adoc

[id="nodes-nodes-resources-configuring-setting_{context}"]
= Viewing Node Allocatable Resources and Capacity

As an administrator, you can view the current capacity and allocatable resources of a specific node.

.Procedure

To see a node's current capacity and allocatable resources:

. Run the following command:

----
$ oc get node/<node_name> -o yaml
----

. Locate the following section in the output:
+
[source,yaml]
----
...
status:
...
  allocatable:
    cpu: "4"
    memory: 8010948Ki
    pods: "110"
  capacity:
    cpu: "4"
    memory: 8010948Ki
    pods: "110"
...
----
