:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="installing-log-storage"]
= Installing log storage
:context: installing-log-storage

toc::[]

You can use the {oc-first} or the {product-title} web console to install a log store on your {product-title} cluster.

include::snippets/logging-elastic-dep-snip.adoc[]

[id="installing-log-storage-loki"]
== Installing a Loki log store

You can use the {loki-op} to install an internal Loki log store on your {product-title} cluster.

include::modules/loki-deployment-sizing.adoc[leveloffset=+2]
include::modules/logging-loki-gui-install.adoc[leveloffset=+2]
include::modules/logging-loki-cli-install.adoc[leveloffset=+2]

[id="installing-log-storage-es"]
== Installing an Elasticsearch log store

You can use the {es-op} to install an internal Elasticsearch log store on your {product-title} cluster.

include::snippets/logging-elastic-dep-snip.adoc[]
include::modules/logging-es-storage-considerations.adoc[leveloffset=+2]
include::modules/logging-install-es-operator.adoc[leveloffset=+2]
include::modules/cluster-logging-deploy-cli.adoc[leveloffset=+2]

// configuring log store in the clusterlogging CR
include::modules/configuring-log-storage-cr.adoc[leveloffset=+1]
