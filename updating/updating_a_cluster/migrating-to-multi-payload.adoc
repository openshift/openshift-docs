:_mod-docs-content-type: ASSEMBLY
[id="migrating-clusters-to-multi-payload"]
= Migrating to a cluster with multi-architecture compute machines
include::_attributes/common-attributes.adoc[]
:context: updating-clusters-overview

toc::[]

////
WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.
////

You can migrate your current cluster with single-architecture compute machines to a cluster with multi-architecture compute machines by updating to a multi-architecture, manifest-listed payload. This allows you to add mixed architecture compute nodes to your cluster.

For information about configuring your multi-architecture compute machines, see _Configuring multi-architecture compute machines on an {product-title} cluster_.

[IMPORTANT]
====
Migration from a multi-architecture payload to a single-architecture payload is not supported. Once a cluster has transitioned to using a multi-architecture payload, it can no longer accept a single-architecture update payload.
====

// Migrating to a cluster with multi-architecture compute machines using the CLI
include::modules/migrating-to-multi-arch-cli.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-configuration.adoc#multi-architecture-configuration[Configuring multi-architecture compute machines on an {product-title} cluster]
* xref:../../updating/updating_a_cluster/updating-cluster-web-console.adoc#updating-cluster-web-console[Updating a cluster using the web console]
* xref:../../updating/updating_a_cluster/updating-cluster-cli.adoc#updating-cluster-cli[Updating a cluster using the CLI]
* xref:../../updating/understanding_updates/intro-to-updates.adoc#understanding-clusterversion-conditiontypes_understanding-openshift-updates[Understanding cluster version condition types]
* xref:../../updating/understanding_updates/understanding-update-channels-release.adoc#understanding-update-channels-releases[Understanding update channels and releases]
* xref:../../installing/installing-preparing.adoc#installing-preparing-selecting-cluster-type[Selecting a cluster installation type]
* xref:../../machine_management/deploying-machine-health-checks.adoc#machine-health-checks-about_deploying-machine-health-checks[About machine health checks]
