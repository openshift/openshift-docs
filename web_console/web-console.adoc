:_mod-docs-content-type: ASSEMBLY

[id="web-console"]
= Accessing the web console
include::_attributes/common-attributes.adoc[]
:context: web-console

toc::[]

The {product-title} web console is a user interface accessible from a web browser.
Developers can use the web console to visualize, browse, and manage the contents
of projects.

== Prerequisites

* JavaScript must be enabled to use the web console. For the best experience, use
a web browser that supports
link:http://caniuse.com/#feat=websockets[WebSockets].
* Review the link:https://access.redhat.com/articles/4128421[OpenShift Container
Platform 4.x Tested Integrations] page before you create the supporting
infrastructure for your cluster.

include::modules/web-console-overview.adoc[leveloffset=+1]
// include::modules/multi-cluster-about.adoc[leveloffset=+1]
//include::modules/enabling-multi-cluster-console.adoc[leveloffset=+2]

ifndef::openshift-rosa,openshift-dedicated[]
[role="_additional-resources"]
.Additional resources
* xref:../nodes/clusters/nodes-cluster-enabling-features.adoc[Enabling feature sets using the web console]
endif::openshift-rosa,openshift-dedicated[]