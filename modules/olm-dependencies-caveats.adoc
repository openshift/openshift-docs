// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-dependency-resolution.adoc

[id="olm-dependency-caveats_{context}"]
= Dependency caveats

When specifying dependencies, there are caveats you should consider.

No compound constraints (AND)::
There is currently no method for specifying an AND relationship between constraints. In other words, there is no way to specify that one Operator depends on another Operator that both provides a given API and has version `>1.1.0`.
+
This means that when specifying a dependency such as:
+
[source,yaml]
----
dependencies:
- type: olm.package
  value:
    packageName: etcd
    version: ">3.1.0"
- type: olm.gvk
  value:
    group: etcd.database.coreos.com
    kind: EtcdCluster
    version: v1beta2
----
+
It would be possible for OLM to satisfy this with two Operators: one that provides EtcdCluster and one that has version `>3.1.0`. Whether that happens, or whether an Operator is selected that satisfies both constraints, depends on the ordering that potential options are visited. Dependency preferences and ordering options are well-defined and can be reasoned about, but to exercise caution, Operators should stick to one mechanism or the other.

Cross-namespace compatibility::
OLM performs dependency resolution at the namespace scope. It is possible to get into an update deadlock if updating an Operator in one namespace would be an issue for an Operator in another namespace, and vice-versa.
