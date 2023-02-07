// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-intersection_{context}"]
= Operator group intersection

Two Operator groups are said to have _intersecting provided APIs_ if the intersection of their target namespace sets is not an empty set and the intersection of their provided API sets, defined by `olm.providedAPIs` annotations, is not an empty set.

A potential issue is that Operator groups with intersecting provided APIs can compete for the same resources in the set of intersecting namespaces.

[NOTE]
====
When checking intersection rules, an Operator group namespace is always included as part of its selected target namespaces.
====

[discrete]
[id="olm-operatorgroups-intersection-rules_{context}"]
=== Rules for intersection

Each time an active member CSV synchronizes, OLM queries the cluster for the set of intersecting provided APIs between the Operator group of the CSV and all others. OLM then checks if that set is an empty set:

* If `true` and the CSV's provided APIs are a subset of the Operator group's:
** Continue transitioning.
* If `true` and the CSV's provided APIs are _not_ a subset of the Operator group's:
** If the Operator group is static:
*** Clean up any deployments that belong to the CSV.
*** Transition the CSV to a failed state with status reason
`CannotModifyStaticOperatorGroupProvidedAPIs`.
** If the Operator group is _not_ static:
*** Replace the Operator group's `olm.providedAPIs` annotation with the union of itself and the CSV's provided APIs.
* If `false` and the CSV's provided APIs are _not_ a subset of the Operator group's:
** Clean up any deployments that belong to the CSV.
** Transition the CSV to a failed state with status reason `InterOperatorGroupOwnerConflict`.
* If `false` and the CSV's provided APIs are a subset of the Operator group's:
** If the Operator group is static:
*** Clean up any deployments that belong to the CSV.
*** Transition the CSV to a failed state with status reason `CannotModifyStaticOperatorGroupProvidedAPIs`.
** If the Operator group is _not_ static:
*** Replace the Operator group's `olm.providedAPIs` annotation with the difference between itself and the CSV's provided APIs.

[NOTE]
====
Failure states caused by Operator groups are non-terminal.
====

The following actions are performed each time an Operator group synchronizes:

* The set of provided APIs from active member CSVs is calculated from the cluster. Note that copied CSVs are ignored.
* The cluster set is compared to `olm.providedAPIs`, and if `olm.providedAPIs` contains any extra APIs, then those APIs are pruned.
* All CSVs that provide the same APIs across all namespaces are requeued. This notifies conflicting CSVs in intersecting groups that their conflict has possibly been resolved, either through resizing or through deletion of the conflicting CSV.
