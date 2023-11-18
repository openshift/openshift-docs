// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-LowVirtOperatorCount"]
= LowVirtOperatorCount

[discrete]
[id="meaning-lowvirtoperatorcount"]
== Meaning

This alert fires when only one `virt-operator` pod in a `Ready` state has
been running for the last 60 minutes.

The `virt-operator` is the first Operator to start in a cluster. Its primary
responsibilities include the following:

* Installing, live-updating, and live-upgrading a cluster
* Monitoring the lifecycle of top-level controllers, such as `virt-controller`,
`virt-handler`, `virt-launcher`, and managing their reconciliation
* Certain cluster-wide tasks, such as certificate rotation and infrastructure
management

[discrete]
[id="impact-lowvirtoperatorcount"]
== Impact

The `virt-operator` cannot provide high availability (HA) for the deployment.
HA requires two or more `virt-operator` pods in a `Ready` state. The default
deployment is two pods.

The `virt-operator` is not directly responsible for virtual machines (VMs)
in the cluster. Therefore, its decreased availability does not significantly
affect VM workloads.

[discrete]
[id="diagnosis-lowvirtoperatorcount"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A \
  -o custom-columns="":.metadata.namespace)"
----

. Check the states of the `virt-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l kubevirt.io=virt-operator
----

. Review the logs of the affected `virt-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs <virt-operator>
----

. Obtain the details of the affected `virt-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pod <virt-operator>
----

[discrete]
[id="mitigation-lowvirtoperatorcount"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to
identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the link:https://access.redhat.com[Customer Portal]
and open a support case, attaching the artifacts gathered during the Diagnosis
procedure.
