// Module included in the following assemblies:
//
// * operators/admin/olm-managing-custom-catalogs.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-migrating-sqlite-catalog-to-fbc_{context}"]
= Migrating SQLite database catalogs to the file-based catalog format

You can update your deprecated SQLite database format catalogs to the file-based catalog format.

.Prerequisites

* You have a SQLite database catalog source.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]
* You have the latest version of the `opm` CLI tool released with {product-title} {product-version} on your workstation.

.Procedure

. Migrate your SQLite database catalog to a file-based catalog by running the following command:
+
[source,terminal]
----
$ opm migrate <registry_image> <fbc_directory>
----

. Generate a Dockerfile for your file-based catalog by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ opm generate dockerfile <fbc_directory> \
  --binary-image \
  registry.redhat.io/openshift4/ose-operator-registry:v{product-version}
----

.Next steps

* The generated Dockerfile can be built, tagged, and pushed to your registry.
