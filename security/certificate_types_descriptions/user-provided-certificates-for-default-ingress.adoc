:_mod-docs-content-type: ASSEMBLY
[id="cert-types-user-provided-certificates-for-default-ingress"]
= User-provided certificates for default ingress
include::_attributes/common-attributes.adoc[]
:context: cert-types-user-provided-certificates-for-default-ingress

toc::[]

== Purpose

Applications are usually exposed at `<route_name>.apps.<cluster_name>.<base_domain>`. The `<cluster_name>` and `<base_domain>` come from the installation config file. `<route_name>` is the host field of the route, if specified, or the route name. For example, `hello-openshift-default.apps.username.devcluster.openshift.com`. `hello-openshift` is the name of the route and the route is in the default namespace. You might want clients to access the applications without the need to distribute the cluster-managed CA certificates to the clients. The administrator must set a custom default certificate when serving application content.

[WARNING]
====
The Ingress Operator generates a default certificate for an Ingress Controller to serve as a placeholder until you configure a custom default certificate. Do not use operator-generated default certificates in production clusters.
====

== Location

The user-provided certificates must be provided in a `tls` type `Secret` resource in the `openshift-ingress` namespace. Update the `IngressController` CR in the `openshift-ingress-operator` namespace to enable the use of the user-provided certificate. For more information on this process, see xref:../../networking/ingress-operator.adoc#nw-ingress-setting-a-custom-default-certificate_configuring-ingress[Setting a custom default certificate].

== Management

User-provided certificates are managed by the user.

== Expiration

User-provided certificates are managed by the user.

== Services

Applications deployed on the cluster use user-provided certificates for default ingress.

== Customization

Update the secret containing the user-managed certificate as needed.

[discrete]
[role="_additional-resources"]
== Additional resources

* xref:../../security/certificates/replacing-default-ingress-certificate.adoc#replacing-default-ingress[Replacing the default ingress certificate]
