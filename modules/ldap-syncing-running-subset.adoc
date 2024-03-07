// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-running-subset_{context}"]
= Syncing subgroups from the LDAP server with {product-title}

You can sync a subset of LDAP groups with {product-title} using whitelist files,
blacklist files, or both.

[NOTE]
====
You can use any combination of blacklist files, whitelist files, or whitelist
literals. Whitelist and blacklist files must contain one unique group identifier
per line, and you can include whitelist literals directly in the command itself.
These guidelines apply to groups found on LDAP servers as well as groups already
present in {product-title}.
====

.Prerequisites

* Create a sync configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* To sync a subset of LDAP groups with {product-title}, use any the following commands:
+
[source,terminal]
----
$ oc adm groups sync --whitelist=<whitelist_file> \
                   --sync-config=config.yaml      \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync --blacklist=<blacklist_file> \
                   --sync-config=config.yaml      \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync <group_unique_identifier>    \
                   --sync-config=config.yaml      \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync <group_unique_identifier>  \
                   --whitelist=<whitelist_file> \
                   --blacklist=<blacklist_file> \
                   --sync-config=config.yaml    \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync --type=openshift           \
                   --whitelist=<whitelist_file> \
                   --sync-config=config.yaml    \
                   --confirm
----
+
[NOTE]
====
By default, all group synchronization operations are dry-run, so you
must set the `--confirm` flag on the `oc adm groups sync` command to make
changes to {product-title} group records.
====
