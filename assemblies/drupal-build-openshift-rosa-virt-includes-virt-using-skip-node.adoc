// Module included in the following assembly:
//
// * virt/nodes/virt-preventing-node-reconciliation.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="virt-using-skip-node_{context}"]
= Using skip-node annotation

If you want the `node-labeller` to skip a node, annotate that node by using the `oc` CLI.

.Prerequisites
* You have installed the OpenShift CLI (`oc`).

.Procedure

* Annotate the node that you want to skip by running the following command:

+
[source,terminal]
----
$ oc annotate node <node_name> node-labeller.kubevirt.io/skip-node=true <1>
----
<1> Replace `<node_name>` with the name of the relevant node to skip.
+
Reconciliation resumes on the next cycle after the node annotation is removed or set to false.
