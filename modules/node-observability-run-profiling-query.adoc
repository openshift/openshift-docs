// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="running-profiling-query_{context}"]
= Running the profiling query

To run the profiling query, you must create a `NodeObservabilityRun` resource. The profiling query is a blocking operation that fetches CRI-O and Kubelet profiling data for a duration of 30 seconds. After the profiling query is complete, you must retrieve the profiling data inside the container file system `/run/node-observability` directory. The lifetime of data is bound to the agent pod through the `emptyDir` volume, so you can access the profiling data while the agent pod is in the `running` status.

[IMPORTANT]
====
You can request only one profiling query at any point of time.
====

.Prerequisites
* You have installed the Node Observability Operator.
* You have created the `NodeObservability` custom resource (CR).
* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create a `NodeObservabilityRun` resource file named `nodeobservabilityrun.yaml` that contains the following text:
+
[source,yaml]
----
apiVersion: nodeobservability.olm.openshift.io/v1alpha2
kind: NodeObservabilityRun
metadata:
  name: nodeobservabilityrun
spec:
  nodeObservabilityRef:
    name: cluster
----

. Trigger the profiling query by running the `NodeObservabilityRun` resource:
+
[source,terminal]
----
$ oc apply -f nodeobservabilityrun.yaml
----

. Review the status of the `NodeObservabilityRun` by running the following command:
+
[source,terminal]
----
$ oc get nodeobservabilityrun nodeobservabilityrun -o yaml  | yq '.status.conditions'
----

+
.Example output
[source,terminal]
----
conditions:
- lastTransitionTime: "2022-07-07T14:57:34Z"
  message: Ready to start profiling
  reason: Ready
  status: "True"
  type: Ready
- lastTransitionTime: "2022-07-07T14:58:10Z"
  message: Profiling query done
  reason: Finished
  status: "True"
  type: Finished
----

+
The profiling query is complete once the status is `True` and type is `Finished`.

. Retrieve the profiling data from the container's `/run/node-observability` path by running the following bash script:
+
[source,bash]
----
for a in $(oc get nodeobservabilityrun nodeobservabilityrun -o yaml | yq .status.agents[].name); do
  echo "agent ${a}"
  mkdir -p "/tmp/${a}"
  for p in $(oc exec "${a}" -c node-observability-agent -- bash -c "ls /run/node-observability/*.pprof"); do
    f="$(basename ${p})"
    echo "copying ${f} to /tmp/${a}/${f}"
    oc exec "${a}" -c node-observability-agent -- cat "${p}" > "/tmp/${a}/${f}"
  done
done
----
