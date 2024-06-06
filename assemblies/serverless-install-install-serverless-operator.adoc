:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="install-serverless-operator"]
= Installing the {ServerlessOperatorName}
:context: install-serverless-operator

toc::[]

Installing the {ServerlessOperatorName} enables you to install and use Knative Serving, Knative Eventing, and the Knative broker for Apache Kafka on a {product-title} cluster. The {ServerlessOperatorName} manages Knative custom resource definitions (CRDs) for your cluster and enables you to configure them without directly modifying individual config maps for each component.

// universal install doc
include::modules/serverless-install-web-console.adoc[leveloffset=+1]

[IMPORTANT]
====
If you want to xref:../../serverless/observability/tracing/serverless-tracing.adoc#serverless-tracing[use {DTProductName} with {ServerlessProductName}], you must install and configure {DTProductName} before you install Knative Serving or Knative Eventing.
====

include::modules/serverless-install-cli.adoc[leveloffset=+1]

[IMPORTANT]
====
If you want to xref:../../serverless/observability/tracing/serverless-tracing.adoc#serverless-tracing[use {DTProductName} with {ServerlessProductName}], you must install and configure {DTProductName} before you install Knative Serving or Knative Eventing.
====


[id="serverless-configuration"]
== Global configuration

The {ServerlessOperatorName} manages the global configuration of a Knative installation, including propagating values from the `KnativeServing` and `KnativeEventing` custom resources to system link:https://kubernetes.io/docs/concepts/configuration/configmap/[config maps]. Any updates to config maps which are applied manually are overwritten by the Operator. However, modifying the Knative custom resources allows you to set values for these config maps.

Knative has multiple config maps that are named with the prefix `config-`. All Knative config maps are created in the same namespace as the custom resource that they apply to. For example, if the `KnativeServing` custom resource is created in the `knative-serving` namespace, all Knative Serving config maps are also created in this namespace.

The `spec.config` in the Knative custom resources have one `<name>` entry for each config map, named `config-<name>`, with a value which is be used for the config map `data`.



ifdef::openshift-enterprise[]
[id="additional-resources_knative-serving-CR-config"]
[role="_additional-resources"]
== Additional resources
* xref:../../operators/understanding/crds/crd-managing-resources-from-crds.adoc[Managing resources from custom resource definitions]
* xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[Understanding persistent storage]
* xref:../../networking/configuring-a-custom-pki.adoc[Configuring a custom PKI]
endif::[]

[id="next-steps_install-serverless-operator"]
== Next steps

* After the {ServerlessOperatorName} is installed, you can xref:../../serverless/install/installing-knative-serving.adoc#installing-knative-serving[install Knative Serving] or xref:../../serverless/install/installing-knative-eventing.adoc#installing-knative-eventing[install Knative Eventing].
