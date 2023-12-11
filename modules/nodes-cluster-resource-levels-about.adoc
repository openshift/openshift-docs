// Module included in the following assemblies:
//
// * nodes/nodes-cluster-resource-about.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-cluster-resource-levels-about_{context}"]
= Understanding the OpenShift Cluster Capacity Tool

The OpenShift Cluster Capacity Tool simulates a sequence of scheduling decisions to
determine how many instances of an input pod can be scheduled on the cluster
before it is exhausted of resources to provide a more accurate estimation.

[NOTE]
====
The remaining allocatable capacity is a rough estimation, because it does not
count all of the resources being distributed among nodes. It analyzes only the
remaining resources and estimates the available capacity that is still
consumable in terms of a number of instances of a pod with given requirements
that can be scheduled in a cluster.

Also, pods might only have scheduling support on particular sets of nodes based
on its selection and affinity criteria. As a result, the estimation of which
remaining pods a cluster can schedule can be difficult.
====

You can run the OpenShift Cluster Capacity Tool as a stand-alone utility from
the command line, or as a job in a pod inside an {product-title} cluster.
Running the tool as job inside of a pod enables you to run it multiple times without intervention.
