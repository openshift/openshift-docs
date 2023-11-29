:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="cluster-local-availability"]
= Cluster local availability
:context: cluster-local-availability

toc::[]

By default, Knative services are published to a public IP address.
Being published to a public IP address means that Knative services are public applications, and have a publicly accessible URL.

Publicly accessible URLs are accessible from outside of the cluster.
However, developers may need to build back-end services that are only be accessible from inside the cluster, known as _private services_.
// Cluster administrators can configure private services for the cluster so that all services are private by default.
// Need to add additional details about editing the configmap for admins
Developers can label individual services in the cluster with the `networking.knative.dev/visibility=cluster-local` label to make them private.

[IMPORTANT]
====
For {ServerlessProductName} 1.15.0 and newer versions, the `serving.knative.dev/visibility` label is no longer available. You must update existing services to use the `networking.knative.dev/visibility` label instead.
====

include::modules/knative-service-cluster-local.adoc[leveloffset=+1]

include::modules/serverless-enabling-tls-local-services.adoc[leveloffset=+1]

