// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubeVirtComponentExceedsRequestedMemory"]
= KubeVirtComponentExceedsRequestedMemory

[discrete]
[id="meaning-kubevirtcomponentexceedsrequestedmemory"]
== Meaning

This alert fires when a component's memory usage exceeds the requested limit.

[discrete]
[id="impact-kubevirtcomponentexceedsrequestedmemory"]
== Impact

Usage of memory resources is not optimal and the node might be overloaded.

[discrete]
[id="diagnosis-kubevirtcomponentexceedsrequestedmemory"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the component's memory request limit:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deployment <component> -o yaml | \
  grep requests: -A 2
----

. Check the actual memory usage by using a PromQL query:
+
[source,text]
----
container_memory_usage_bytes{namespace="$NAMESPACE",container="<component>"}
----

See the
link:https://prometheus.io/docs/prometheus/latest/querying/basics/[Prometheus documentation]
for more information.

[discrete]
[id="mitigation-kubevirtcomponentexceedsrequestedmemory"]
== Mitigation

Update the memory request limit in the `HCO` custom resource.
