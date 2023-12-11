// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubemacpoolDown"]
= KubemacpoolDown

[discrete]
[id="meaning-kubemacpooldown"]
== Meaning

`KubeMacPool` is down. `KubeMacPool` is responsible for allocating MAC
addresses and preventing MAC address conflicts.

[discrete]
[id="impact-kubemacpooldown"]
== Impact

If `KubeMacPool` is down, `VirtualMachine` objects cannot be created.

[discrete]
[id="diagnosis-kubemacpooldown"]
== Diagnosis

. Set the `KMP_NAMESPACE` environment variable:
+
[source,terminal]
----
$ export KMP_NAMESPACE="$(oc get pod -A --no-headers -l \
  control-plane=mac-controller-manager | awk '{print $1}')"
----

. Set the `KMP_NAME` environment variable:
+
[source,terminal]
----
$ export KMP_NAME="$(oc get pod -A --no-headers -l \
  control-plane=mac-controller-manager | awk '{print $2}')"
----

. Obtain the `KubeMacPool-manager` pod details:
+
[source,terminal]
----
$ oc describe pod -n $KMP_NAMESPACE $KMP_NAME
----

. Check the `KubeMacPool-manager` logs for error messages:
+
[source,terminal]
----
$ oc logs -n $KMP_NAMESPACE $KMP_NAME
----

[discrete]
[id="mitigation-kubemacpooldown"]
== Mitigation

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
