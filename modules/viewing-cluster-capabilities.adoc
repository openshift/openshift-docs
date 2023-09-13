// Module included in the following assemblies:
//
// *post_installation_configuration/cluster-capabilities.adoc

[id="viewing_the_cluster_capabilities_{context}"]
= Viewing the cluster capabilities
As a cluster administrator, you can view the capabilities by using the `clusterversion` resource status.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

.Procedure

* To view the status of the cluster capabilities, run the following command:
+
[source,terminal]
----
$ oc get clusterversion version -o jsonpath='{.spec.capabilities}{"\n"}{.status.capabilities}{"\n"}'
----

+
.Example output
[source,terminal]
----
{"additionalEnabledCapabilities":["openshift-samples"],"baselineCapabilitySet":"None"}
{"enabledCapabilities":["openshift-samples"],"knownCapabilities":["CSISnapshot","Console","Insights","Storage","baremetal","marketplace","openshift-samples"]}
----
