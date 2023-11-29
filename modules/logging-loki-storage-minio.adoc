// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
//
:_mod-docs-content-type: PROCEDURE
[id="logging-loki-storage-minio_{context}"]
= Minio storage

.Prerequisites

* You have deployed Loki Operator.

* You have link:https://operator.min.io/[Minio] deployed on your Cluster.

* You have created a link:https://docs.min.io/docs/minio-client-complete-guide.html[bucket] on Minio.

.Procedure

* Create an object storage secret with the name `logging-loki-minio` by running the following command:

[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-minio \
  --from-literal=bucketnames="<bucket_name>" \
  --from-literal=endpoint="<minio_bucket_endpoint>" \
  --from-literal=access_key_id="<minio_access_key_id>" \
  --from-literal=access_key_secret="<minio_access_key_secret>"
----
