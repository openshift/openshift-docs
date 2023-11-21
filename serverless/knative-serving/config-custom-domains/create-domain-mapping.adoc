:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="create-domain-mapping"]
= Custom domain mapping
:context: create-domain-mapping

You can customize the domain for your Knative service by mapping a custom domain name that you own to a Knative service. To map a custom domain name to a custom resource (CR), you must create a `DomainMapping` CR that maps to an Addressable target CR, such as a Knative service or a Knative route.

include::modules/serverless-create-domain-mapping.adoc[leveloffset=+1]
