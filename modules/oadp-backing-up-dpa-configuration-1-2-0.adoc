// Module included in the following assemblies:
//
// * backup_and_restore/oadp-release-notes-1-2.adoc

:_mod-docs-content-type: PROCEDURE

[id="oadp-backing-up-dpa-configuration-1-2-0_{context}"]
= Backing up the DPA configuration

You must back up your current `DataProtectionApplication` (DPA) configuration.

.Procedure
* Save your current DPA configuration by running the following command:
+
.Example
[source,terminal]
----
$ oc get dpa -n openshift-adp -o yaml > dpa.orig.backup
----

