:_mod-docs-content-type: ASSEMBLY
[id="kiali-config-ref"]
= Kiali configuration reference
include::_attributes/common-attributes.adoc[]
:context: kiali-config-ref

toc::[]

When the {SMProductShortName} Operator creates the `ServiceMeshControlPlane` it also processes the Kiali resource. The Kiali Operator then uses this object when creating Kiali instances.

// The following include statements pull in the module files for the assembly.
include::modules/ossm-config-smcp-kiali.adoc[leveloffset=+1]

include::modules/ossm-configuring-external-kiali.adoc[leveloffset=+1]
