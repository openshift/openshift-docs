// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-running-openshift_{context}"]
= Syncing {product-title} groups with the LDAP server

You can sync all groups already in {product-title} that correspond to groups in the
LDAP server specified in the configuration file.

.Prerequisites

* Create a sync configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* To sync {product-title} groups with the LDAP server:
+
[source,terminal]
----
$ oc adm groups sync --type=openshift --sync-config=config.yaml --confirm
----
+
[NOTE]
====
By default, all group synchronization operations are dry-run, so you
must set the `--confirm` flag on the `oc adm groups sync` command to make
changes to {product-title} group records.
====
