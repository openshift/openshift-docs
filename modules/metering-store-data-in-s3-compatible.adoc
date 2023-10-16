// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-persistent-storage.adoc

[id="metering-store-data-in-s3-compatible_{context}"]
= Storing data in S3-compatible storage

You can use S3-compatible storage such as Noobaa.

.Procedure

. Edit the `spec.storage` section in the `s3-compatible-storage.yaml` file:
+
.Example `s3-compatible-storage.yaml` file
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
      type: "s3Compatible"
      s3Compatible:
        bucket: "bucketname" <1>
        endpoint: "http://example:port-number" <2>
        secretName: "my-aws-secret" <3>
----
<1> Specify the name of your S3-compatible bucket.
<2> Specify the endpoint for your storage.
<3> The name of a secret in the metering namespace containing the AWS credentials in the `data.aws-access-key-id` and `data.aws-secret-access-key` fields. See the example `Secret` object below for more details.

. Use the following `Secret` object as a template:
+
.Example S3-compatible `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-aws-secret
data:
  aws-access-key-id: "dGVzdAo="
  aws-secret-access-key: "c2VjcmV0Cg=="
----
