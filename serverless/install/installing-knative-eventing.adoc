:_mod-docs-content-type: ASSEMBLY
[id="installing-knative-eventing"]
= Installing Knative Eventing
include::_attributes/common-attributes.adoc[]
:context: installing-knative-eventing

toc::[]

To use event-driven architecture on your cluster, install Knative Eventing. You can create Knative components such as event sources, brokers, and channels and then use them to send events to applications or external systems.

After you install the {ServerlessOperatorName}, you can install Knative Eventing by using the default settings, or configure more advanced settings in the `KnativeEventing` custom resource (CR). For more information about configuration options for the `KnativeEventing` CR, see xref:../../serverless/install/install-serverless-operator.adoc#serverless-configuration[Global configuration].

[IMPORTANT]
====
If you want to xref:../../serverless/observability/tracing/serverless-tracing.adoc#serverless-tracing[use {DTProductName} with {ServerlessProductName}], you must install and configure {DTProductName} before you install Knative Eventing.
====

include::modules/serverless-install-eventing-web-console.adoc[leveloffset=+1]
include::modules/serverless-install-eventing-yaml.adoc[leveloffset=+1]

include::modules/serverless-install-kafka-odc.adoc[leveloffset=+1]

[id="next-steps_installing-knative-eventing"]
== Next steps

* If you want to use Knative services you can xref:../../serverless/install/installing-knative-serving.adoc#installing-knative-serving[install Knative Serving].
