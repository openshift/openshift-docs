// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc

[id="cluster-machine-approver-operator_{context}"]
= Cluster Machine Approver Operator

[discrete]
== Purpose

The Cluster Machine Approver Operator automatically approves the CSRs requested for a new worker node after cluster installation.

[NOTE]
====
For the control plane node, the `approve-csr` service on the bootstrap node automatically approves all CSRs during the cluster bootstrapping phase.
====

[discrete]
== Project

link:https://github.com/openshift/cluster-machine-approver[cluster-machine-approver-operator]
