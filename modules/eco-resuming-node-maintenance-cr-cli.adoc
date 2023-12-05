// Module included in the following assemblies:
//
//nodes/nodes/eco-node-maintenance-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="eco-resuming-node-from-maintenance-mode-with-cr_{context}"]
= Resuming a node from maintenance mode by using the CLI

You can resume a node from maintenance mode that was initiated with a `NodeMaintenance` CR by deleting the `NodeMaintenance` CR.

.Prerequisites

* Install the {product-title} CLI `oc`.
* Log in to the cluster as a user with `cluster-admin` privileges.

.Procedure

* When your node maintenance task is complete, delete the active `NodeMaintenance` CR:
+
[source,terminal]
----
$ oc delete -f nodemaintenance-cr.yaml
----
+
.Example output
+
[source,terminal]
----
nodemaintenance.nodemaintenance.medik8s.io "maintenance-example" deleted
----

.Verification

. Check the progress of the maintenance task by running the following command:
+
[source,terminal]
----
$ oc describe node <node-name>
----
+
where `<node-name>` is the name of your node; for example, `node-1.example.com`

. Check the example output:
+
[source,terminal]
----
Events:
  Type     Reason                  Age                   From     Message
  ----     ------                  ----                  ----     -------
  Normal   NodeSchedulable         2m                    kubelet  Node node-1.example.com status is now: NodeSchedulable
----
