:_mod-docs-content-type: ASSEMBLY
[id="rosa-accessing-the-service-logs"]
= Accessing the service logs for ROSA clusters
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-accessing-the-service-logs

toc::[]

[role="_abstract"]
You can view the service logs for your {product-title} (ROSA) clusters by using {cluster-manager-first}. The service logs detail cluster events such as load balancer quota updates and scheduled maintenance upgrades. The logs also show cluster resource changes such as the addition or deletion of users, groups, and identity providers.

// Commented out while the OpenShift Cluster Manager CLI is in Developer Preview:
//You can view the service logs for your {product-title} (ROSA) clusters by using {cluster-manager-first} or the {cluster-manager} CLI (`ocm`). The service logs detail cluster events such as load balancer quota updates and scheduled maintenance upgrades. The logs also show cluster resource changes such as the addition or deletion of users, groups, and identity providers.

Additionally, you can add notification contacts for a ROSA cluster. Subscribed users receive emails about cluster events that require customer action, known cluster incidents, upgrade maintenance, and other topics.

// Commented out while the OpenShift Cluster Manager CLI is in Developer Preview:
//include::modules/viewing-the-service-logs.adoc[leveloffset=+1]
//include::modules/viewing-the-service-logs-ocm.adoc[leveloffset=+2]
//include::modules/viewing-the-service-logs-cli.adoc[leveloffset=+2]
include::modules/viewing-the-service-logs-ocm.adoc[leveloffset=+1]
include::modules/adding-cluster-notification-contacts.adoc[leveloffset=+1]
