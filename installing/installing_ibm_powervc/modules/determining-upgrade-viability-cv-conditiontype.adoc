// Module included in the following assemblies:
//
// * updating/index.adoc

:_mod-docs-content-type: CONCEPT
[id="understanding-clusterversion-conditiontypes_{context}"]
= Understanding cluster version condition types

The Cluster Version Operator (CVO) monitors cluster Operators and other components, and is responsible for collecting the status of both the cluster version and its Operators. This status includes the condition type, which informs you of the health and current state of the {product-title} cluster.

In addition to `Available`, `Progressing`, and `Upgradeable`, there are condition types that affect cluster versions and Operators.

* Failing:
The cluster version condition type `Failing` indicates that a cluster cannot reach its desired state, is unhealthy, and requires an administrator to intervene.

* Invalid:
The cluster version condition type `Invalid` indicates that the cluster version has an error that prevents the server from taking action. The CVO only reconciles the current state as long as this condition is set.

* RetrievedUpdates:
The cluster version condition type `RetrievedUpdates` indicates whether or not available updates have been retrieved from the upstream update server. The condition is `Unknown` before retrieval, `False` if the updates either recently failed or could not be retrieved, or `True` if the `availableUpdates` field is both recent and accurate.

* ReleaseAccepted:
The cluster version condition type `ReleaseAccepted` with a `True` status indicates that the requested release payload was successfully loaded without failure during image verification and precondition checking.

* ImplicitlyEnabledCapabilities:
The cluster version condition type `ImplicitlyEnabledCapabilities` with a `True` status indicates that there are enabled capabilities that the user is not currently requesting through `spec.capabilities`. The CVO does not support disabling capabilities if any associated resources were previously managed by the CVO.


