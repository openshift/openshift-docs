:_mod-docs-content-type: ASSEMBLY
[id="deprecated-features"]
= Deprecated features
include::_attributes/common-attributes.adoc[]
:context: deprecated-features

toc::[]

Large changes to the underlying architecture and installation process are
applied in {product-title} v4, and many features from {product-title} v3 are
now deprecated.

[id="deprecated"]
== Features deprecated in {product-title} v4

.Features Deprecated in {product-version}
[cols="2",options="header"]
|====
|Feature |Justification

|Hawkular
|Replaced by cluster monitoring.

|Cassandra
|Replaced by cluster monitoring.

|Heapster
|Replaced by Prometheus adapter.

|Atomic Host
|Replaced by {op-system-first}.

|System containers
|Replaced by {op-system-first}.

|`projectatomic/docker-1.13` additional search registries
|CRI-O is the default container runtime for {product-title} v4 on Fedora.

|`oc adm diagnostics`
|Operator-based diagnostics.

|`oc adm registry`
|Replaced by the Image Registry Operator.

|Custom strategy builds using Docker
|If you want to continue using custom builds, you should replace your Docker
invocations with Podman or Buildah. The custom build strategy will not be
removed, but the functionality changed significantly in OpenShift v4.

|Cockpit
|Improved OpenShift v4 web console.

|Stand-alone registry installations
|Quay is Red Hat's container image registry.

|DNSmasq
|CoreDNS is the default.

|External etcd nodes
|etcd is always on the cluster in OpenShift v4.

|CloudForms OpenShift Provider and Podified CloudForms
|Replaced by built-in management tooling.

|Volume Provisioning via installer
|Replaced by dynamic volumes or, if NFS is required, NFS provisioner.

|Blue-green installation method
|Ease of upgrade is a core value of OpenShift v4.

|OpenShift Service Broker and Service Catalog
|The Service Catalog and the OpenShift service brokers are being replaced over
the course of several future OpenShift v4 releases. Reference the Operator
Framework and Operator Lifecycle Manager (OLM) to continue providing your
applications to OpenShift v4 clusters. These new technologies provide many
benefits around complete management of the lifecycle of your application.

|`oc adm ca`
|Certificates are managed by Operators internally.

|`oc adm create-api-client-config`
.2+.^|Functions are managed by Operators internally.

|`oc adm create-bootstrap-policy-file`

|`oc adm policy reconcile-sccs`
|Functions are managed by `openshift-apiserver` internally.

|Web console
|The web console from OpenShift v3 has been replaced by a new web
console in OpenShift v4.

|====
