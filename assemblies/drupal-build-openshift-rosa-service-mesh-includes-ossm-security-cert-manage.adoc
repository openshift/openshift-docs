// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-cert-manage_{context}"]
= Adding an external certificate authority key and certificate

By default, {SMProductName} generates a self-signed root certificate and key and uses them to sign the workload certificates. You can also use the user-defined certificate and key to sign workload certificates with user-defined root certificate. This task demonstrates an example to plug certificates and key into {SMProductShortName}.

.Prerequisites

* Install {SMProductName} with mutual TLS enabled to configure certificates.
* This example uses the certificates from the link:https://github.com/maistra/istio/tree/maistra-{MaistraVersion}/samples/certs[Maistra repository]. For production, use your own certificates from your certificate authority.
* Deploy the Bookinfo sample application to verify the results with these instructions.
* OpenSSL is required to verify certificates.
