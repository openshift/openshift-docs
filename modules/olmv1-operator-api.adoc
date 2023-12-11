// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-plain-bundles.adoc

:_mod-docs-content-type: CONCEPT

[id="olmv1-operator-api"]
= Operator API

Operator Controller provides a new `Operator` API object, which is a single resource that represents an instance of an installed Operator. This `operator.operators.operatorframework.io` API streamlines management of installed Operators by consolidating user-facing APIs into a single object.

[IMPORTANT]
====
In {olmv1}, `Operator` objects are cluster-scoped. This differs from earlier OLM versions where Operators could be either namespace-scoped or cluster-scoped, depending on the configuration of their related `Subscription` and `OperatorGroup` objects.

For more information about the earlier behavior, see _Multitenancy and Operator colocation_.
====

.Example `Operator` object
[source,yaml]
----
apiVersion: operators.operatorframework.io/v1alpha1
kind: Operator
metadata:
  name: <operator_name>
spec:
  packageName: <package_name>
  channel: <channel_name>
  version: <version_number>
----

include::snippets/olmv1-operator-api-group.adoc[]