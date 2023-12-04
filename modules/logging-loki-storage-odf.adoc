// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
//
:_mod-docs-content-type: PROCEDURE
[id="logging-loki-storage-odf_{context}"]

= ODF storage

.Prerequisites

* You have deployed Loki Operator.

* You have deployed link:https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/[OpenShift Data Foundation].

* You have configured your OpenShift Data Foundation cluster https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.14/html/managing_and_allocating_storage_resources/adding-file-and-object-storage-to-an-existing-external-ocs-cluster[for object storage].

.Procedure

. Create an `ObjectBucketClaim` custom resource in the `openshift-logging` namespace:
+
[source,yaml]
----
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: loki-bucket-odf
  namespace: openshift-logging
spec:
  generateBucketName: loki-bucket-odf
  storageClassName: openshift-storage.noobaa.io
----

. Get bucket properties from the associated `ConfigMap` object by running the following command:
+
[source,terminal]
----
BUCKET_HOST=$(oc get -n openshift-logging configmap loki-bucket-odf -o jsonpath='{.data.BUCKET_HOST}')
BUCKET_NAME=$(oc get -n openshift-logging configmap loki-bucket-odf -o jsonpath='{.data.BUCKET_NAME}')
BUCKET_PORT=$(oc get -n openshift-logging configmap loki-bucket-odf -o jsonpath='{.data.BUCKET_PORT}')
----

. Get bucket access key from the associated secret by running the following command:
+
[source,terminal]
----
ACCESS_KEY_ID=$(oc get -n openshift-logging secret loki-bucket-odf -o jsonpath='{.data.AWS_ACCESS_KEY_ID}' | base64 -d)
SECRET_ACCESS_KEY=$(oc get -n openshift-logging secret loki-bucket-odf -o jsonpath='{.data.AWS_SECRET_ACCESS_KEY}' | base64 -d)
----

.. Create an object storage secret with the name `logging-loki-odf` by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create -n openshift-logging secret generic logging-loki-odf \
--from-literal=access_key_id="<access_key_id>" \
--from-literal=access_key_secret="<secret_access_key>" \
--from-literal=bucketnames="<bucket_name>" \
--from-literal=endpoint="https://<bucket_host>:<bucket_port>"
----
