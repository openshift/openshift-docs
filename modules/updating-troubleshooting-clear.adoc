// Module included in the following assemblies:
//
// * updating/troubleshooting_updates/recovering-update-before-applied.adoc

[id="updating-troubleshooting-clear_{context}"]
= Recovering when an update fails before it is applied

If an update fails before it is applied, such as when the version that you specify cannot be found, you can cancel the update:

[source,terminal]
----
$ oc adm upgrade --clear
----

[IMPORTANT]
====
If an update fails at any other point, you must contact Red Hat support. Rolling your cluster back to a previous version is not supported.
====