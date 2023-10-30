:_mod-docs-content-type: ASSEMBLY
[id="troubleshooting-operator-issues"]
= Troubleshooting Operator issues
include::_attributes/common-attributes.adoc[]
:context: troubleshooting-operator-issues

// This assembly is duplicated in operators/admin/olm-troubleshooting-operator-issues.adoc.

toc::[]

Operators are a method of packaging, deploying, and managing an {product-title} application. They act like an extension of the software vendor's engineering team, watching over an {product-title} environment and using its current state to make decisions in real time. Operators are designed to handle upgrades seamlessly, react to failures automatically, and not take shortcuts, such as skipping a software backup process to save time.

{product-title} {product-version} includes a default set of Operators that are required for proper functioning of the cluster. These default Operators are managed by the Cluster Version Operator (CVO).

As a cluster administrator, you can install application Operators from the OperatorHub using the {product-title} web console or the CLI. You can then subscribe the Operator to one or more namespaces to make it available for developers on your cluster. Application Operators are managed by Operator Lifecycle Manager (OLM).

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
// cannot delete resource "clusterserviceversions", "jobs" in API group "operators.coreos.com" in the namespace "openshift-apiserver"
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/olm-refresh-subs.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

// Reinstalling Operators after failed uninstallation
// cannot delete resource "customresourcedefinitions"
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/olm-reinstall.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

ifndef::openshift-rosa,openshift-dedicated[]
[role="_additional-resources"]
.Additional resources

* xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster]
* xref:../../operators/admin/olm-adding-operators-to-cluster.adoc#olm-adding-operators-to-a-cluster[Adding Operators to a cluster]
endif::openshift-rosa,openshift-dedicated[]


