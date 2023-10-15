// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

:_mod-docs-content-type: PROCEDURE
[id="oadp-configuring-noobaa-for-dr_{context}"]
= Configuring Multicloud Object Gateway (MCG) for disaster recovery on {rh-storage}

If you use cluster storage for your MCG bucket `backupStorageLocation` on {rh-storage}, configure MCG as an external object store.

[WARNING]
====
Failure to configure MCG as an external object store might lead to backups not being available.
====

include::snippets/snip-noobaa-and-mcg.adoc[]

.Procedure

* Configure MCG as an external object store as described in link:https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.13/html/managing_hybrid_and_multicloud_resources/adding-storage-resources-for-hybrid-or-multicloud_rhodf#doc-wrapper[Adding storage resources for hybrid or Multicloud].
