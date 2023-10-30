// Module included in the following assemblies:
//
// * post_installation_configuration/preparing-for-users.adoc
// * operators/admin/olm-restricted-networks.adoc
// * operators/admin/managing-custom-catalogs.adoc

ifdef::openshift-origin[]
:index-image: catalog
:tag: latest
:namespace: olm
endif::[]
ifndef::openshift-origin[]
:index-image: redhat-operator-index
:tag: v{product-version}
:namespace: openshift-marketplace
endif::[]
ifeval::["{context}" == "post-install-preparing-for-users"]
:olm-restricted-networks:
endif::[]
ifeval::["{context}" == "olm-restricted-networks"]
:olm-restricted-networks:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="olm-creating-catalog-from-index_{context}"]
= Adding a catalog source to a cluster

Adding a catalog source to an {product-title} cluster enables the discovery and installation of Operators for users.
ifndef::openshift-dedicated,openshift-rosa[]
Cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
Administrators with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
can create a `CatalogSource` object that references an index image. OperatorHub uses catalog sources to populate the user interface.

// In OSD/ROSA, a dedicated-admin can see catalog sources here, but can't add, edit, or delete them.
ifndef::openshift-dedicated,openshift-rosa[]
[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Administration* -> *Cluster Settings* -> *Configuration* -> *OperatorHub* page, click the *Sources* tab, where you can create, update, delete, disable, and enable individual sources.
====
endif::openshift-dedicated,openshift-rosa[]

// In OSD/ROSA, a dedicated-admin can update catalog sources in the console by searching for them.
ifdef::openshift-dedicated,openshift-rosa[]
[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Home* -> *Search* page, select a project, click the *Resources* drop-down and search for `CatalogSource`. You can create, update, delete, disable, and enable individual sources.
====
endif::openshift-dedicated,openshift-rosa[]

.Prerequisites

* You built and pushed an index image to a registry.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

. Create a `CatalogSource` object that references your index image.
ifdef::olm-restricted-networks[]
If you used the `oc adm catalog mirror` command to mirror your catalog to a target registry, you can use the generated `catalogSource.yaml` file in your manifests directory as a starting point.
endif::[]

.. Modify the following to your specifications and save it as a `catalogSource.yaml` file:
+
ifdef::olm-restricted-networks[]
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: my-operator-catalog <1>
  namespace: {namespace} <2>
spec:
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode> <3>
  image: <registry>/<namespace>/{index-image}:{tag} <4>
  displayName: My Operator Catalog
  publisher: <publisher_name> <5>
  updateStrategy:
    registryPoll: <6>
      interval: 30m
----
<1> If you mirrored content to local files before uploading to a registry, remove any backslash (`/`) characters from the `metadata.name` field to avoid an "invalid resource name" error when you create the object.
<2> If you want the catalog source to be available globally to users in all namespaces, specify the `{namespace}` namespace. Otherwise, you can specify a different namespace for the catalog to be scoped and available only for that namespace.
<3> Specify the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future {product-title} release, it is planned that the default value will be `restricted`. If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`.
<4> Specify your index image. If you specify a tag after the image name, for example `:{tag}`, the catalog source pod uses an image pull policy of `Always`, meaning the pod always pulls the image prior to starting the container. If you specify a digest, for example `@sha256:<id>`, the image pull policy is `IfNotPresent`, meaning the pod pulls the image only if it does not already exist on the node.
<5> Specify your name or an organization name publishing the catalog.
<6> Catalog sources can automatically check for new versions to keep up to date.
endif::[]
ifndef::olm-restricted-networks[]
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: my-operator-catalog
  namespace: {namespace} <1>
  annotations:
    olm.catalogImageTemplate: <2>
      "<registry>/<namespace>/<index_image_name>:v{kube_major_version}.{kube_minor_version}.{kube_patch_version}"
spec:
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode> <3>
  image: <registry>/<namespace>/<index_image_name>:<tag> <4>
  displayName: My Operator Catalog
  publisher: <publisher_name> <5>
  updateStrategy:
    registryPoll: <6>
      interval: 30m
----
<1> If you want the catalog source to be available globally to users in all namespaces, specify the `{namespace}` namespace. Otherwise, you can specify a different namespace for the catalog to be scoped and available only for that namespace.
<2> Optional: Set the `olm.catalogImageTemplate` annotation to your index image name and use one or more of the Kubernetes cluster version variables as shown when constructing the template for the image tag.
<3> Specify the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future {product-title} release, it is planned that the default value will be `restricted`. If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`.
<4> Specify your index image. If you specify a tag after the image name, for example `:{tag}`, the catalog source pod uses an image pull policy of `Always`, meaning the pod always pulls the image prior to starting the container. If you specify a digest, for example `@sha256:<id>`, the image pull policy is `IfNotPresent`, meaning the pod pulls the image only if it does not already exist on the node.
<5> Specify your name or an organization name publishing the catalog.
<6> Catalog sources can automatically check for new versions to keep up to date.
endif::[]

.. Use the file to create the `CatalogSource` object:
+
[source,terminal]
----
$ oc apply -f catalogSource.yaml
----

. Verify the following resources are created successfully.

.. Check the pods:
+
[source,terminal,subs="attributes+"]
----
$ oc get pods -n {namespace}
----
+
.Example output
[source,terminal]
----
NAME                                    READY   STATUS    RESTARTS  AGE
my-operator-catalog-6njx6               1/1     Running   0         28s
marketplace-operator-d9f549946-96sgr    1/1     Running   0         26h
----

.. Check the catalog source:
+
[source,terminal,subs="attributes+"]
----
$ oc get catalogsource -n {namespace}
----
+
.Example output
[source,terminal]
----
NAME                  DISPLAY               TYPE PUBLISHER  AGE
my-operator-catalog   My Operator Catalog   grpc            5s
----

.. Check the package manifest:
+
[source,terminal,subs="attributes+"]
----
$ oc get packagemanifest -n {namespace}
----
+
.Example output
[source,terminal]
----
NAME                          CATALOG               AGE
jaeger-product                My Operator Catalog   93s
----

You can now install the Operators from the *OperatorHub* page on your {product-title} web console.

:!index-image:
:!tag:
:!namespace:
ifeval::["{context}" == "post-install-preparing-for-users"]
:!olm-restricted-networks:
endif::[]
ifeval::["{context}" == "olm-restricted-networks"]
:!olm-restricted-networks:
endif::[]
