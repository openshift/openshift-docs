// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-membership_{context}"]
= Operator group membership

An Operator is considered a _member_ of an Operator group if the following conditions are true:

* The CSV of the Operator exists in the same namespace as the Operator group.
* The install modes in the CSV of the Operator support the set of namespaces targeted by the Operator group.

An install mode in a CSV consists of an `InstallModeType` field and a boolean `Supported` field. The spec of a CSV can contain a set of install modes of four distinct `InstallModeTypes`:

.Install modes and supported Operator groups
[cols="1,2",options="header"]
|===
|InstallModeType |Description

|`OwnNamespace`
|The Operator can be a member of an Operator group that selects its own namespace.

|`SingleNamespace`
|The Operator can be a member of an Operator group that selects one namespace.

|`MultiNamespace`
|The Operator can be a member of an Operator group that selects more than one namespace.

|`AllNamespaces`
|The Operator can be a member of an Operator group that selects all namespaces (target namespace set is the empty string `""`).
|===

[NOTE]
====
If the spec of a CSV omits an entry of `InstallModeType`, then that type is considered unsupported unless support can be inferred by an existing entry that implicitly supports it.
====
