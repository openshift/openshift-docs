// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubeVirtComponentExceedsRequestedCPU"]
= KubeVirtComponentExceedsRequestedCPU

[discrete]
[id="meaning-kubevirtcomponentexceedsrequestedcpu"]
== Meaning

This alert fires when a component's CPU usage exceeds the requested limit.

[discrete]
[id="impact-kubevirtcomponentexceedsrequestedcpu"]
== Impact

Usage of CPU resources is not optimal and the node might be overloaded.

[discrete]
[id="diagnosis-kubevirtcomponentexceedsrequestedcpu"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the component's CPU request limit:
+
[source,terminal]
----
$ oc -n $NAMESPACE get deployment <component> -o yaml | grep requests: -A 2
----

. Check the actual CPU usage by using a PromQL query:
+
[source,text]
----
node_namespace_pod_container:container_cpu_usage_seconds_total:sum_rate
{namespace="$NAMESPACE",container="<component>"}
----

See the
link:https://prometheus.io/docs/prometheus/latest/querying/basics/[Prometheus documentation]
for more information.

[discrete]
[id="mitigation-kubevirtcomponentexceedsrequestedcpu"]
== Mitigation

Update the CPU request limit in the `HCO` custom resource.
