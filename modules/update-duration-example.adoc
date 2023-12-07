// Module included in the following assemblies:
//
// * updating/understanding_updates/understanding-openshift-update-duration.adoc

:_mod-docs-content-type: CONCEPT
[id="update-duration-example_{context}"]
= Example update duration of cluster Operators

image::update-duration.png[A diagram displaying the periods during which cluster Operators update themselves during an OCP update]

The previous diagram shows an example of the time that cluster Operators might take to update to their new versions.
The example is based on a three-node AWS OVN cluster, which has a healthy compute `MachineConfigPool` and no workloads that take long to drain, updating from 4.13 to 4.14.

[NOTE]
====
* The specific update duration of a cluster and its Operators can vary based on several cluster characteristics, such as the target version, the amount of nodes, and the types of workloads scheduled to the nodes.

* Some Operators, such as the Cluster Version Operator, update themselves in a short amount of time.
These Operators have either been omitted from the diagram or are included in the broader group of Operators labeled "Other Operators in parallel".
====

Each cluster Operator has characteristics that affect the time it takes to update itself.
For instance, the Kube API Server Operator in this example took more than eleven minutes to update because `kube-apiserver` provides graceful termination support, meaning that existing, in-flight requests are allowed to complete gracefully.
This might result in a longer shutdown of the `kube-apiserver`.
In the case of this Operator, update speed is sacrificed to help prevent and limit disruptions to cluster functionality during an update.

Another characteristic that affects the update duration of an Operator is whether the Operator utilizes DaemonSets.
The Network and DNS Operators utilize full-cluster DaemonSets, which can take time to roll out their version changes, and this is one of several reasons why these Operators might take longer to update themselves.

The update duration for some Operators is heavily dependent on characteristics of the cluster itself. For instance, the Machine Config Operator update applies machine configuration changes to each node in the cluster. A cluster with many nodes has a longer update duration for the Machine Config Operator compared to a cluster with fewer nodes.

[NOTE]
====
Each cluster Operator is assigned a stage during which it can be updated.
Operators within the same stage can update simultaneously, and Operators in a given stage cannot begin updating until all previous stages have been completed.
For more information, see "Understanding how manifests are applied during an update" in the "Additional resources" section.
====