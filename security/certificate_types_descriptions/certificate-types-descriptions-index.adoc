:_mod-docs-content-type: ASSEMBLY
[id="ocp-certificates"]
= Certificate types and descriptions
include::_attributes/common-attributes.adoc[]
:context: ocp-certificates

toc::[]

== Certificate validation

{product-title} monitors certificates for proper validity, for the cluster certificates it issues and manages. The {product-title} alerting framework has rules to help identify when a certificate issue is about to occur. These rules consist of the following checks:

* API server client certificate expiration is less than five minutes.
