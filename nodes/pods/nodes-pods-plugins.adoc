:_mod-docs-content-type: ASSEMBLY
:context: nodes-pods-device
[id="nodes-pods-device"]
= Using device plugins to access external resources with pods
include::_attributes/common-attributes.adoc[]

toc::[]


Device plugins allow you to use a particular device type (GPU, InfiniBand,
or other similar computing resources that require vendor-specific initialization
and setup) in your {product-title} pod without needing to write custom code.


// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-pods-plugins-about.adoc[leveloffset=+1]

include::modules/nodes-pods-plugins-device-mgr.adoc[leveloffset=+1]

include::modules/nodes-pods-plugins-install.adoc[leveloffset=+1]

