// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-target-namespace_{context}"]
= Target namespace selection

You can explicitly name the target namespace for an Operator group using the `spec.targetNamespaces` parameter:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
spec:
  targetNamespaces:
  - my-namespace
----

You can alternatively specify a namespace using a label selector with the `spec.selector` parameter:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
spec:
  selector:
    cool.io/prod: "true"
----

[IMPORTANT]
====
Listing multiple namespaces via `spec.targetNamespaces` or use of a label selector via `spec.selector` is not recommended, as the support for more than one target namespace in an Operator group will likely be removed in a future release.
====

If both `spec.targetNamespaces` and `spec.selector` are defined, `spec.selector` is ignored. Alternatively, you can omit both `spec.selector` and `spec.targetNamespaces` to specify a _global_ Operator group, which selects all namespaces:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
----

The resolved set of selected namespaces is shown in the `status.namespaces` parameter of an Opeator group. The `status.namespace` of a global Operator group contains the empty string (`""`), which signals to a consuming Operator that it should watch all namespaces.
