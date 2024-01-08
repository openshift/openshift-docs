// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-configuring-jwks-resolver-ca_{context}"]
= Configuring JSON Web Key Sets resolver certificate authority

You can configure your own JSON Web Key Sets (JWKS) resolver certificate authority (CA) from the `ServiceMeshControlPlane` (SMCP) spec.

.Procedure

. Edit the `ServiceMeshControlPlane` spec file:
+
[source, yaml]
----
$ oc edit smcp <smcp-name>
----

. Enable `mtls` for the data plane by setting the value of the `mtls` field to `true` in the `ServiceMeshControlPlane` spec, as shown in the following example:
+
[source,yaml]
----
spec:
  security:
    dataPlane:
        mtls: true # enable mtls for data plane
    # JWKSResolver extra CA
    # PEM-encoded certificate content to trust an additional CA
    jwksResolverCA: |
        -----BEGIN CERTIFICATE-----
        [...]
        [...]
        -----END CERTIFICATE-----
...
----

. Save the changes. {product-title} automatically applies them.

A `ConfigMap` such as `pilot-jwks-cacerts-<SMCP name>` is created with the CA `.pem data`.

.Example ConfigMap `pilot-jwks-cacerts-<SMCP name>`
[source, yaml]
----
kind: ConfigMap
apiVersion: v1
data:
  extra.pem: |
      -----BEGIN CERTIFICATE-----
      [...]
      [...]
      -----END CERTIFICATE-----
----