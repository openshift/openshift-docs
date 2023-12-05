// Module included in the following assemblies:
//
// * /serverless/security/serverless-config-tls.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-enabling-tls-local-services_{context}"]
= Enabling TLS authentication for cluster local services

For cluster local services, the Kourier local gateway `kourier-internal` is used. If you want to use TLS traffic against the Kourier local gateway, you must configure your own server certificates in the local gateway.

.Prerequisites

* You have installed the {ServerlessOperatorName} and Knative Serving.
* You have administrator permissions.
* You have installed the OpenShift (`oc`) CLI.

.Procedure

. Deploy server certificates in the `knative-serving-ingress` namespace:
+
[source,terminal]
----
$ export san="knative"
----
+
[NOTE]
====
Subject Alternative Name (SAN) validation is required so that these certificates can serve the request to `<app_name>.<namespace>.svc.cluster.local`.
====

. Generate a root key and certificate:
+
[source,terminal]
----
$ openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 \
    -subj '/O=Example/CN=Example' \
    -keyout ca.key \
    -out ca.crt
----

. Generate a server key that uses SAN validation:
+
[source,terminal]
----
$ openssl req -out tls.csr -newkey rsa:2048 -nodes -keyout tls.key \
  -subj "/CN=Example/O=Example" \
  -addext "subjectAltName = DNS:$san"
----

. Create server certificates:
+
[source,terminal]
----
$ openssl x509 -req -extfile <(printf "subjectAltName=DNS:$san") \
  -days 365 -in tls.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial -out tls.crt
----

. Configure a secret for the Kourier local gateway:
.. Deploy a secret in `knative-serving-ingress` namespace from the certificates created by the previous steps:
+
[source,terminal]
----
$ oc create -n knative-serving-ingress secret tls server-certs \
    --key=tls.key \
    --cert=tls.crt --dry-run=client -o yaml | oc apply -f -
----

.. Update the `KnativeServing` custom resource (CR) spec to use the secret that was created by the Kourier gateway:
+
.Example KnativeServing CR
[source,yaml]
----
...
spec:
  config:
    kourier:
      cluster-cert-secret: server-certs
...
----

The Kourier controller sets the certificate without restarting the service, so that you do not need to restart the pod.

You can access the Kourier internal service with TLS through port `443` by mounting and using the `ca.crt` from the client.
