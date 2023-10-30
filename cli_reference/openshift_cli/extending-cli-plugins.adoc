:_mod-docs-content-type: ASSEMBLY
[id="cli-extend-plugins"]
= Extending the OpenShift CLI with plugins
include::_attributes/common-attributes.adoc[]
:context: cli-extend-plugins

toc::[]

You can write and install plugins to build on the default `oc` commands,
allowing you to perform new and more complex tasks with the
ifndef::openshift-dedicated,openshift-rosa[]
{product-title}
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-rosa,openshift-dedicated[]
OpenShift
endif::openshift-rosa,openshift-dedicated[]
CLI.

// Writing CLI plugins
include::modules/cli-extending-plugins-writing.adoc[leveloffset=+1]

// Installing and using CLI plugins
include::modules/cli-extending-plugins-installing.adoc[leveloffset=+1]
