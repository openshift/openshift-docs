// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
//
:_mod-docs-content-type: PROCEDURE
[id="logging-loki-storage-gcp_{context}"]
= GCP storage

.Prerequisites

* You have deployed Loki Operator.

* You have created a link:https://cloud.google.com/resource-manager/docs/creating-managing-projects[project] on Google Cloud Platform.

* You have created a link:https://cloud.google.com/storage/docs/creating-buckets[bucket] in the same project.

* You have created a link:https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account[service account] in the same project for GCP authentication.

.Procedure

. Copy the service account credentials received from GCP into a file called `key.json`.

. Create an object storage secret with the name `logging-loki-gcs` by running the following command:

+
[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-gcs \
  --from-literal=bucketname="<bucket_name>" \
  --from-file=key.json="<path/to/key.json>"
----
