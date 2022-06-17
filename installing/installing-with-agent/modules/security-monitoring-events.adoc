// Module included in the following assemblies:
//
// * security/container_security/security-monitoring.adoc

[id="security-monitoring-events_{context}"]
= Watching cluster events

Cluster administrators are encouraged to familiarize themselves with the `Event` resource
type and review the list of system events to
determine which events are of interest.
Events are associated with a namespace, either the namespace of the
resource they are related to or, for cluster events, the `default`
namespace. The default namespace holds relevant events for monitoring or auditing a cluster,
such as node events and resource events related to infrastructure components.

The master API and `oc` command do not provide parameters to scope a listing of events to only those
related to nodes. A simple approach would be to use `grep`:

[source,terminal]
----
$ oc get event -n default | grep Node
----

.Example output
[source,terminal]
----
1h         20h         3         origin-node-1.example.local   Node      Normal    NodeHasDiskPressure   ...
----

A more flexible approach is to output the events in a form that other
tools can process. For example, the following example uses the `jq`
tool against JSON output to extract only `NodeHasDiskPressure` events:

[source,terminal]
----
$ oc get events -n default -o json \
  | jq '.items[] | select(.involvedObject.kind == "Node" and .reason == "NodeHasDiskPressure")'
----

.Example output
[source,terminal]
----
{
  "apiVersion": "v1",
  "count": 3,
  "involvedObject": {
    "kind": "Node",
    "name": "origin-node-1.example.local",
    "uid": "origin-node-1.example.local"
  },
  "kind": "Event",
  "reason": "NodeHasDiskPressure",
  ...
}
----

Events related to resource creation, modification, or deletion can also be
good candidates for detecting misuse of the cluster. The following query,
for example, can be used to look for excessive pulling of images:

[source,terminal]
----
$ oc get events --all-namespaces -o json \
  | jq '[.items[] | select(.involvedObject.kind == "Pod" and .reason == "Pulling")] | length'
----

.Example output
[source,terminal]
----
4
----

[NOTE]
====
When a namespace is deleted, its events are deleted as well. Events can also expire and are deleted to prevent
filling up etcd storage. Events are
not stored as a permanent record and frequent polling is necessary to capture statistics over time.
====
