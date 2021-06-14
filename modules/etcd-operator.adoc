// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="etcd-cluster-operator_{context}"]
= etcd cluster Operator

[discrete]
== Purpose

The etcd cluster Operator automates etcd cluster scaling, enables etcd monitoring and metrics, and simplifies disaster recovery procedures.
[discrete]
== Project

link:https://github.com/openshift/cluster-etcd-operator/[cluster-etcd-operator]

[discrete]
== CRDs

* `etcds.operator.openshift.io`
** Scope: Cluster
** CR: `etcd`
** Validation: Yes

[discrete]
== Configuration objects

[source,terminal]
----
$ oc edit etcd cluster
----
