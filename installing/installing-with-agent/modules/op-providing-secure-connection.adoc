[id='op-providing-secure-connection_{context}']
= Providing secure connection with OpenShift routes

To create a route with the re-encrypted TLS termination, run:

[source,terminal,subs="attributes+"]
----
$ oc create route reencrypt --service=<svc-name> --cert=tls.crt --key=tls.key --ca-cert=ca.crt --hostname=<hostname>
----

Alternatively, you can create a re-encrypted TLS termination YAML file to create a secure route.

.Example re-encrypt TLS termination YAML to create a secure route
[source,yaml,subs="attributes+"]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: route-passthrough-secured  <1>
spec:
  host: <hostname>
  to:
    kind: Service
    name: frontend <1>
  tls:
    termination: reencrypt <2>
    key: [as in edge termination]
    certificate: [as in edge termination]
    caCertificate: [as in edge termination]
    destinationCACertificate: |- <3>
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
----
<1> The name of the object, which is limited to only 63 characters.
<2> The termination field is set to `reencrypt`. This is the only required TLS field.
<3> This is required for re-encryption. The `destinationCACertificate` field specifies a CA certificate to validate the endpoint certificate, thus securing the connection from the router to the destination pods. You can omit this field in either of the following scenarios:
* The service uses a service signing certificate.
* The administrator specifies a default CA certificate for the router, and the service has a certificate signed by that CA.

You can run the `oc create route reencrypt --help` command to display more options.
