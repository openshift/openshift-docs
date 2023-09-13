// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-troubleshooting_{context}"]
= Troubleshooting Operator groups

[discrete]
[id="olm-operatorgroups-troubleshooting-membership_{context}"]
=== Membership

* An install plan's namespace must contain only one Operator group. When attempting to generate a cluster service version (CSV) in a namespace, an install plan considers an Operator group invalid in the following scenarios:
+
--
** No Operator groups exist in the install plan's namespace.
** Multiple Operator groups exist in the install plan's namespace.
** An incorrect or non-existent service account name is specified in the Operator group.
--
+
If an install plan encounters an invalid Operator group, the CSV is not generated and the `InstallPlan` resource continues to install with a relevant message. For example, the following message is provided if more than one Operator group exists in the same namespace:
+
[source,terminal]
----
attenuated service account query failed - more than one operator group(s) are managing this namespace count=2
----
+
where `count=` specifies the number of Operator groups in the namespace.

* If the install modes of a CSV do not support the target namespace selection of the Operator group in its namespace, the CSV transitions to a failure state with the reason `UnsupportedOperatorGroup`. CSVs in a failed state for this reason transition to pending after either the target namespace selection of the Operator group changes to a supported configuration, or the install modes of the CSV are modified to support the target namespace selection.
