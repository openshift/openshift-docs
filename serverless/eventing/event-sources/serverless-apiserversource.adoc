:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-apiserversource"]
= Creating an API server source
:context: serverless-apiserversource

toc::[]

The API server source is an event source that can be used to connect an event sink, such as a Knative service, to the Kubernetes API server. The API server source watches for Kubernetes events and forwards them to the Knative Eventing broker.

// dev console
include::modules/odc-creating-apiserversource.adoc[leveloffset=+1]
// kn commands
include::modules/apiserversource-kn.adoc[leveloffset=+1]
include::modules/specifying-sink-flag-kn.adoc[leveloffset=+2]
// YAML
include::modules/apiserversource-yaml.adoc[leveloffset=+1]
