// Module included in the following assemblies:
//
// * osd_getting_started/osd-getting-started.adoc

:_mod-docs-content-type: PROCEDURE
[id="scaling-cluster_{context}"]
= Scaling your cluster

You can scale the number of load balancers, the persistent storage capacity, and the node count for your {product-title} cluster from {cluster-manager}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an {product-title} cluster.

.Procedure

* To scale the number of load balancers or the persistent storage capacity:
. Navigate to {cluster-manager-url} and select your cluster.
. Select *Edit load balancers and persistent storage* from the *Actions* drop-down menu.
. Select how many *Load balancers* that you want to scale to.
. Select the *Persistent storage* capacity that you want to scale to.
. Click *Apply*. Scaling occurs automatically.

* To scale the node count:
. Navigate to {cluster-manager-url} and select your cluster.
. Select *Edit node count* from the *Actions* drop-down menu.
. Select a *Machine pool*.
. Select a *Node count* per zone.
. Click *Apply*. Scaling occurs automatically.

.Verification

* In the *Overview* tab under the *Details* heading, you can review the load balancer configuration, persistent storage details, and actual and desired node counts.
