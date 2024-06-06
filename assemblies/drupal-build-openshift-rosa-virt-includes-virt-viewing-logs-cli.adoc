// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-viewing-logs-cli_{context}"]
= Viewing {VirtProductName} pod logs with the CLI

You can view logs for the {VirtProductName} pods by using the `oc` CLI tool.

.Procedure

. View a list of pods in the {VirtProductName} namespace by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get pods -n {CNVNamespace}
----
+
.Example output
[%collapsible]
====
[source,terminal]
----
NAME                               READY   STATUS    RESTARTS   AGE
disks-images-provider-7gqbc        1/1     Running   0          32m
disks-images-provider-vg4kx        1/1     Running   0          32m
virt-api-57fcc4497b-7qfmc          1/1     Running   0          31m
virt-api-57fcc4497b-tx9nc          1/1     Running   0          31m
virt-controller-76c784655f-7fp6m   1/1     Running   0          30m
virt-controller-76c784655f-f4pbd   1/1     Running   0          30m
virt-handler-2m86x                 1/1     Running   0          30m
virt-handler-9qs6z                 1/1     Running   0          30m
virt-operator-7ccfdbf65f-q5snk     1/1     Running   0          32m
virt-operator-7ccfdbf65f-vllz8     1/1     Running   0          32m
----
====

. View the pod log by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc logs -n {CNVNamespace} <pod_name>
----
+
[NOTE]
====
If a pod fails to start, you can use the `--previous` option to view logs from the last attempt.

To monitor log output in real time, use the `-f` option.
====
+
.Example output
[%collapsible]
====
[source,terminal]
----
{"component":"virt-handler","level":"info","msg":"set verbosity to 2","pos":"virt-handler.go:453","timestamp":"2022-04-17T08:58:37.373695Z"}
{"component":"virt-handler","level":"info","msg":"set verbosity to 2","pos":"virt-handler.go:453","timestamp":"2022-04-17T08:58:37.373726Z"}
{"component":"virt-handler","level":"info","msg":"setting rate limiter to 5 QPS and 10 Burst","pos":"virt-handler.go:462","timestamp":"2022-04-17T08:58:37.373782Z"}
{"component":"virt-handler","level":"info","msg":"CPU features of a minimum baseline CPU model: map[apic:true clflush:true cmov:true cx16:true cx8:true de:true fpu:true fxsr:true lahf_lm:true lm:true mca:true mce:true mmx:true msr:true mtrr:true nx:true pae:true pat:true pge:true pni:true pse:true pse36:true sep:true sse:true sse2:true sse4.1:true ssse3:true syscall:true tsc:true]","pos":"cpu_plugin.go:96","timestamp":"2022-04-17T08:58:37.390221Z"}
{"component":"virt-handler","level":"warning","msg":"host model mode is expected to contain only one model","pos":"cpu_plugin.go:103","timestamp":"2022-04-17T08:58:37.390263Z"}
{"component":"virt-handler","level":"info","msg":"node-labeller is running","pos":"node_labeller.go:94","timestamp":"2022-04-17T08:58:37.391011Z"}
----
====