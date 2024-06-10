// Module included in the following assemblies:
//
// * operators/admin/olm-managing-operatorconditions.adoc

[id="olm-updating-use-operatorconditions_{context}"]
= Updating your Operator to use Operator conditions

Operator Lifecycle Manager (OLM) automatically creates an `OperatorCondition` resource for each `ClusterServiceVersion` resource that it reconciles. All service accounts in the CSV are granted the RBAC to interact with the `OperatorCondition` owned by the Operator.

An Operator author can develop their Operator to use the `operator-lib` library such that, after the Operator has been deployed by OLM, it can set its own conditions. For more resources about setting Operator conditions as an Operator author, see the link:https://docs.openshift.com/container-platform/4.12/operators/operator_sdk/osdk-generating-csvs.html#osdk-operatorconditions_osdk-generating-csvs[Enabling Operator conditions] page.

[id="olm-updating-use-operatorconditions-defaults_{context}"]
== Setting defaults

In an effort to remain backwards compatible, OLM treats the absence of an `OperatorCondition` resource as opting out of the condition. Therefore, an Operator that opts in to using Operator conditions should set default conditions before the ready probe for the pod is set to `true`. This provides the Operator with a grace period to update the condition to the correct state.
