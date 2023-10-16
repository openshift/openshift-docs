// Module included in the following assemblies:
//
// * authentication/understanding-authentication.adoc

[id="rbac-groups_{context}"]
= Groups

A user can be assigned to one or more _groups_, each of which represent a
certain set of users. Groups are useful when managing authorization policies
to grant permissions to multiple users at once, for example allowing
access to objects within a project, versus granting
them to users individually.

In addition to explicitly defined groups, there are also
system groups, or _virtual groups_, that are automatically provisioned by
the cluster.

The following default virtual groups are most important:

//WHY?

[cols="2,5",options="header"]
|===

|Virtual group |Description

|`system:authenticated` |Automatically associated with all authenticated users.
|`system:authenticated:oauth` |Automatically associated with all users authenticated with an OAuth access token.
|`system:unauthenticated` |Automatically associated with all unauthenticated users.

|===
