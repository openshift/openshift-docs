:_mod-docs-content-type: ASSEMBLY
[id="how-updates-work"]
= How cluster updates work
include::_attributes/common-attributes.adoc[]
:context: how-updates-work

toc::[]

The following sections describe each major aspect of the {product-title} (OCP) update process in detail. For a general overview of how updates work, see the xref:../../updating/understanding_updates/intro-to-updates.adoc#understanding-openshift-updates[Introduction to OpenShift updates].

// The Cluster Version Operator
include::modules/update-cvo.adoc[leveloffset=+1]

// The ClusterVersion object
include::modules/update-cluster-version-object.adoc[leveloffset=+2]

// Evaluation of update availability
include::modules/update-evaluate-availability.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../updating/understanding_updates/understanding-update-channels-release.adoc#conditional-updates-overview_understanding-update-channels-releases[Update recommendation removals and Conditional Updates]

// Release images
include::modules/update-release-images.adoc[leveloffset=+1]

// Update process workflow
include::modules/update-process-workflow.adoc[leveloffset=+1]

// Understanding how manifests are applied during an update
include::modules/update-manifest-application.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../updating/understanding_updates/understanding-openshift-update-duration.adoc#understanding-openshift-update-duration[Understanding {product-title} update duration]

// Understanding how the Machine Config Operator updates nodes
include::modules/update-mco-process.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../post_installation_configuration/machine-configuration-tasks.adoc#machine-config-overview-post-install-machine-configuration-tasks[Machine config overview]