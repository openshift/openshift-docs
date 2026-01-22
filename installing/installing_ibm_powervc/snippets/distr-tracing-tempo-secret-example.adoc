// Text snippet included in the following modules:
//
// * distr-tracing-tempo-install-web-console.adoc
// * distr-tracing-tempo-install-cli.adoc

:_mod-docs-content-type: SNIPPET

.Example secret for Amazon S3 and MinIO storage
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: minio-test
stringData:
  endpoint: http://minio.minio.svc:9000
  bucket: tempo
  access_key_id: tempo
  access_key_secret: <secret>
type: Opaque
----
