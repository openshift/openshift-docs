:_mod-docs-content-type: ASSEMBLY
[id="understanding-openshift-updates"]
= Introduction to OpenShift updates
include::_attributes/common-attributes.adoc[]
:context: understanding-openshift-updates

toc::[]

With {product-title} 4, you can update an {product-title} cluster with a single operation by using the web console or the OpenShift CLI (`oc`). Platform administrators can view new update options either by going to *Administration* -> *Cluster Settings* in the web console or by looking at the output of the `oc adm upgrade` command.

Red Hat hosts a public OpenShift Update Service (OSUS), which serves a graph of update possibilities based on the {product-title} release images in the official registry.
The graph contains update information for any public OCP release.
{product-title} clusters are configured to connect to the OSUS by default, and the OSUS responds to clusters with information about known update targets.

An update begins when either a cluster administrator or an automatic update controller edits the custom resource (CR) of the Cluster Version Operator (CVO) with a new version.
To reconcile the cluster with the newly specified version, the CVO retrieves the target release image from an image registry and begins to apply changes to the cluster.

[NOTE]
====
Operators previously installed through Operator Lifecycle Manager (OLM) follow a different process for updates. See xref:../../operators/admin/olm-upgrading-operators.adoc#olm-upgrading-operators[Updating installed Operators] for more information.
====

The target release image contains manifest files for all cluster components that form a specific OCP version.
When updating the cluster to a new version, the CVO applies manifests in separate stages called Runlevels.
Most, but not all, manifests support one of the cluster Operators.
As the CVO applies a manifest to a cluster Operator, the Operator might perform update tasks to reconcile itself with its new specified version.

The CVO monitors the state of each applied resource and the states reported by all cluster Operators. The CVO only proceeds with the update when all manifests and cluster Operators in the active Runlevel reach a stable condition.
After the CVO updates the entire control plane through this process, the Machine Config Operator (MCO) updates the operating system and configuration of every node in the cluster.

ifdef::openshift-enterprise[]

// Common questions about update availability
include::modules/update-availability-faq.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../updating/understanding_updates/understanding-update-channels-release.adoc#understanding-update-channels-releases[Understanding update channels and releases]

endif::openshift-enterprise[]

// About the OpenShift Update Service
include::modules/update-service-overview.adoc[leveloffset=+1]

// Understanding cluster Operator condition types
include::modules/determining-upgrade-viability-conditiontype.adoc[leveloffset=+1]

// Understanding cluster version condition types
include::modules/determining-upgrade-viability-cv-conditiontype.adoc[leveloffset=+1]

// Common terms
include::modules/update-common-terms.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../post_installation_configuration/machine-configuration-tasks.adoc#machine-config-overview-post-install-machine-configuration-tasks[Machine config overview]
ifdef::openshift-enterprise[]
* xref:../../updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc#update-service-overview_updating-restricted-network-cluster-osus[Using the OpenShift Update Service in a disconnected environment]
* xref:../../updating/understanding_updates/understanding-update-channels-release.adoc#understanding-update-channels_understanding-update-channels-releases[Update channels]

[id="{context}-additional-resources"]
[role="_additional-resources"]
== Additional resources
* xref:../../updating/understanding_updates/how-updates-work.adoc#how-updates-work[How cluster updates work].

endif::openshift-enterprise[]