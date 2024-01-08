:_mod-docs-content-type: ASSEMBLY
:context: nodes-containers-init
[id="nodes-containers-init"]
= Using Init Containers to perform tasks before a pod is deployed
include::_attributes/common-attributes.adoc[]

toc::[]




{product-title} provides _init containers_, which are specialized containers
that run before application containers and can contain utilities or setup scripts not present in an app image.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-containers-init-about.adoc[leveloffset=+1]

include::modules/nodes-containers-init-creating.adoc[leveloffset=+1]


