// Module included in the following assemblies:
//
// * nodes/nodes-containers-port-forwarding.adoc

[id="nodes-containers-port-forwarding-protocol_{context}"]
= Protocol for initiating port forwarding from a client

Clients initiate port forwarding to a pod by issuing a request to the
Kubernetes API server:

----
/proxy/nodes/<node_name>/portForward/<namespace>/<pod>
----

In the above URL:

- `<node_name>` is the FQDN of the node.
- `<namespace>` is the namespace of the target pod.
- `<pod>` is the name of the target pod.

For example:

----
/proxy/nodes/node123.openshift.com/portForward/myns/mypod
----

After sending a port forward request to the API server, the client upgrades the
connection to one that supports multiplexed streams; the current implementation
uses link:https://httpwg.org/specs/rfc7540.html[*Hyptertext Transfer Protocol Version 2 (HTTP/2)*].

The client creates a stream with the `port` header containing the target port in
the pod. All data written to the stream is delivered via the kubelet to the
target pod and port. Similarly, all data sent from the pod for that forwarded
connection is delivered back to the same stream in the client.

The client closes all streams, the upgraded connection, and the underlying
connection when it is finished with the port forwarding request.
