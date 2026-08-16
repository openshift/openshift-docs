// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

:_mod-docs-content-type: PROCEDURE
[id="pruning-groups_{context}"]
= Pruning groups

To prune groups records from an external provider, administrators can run the
following command:

[source,terminal]
----
$ oc adm prune groups \
    --sync-config=path/to/sync/config [<options>]
----

.`oc adm prune groups` flags
[cols="4,8",options="header"]
|===

|Options |Description

.^|`--confirm`
|Indicate that pruning should occur, instead of performing a dry-run.

.^|`--blacklist`
|Path to the group blacklist file.

.^|`--whitelist`
|Path to the group whitelist file.

.^|`--sync-config`
|Path to the synchronization configuration file.
|===

.Procedure

. To see the groups that the prune command deletes, run the following command:
+
[source,terminal]
----
$ oc adm prune groups --sync-config=ldap-sync-config.yaml
----

. To perform the prune operation, add the `--confirm` flag:
+
[source,terminal]
----
$ oc adm prune groups --sync-config=ldap-sync-config.yaml --confirm
----

////
Needs "Additional resources" links when converted:

//Future xref:../install_config/syncing_groups_with_ldap.adoc#configuring-ldap-sync[Configuring LDAP Sync]
//Future xref:../install_config/syncing_groups_with_ldap.adoc#overview[Syncing Groups With LDAP]
////
