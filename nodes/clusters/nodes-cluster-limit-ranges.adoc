:_mod-docs-content-type: ASSEMBLY
:context: nodes-cluster-limit-ranges
[id="nodes-cluster-limit-ranges"]
= Restrict resource consumption with limit ranges
include::_attributes/common-attributes.adoc[]

toc::[]


By default, containers run with unbounded compute resources on an {product-title}
cluster. With limit ranges, you can restrict resource consumption for specific
objects in a project:

* pods and containers: You can set minimum and maximum requirements for CPU and
memory for pods and their containers.
* Image streams: You can set limits on the number of images and tags in an
`ImageStream` object.
* Images: You can limit the size of images that can be pushed to an internal
registry.
* Persistent volume claims (PVC): You can restrict the size of the PVCs that can
be requested.

If a pod does not meet the constraints imposed by the limit
range, the pod cannot be created in the namespace.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.


include::modules/nodes-cluster-limit-ranges-about.adoc[leveloffset=+1]

include::modules/nodes-cluster-limit-ranges-limits.adoc[leveloffset=+2]

include::modules/nodes-cluster-limit-ranges-creating.adoc[leveloffset=+1]

include::modules/nodes-cluster-limit-ranges-viewing.adoc[leveloffset=+1]

include::modules/nodes-cluster-limit-ranges-deleting.adoc[leveloffset=+1]
