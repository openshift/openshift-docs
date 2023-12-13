// Module included in the following assemblies:
//
// * updating/understanding_updates/how-updates-work.adoc

:_mod-docs-content-type: CONCEPT
[id="update-manifest-application_{context}"]
= Understanding how manifests are applied during an update

Some manifests supplied in a release image must be applied in a certain order because of the dependencies between them.
For example, the `CustomResourceDefinition` resource must be created before the matching custom resources.
Additionally, there is a logical order in which the individual cluster Operators must be updated to minimize disruption in the cluster.
The Cluster Version Operator (CVO) implements this logical order through the concept of Runlevels.

These dependencies are encoded in the filenames of the manifests in the release image:

[source,terminal]
----
0000_<runlevel>_<component>_<manifest-name>.yaml
----

For example:

[source,terminal]
----
0000_03_config-operator_01_proxy.crd.yaml
----

The CVO internally builds a dependency graph for the manifests, where the CVO obeys the following rules:

* During an update, manifests at a lower Runlevel are applied before those at a higher Runlevel.

* Within one Runlevel, manifests for different components can be applied in parallel.

* Within one Runlevel, manifests for a single component are applied in lexicographic order.

The CVO then applies manifests following the generated dependency graph.

[NOTE]
====
For some resource types, the CVO monitors the resource after its manifest is applied, and considers it to be successfully updated only after the resource reaches a stable state.
Achieving this state can take some time.
This is especially true for `ClusterOperator` resources, while the CVO waits for a cluster Operator to update itself and then update its `ClusterOperator` status.
====

// to do: potentially reword the note above to clarify that specific resources are being applied at one time, and not necessarily all the resources for that component.

The CVO waits until all cluster Operators in the Runlevel meet the following conditions before it proceeds to the next Runlevel:

* The cluster Operators have an `Available=True` condition.

* The cluster Operators have a `Degraded=False` condition.

// to do: potentially clarify that this condition is not applicable during installations, and also potentially add documentation (here or elsewhere) that explains how the CVO is constantly reconciling states whether or not an update is happening.

* The cluster Operators declare they have achieved the desired version in their ClusterOperator resource.

Some actions can take significant time to finish. The CVO waits for the actions to complete in order to ensure the subsequent Runlevels can proceed safely.
Initially reconciling the new release's manifests is expected to take 60 to 120 minutes in total; see *Understanding {product-title} update duration* for more information about factors that influence update duration.

image::update-runlevels.png[A diagram displaying the sequence of Runlevels and the manifests of components within each level]

In the previous example diagram, the CVO is waiting until all work is completed at Runlevel 20.
The CVO has applied all manifests to the Operators in the Runlevel, but the `kube-apiserver-operator ClusterOperator` performs some actions after its new version was deployed. The `kube-apiserver-operator ClusterOperator` declares this progress through the `Progressing=True` condition and by not declaring the new version as reconciled in its `status.versions`.
The CVO waits until the ClusterOperator reports an acceptable status, and then it will start reconciling manifests at Runlevel 25.
