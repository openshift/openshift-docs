:_mod-docs-content-type: ASSEMBLY
[id="removing-ossm"]
= Uninstalling Service Mesh
include::_attributes/common-attributes.adoc[]
:context: removing-ossm

toc::[]

To uninstall {SMProductName} from an existing {product-title} instance and remove its resources, you must delete the control plane, delete the Operators, and run commands to manually remove some resources.

include::modules/ossm-control-plane-remove.adoc[leveloffset=+1]

include::modules/ossm-remove-operators.adoc[leveloffset=+1]

include::modules/ossm-remove-cleanup.adoc[leveloffset=+1]
