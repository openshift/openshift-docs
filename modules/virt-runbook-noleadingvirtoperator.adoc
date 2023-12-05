// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-NoLeadingVirtOperator"]
= NoLeadingVirtOperator

[discrete]
[id="meaning-noleadingvirtoperator"]
== Meaning

This alert fires when no `virt-operator` pod with a leader lease has been detected
for 10 minutes, although the `virt-operator` pods are in a `Ready` state. The
alert indicates that no leader pod is available.

The `virt-operator` is the first Operator to start in a cluster. Its primary
responsibilities include the following:

* Installing, live updating, and live upgrading a cluster
* Monitoring the lifecycle of top-level controllers, such as `virt-controller`,
`virt-handler`, `virt-launcher`, and managing their reconciliation
* Certain cluster-wide tasks, such as certificate rotation and infrastructure
management

The `virt-operator` deployment has a default replica of 2 pods, with one pod
holding a leader lease.

[discrete]
[id="impact-noleadingvirtoperator"]
== Impact

This alert indicates a failure at the level of the cluster. As a result, critical
cluster-wide management functionalities, such as certification rotation, upgrade,
and reconciliation of controllers, might not be available.

[discrete]
[id="diagnosis-noleadingvirtoperator"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get kubevirt -A -o \
  custom-columns="":.metadata.namespace)"
----

. Obtain the status of the `virt-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l kubevirt.io=virt-operator
----

. Check the `virt-operator` pod logs to determine the leader status:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs | grep lead
----
+
Leader pod example:
+
[source,text]
----
{"component":"virt-operator","level":"info","msg":"Attempting to acquire
leader status","pos":"application.go:400","timestamp":"2021-11-30T12:15:18.635387Z"}
I1130 12:15:18.635452       1 leaderelection.go:243] attempting to acquire
leader lease <namespace>/virt-operator...
I1130 12:15:19.216582       1 leaderelection.go:253] successfully acquired
lease <namespace>/virt-operator
{"component":"virt-operator","level":"info","msg":"Started leading",
"pos":"application.go:385","timestamp":"2021-11-30T12:15:19.216836Z"}
----
+
Non-leader pod example:
+
[source,text]
----
{"component":"virt-operator","level":"info","msg":"Attempting to acquire
leader status","pos":"application.go:400","timestamp":"2021-11-30T12:15:20.533696Z"}
I1130 12:15:20.533792       1 leaderelection.go:243] attempting to acquire
leader lease <namespace>/virt-operator...
----

. Obtain the details of the affected `virt-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pod <virt-operator>
----

[discrete]
[id="mitigation-noleadingvirtoperator"]
== Mitigation

Based on the information obtained during the diagnosis procedure, try to find
the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
