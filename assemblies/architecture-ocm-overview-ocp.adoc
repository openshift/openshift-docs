:_mod-docs-content-type: ASSEMBLY
[id="ocm-overview-ocp"]
= Red Hat OpenShift Cluster Manager
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: ocm-overview-ocp
toc::[]

{cluster-manager-first} is a managed service where you can install, modify, operate, and upgrade your Red Hat OpenShift clusters. This service allows you to work with all of your organization’s clusters from a single dashboard.

{cluster-manager} guides you to install {OCP}, Red Hat OpenShift Service on AWS (ROSA), and {product-short-name} clusters. It is also responsible for managing both {OCP} clusters after self-installation as well as your ROSA and {product-short-name} clusters.

You can use {cluster-manager} to do the following actions:

* Create new clusters
* View cluster details and metrics
* Manage your clusters with tasks such as scaling, changing node labels, networking, authentication
* Manage access control
* Monitor clusters
* Schedule upgrades

include::modules/ocm-accessing.adoc[leveloffset=+1]

[id="ocm-general-actions-ocp"]
== General actions

On the top right of the cluster page, there are some actions that a user can perform on the entire cluster:

* **Open console** launches a web console so that the cluster owner can issue commands to the cluster.
* **Actions** drop-down menu allows the cluster owner to rename the display name of the cluster, change the amount of load balancers and persistent storage on the cluster, if applicable, manually set the node count, and delete the cluster.
* **Refresh** icon forces a refresh of the cluster.

[id="ocm-cluster-tabs-ocp"]
== Cluster tabs

Selecting an active, installed cluster shows tabs associated with that cluster. The following tabs display after the cluster's installation completes:

* Overview
* Access control
* Add-ons
* Networking
* Insights Advisor
* Machine pools
* Support
* Settings

include::modules/ocm-overview-tab.adoc[leveloffset=+2]
include::modules/ocm-accesscontrol-tab.adoc[leveloffset=+2]
include::modules/ocm-addons-tab.adoc[leveloffset=+2]
include::modules/ocm-insightsadvisor-tab.adoc[leveloffset=+2]
include::modules/ocm-machinepools-tab.adoc[leveloffset=+2]
include::modules/ocm-support-tab.adoc[leveloffset=+2]
include::modules/ocm-settings-tab.adoc[leveloffset=+2]

[id="ocm-additional-resources-ocp"]
== Additional resources

* For the complete documentation for {cluster-manager}, see link:https://access.redhat.com/documentation/en-us/openshift_cluster_manager/2022/html-single/managing_clusters/index[{cluster-manager} documentation].
