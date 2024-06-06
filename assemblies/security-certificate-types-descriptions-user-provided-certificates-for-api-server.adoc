:_mod-docs-content-type: ASSEMBLY
[id="cert-types-user-provided-certificates-for-the-api-server"]
= User-provided certificates for the API server
include::_attributes/common-attributes.adoc[]
:context: cert-types-user-provided-certificates-for-the-api-server

toc::[]

== Purpose

The API server is accessible by clients external to the cluster at `api.<cluster_name>.<base_domain>`. You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients. The administrator must set a custom default certificate to be used by the API server when serving content.

== Location

The user-provided certificates must be provided in a `kubernetes.io/tls` type `Secret` in the `openshift-config` namespace. Update the API server cluster configuration, the `apiserver/cluster` resource, to enable the use of the user-provided certificate.

== Management

User-provided certificates are managed by the user.

== Expiration

API server client certificate expiration is less than five minutes.

User-provided certificates are managed by the user.

== Customization

Update the secret containing the user-managed certificate as needed.

[discrete]
[role="_additional-resources"]
== Additional resources

* xref:../../security/certificates/api-server.adoc#api-server-certificates[Adding API server certificates]
