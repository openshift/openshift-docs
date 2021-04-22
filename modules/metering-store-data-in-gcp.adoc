// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-persistent-storage.adoc

[id="metering-store-data-in-gcp_{context}"]
= Storing data in Google Cloud Storage

To store your data in Google Cloud Storage, you must use an existing bucket.

.Procedure

. Edit the `spec.storage` section in the `gcs-storage.yaml` file:
+
.Example `gcs-storage.yaml` file
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: MeteringConfig
metadata:
  name: "operator-metering"
spec:
  storage:
    type: "hive"
    hive:
      type: "gcs"
      gcs:
        bucket: "metering-gcs/test1" <1>
        secretName: "my-gcs-secret" <2>
----
<1> Specify the name of the bucket. You can optionally specify the directory within the bucket where you would like to store your data.
<2> Specify a secret in the metering namespace. See the example `Secret` object below for more details.

. Use the following `Secret` object as a template:
+
.Example Google Cloud Storage `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-gcs-secret
data:
  gcs-service-account.json: "c2VjcmV0Cg=="
----

. Create the secret:
+
[source,terminal]
----
$ oc create secret -n openshift-metering generic my-gcs-secret \
  --from-file gcs-service-account.json=/path/to/my/service-account-key.json
----
