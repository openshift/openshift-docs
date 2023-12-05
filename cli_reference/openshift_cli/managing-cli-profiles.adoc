:_mod-docs-content-type: ASSEMBLY
[id="managing-cli-profiles"]
= Managing CLI profiles
include::_attributes/common-attributes.adoc[]
:context: managing-cli-profiles

toc::[]

A CLI configuration file allows you to configure different profiles, or contexts, for use with the xref:../../cli_reference/index.adoc#cli-tools-overview[CLI tools overview]. A context consists of
ifndef::microshift,openshift-dedicated,openshift-rosa[]
xref:../../authentication/understanding-authentication.adoc#understanding-authentication[user authentication]
endif::microshift,openshift-dedicated,openshift-rosa[]
ifdef::microshift[]
user authentication
endif::[]
ifndef::openshift-rosa[]
an {product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
the {product-title} (ROSA)
endif::openshift-rosa[]
server information associated with a _nickname_.

include::modules/about-cli-profiles-switch.adoc[leveloffset=+1]

include::modules/manual-configuration-of-cli-profiles.adoc[leveloffset=+1]

include::modules/load-and-merge-rules.adoc[leveloffset=+1]
