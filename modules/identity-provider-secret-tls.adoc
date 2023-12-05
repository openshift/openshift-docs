// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc

:_mod-docs-content-type: PROCEDURE
[id="identity-provider-creating-secret-tls_{context}"]
= Creating the secret

Identity providers use {product-title} `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

.Procedure

* Create a `Secret` object that contains the key and certificate by using the following command:
+
[source,terminal]
----
$ oc create secret tls <secret_name> --key=key.pem --cert=cert.pem -n openshift-config
----
+
[TIP]
====
You can alternatively apply the following YAML to create the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <secret_name>
  namespace: openshift-config
type: kubernetes.io/tls
data:
  tls.crt: <base64_encoded_cert>
  tls.key: <base64_encoded_key>
----
====
