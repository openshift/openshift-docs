:_mod-docs-content-type: ASSEMBLY
[id="osd-accessing-the-service-logs"]
= Accessing the service logs for OpenShift Dedicated clusters
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: osd-accessing-the-service-logs

toc::[]

[role="_abstract"]
You can view the service logs for your {product-title} clusters by using {cluster-manager-first}. The service logs detail cluster events such as load balancer quota updates and scheduled maintenance upgrades. The logs also show cluster resource changes such as the addition or deletion of users, groups, and identity providers.

// Commented out while the OpenShift Cluster Manager CLI is in Developer Preview:
//You can view the service logs for your {product-title} clusters by using {cluster-manager-first} or the {cluster-manager} CLI (`ocm`). The service logs detail cluster events such as load balancer quota updates and scheduled maintenance upgrades. The logs also show cluster resource changes such as the addition or deletion of users, groups, and identity providers.

Additionally, you can add notification contacts for an {product-title} cluster. Subscribed users receive emails about cluster events that require customer action, known cluster incidents, upgrade maintenance, and other topics.

// Commented out while the OpenShift Cluster Manager CLI is in Developer Preview:
//include::modules/viewing-the-service-logs.adoc[leveloffset=+1]
//include::modules/viewing-the-service-logs-ocm.adoc[leveloffset=+2]
//include::modules/viewing-the-service-logs-cli.adoc[leveloffset=+2]
include::modules/viewing-the-service-logs-ocm.adoc[leveloffset=+1]
include::modules/adding-cluster-notification-contacts.adoc[leveloffset=+1]
