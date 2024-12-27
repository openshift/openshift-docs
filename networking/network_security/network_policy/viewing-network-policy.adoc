:_mod-docs-content-type: ASSEMBLY
[id="viewing-network-policy"]
= Viewing a network policy
include::_attributes/common-attributes.adoc[]
ifdef::openshift-dedicated,openshift-rosa[]
include::_attributes/attributes-openshift-dedicated.adoc[]
endif::openshift-dedicated,openshift-rosa[]
:context: viewing-network-policy

toc::[]

As a user with the `admin` role, you can view a network policy for a namespace.

include::modules/nw-networkpolicy-object.adoc[leveloffset=+1]

include::modules/nw-networkpolicy-view-cli.adoc[leveloffset=+1]

ifdef::openshift-dedicated,openshift-rosa[]
include::modules/nw-networkpolicy-view-ocm.adoc[leveloffset=+1]
endif::[]