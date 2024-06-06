// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-cert-manager-integration-istio_{context}"]
= About integrating Service Mesh with cert-manager and istio-csr

The cert-manager tool is a solution for X.509 certificate management on Kubernetes. It delivers a unified API to integrate applications with private or public key infrastructure (PKI), such as Vault, Google Cloud Certificate Authority Service, Let's Encrypt, and other providers.

The cert-manager tool ensures the certificates are valid and up-to-date by attempting to renew certificates at a configured time before they expire.

For Istio users, cert-manager also provides integration with `istio-csr`, which is a certificate authority (CA) server that handles certificate signing requests (CSR) from Istio proxies. The server then delegates signing to cert-manager, which forwards CSRs to the configured CA server.

[NOTE]
====
Red Hat provides support for integrating with `istio-csr` and cert-manager. Red Hat does not provide direct support for the `istio-csr` or the community cert-manager components. The use of community cert-manager shown here is for demonstration purposes only.
====

.Prerequisites
* One of these versions of cert-manager:
** {cert-manager-operator} 1.10 or later
** community cert-manager Operator 1.11 or later
** cert-manager 1.11 or later

* OpenShift Service Mesh Operator 2.4 or later
* `istio-csr` 0.6.0 or later

[NOTE]
====
To avoid creating config maps in all namespaces when the `istio-csr` server is installed with the `jetstack/cert-manager-istio-csr` Helm chart, use the following setting: `app.controller.configmapNamespaceSelector: "maistra.io/member-of: <istio-namespace>"` in the `istio-csr.yaml` file.
====


