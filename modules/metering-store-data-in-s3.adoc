// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-persistent-storage.adoc

[id="metering-store-data-in-s3_{context}"]
= Storing data in Amazon S3

Metering can use an existing Amazon S3 bucket or create a bucket for storage.

[NOTE]
====
Metering does not manage or delete any S3 bucket data. You must manually clean up S3 buckets that are used to store metering data.
====

.Procedure

. Edit the `spec.storage` section in the `s3-storage.yaml` file:
+
.Example `s3-storage.yaml` file
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
      type: "s3"
      s3:
        bucket: "bucketname/path/" <1>
        region: "us-west-1" <2>
        secretName: "my-aws-secret" <3>
        # Set to false if you want to provide an existing bucket, instead of
        # having metering create the bucket on your behalf.
        createBucket: true <4>
----
<1> Specify the name of the bucket where you would like to store your data. Optional: Specify the path within the bucket.
<2> Specify the region of your bucket.
<3> The name of a secret in the metering namespace containing the AWS credentials in the `data.aws-access-key-id` and `data.aws-secret-access-key` fields. See the example `Secret` object below for more details.
<4> Set this field to `false` if you want to provide an existing S3 bucket, or if you do not want to provide IAM credentials that have `CreateBucket` permissions.

. Use the following `Secret` object as a template:
+
.Example AWS `Secret` object
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
+
[NOTE]
====
The values of the `aws-access-key-id` and `aws-secret-access-key` must be base64 encoded.
====

. Create the secret:
+
[source,terminal]
----
$ oc create secret -n openshift-metering generic my-aws-secret \
  --from-literal=aws-access-key-id=my-access-key \
  --from-literal=aws-secret-access-key=my-secret-key
----
+
[NOTE]
====
This command automatically base64 encodes your `aws-access-key-id` and `aws-secret-access-key` values.
====

The `aws-access-key-id` and `aws-secret-access-key` credentials must have read and write access to the bucket. The following `aws/read-write.json` file shows an IAM policy that grants the required permissions:

.Example `aws/read-write.json` file
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:HeadBucket",
                "s3:ListBucket",
                "s3:ListMultipartUploadParts",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::operator-metering-data/*",
                "arn:aws:s3:::operator-metering-data"
            ]
        }
    ]
}
----

If `spec.storage.hive.s3.createBucket` is set to `true` or unset in your `s3-storage.yaml` file, then you should use the `aws/read-write-create.json` file that contains permissions for creating and deleting buckets:

.Example `aws/read-write-create.json` file
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:HeadBucket",
                "s3:ListBucket",
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:ListMultipartUploadParts",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::operator-metering-data/*",
                "arn:aws:s3:::operator-metering-data"
            ]
        }
    ]
}
----
