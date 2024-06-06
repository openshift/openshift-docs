[id="osd-updating-cluster-prepare"]
= Preparing to upgrade {product-title} to 4.9
include::_attributes/common-attributes.adoc[]
ifdef::openshift-dedicated,openshift-rosa[]
include::_attributes/attributes-openshift-dedicated.adoc[]
endif::[]
:context: osd-updating-cluster-prepare

toc::[]

Upgrading your {product-title} clusters to OpenShift 4.9 requires you to evaluate and migrate your APIs as the latest version of Kubernetes has removed a significant number of APIs.

Before you can upgrade your {product-title} clusters, you must update the required tools to the appropriate version.

include::modules/upgrade-49-acknowledgement.adoc[leveloffset=+1]

// Removed Kubernetes APIs

// Removed Kubernetes APIs
include::modules/osd-update-preparing-list.adoc[leveloffset=+1]

[id="osd-evaluating-cluster-removed-apis"]
== Evaluating your cluster for removed APIs

There are several methods to help administrators identify where APIs that will be removed are in use. However, {product-title} cannot identify all instances, especially workloads that are idle or external tools that are used. It is the responsibility of the administrator to properly evaluate all workloads and other integrations for instances of removed APIs.

// Reviewing alerts to identify uses of removed APIs
include::modules/osd-update-preparing-evaluate-alerts.adoc[leveloffset=+2]

// Using APIRequestCount to identify uses of removed APIs
include::modules/osd-update-preparing-evaluate-apirequestcount.adoc[leveloffset=+2]

// Using APIRequestCount to identify which workloads are using the removed APIs
include::modules/osd-update-preparing-evaluate-apirequestcount-workloads.adoc[leveloffset=+2]

// Migrating instances of removed APIs
include::modules/osd-update-preparing-migrate.adoc[leveloffset=+1]
