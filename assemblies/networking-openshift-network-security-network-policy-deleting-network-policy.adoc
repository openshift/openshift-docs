:_mod-docs-content-type: ASSEMBLY
[id="deleting-network-policy"]
= Deleting a network policy
include::_attributes/common-attributes.adoc[]
ifdef::openshift-dedicated,openshift-rosa[]
include::_attributes/attributes-openshift-dedicated.adoc[]
endif::openshift-dedicated,openshift-rosa[]
:context: deleting-network-policy

toc::[]

As a user with the `admin` role, you can delete a network policy from a namespace.

include::modules/nw-networkpolicy-delete-cli.adoc[leveloffset=+1]
ifdef::openshift-dedicated,openshift-rosa[]
include::modules/nw-networkpolicy-delete-ocm.adoc[leveloffset=+1]
endif::[]