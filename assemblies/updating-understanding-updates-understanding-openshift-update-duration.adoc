:_mod-docs-content-type: ASSEMBLY
[id="understanding-openshift-update-duration"]
= Understanding {product-title} update duration
include::_attributes/common-attributes.adoc[]
:context: openshift-update-duration

toc::[]

////
WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.
////

{product-title} update duration varies based on the deployment topology. This page helps you understand the factors that affect update duration and estimate how long the cluster update takes in your environment.

// Factors affecting update duration
include::modules/update-duration-factors.adoc[leveloffset=+1]

[id="cluster-update-phases"]
== Cluster update phases
In {product-title}, the cluster update happens in two phases:

* Cluster Version Operator (CVO) target update payload deployment
* Machine Config Operator (MCO) node updates

// Cluster Version Operator target update payload deployment
include::modules/update-duration-cvo.adoc[leveloffset=+2]

// Machine Config Operator node updates
include::modules/update-duration-mco.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../post_installation_configuration/machine-configuration-tasks.adoc#machine-config-overview-post-install-machine-configuration-tasks[Machine config overview]
* xref:../../nodes/pods/nodes-pods-configuring.adoc#nodes-pods-configuring-pod-distruption-about_nodes-pods-configuring[Pod disruption budget]

//Example update duration of cluster Operators
include::modules/update-duration-example.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../updating/understanding_updates/intro-to-updates.adoc#understanding-openshift-updates[Introduction to OpenShift updates]
* xref:../../updating/understanding_updates/how-updates-work.adoc#update-manifest-application_how-updates-work[Understanding how manifests are applied during an update]

// Estimating cluster update time
include::modules/update-duration-estimate-cluster-update-time.adoc[leveloffset=+1]

ifndef::openshift-origin[]
// {op-system-base-full} compute nodes
include::modules/update-duration-rhel-nodes.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../updating/updating_a_cluster/updating-cluster-rhel-compute.adoc#updating-cluster-rhel-compute[Updating RHEL compute machines]
endif::openshift-origin[]

[role="_additional-resources"]
[id="additional-resources_update-duration"]
== Additional resources

* xref:../../architecture/architecture.adoc#architecture[OpenShift Container Platform architecture]
* xref:../../updating/understanding_updates/intro-to-updates.adoc#understanding-openshift-updates[OpenShift Container Platform updates]