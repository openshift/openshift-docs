:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="create-domain-mapping-kn"]
= Custom domains for Knative services using the Knative CLI
:context: create-domain-mapping-kn

You can customize the domain for your Knative service by mapping a custom domain name that you own to a Knative service. You can use the Knative (`kn`) CLI to create a `DomainMapping` custom resource (CR) that maps to an Addressable target CR, such as a Knative service or a Knative route.

include::modules/serverless-create-domain-mapping-kn.adoc[leveloffset=+1]
