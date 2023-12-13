:_mod-docs-content-type: ASSEMBLY
[id="configuring-web-console"]
= Configuring the web console in {product-title}
include::_attributes/common-attributes.adoc[]
:context: configuring-web-console

toc::[]

You can modify the {product-title} web console to set a logout redirect URL
or disable the quick start tutorials.

== Prerequisites

* Deploy an {product-title} cluster.

// Hiding in ROSA/OSD, as dedicated-admins cannot create "consoles" resource
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/web-console-configuration.adoc[leveloffset=+1]
// Hiding in ROSA/OSD, as dedicated-admins do not have sufficient permissions to read any cluster configuration
include::modules/disable-quickstarts-admin-console.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]
