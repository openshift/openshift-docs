// Module included in the following assemblies:
//
// * operators/understanding/olm-understanding-operatorhub.adoc

[id="olm-operatorhub-arch_{context}"]
= OperatorHub architecture

The OperatorHub UI component is driven by the Marketplace Operator by default on {product-title} in the `openshift-marketplace` namespace.

[id="olm-operatorhub-arch-operatorhub_crd_{context}"]
== OperatorHub custom resource

The Marketplace Operator manages an `OperatorHub` custom resource (CR) named `cluster` that manages the default `CatalogSource` objects provided with OperatorHub.
ifndef::openshift-dedicated,openshift-rosa[]
You can modify this resource to enable or disable the default catalogs, which is useful when configuring {product-title} in restricted network environments.

.Example `OperatorHub` custom resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OperatorHub
metadata:
  name: cluster
spec:
  disableAllDefaultSources: true <1>
  sources: [ <2>
    {
      name: "community-operators",
      disabled: false
    }
  ]
----
<1> `disableAllDefaultSources` is an override that controls availability of all default catalogs that are configured by default during an {product-title} installation.
<2> Disable default catalogs individually by changing the `disabled` parameter value per source.
endif::openshift-dedicated,openshift-rosa[]
