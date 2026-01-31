// Module included in the following assemblies:
//
// * nodes/nodes-containers-port-forwarding.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-port-forwarding-using_{context}"]
= Using port forwarding

You can use the CLI to port-forward one or more local ports to a pod.

.Procedure

Use the following command to listen on the specified port in a pod:

[source,terminal]
----
$ oc port-forward <pod> [<local_port>:]<remote_port> [...[<local_port_n>:]<remote_port_n>]
----

For example:

* Use the following command to listen on ports `5000` and `6000` locally and forward data to and from ports `5000` and `6000` in the pod:
+
[source,terminal]
----
$ oc port-forward <pod> 5000 6000
----
+
.Example output
[source,terminal]
----
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Forwarding from 127.0.0.1:6000 -> 6000
Forwarding from [::1]:6000 -> 6000
----

* Use the following command to listen on port `8888` locally and forward to `5000` in the pod:
+
[source,terminal]
----
$ oc port-forward <pod> 8888:5000
----
+
.Example output
[source,terminal]
----
Forwarding from 127.0.0.1:8888 -> 5000
Forwarding from [::1]:8888 -> 5000
----

* Use the following command to listen on a free port locally and forward to `5000` in the pod:
+
[source,terminal]
----
$ oc port-forward <pod> :5000
----
+
.Example output
[source,terminal]
----
Forwarding from 127.0.0.1:42390 -> 5000
Forwarding from [::1]:42390 -> 5000
----
+
Or:
+
[source,terminal]
----
$ oc port-forward <pod> 0:5000
----

