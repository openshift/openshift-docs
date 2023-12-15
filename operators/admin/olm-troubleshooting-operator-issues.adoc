:_mod-docs-content-type: ASSEMBLY
[id="olm-troubleshooting-operator-issues"]
= Troubleshooting Operator issues
include::_attributes/common-attributes.adoc[]
:context: olm-troubleshooting-operator-issues

// This assembly is a duplicate of support/troubleshooting-operator-issues.adoc. Most of the intro text is unnecessary in this context and has been removed.

toc::[]

If you experience Operator issues, verify Operator subscription status. Check Operator pod health across the cluster and gather Operator logs for diagnosis.

// Operator subscription condition types
include::modules/olm-status-conditions.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources

* xref:../../operators/understanding/olm/olm-understanding-olm.adoc#olm-cs-health_olm-understanding-olm[Catalog health requirements]

// Viewing Operator subscription status by using the CLI
include::modules/olm-status-viewing-cli.adoc[leveloffset=+1]

// Viewing Operator catalog source status by using the CLI
include::modules/olm-cs-status-cli.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

ifndef::openshift-rosa,openshift-dedicated[]
* xref:../../operators/understanding/olm/olm-understanding-olm.adoc#olm-catalogsource_olm-understanding-olm[Operator Lifecycle Manager concepts and resources -> Catalog source]
endif::openshift-rosa,openshift-dedicated[]
* gRPC documentation: link:https://grpc.github.io/grpc/core/md_doc_connectivity-semantics-and-api.html[States of Connectivity]
ifndef::openshift-rosa,openshift-dedicated[]
* xref:../../operators/admin/olm-managing-custom-catalogs.adoc#olm-accessing-images-private-registries_olm-managing-custom-catalogs[Accessing images for Operators from private registries]
endif::openshift-rosa,openshift-dedicated[]

// Querying Operator Pod status
include::modules/querying-operator-pod-status.adoc[leveloffset=+1]

// Gathering Operator logs
include::modules/gathering-operator-logs.adoc[leveloffset=+1]

// cannot patch resource "machineconfigpools"
ifndef::openshift-rosa,openshift-dedicated[]
// Disabling Machine Config Operator from autorebooting
include::modules/troubleshooting-disabling-autoreboot-mco.adoc[leveloffset=+1]
include::modules/troubleshooting-disabling-autoreboot-mco-console.adoc[leveloffset=+2]
include::modules/troubleshooting-disabling-autoreboot-mco-cli.adoc[leveloffset=+2]
endif::openshift-rosa,openshift-dedicated[]

// Refreshing failing subscriptions
// OSD/ROSA cannot delete resource "clusterserviceversions", "jobs" in API group "operators.coreos.com" in the namespace "openshift-apiserver"
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/olm-refresh-subs.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

// Reinstalling Operators after failed uninstallation
// OSD/ROSA gitcannot delete resource "customresourcedefinitions"
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/olm-reinstall.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

ifndef::openshift-rosa,openshift-dedicated[]
[role="_additional-resources"]
.Additional resources

* xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster]
* xref:../../operators/admin/olm-adding-operators-to-cluster.adoc#olm-adding-operators-to-a-cluster[Adding Operators to a cluster]
endif::openshift-rosa,openshift-dedicated[]
