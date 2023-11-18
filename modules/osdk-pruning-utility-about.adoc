// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-pruning-utility.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-about-pruning-utility_{context}"]
= About the operator-lib pruning utility

Objects, such as jobs or pods, are created as a normal part of the Operator life cycle. If
ifndef::openshift-dedicated,openshift-rosa[]
the cluster administrator
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
an administrator with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
or the Operator does not remove these object, they can stay in the cluster and consume resources.

Previously, the following options were available for pruning unnecessary objects:

* Operator authors had to create a unique pruning solution for their Operators.
* Cluster administrators had to clean up objects on their own.

The `operator-lib` link:https://github.com/operator-framework/operator-lib/tree/main/prune[pruning utility] removes objects from a Kubernetes cluster for a given namespace. The library was added in version `0.9.0` of the link:https://github.com/operator-framework/operator-lib/releases/tag/v0.9.0[`operator-lib` library] as part of the Operator Framework.
