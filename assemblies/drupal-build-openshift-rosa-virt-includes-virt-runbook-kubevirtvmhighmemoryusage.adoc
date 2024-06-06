// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubevirtVmHighMemoryUsage"]
= KubevirtVmHighMemoryUsage

[discrete]
[id="meaning-kubevirtvmhighmemoryusage"]
== Meaning

This alert fires when a container hosting a virtual machine (VM) has less
than 20 MB free memory.

[discrete]
[id="impact-kubevirtvmhighmemoryusage"]
== Impact

The virtual machine running inside the container is terminated by the runtime
if the container's memory limit is exceeded.

[discrete]
[id="diagnosis-kubevirtvmhighmemoryusage"]
== Diagnosis

. Obtain the `virt-launcher` pod details:
+
[source,terminal]
----
$ oc get pod <virt-launcher> -o yaml
----

. Identify `compute` container processes with high memory usage in the
`virt-launcher` pod:
+
[source,terminal]
----
$ oc exec -it <virt-launcher> -c compute -- top
----

[discrete]
[id="mitigation-kubevirtvmhighmemoryusage"]
== Mitigation

* Increase the memory limit in the `VirtualMachine` specification as in
the following example:
+
[source,yaml]
----
spec:
  running: false
  template:
    metadata:
      labels:
        kubevirt.io/vm: vm-name
    spec:
      domain:
        resources:
          limits:
            memory: 200Mi
          requests:
            memory: 128Mi
----
