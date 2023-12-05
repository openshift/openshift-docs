// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

:_mod-docs-content-type: PROCEDURE
[id="cnf-topology-aware-lifecycle-manager-operator-troubleshooting_{context}"]
= Troubleshooting missed Operator updates due to out-of-date policy compliance states

In some scenarios, {cgu-operator-first} might miss Operator updates due to an out-of-date policy compliance state.

After a catalog source update, it takes time for the Operator Lifecycle Manager (OLM) to update the subscription status. The status of the subscription policy might continue to show as compliant while {cgu-operator} decides whether remediation is needed. As a result, the Operator specified in the subscription policy does not get upgraded.

To avoid this scenario, add another catalog source configuration to the `PolicyGenTemplate` and specify this configuration in the subscription for any Operators that require an update.

.Procedure

. Add a catalog source configuration in the `PolicyGenTemplate` resource:
+
[source,yaml]
----
- fileName: DefaultCatsrc.yaml
      remediationAction: inform
      policyName: "operator-catsrc-policy"
      metadata:
        name: redhat-operators
      spec:
        displayName: Red Hat Operators Catalog
        image: registry.example.com:5000/olm/redhat-operators:v{product-version}
        updateStrategy:
          registryPoll:
            interval: 1h
      status:
        connectionState:
            lastObservedState: READY
- fileName: DefaultCatsrc.yaml
      remediationAction: inform
      policyName: "operator-catsrc-policy"
      metadata:
        name: redhat-operators-v2 <1>
      spec:
        displayName: Red Hat Operators Catalog v2 <2>
        image: registry.example.com:5000/olredhat-operators:<version> <3>
        updateStrategy:
          registryPoll:
            interval: 1h
      status:
        connectionState:
            lastObservedState: READY
----
<1> Update the name for the new configuration.
<2> Update the display name for the new configuration.
<3> Update the index image URL. This `fileName.spec.image` field overrides any configuration in the `DefaultCatsrc.yaml` file.

. Update the `Subscription` resource to point to the new configuration for Operators that require an update:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: operator-subscription
  namespace: operator-namspace
# ...
spec:
  source: redhat-operators-v2 <1>
# ...
----
<1> Enter the name of the additional catalog source configuration that you defined in the `PolicyGenTemplate` resource.
