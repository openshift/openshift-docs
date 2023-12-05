// Module included in the following assemblies:
//
// * operators/admin/olm-managing-custom-catalogs.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-updating-sqlite-catalog-to-a-new-opm-version_{context}"]
= Rebuilding SQLite database catalog images

You can rebuild your SQLite database catalog image with the latest version of the `opm` CLI tool that is released with your version of {product-title}.

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

* Run the following command to rebuild your catalog with a more recent version of the `opm` CLI tool:
+
[source,terminal,subs="attributes+"]
----
$ opm index add --binary-image \
  registry.redhat.io/openshift4/ose-operator-registry:v{product-version} \
  --from-index <your_registry_image> \
  --bundles "" -t \<your_registry_image>
----
