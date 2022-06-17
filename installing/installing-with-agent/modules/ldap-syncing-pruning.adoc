// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-pruning_{context}"]
= Running a group pruning job

An administrator can also choose to remove groups from {product-title} records
if the records on the LDAP server that created them are no longer present. The
prune job will accept the same sync configuration file and whitelists or blacklists
as used for the sync job.

For example:

[source,terminal]
----
$ oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm
----

[source,terminal]
----
$ oc adm prune groups --whitelist=/path/to/whitelist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
----

[source,terminal]
----
$ oc adm prune groups --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
----
