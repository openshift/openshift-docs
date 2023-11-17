// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
//
:_mod-docs-content-type: CONCEPT
[id="logging-loki-storage_{context}"]
= Loki object storage

The Loki Operator supports link:https://aws.amazon.com/[AWS S3], as well as other S3 compatible object stores such as link:https://min.io/[Minio] and link:https://www.redhat.com/en/technologies/cloud-computing/openshift-data-foundation[OpenShift Data Foundation]. link:https://azure.microsoft.com[Azure], link:https://cloud.google.com/[GCS], and link:https://docs.openstack.org/swift/latest/[Swift] are also supported.

The recommended nomenclature for Loki storage is `logging-loki-_<your_storage_provider>_`.

You can create a secret in the directory that contains your certificate and key files by using the following command:

[source,terminal]
----
$ oc create secret generic -n openshift-logging <your_secret_name> \
 --from-file=tls.key=<your_key_file>
 --from-file=tls.crt=<your_crt_file>
 --from-file=ca-bundle.crt=<your_bundle_file>
 --from-literal=username=<your_username>
 --from-literal=password=<your_password>
----

[NOTE]
====
Use generic or opaque secrets for best results.
====

You can verify a secret has been created by running the following command:

[source,terminal]
----
$ oc get secrets
----

The following table shows the `type` values within the `LokiStack` custom resource (CR) for each storage provider. For more information, see the section on your storage provider.

[options="header"]
.Secret type quick reference
|===
| Storage provider          | Secret `type` value
| AWS                       | s3
| Azure                     | azure
| Google Cloud              | gcs
| Minio                     | s3
| OpenShift Data Foundation | s3
| Swift                     | swift
|===
