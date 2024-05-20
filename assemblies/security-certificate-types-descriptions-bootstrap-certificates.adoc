:_mod-docs-content-type: ASSEMBLY
[id="cert-types-bootstrap-certificates"]
= Bootstrap certificates
include::_attributes/common-attributes.adoc[]
:context: cert-types-bootstrap-certificates

toc::[]

== Purpose

The kubelet, in {product-title} 4 and later, uses the bootstrap certificate located in `/etc/kubernetes/kubeconfig` to initially bootstrap. This is followed by the link:https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#bootstrap-initialization[bootstrap initialization process] and link:https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#authorize-kubelet-to-create-csr[authorization of the kubelet to create a CSR].

In that process, the kubelet generates a CSR while communicating over the bootstrap channel. The controller manager signs the CSR, resulting in a certificate that the kubelet manages.

== Management

These certificates are managed by the system and not the user.

== Expiration
This bootstrap certificate is valid for 10 years.

The kubelet-managed certificate is valid for one year and rotates automatically at around the 80 percent mark of that one year.

[NOTE]
====
OpenShift Lifecycle Manager (OLM) does not update the bootstrap certificate.
====

== Customization

You cannot customize the bootstrap certificates.
