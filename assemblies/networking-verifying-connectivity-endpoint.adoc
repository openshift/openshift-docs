:_mod-docs-content-type: ASSEMBLY
[id="verifying-connectivity-endpoint"]
= Verifying connectivity to an endpoint
include::_attributes/common-attributes.adoc[]
:context: verifying-connectivity-endpoint

toc::[]

The Cluster Network Operator (CNO) runs a controller, the connectivity check controller, that performs a connection health check between resources within your cluster.
By reviewing the results of the health checks, you can diagnose connection problems or eliminate network connectivity as the cause of an issue that you are investigating.

include::modules/nw-pod-network-connectivity-checks.adoc[leveloffset=+1]
include::modules/nw-pod-network-connectivity-implementation.adoc[leveloffset=+1]
include::modules/nw-pod-network-connectivity-check-object.adoc[leveloffset=+1]
include::modules/nw-pod-network-connectivity-verify.adoc[leveloffset=+1]
