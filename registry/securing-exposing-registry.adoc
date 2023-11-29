:_mod-docs-content-type: ASSEMBLY
:context: securing-exposing-registry
[id="securing-exposing-registry"]
= Exposing the registry
include::_attributes/common-attributes.adoc[]

toc::[]

By default, the {product-registry} is secured during cluster installation
so that it serves traffic through TLS. Unlike previous versions of
{product-title}, the registry is not exposed outside of the cluster at the time
of installation.

include::modules/registry-exposing-default-registry-manually.adoc[leveloffset=+1]
include::modules/registry-exposing-secure-registry-manually.adoc[leveloffset=+1]
