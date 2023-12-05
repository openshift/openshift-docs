:_mod-docs-content-type: ASSEMBLY
[id="api-server-certificates"]
= Adding API server certificates
include::_attributes/common-attributes.adoc[]
:context: api-server-certificates

toc::[]

The default API server certificate is issued by an internal {product-title}
cluster CA. Clients outside of the cluster will not be able to verify the
API server's certificate by default. This certificate can be replaced
by one that is issued by a CA that clients trust.

include::modules/customize-certificates-api-add-named.adoc[leveloffset=+1]
