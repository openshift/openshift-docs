:_mod-docs-content-type: ASSEMBLY
[id="cert-types-aggregated-api-client-certificates"]
= Aggregated API client certificates
include::_attributes/common-attributes.adoc[]
:context: cert-types-aggregated-api-client-certificates

toc::[]

== Purpose

Aggregated API client certificates are used to authenticate the KubeAPIServer when connecting to the Aggregated API Servers.

== Management

These certificates are managed by the system and not the user.

== Expiration
This CA is valid for 30 days.

The managed client certificates are valid for 30 days.

CA and client certificates are rotated automatically through the use of controllers.

== Customization

You cannot customize the aggregated API server certificates.
