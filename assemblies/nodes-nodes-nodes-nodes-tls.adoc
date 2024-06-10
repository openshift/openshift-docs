:_mod-docs-content-type: ASSEMBLY
:context: nodes-nodes-tls
[id="nodes-nodes-tls"]
= Enabling TLS security profiles for the kubelet
include::_attributes/common-attributes.adoc[]

toc::[]

You can use a TLS (Transport Layer Security) security profile to define which TLS ciphers are required by the kubelet when it is acting as an HTTP server. The kubelet uses its HTTP/GRPC server to communicate with the Kubernetes API server, which sends commands to pods, gathers logs, and run exec commands on pods through the kubelet.

A TLS security profile defines the TLS ciphers that the Kubernetes API server must use when connecting with the kubelet to protect communication between the kubelet and the Kubernetes API server.

[NOTE]
====
By default, when the kubelet acts as a client with the Kubernetes API server, it automatically negotiates the TLS parameters with the API server.
====

include::modules/tls-profiles-understanding.adoc[leveloffset=+1]

include::modules/tls-profiles-kubelet-configuring.adoc[leveloffset=+1]


