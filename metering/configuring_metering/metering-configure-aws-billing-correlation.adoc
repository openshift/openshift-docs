:_mod-docs-content-type: ASSEMBLY
[id="metering-configure-aws-billing-correlation"]
= Configure AWS billing correlation
include::_attributes/common-attributes.adoc[]
:context: metering-configure-aws-billing-correlation

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

Metering can correlate cluster usage information with https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage.html[AWS detailed billing information], attaching a dollar amount to resource usage. For clusters running in EC2, you can enable this by modifying the example `aws-billing.yaml` file below.

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: MeteringConfig
metadata:
  name: "operator-metering"
spec:
  openshift-reporting:
    spec:
      awsBillingReportDataSource:
        enabled: true
        # Replace these with where your AWS billing reports are
        # stored in S3.
        bucket: "<your-aws-cost-report-bucket>" <1>
        prefix: "<path/to/report>"
        region: "<your-buckets-region>"

  reporting-operator:
    spec:
      config:
        aws:
          secretName: "<your-aws-secret>" <2>

  presto:
    spec:
      config:
        aws:
          secretName: "<your-aws-secret>" <2>

  hive:
    spec:
      config:
        aws:
          secretName: "<your-aws-secret>" <2>
----
To enable AWS billing correlation, first ensure the AWS Cost and Usage Reports are enabled. For more information, see https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-gettingstarted-turnonreports.html[Turning on the AWS Cost and Usage Report] in the AWS documentation.

<1> Update the bucket, prefix, and region to the location of your AWS Detailed billing report.
<2> All `secretName` fields should be set to the name of a secret in the metering namespace containing AWS credentials in the `data.aws-access-key-id` and `data.aws-secret-access-key` fields. See the example secret file below for more details.

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <your-aws-secret>
data:
  aws-access-key-id: "dGVzdAo="
  aws-secret-access-key: "c2VjcmV0Cg=="
----

To store data in S3, the `aws-access-key-id` and `aws-secret-access-key` credentials must have read and write access to the bucket. For an example of an IAM policy granting the required permissions, see the `aws/read-write.json` file below.

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
                "arn:aws:s3:::operator-metering-data/*", <1>
                "arn:aws:s3:::operator-metering-data" <1>
            ]
        }
    ]
}
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
                "arn:aws:s3:::operator-metering-data/*", <1>
                "arn:aws:s3:::operator-metering-data" <1>
            ]
        }
    ]
}
----
<1> Replace `operator-metering-data` with the name of your bucket.

This can be done either preinstallation or postinstallation. Disabling it postinstallation can cause errors in the Reporting Operator.
