:_mod-docs-content-type: ASSEMBLY
[id="installing-knative-serving"]
= Installing Knative Serving
include::_attributes/common-attributes.adoc[]
:context: installing-knative-serving

toc::[]

Installing Knative Serving allows you to create Knative services and functions on your cluster. It also allows you to use additional functionality such as autoscaling and networking options for your applications.

After you install the {ServerlessOperatorName}, you can install Knative Serving by using the default settings, or configure more advanced settings in the `KnativeServing` custom resource (CR). For more information about configuration options for the `KnativeServing` CR, see xref:../../serverless/install/install-serverless-operator.adoc#serverless-configuration[Global configuration].

[IMPORTANT]
====
If you want to xref:../../serverless/observability/tracing/serverless-tracing.adoc#serverless-tracing[use {DTProductName} with {ServerlessProductName}], you must install and configure {DTProductName} before you install Knative Serving.
====

include::modules/serverless-install-serving-web-console.adoc[leveloffset=+1]
include::modules/serverless-install-serving-yaml.adoc[leveloffset=+1]

[id="next-steps_installing-knative-serving"]
== Next steps

* If you want to use Knative event-driven architecture you can xref:../../serverless/install/installing-knative-eventing.adoc#installing-knative-eventing[install Knative Eventing].
