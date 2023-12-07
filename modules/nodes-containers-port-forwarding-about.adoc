// Module included in the following assemblies:
//
// * nodes/nodes-containers-port-forwarding.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-port-forwarding-about_{context}"]
= Understanding port forwarding

You can use the CLI to forward one or more local ports to a pod. This allows you
to listen on a given or random port locally, and have data forwarded to and from
given ports in the pod.

Support for port forwarding is built into the CLI:

[source,terminal]
----
$ oc port-forward <pod> [<local_port>:]<remote_port> [...[<local_port_n>:]<remote_port_n>]
----

The CLI listens on each local port specified by the user, forwarding using the protocol described below.

Ports may be specified using the following formats:

[horizontal]
`5000`:: The client listens on port 5000 locally and forwards to 5000 in the
pod.
`6000:5000`:: The client listens on port 6000 locally and forwards to 5000 in
the pod.
`:5000` or `0:5000`:: The client selects a free local port and forwards to 5000
in the pod.

{product-title} handles port-forward requests from clients. Upon receiving a request, {product-title} upgrades the response and waits for the client
to create port-forwarding streams. When {product-title} receives a new stream, it copies data between the stream and the pod's port.

Architecturally, there are options for forwarding to a pod's port. The supported {product-title} implementation invokes `nsenter` directly on the node host
to enter the pod's network namespace, then invokes `socat` to copy data between the stream and the pod's port. However, a custom implementation could
include running a _helper_ pod that then runs `nsenter` and `socat`, so that those binaries are not required to be installed on the host.

