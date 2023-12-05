// This is included in the following assemblies:
//
// networking/routes/route-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-re-encrypt-route-with-custom-certificate_{context}"]
= Creating a route using the destination CA certificate in the Ingress annotation

The `route.openshift.io/destination-ca-certificate-secret` annotation can be used on an Ingress object to define a route with a custom destination CA certificate.

.Prerequisites
* You may have a certificate/key pair in PEM-encoded files, where the certificate is valid for the route host.
* You may have a separate CA certificate in a PEM-encoded file that completes the certificate chain.
* You must have a separate destination CA certificate in a PEM-encoded file.
* You must have a service that you want to expose.


.Procedure

. Add the `route.openshift.io/destination-ca-certificate-secret` to the Ingress annotations:
+
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend
  annotations:
    route.openshift.io/termination: "reencrypt"
    route.openshift.io/destination-ca-certificate-secret: secret-ca-cert <1>
...
----
<1> The annotation references a kubernetes secret.

+
. The secret referenced in this annotation will be inserted into the generated route.
+
.Example output
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: frontend
  annotations:
    route.openshift.io/termination: reencrypt
    route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
spec:
...
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: reencrypt
    destinationCACertificate: |
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
...
----
