:_mod-docs-content-type: ASSEMBLY
[id="metallb-configure-community-alias"]
= Configuring community alias
include::_attributes/common-attributes.adoc[]
:context: configure-community-alias

toc::[]

As a cluster administrator, you can configure a community alias and use it across different advertisements.

// Address pool custom resource
include::modules/nw-metallb-community-cr.adoc[leveloffset=+1]

// Configure advertisement with community alias
include::modules/nw-metallb-configure-community-bgp-advertisement.adoc[leveloffset=+1]
