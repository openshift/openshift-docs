:_mod-docs-content-type: ASSEMBLY
[id="osd-upgrades"]
= {product-title} cluster upgrades
:context: osd-upgrades
include::_attributes/attributes-openshift-dedicated.adoc[]

toc::[]

[role="_abstract"]
You can schedule automatic or manual upgrade policies to update the version of your {product-title} clusters. Upgrading {product-title} clusters can be done through {cluster-manager-first} or {cluster-manager} CLI.

Red Hat Site Reliability Engineers (SREs) monitor upgrade progress and remedy any issues encountered.

include::modules/upgrade.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* For more information about the service log and adding cluster notification contacts, see xref:../osd_cluster_admin/osd_logging/osd-accessing-the-service-logs.adoc#osd-accessing-the-service-logs[Accessing the service logs for {product-title} clusters].

include::modules/upgrade-auto.adoc[leveloffset=+1]
include::modules/upgrade-manual.adoc[leveloffset=+1]
