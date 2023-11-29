// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-updating-gitops.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-roll-out-the-configuration-changes_{context}"]
= Rolling out the {ztp} configuration changes

If any configuration changes were included in the upgrade due to implementing recommended changes, the upgrade process results in a set of policy CRs on the hub cluster in the `Non-Compliant` state. With the {ztp-first} version 4.10 and later `ztp-site-generate` container, these policies are set to `inform` mode and are not pushed to the managed clusters without an additional step by the user. This ensures that potentially disruptive changes to the clusters can be managed in terms of when the changes are made, for example, during a maintenance window, and how many clusters are updated concurrently.

To roll out the changes, create one or more `ClusterGroupUpgrade` CRs as detailed in the {cgu-operator} documentation. The CR must contain the list of `Non-Compliant` policies that you want to push out to the managed clusters as well as a list or selector of which clusters should be included in the update.
