// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc
// * operators/olm_v1/arch/olmv1-catalogd.adoc

:_mod-docs-content-type: REFERENCE

[id="olmv1-red-hat-catalogs_{context}"]
= Red Hat-provided Operator catalogs in {olmv1}

{olmv1-first} does not include Red Hat-provided Operator catalogs by default. If you want to add a Red Hat-provided catalog to your cluster, create a custom resource (CR) for the catalog and apply it to the cluster. The following custom resource (CR) examples show how to create a catalog resources for {olmv1}.

.Example Red Hat Operators catalog
[source,yaml,subs="attributes+"]
----
apiVersion: catalogd.operatorframework.io/v1alpha1
kind: Catalog
metadata:
  name: redhat-operators
spec:
  source:
    type: image
    image:
      ref: registry.redhat.io/redhat/redhat-operator-index:v{product-version}
----

.Example Certified Operators catalog
[source,yaml,subs="attributes+"]
----
apiVersion: catalogd.operatorframework.io/v1alpha1
kind: Catalog
metadata:
  name: certified-operators
spec:
  source:
    type: image
    image:
      ref: registry.redhat.io/redhat/certified-operator-index:v{product-version}
----

.Example Community Operators catalog
[source,yaml,subs="attributes+"]
----
apiVersion: catalogd.operatorframework.io/v1alpha1
kind: Catalog
metadata:
  name: community-operators
spec:
  source:
    type: image
    image:
      ref: registry.redhat.io/redhat/community-operator-index:v{product-version}
----

The following command adds a catalog to your cluster:

.Command syntax
[source,terminal]
----
$ oc apply -f <catalog_name>.yaml <1>
----
<1> Specifies the catalog CR, such as `redhat-operators.yaml`.
