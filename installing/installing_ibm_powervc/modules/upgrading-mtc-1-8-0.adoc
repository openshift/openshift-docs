// Module included in the following assemblies:
//
// * migration_toolkit_for_containers/upgrading-mtc.adoc

:_mod-docs-content-type: PROCEDURE
[id="migration-upgrading-mtc-18_{context}"]
= Upgrading the {mtc-full} to 1.8.0

To upgrade the {mtc-full} to 1.8.0, complete the following steps.

.Procedure

. Determine subscription names and current channels to work with for upgrading by using one of the following methods:

** Determine the subscription names and channels by running the following command:
+
[source,terminal]
----
$ oc -n openshift-migration get sub
----
+
.Example output
[source,terminal]
----
NAME                                                                         PACKAGE                SOURCE                 CHANNEL
mtc-operator                                                                 mtc-operator           mtc-operator-catalog   release-v1.7
redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace   redhat-oadp-operator   mtc-operator-catalog   stable-1.0
----

** Or return the subscription names and channels in JSON by running the following command:
+
[source,terminal]
----
$ oc -n openshift-migration get sub -o json | jq -r '.items[] | { name: .metadata.name, package: .spec.name, channel: .spec.channel }'
----
+
.Example output
[source,terminal]
----
{
  "name": "mtc-operator",
  "package": "mtc-operator",
  "channel": "release-v1.7"
}
{
  "name": "redhat-oadp-operator-stable-1.0-mtc-operator-catalog-openshift-marketplace",
  "package": "redhat-oadp-operator",
  "channel": "stable-1.0"
}
----

. For each subscription, patch to move from the {mtc-short} 1.7 channel to the {mtc-short} 1.8 channel by running the following command:
+
[source,terminal]
----
$ oc -n openshift-migration patch subscription mtc-operator --type merge --patch '{"spec": {"channel": "release-v1.8"}}'
----
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com/mtc-operator patched
----

