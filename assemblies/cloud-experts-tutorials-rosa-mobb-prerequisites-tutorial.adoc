:_mod-docs-content-type: ASSEMBLY
[id="rosa-mobb-prerequisites-tutorial"]
= Tutorial: ROSA prerequisites
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-mobb-prerequisites-tutorial

toc::[]

//Mobb content metadata
//Brought into ROSA product docs 2023-09-18
//---
//date: '2021-06-10'
//title: ROSA Prerequisites
//weight: 1
//tags: ["AWS", "ROSA", "Quickstarts"]
//authors:
//  - Steve Mirman
//  - Paul Czarkowski
//---
//This file is not being built as of 2023-09-22 based on a conversation with Michael McNeill.

This document contains a set of prerequisites that must be run once before you can create your first ROSA cluster.

== AWS

An AWS account with the link:https://console.aws.amazon.com/rosa/home?#/get-started[AWS ROSA prerequisites] met.


image::rosa-aws-pre.png[AWS console ROSA prequisites]

== AWS CLI

.MacOS

* Install AWS CLI using the MacOS command line:
+
[source,terminal]
----
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
----
+
[NOTE]
====
See link:https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html[AWS Documentation] for alternative install options.
====

.Linux

* Install AWS CLI using the Linux command line:
+
[source,terminal]
----
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
----
+
[NOTE]
====
See link:https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html[AWS Documentation] for alternative install options.
====

.Windows

* Install AWS CLI using the Windows command line:
+
[source,terminal]
----
$ C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
----
+
[NOTE]
====
See link:https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html[AWS Documentation] for alternative install options.
====

////
.Docker

* To run the AWS CLI version 2 Docker image, use the docker run command:
+
[source,terminal]
----
$ docker run --rm -it amazon/aws-cli command
----
+
[NOTE]
====
See link:https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-docker.html[AWS Documentation] for alternative install options.
====
////

== Prepare AWS Account for OpenShift

. Configure the AWS CLI by running:
+
[source,terminal]
----
$ aws configure
----
+
. You will be required to enter an `AWS Access Key ID` and an `AWS Secret Access Key` along with a default region name and output format:
+
[source,terminal]
----
$ aws configure
----
+
.Sample output
[source,terminal]
----
AWS Access Key ID []:
AWS Secret Access Key []:
Default region name [us-east-2]:
Default output format [json]:
----
+
The `AWS Access Key ID` and `AWS Secret Access Key` values can be obtained by logging in to the AWS console and creating an *Access Key* in the *Security Credentials* section of the IAM dashboard for your user.
+
. Validate your credentials:
+
[source,terminal]
----
$ aws sts get-caller-identity
----
+
You should receive output similar to the following:
+
.Sample output
[source,terminal]
----
{
    "UserId": <your ID>,
    "Account": <your account>,
    "Arn": <your arn>
}
----
+
. If this is a new AWS account that has never had a AWS Load Balancer (ALB) installed in it, run the following:
+
[source,terminal]
----
$ aws iam create-service-linked-role --aws-service-name \
    "elasticloadbalancing.amazonaws.com"
----

== Get a Red Hat Offline Access Token

. Log into {cluster-manager-url}.
. Navigate to link:https://cloud.redhat.com/openshift/token/rosa[OpenShift Cluster Manager API Token].
. Copy the *Offline Access Token* and save it for the next step.


== Set up the OpenShift CLI (oc)

. Download the operating system specific OpenShift CLI from link:https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/[Red Hat].
. Extract the downloaded file on your local machine.
. Place the extracted `oc` executable in your operating system path or local directory.

== Set up the ROSA CLI (rosa)

. Download the operating system specific ROSA CLI from link:https://www.openshift.com/products/amazon-openshift/download[Red Hat].
. Extract the downloaded file on your local machine.
. Place the extracted `rosa` and `kubectl` executables in your operating system path or local directory.
. Log in to ROSA:
+
[source,terminal]
----
$ rosa login
----
+
You will be prompted to enter in the *Red Hat Offline Access Token* you retrieved earlier and should receive the following message:
+
[source,terminal]
----
Logged in as <email address> on 'https://api.openshift.com'
----
+
. Verify that ROSA has the minimal quota:
+
[source,terminal]
----
$ rosa verify quota
----
+
Expected output:
+
[source,terminal]
----
AWS quota ok
----

== Associate your AWS account with your Red Hat account

To perform ROSA cluster provisioning tasks, you must create `ocm-role` and `user-role` IAM resources in your AWS account and link them to your Red Hat organization.

. Create the `ocm-role` which the OpenShift Cluster Manager will use to be able to administer and Create ROSA clusters. If this has already been done for your OpenShift Cluster Manager Organization, you can skip to creating the user-role:
+
[TIP]
====
If you have multiple AWS accounts that you want to associate with your Red Hat Organization, you can use the `--profile` option to specify the AWS profile you want to associate.
====
+
[source,terminal]
----
$ rosa create ocm-role --mode auto --yes
----
+
. Create the User Role that allows OpenShift Cluster Manager to verify that users creating a cluster have access to the current AWS account:
+
[TIP]
====
If you have multiple AWS accounts that you want to associate with your Red Hat Organization, you can use the `--profile` option to specify the AWS profile you want to associate.
====
+
[source,terminal]
----
$ rosa create user-role --mode auto --yes
----
+
. Create the ROSA Account Roles which give the ROSA installer and machines permissions to perform actions in your account:
+
[source,terminal]
----
$ rosa create account-roles --mode auto --yes
----

== Conclusion

You are now ready to create your first cluster.
