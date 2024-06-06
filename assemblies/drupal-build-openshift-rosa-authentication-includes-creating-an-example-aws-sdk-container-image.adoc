// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-an-example-aws-sdk-container-image_{context}"]
= Creating an example AWS SDK container image

The steps in this procedure provide an example method to create a container image that includes an AWS SDK.

The example steps use Podman to create the container image and Quay.io to host the image. For more information about Quay.io, see link:https://docs.quay.io/solution/getting-started.html[Getting Started with Quay.io]. The container image can be used to deploy pods that can run AWS SDK operations.

[NOTE]
====
In this example procedure, the AWS Boto3 SDK for Python is installed into a container image. For more information about installing and using the AWS Boto3 SDK, see the link:https://boto3.amazonaws.com/v1/documentation/api/latest/index.html[AWS Boto3 documentation]. For details about other AWS SDKs, see link:https://docs.aws.amazon.com/sdkref/latest/guide/overview.html[AWS SDKs and Tools Reference Guide] in the AWS documentation.
====

.Prerequisites

* You have installed Podman on your installation host.
* You have a Quay.io user account.

.Procedure

. Add the following configuration to a file named `Containerfile`:
+
[source,terminal]
----
FROM ubi9/ubi <1>
RUN dnf makecache && dnf install -y python3-pip && dnf clean all && pip3 install boto3>=1.15.0 <2>
----
<1> Specifies the Red Hat Universal Base Image version 9.
<2> Installs the AWS Boto3 SDK by using the `pip` package management system. In this example, AWS Boto3 SDK version 1.15.0 or later is installed.

. From the directory that contains the file, build a container image named `awsboto3sdk`:
+
[source,terminal]
----
$ podman build -t awsboto3sdk .
----

. Log in to Quay.io:
+
[source,terminal]
----
$ podman login quay.io
----

. Tag the image in preparation for the upload to Quay.io:
+
[source,terminal]
----
$ podman tag localhost/awsboto3sdk quay.io/<quay_username>/awsboto3sdk:latest <1>
----
<1> Replace `<quay_username>` with your Quay.io username.

. Push the tagged container image to Quay.io:
+
[source,terminal]
----
$ podman push quay.io/<quay_username>/awsboto3sdk:latest <1>
----
<1> Replace `<quay_username>` with your Quay.io username.

. Make the Quay.io repository that contains the image public. This publishes the image so that it can be used to deploy a pod in your {product-title} cluster:
.. On https://quay.io/, navigate to the *Repository Settings* page for repository that contains the image.
.. Click *Make Public* to make the repository publicly available.
