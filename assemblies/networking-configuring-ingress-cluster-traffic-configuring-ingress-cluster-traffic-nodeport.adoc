:_mod-docs-content-type: ASSEMBLY
[id="configuring-ingress-cluster-traffic-nodeport"]
= Configuring ingress cluster traffic using a NodePort
include::_attributes/common-attributes.adoc[]
:context: configuring-ingress-cluster-traffic-nodeport

toc::[]

{product-title} provides methods for communicating from
outside the cluster with services running in the cluster. This method uses a
`NodePort`.

include::modules/nw-using-nodeport.adoc[leveloffset=+1]

[NOTE]
====
The procedures in this section require prerequisites performed by the cluster
administrator.
====

== Prerequisites

Before starting the following procedures, the administrator must:

* Set up the external port to the cluster networking environment so that requests
can reach the cluster.

* Make sure there is at least one user with cluster admin role. To add this role
to a user, run the following command:
+
----
$ oc adm policy add-cluster-role-to-user cluster-admin <user_name>
----

* Have an {product-title} cluster with at least one master and at least one node
and a system outside the cluster that has network access to the cluster. This
procedure assumes that the external system is on the same subnet as the cluster.
The additional networking required for external systems on a different subnet is
out-of-scope for this topic.

include::modules/nw-creating-project-and-service.adoc[leveloffset=+1]

include::modules/nw-exposing-service.adoc[leveloffset=+1]


[role="_additional-resources"]
[id="configuring-ingress-cluster-traffic-nodeport-additional-resources"]
== Additional resources

* xref:../../networking/configuring-node-port-service-range.adoc#configuring-node-port-service-range[Configuring the node port service range]
