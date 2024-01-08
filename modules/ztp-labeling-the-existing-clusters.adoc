// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-labeling-the-existing-clusters_{context}"]
= Labeling the existing clusters

To ensure that existing clusters remain untouched by the tool updates, label all existing managed clusters with the `ztp-done` label.

[NOTE]
====
This procedure only applies when updating clusters that were not provisioned with {cgu-operator-first}. Clusters that you provision with {cgu-operator} are automatically labeled with `ztp-done`.
====

.Procedure

. Find a label selector that lists the managed clusters that were deployed with {ztp-first}, such as `local-cluster!=true`:
+
[source,terminal]
----
$ oc get managedcluster -l 'local-cluster!=true'
----

. Ensure that the resulting list contains all the managed clusters that were deployed with {ztp}, and then use that selector to add the `ztp-done` label:
+
[source,terminal]
----
$ oc label managedcluster -l 'local-cluster!=true' ztp-done=
----
