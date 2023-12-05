:_mod-docs-content-type: ASSEMBLY
[id="understanding-update-channels-releases"]
= Understanding update channels and releases
include::_attributes/common-attributes.adoc[]
:context: understanding-update-channels-releases

toc::[]

////
WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.
////

Update channels are the mechanism by which users declare the {product-title} minor version they intend to update their clusters to. They also allow users to choose the timing and level of support their updates will have through the `fast`, `stable`, `candidate`, and `eus` channel options. The Cluster Version Operator uses an update graph based on the channel declaration, along with other conditional information, to provide a list of recommended and conditional updates available to the cluster.

Update channels correspond to a minor version of {product-title}. The version number in the channel represents the target minor version that the cluster will eventually be updated to, even if it is higher than the cluster's current minor version.

For instance, {product-title} 4.10 update channels provide the following recommendations:

* Updates within 4.10.
* Updates within 4.9.
* Updates from 4.9 to 4.10, allowing all 4.9 clusters to eventually update to 4.10, even if they do not immediately meet the minimum z-stream version requirements.
* `eus-4.10` only: updates within 4.8.
* `eus-4.10` only: updates from 4.8 to 4.9 to 4.10, allowing all 4.8 clusters to eventually update to 4.10.

4.10 update channels do not recommend updates to 4.11 or later releases. This strategy ensures that administrators must explicitly decide to update to the next minor version of {product-title}.

Update channels control only release selection and do not impact the version of the cluster that you install. The `openshift-install` binary file for a specific version of {product-title} always installs that version.

ifndef::openshift-origin[]
{product-title} {product-version} offers the following update channels:

* `stable-{product-version}`
* `eus-4.y` (only offered for EUS versions and meant to facilitate updates between EUS versions)
* `fast-{product-version}`
* `candidate-{product-version}`

If you do not want the Cluster Version Operator to fetch available updates from the update recommendation service, you can use the `oc adm upgrade channel` command in the OpenShift CLI to configure an empty channel. This configuration can be helpful if, for example, a cluster has restricted network access and there is no local, reachable update recommendation service.

[WARNING]
====
Red Hat recommends updating to versions suggested by OpenShift Update Service only. For a minor version update, versions must be contiguous. Red Hat does not test updates to noncontiguous versions and cannot guarantee compatibility with earlier versions.
====

endif::openshift-origin[]
ifdef::openshift-origin[]
{product-title} {product-version} offers the following update channel:

* `stable-4`

endif::openshift-origin[]

// Update channels
include::modules/understanding-update-channels.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../updating/updating_a_cluster/updating-cluster-cli.adoc#update-conditional-upgrade-pathupdating-cluster-cli[Updating along a conditional upgrade path]
* xref:../../updating/understanding_updates/understanding-update-channels-release.adoc#fast-stable-channel-strategies_understanding-update-channels-releases[Choosing the correct channel for your cluster]
