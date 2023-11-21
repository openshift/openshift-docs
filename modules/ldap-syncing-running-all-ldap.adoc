// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-running-all-ldap_{context}"]
= Syncing the LDAP server with {product-title}

You can sync all groups from the LDAP server with {product-title}.

.Prerequisites

* Create a sync configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* To sync all groups from the LDAP server with {product-title}:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=config.yaml --confirm
----
+
[NOTE]
====
By default, all group synchronization operations are dry-run, so you
must set the `--confirm` flag on the `oc adm groups sync` command to make
changes to {product-title} group records.
====
