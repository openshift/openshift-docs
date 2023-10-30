// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-working-bundle-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-publish-catalog_{context}"]
= Publishing a catalog containing a bundled Operator

To install and manage Operators, Operator Lifecycle Manager (OLM) requires that Operator bundles are listed in an index image, which is referenced by a catalog on the cluster. As an Operator author, you can use the Operator SDK to create an index containing the bundle for your Operator and all of its dependencies. This is useful for testing on remote clusters and publishing to container registries.

[NOTE]
====
The Operator SDK uses the `opm` CLI to facilitate index image creation. Experience with the `opm` command is not required. For advanced use cases, the `opm` command can be used directly instead of the Operator SDK.
====

.Prerequisites

- Operator SDK CLI installed on a development workstation
- Operator bundle image built and pushed to a registry
- OLM installed on a Kubernetes-based cluster (v1.16.0 or later if you use `apiextensions.k8s.io/v1` CRDs, for example {product-title} {product-version})
ifndef::openshift-dedicated,openshift-rosa[]
- Logged in to the cluster with `oc` using an account with `cluster-admin` permissions
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
- Logged in to the cluster with `oc` using an account with `dedicated-admin` permissions
endif::openshift-dedicated,openshift-rosa[]

.Procedure

. Run the following `make` command in your Operator project directory to build an index image containing your Operator bundle:
+
[source,terminal]
----
$ make catalog-build CATALOG_IMG=<registry>/<user>/<index_image_name>:<tag>
----
+
where the `CATALOG_IMG` argument references a repository that you have access to. You can obtain an account for storing containers at repository sites such as Quay.io.

. Push the built index image to a repository:
+
[source,terminal]
----
$ make catalog-push CATALOG_IMG=<registry>/<user>/<index_image_name>:<tag>
----
+
[TIP]
====
You can use Operator SDK `make` commands together if you would rather perform multiple actions in sequence at once. For example, if you had not yet built a bundle image for your Operator project, you can build and push both a bundle image and an index image with the following syntax:

[source,terminal]
----
$ make bundle-build bundle-push catalog-build catalog-push \
    BUNDLE_IMG=<bundle_image_pull_spec> \
    CATALOG_IMG=<index_image_pull_spec>
----

Alternatively, you can set the `IMAGE_TAG_BASE` field in your `Makefile`  to an existing repository:

[source,terminal]
----
IMAGE_TAG_BASE=quay.io/example/my-operator
----

You can then use the following syntax to build and push images with automatically-generated names, such as `quay.io/example/my-operator-bundle:v0.0.1` for the bundle image and `quay.io/example/my-operator-catalog:v0.0.1` for the index image:

[source,terminal]
----
$ make bundle-build bundle-push catalog-build catalog-push
----
====

. Define a `CatalogSource` object that references the index image you just generated, and then create the object by using the `oc apply` command or web console:
+
.Example `CatalogSource` YAML
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: cs-memcached
  namespace: <operator_namespace>
spec:
  displayName: My Test
  publisher: Company
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode> <1>
  image: quay.io/example/memcached-catalog:v0.0.1 <2>
  updateStrategy:
    registryPoll:
      interval: 10m
----
<1> Specify the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future {product-title} release, it is planned that the default value will be `restricted`. If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`.
<2> Set `image` to the image pull spec you used previously with the `CATALOG_IMG` argument.

. Check the catalog source:
+
[source,terminal]
----
$ oc get catalogsource
----
+
.Example output
[source,terminal]
----
NAME           DISPLAY     TYPE   PUBLISHER   AGE
cs-memcached   My Test     grpc   Company     4h31m
----

.Verification

. Install the Operator using your catalog:

.. Define an `OperatorGroup` object and create it by using the `oc apply` command or web console:
+
.Example `OperatorGroup` YAML
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-test
  namespace: <operator_namespace>
spec:
  targetNamespaces:
  - <operator_namespace>
----

.. Define a `Subscription` object and create it by using the `oc apply` command or web console:
+
.Example `Subscription` YAML
[source,yaml]
----
﻿apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: catalogtest
  namespace: <catalog_namespace>
spec:
  channel: "alpha"
  installPlanApproval: Manual
  name: catalog
  source: cs-memcached
  sourceNamespace: <operator_namespace>
  startingCSV: memcached-operator.v0.0.1
----

. Verify the installed Operator is running:

.. Check the Operator group:
+
[source,terminal]
----
$ oc get og
----
+
.Example output
[source,terminal]
----
NAME             AGE
my-test           4h40m
----

.. Check the cluster service version (CSV):
+
[source,terminal]
----
$ oc get csv
----
+
.Example output
[source,terminal]
----
NAME                        DISPLAY   VERSION   REPLACES   PHASE
memcached-operator.v0.0.1   Test      0.0.1                Succeeded
----

.. Check the pods for the Operator:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                                              READY   STATUS      RESTARTS   AGE
9098d908802769fbde8bd45255e69710a9f8420a8f3d814abe88b68f8ervdj6   0/1     Completed   0          4h33m
catalog-controller-manager-7fd5b7b987-69s4n                       2/2     Running     0          4h32m
cs-memcached-7622r                                                1/1     Running     0          4h33m
----
