:_mod-docs-content-type: ASSEMBLY
[id="rosa-private-cluster"]
= Configuring a private cluster
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-private-cluster

toc::[]

A {product-title} cluster can be made private so that internal applications can be hosted inside a corporate network. In addition, private clusters can be configured to have only internal API endpoints for increased security.

// {product-title} administrators can choose between public and private cluster configuration from within *{cluster-manager}*.

Privacy settings can be configured during cluster creation or after a cluster is established.
////
[NOTE]
====
Red Hat Service Reliability Engineers (SREs) can access a public or private cluster through the `cloud-ingress-operator` and existing ElasticSearch Load Balancer or Amazon S3 framework. SREs can access clusters through a secure endpoint to perform maintenance and service tasks.
====
////
include::modules/rosa-enable-private-cluster-new.adoc[leveloffset=+1]
include::modules/rosa-enable-private-cluster-existing.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

* xref:../../rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc#rosa-aws-privatelink-creating-cluster[Creating an AWS PrivateLink cluster on ROSA]
