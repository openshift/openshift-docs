// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-NetworkAddonsConfigNotReady"]
= NetworkAddonsConfigNotReady

[discrete]
[id="meaning-networkaddonsconfignotready"]
== Meaning

This alert fires when the `NetworkAddonsConfig` custom resource (CR) of the
Cluster Network Addons Operator (CNAO) is not ready.

CNAO deploys additional networking components on the cluster. This alert indicates
that one of the deployed components is not ready.

[discrete]
[id="impact-networkaddonsconfignotready"]
== Impact

Network functionality is affected.

[discrete]
[id="diagnosis-networkaddonsconfignotready"]
== Diagnosis

. Check the status conditions of the `NetworkAddonsConfig` CR to identify the
deployment or daemon set that is not ready:
+
[source,terminal]
----
$ oc get networkaddonsconfig \
  -o custom-columns="":.status.conditions[*].message
----
+
.Example output
+
[source,text]
----
DaemonSet "cluster-network-addons/macvtap-cni" update is being processed...
----

. Check the component's pod for errors:
+
[source,terminal]
----
$ oc -n cluster-network-addons get daemonset <pod> -o yaml
----

. Check the component's logs:
+
[source,terminal]
----
$ oc -n cluster-network-addons logs <pod>
----

. Check the component's details for error conditions:
+
[source,terminal]
----
$ oc -n cluster-network-addons describe <pod>
----

[discrete]
[id="mitigation-networkaddonsconfignotready"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
