// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

:_mod-docs-content-type: PROCEDURE
[id="verifying-the-assumed-iam-role-in-your-pod_{context}"]
= Verifying the assumed IAM role in your pod

After deploying an `awsboto3sdk` pod in your project, verify that the pod identity webhook has mutated the pod. Check that the required AWS environment variables, volume mount, and OIDC token volume are present within the pod.

You can also verify that the service account assumes the AWS Identity and Access Management (IAM) role for your AWS account when you run AWS SDK operations in the pod.

.Prerequisites

* You have created an AWS IAM role for your service account. For more information, see _Setting up an AWS IAM role for a service account_.
* You have access to a {product-title} cluster that uses the AWS Security Token Service (STS). Admin-level user privileges are not required.
* You have installed the OpenShift CLI (`oc`).
* You have created a service account in your project that includes an `eks.amazonaws.com/role-arn` annotation that references the Amazon Resource Name (ARN) for the IAM role that you want the service account to assume.
* You have deployed a pod in your user-defined project that includes an AWS SDK. The pod references the service account that uses the pod identity webhook to assume the AWS IAM role required to run the AWS SDK operations. For detailed steps, see _Deploying a pod that includes an AWS SDK_.
+
[NOTE]
====
In this example procedure, a pod that includes the AWS Boto3 SDK for Python is used. For more information about installing and using the AWS Boto3 SDK, see the link:https://boto3.amazonaws.com/v1/documentation/api/latest/index.html[AWS Boto3 documentation]. For details about other AWS SDKs, see link:https://docs.aws.amazon.com/sdkref/latest/guide/overview.html[AWS SDKs and Tools Reference Guide] in the AWS documentation.
====

.Procedure

. Verify that the AWS environment variables, the volume mount, and the OIDC token volume are listed in the description of the deployed `awsboto3sdk` pod:
+
[source,terminal]
----
$ oc describe pod awsboto3sdk
----
+
.Example output:
[source,terminal]
----
Name:         awsboto3sdk
Namespace:    <project_name>
...
Containers:
  awsboto3sdk:
    ...
    Environment:
      AWS_ROLE_ARN:                 <aws_iam_role_arn> <1>
      AWS_WEB_IDENTITY_TOKEN_FILE:  /var/run/secrets/eks.amazonaws.com/serviceaccount/token <2>
    Mounts:
      /var/run/secrets/eks.amazonaws.com/serviceaccount from aws-iam-token (ro) <3>
...
Volumes:
  aws-iam-token: <4>
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  86400
...
----
<1> Lists the `AWS_ROLE_ARN` environment variable that was injected into the pod by the pod identity webhook. The variable contains the ARN of the AWS IAM role to be assumed by the service account.
<2> Lists the `AWS_WEB_IDENTITY_TOKEN_FILE` environment variable that was injected into the pod by the pod identity webhook. The variable contains the full path of the OIDC token that is used to verify the service account identity.
<3> Lists the volume mount that was injected into the pod by the pod identity webhook.
<4> Lists the `aws-iam-token` volume that is mounted onto the `/var/run/secrets/eks.amazonaws.com/serviceaccount` mount point. The volume contains the OIDC token that is used to authenticate the service account to assume the AWS IAM role.

. Start an interactive terminal in the `awsboto3sdk` pod:
+
[source,terminal]
----
$ oc exec -ti awsboto3sdk -- /bin/sh
----

. In the interactive terminal for the pod, verify that the `$AWS_ROLE_ARN` environment variable was mutated into the pod by the pod identity webhook:
+
[source,terminal]
----
$ echo $AWS_ROLE_ARN
----
+
.Example output:
[source,terminal]
----
arn:aws:iam::<aws_account_id>:role/<aws_iam_role_name> <1>
----
<1> The output must specify the ARN for the AWS IAM role that has the permissions required to run AWS SDK operations.

. In the interactive terminal for the pod, verify that the `$AWS_WEB_IDENTITY_TOKEN_FILE` environment variable was mutated into the pod by the pod identity webhook:
+
[source,terminal]
----
$ echo $AWS_WEB_IDENTITY_TOKEN_FILE
----
+
.Example output:
[source,terminal]
----
/var/run/secrets/eks.amazonaws.com/serviceaccount/token <1>
----
<1> The output must specify the full path in the pod to the OIDC token for the service account.

. In the interactive terminal for the pod, verify that the `aws-iam-token` volume mount containing the OIDC token file was mounted by the pod identity webhook:
+
[source,terminal]
----
$ mount | grep -is 'eks.amazonaws.com'
----
+
.Example output:
[source,terminal]
----
tmpfs on /run/secrets/eks.amazonaws.com/serviceaccount type tmpfs (ro,relatime,seclabel,size=13376888k)
----

. In the interactive terminal for the pod, verify that an OIDC token file named `token` is present on the `/var/run/secrets/eks.amazonaws.com/serviceaccount/` mount point:
+
[source,terminal]
----
$ ls /var/run/secrets/eks.amazonaws.com/serviceaccount/token
----
+
.Example output:
[source,terminal]
----
/var/run/secrets/eks.amazonaws.com/serviceaccount/token <1>
----
<1> The OIDC token file in the `aws-iam-token` volume that was mounted in the pod by the pod identity webhook. The token is used to authenticate the identity of the service account in AWS.

. In the pod, verify that AWS Boto3 SDK operations run successfully:

.. In the interactive terminal for the pod, start a Python 3 shell:
+
[source,terminal]
----
$ python3
----

.. In the Python 3 shell, import the `boto3` module:
+
[source,python]
----
>>> import boto3
----

.. Create a variable that includes the Boto3 `s3` service resource:
+
[source,python]
----
>>> s3 = boto3.resource('s3')
----

.. Print the names of all of the S3 buckets in your AWS account:
+
[source,python]
----
>>> for bucket in s3.buckets.all():
...     print(bucket.name)
...
----
+
.Example output:
[source,python]
----
<bucket_name>
<bucket_name>
<bucket_name>
...
----
+
If the service account successfully assumed the AWS IAM role, the output lists all of the S3 buckets that are available in your AWS account.
