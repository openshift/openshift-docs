:_mod-docs-content-type: ASSEMBLY
[id="nodes-nodes-garbage-collection"]
= Freeing node resources using garbage collection
include::_attributes/common-attributes.adoc[]
:context: nodes-nodes-configuring

toc::[]

As an administrator, you can use {product-title} to ensure that your nodes are running efficiently
by freeing up resources through garbage collection.

The {product-title} node performs two types of garbage collection:

* Container garbage collection: Removes terminated containers.
* Image garbage collection: Removes images not referenced by any running pods.


// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-nodes-garbage-collection-containers.adoc[leveloffset=+1]

include::modules/nodes-nodes-garbage-collection-images.adoc[leveloffset=+1]

include::modules/nodes-nodes-garbage-collection-configuring.adoc[leveloffset=+1]
