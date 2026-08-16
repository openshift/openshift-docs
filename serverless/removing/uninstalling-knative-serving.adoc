:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="uninstalling-knative-serving"]
= Uninstalling {ServerlessProductName} Knative Serving
:context: uninstalling-knative-serving

Before you can remove the {ServerlessOperatorName}, you must remove Knative Serving. To uninstall Knative Serving, you must remove the `KnativeServing` custom resource (CR) and delete the `knative-serving` namespace.

// Uninstalling Knative Serving
include::modules/serverless-uninstalling-knative-serving.adoc[leveloffset=+1]