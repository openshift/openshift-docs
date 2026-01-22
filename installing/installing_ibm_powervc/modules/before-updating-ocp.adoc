// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating-cluster-web-console.adoc

:_mod-docs-content-type: CONCEPT
[id="before-updating-ocp_{context}"]
= Before updating the {product-title} cluster

Before updating, consider the following:

* You have recently backed up etcd.

* In `PodDisruptionBudget`, if `minAvailable` is set to `1`, the nodes are drained to apply pending machine configs that might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the `PodDisruptionBudget` field can prevent the node drain.

* You might need to update the cloud provider resources for the new release if your cluster uses manually maintained credentials.

* You must review administrator acknowledgement requests, take any recommended actions, and provide the acknowledgement when you are ready.

* You can perform a partial update by updating the worker or custom pool nodes to accommodate the time it takes to update. You can pause and resume within the progress bar of each pool.