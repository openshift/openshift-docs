// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

:_mod-docs-content-type: PROCEDURE
[id="pruning-builds_{context}"]
= Pruning builds

To prune builds that are no longer required by the system due to age and status, administrators can run the following command:

[source,terminal]
----
$ oc adm prune builds [<options>]
----

.`oc adm prune builds` flags
[cols="4,8",options="header"]
|===

|Option |Description

.^|`--confirm`
|Indicate that pruning should occur, instead of performing a dry-run.

.^|`--orphans`
|Prune all builds whose build configuration no longer exists, status is complete, failed, error, or canceled.

.^|`--keep-complete=<N>`
|Per build configuration, keep the last `N` builds whose status is complete. The default is `5`.

.^|`--keep-failed=<N>`
|Per build configuration, keep the last `N` builds whose status is failed, error, or canceled. The default is `1`.

.^|`--keep-younger-than=<duration>`
|Do not prune any object that is younger than `<duration>` relative to the current time. The default is `60m`.
|===

.Procedure

. To see what a pruning operation would delete, run the following command:
+
[source,terminal]
----
$ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m
----

. To actually perform the prune operation, add the `--confirm` flag:
+
[source,terminal]
----
$ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
    --keep-younger-than=60m --confirm
----

[NOTE]
====
Developers can enable automatic build pruning by modifying their build configuration.
====
