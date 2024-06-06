// Module included in the following assemblies:
//
// * operators/admin/olm-upgrading-operators.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-preparing-upgrade_{context}"]
= Preparing for an Operator update

The subscription of an installed Operator specifies an update channel that tracks and receives updates for the Operator. You can change the update channel to start tracking and receiving updates from a newer channel.

The names of update channels in a subscription can differ between Operators, but the naming scheme typically follows a common convention within a given Operator. For example, channel names might follow a minor release update stream for the application provided by the Operator (`1.2`, `1.3`) or a release frequency (`stable`, `fast`).

[NOTE]
====
You cannot change installed Operators to a channel that is older than the current channel.
====

Red Hat Customer Portal Labs include the following application that helps administrators prepare to update their Operators:

* link:https://access.redhat.com/labs/ocpouic/[Red Hat OpenShift Container Platform Operator Update Information Checker]

You can use the application to search for Operator Lifecycle Manager-based Operators and verify the available Operator version per update channel across different versions of {product-title}. Cluster Version Operator-based Operators are not included.
