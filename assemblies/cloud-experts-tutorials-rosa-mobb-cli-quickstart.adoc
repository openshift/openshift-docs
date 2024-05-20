:_mod-docs-content-type: ASSEMBLY
[id="rosa-mobb-cli-quickstart"]
= Create a {product-title} cluster using the CLI
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-mobb-cli-quickstart

toc::[]


//Mobb content metadata
//Brought into ROSA product docs 2023-09-12
//---
//date: '2021-06-10'
//title: ROSA Quickstart
//weight: 1
//aliases: [/docs/quickstart-rosa.md]
//Tags: ["AWS", "ROSA", "Quickstarts"]
//authors:
//  - Steve Mirman
//  - Paul Czarkowski
//---

A Quickstart guide to deploying a Red Hat OpenShift cluster on AWS using the CLI.

== Video Walkthrough

////
 Introduction to ROSA by Charlotte Fung on [AWS YouTube channel](https://youtu.be/KRqXxek4GvQ)

<iframe width="560" height="315" src="https://www.youtube.com/embed/KRqXxek4GvQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


If you prefer a more visual medium, you can watch [Steve Mirman](https://twitter.com/stevemirman) walk through this quickstart on [YouTube](https://www.youtube.com/watch?v=IFNig_Z_p2Y).
<iframe width="560" height="315" src="https://www.youtube.com/embed/IFNig_Z_p2Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
////

== Prerequisites

=== AWS

You must have an AWS account with the link:https://console.aws.amazon.com/rosa/home?#/get-started[AWS ROSA Prerequisites] met.

image::rosa-aws-pre.png[AWS console rosa requisites]

**MacOS**

//See [AWS Docs](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html) for alternative install options.

* Install AWS CLI using the macOS command line:

[source,bash]
----
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
----

**Linux**

// See [AWS Docs](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html) for alternative install options.

* Install AWS CLI using the Linux command line:

[source,bash]
----
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
----

**Windows**

// See [AWS Docs](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html) for alternative install options.

* Install AWS CLI using the Windows command line

[source,bash]
----
$ C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
----

////
**Docker**

> See [AWS Docs](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-docker.html) for alternative install options.

1. To run the AWS CLI version 2 Docker image, use the docker run command.

    ```bash
    docker run --rm -it amazon/aws-cli command
   ```
////

=== Prepare AWS Account for OpenShift

* Configure the AWS CLI by running the following command:

[source,bash]
----
$ aws configure
----

2. You will be required to enter an `AWS Access Key ID` and an `AWS Secret Access Key` along with a default region name and output format

    ```bash
    % aws configure
    AWS Access Key ID []:
    AWS Secret Access Key []:
    Default region name [us-east-2]:
    Default output format [json]:
    ```
    The `AWS Access Key ID` and `AWS Secret Access Key` values can be obtained by logging in to the AWS console and creating an **Access Key** in the **Security Credentials** section of the IAM dashboard for your user

3. Validate your credentials

    ```bash
    aws sts get-caller-identity
    ```

    You should receive output similar to the following
    ```
    {
      "UserId": <your ID>,
      "Account": <your account>,
      "Arn": <your arn>
    }
    ```

4. If this is a brand new AWS account that has never had a AWS Load Balancer installed in it, you should run the following

    ```bash
    aws iam create-service-linked-role --aws-service-name \
    "elasticloadbalancing.amazonaws.com"
    ```

### Get a Red Hat Offline Access Token

1. Log into cloud.redhat.com

2. Browse to https://cloud.redhat.com/openshift/token/rosa

3. Copy the **Offline Access Token** and save it for the next step


### Set up the OpenShift CLI (oc)

1. Download the OS specific OpenShift CLI from [Red Hat](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/)

2. Unzip the downloaded file on your local machine

3. Place the extracted `oc` executable in your OS path or local directory


### Set up the ROSA CLI

1. Download the OS specific ROSA CLI from [Red Hat](https://www.openshift.com/products/amazon-openshift/download)

2. Unzip the downloaded file on your local machine

3. Place the extracted `rosa` and `kubectl` executables in your OS path or local directory

4. Log in to ROSA

  ```bash
  rosa login
  ```

  You will be prompted to enter in the **Red Hat Offline Access Token** you retrieved earlier and should receive the following message

  ```
  Logged in as <email address> on 'https://api.openshift.com'
  ```

### Verify ROSA privileges

Verify that ROSA has the minimal permissions

  ```bash
  rosa verify permissions
  ```
>Expected output: `AWS SCP policies ok`


Verify that ROSA has the minimal quota

  ```bash
  rosa verify quota
  ```
>Expected output: `AWS quota ok`


### Initialize ROSA

Initialize the ROSA CLI to complete the remaining validation checks and configurations

  ```bash
  rosa init
  ```

## Deploy Red Hat OpenShift on AWS (ROSA)

### Interactive Installation

ROSA can be installed using command line parameters or in interactive mode.  For an interactive installation run the following command

  ```bash
  rosa create cluster --interactive --mode auto
  ```

  As part of the interactive install you will be required to enter the following parameters or accept the default values (if applicable)

  ```
  Cluster name:
  Multiple availability zones (y/N):
  AWS region: (select)
  OpenShift version: (select)
  Install into an existing VPC (y/N):
  Compute nodes instance type (optional): (select)
  Enable autoscaling (y/N):
  Compute nodes [2]:
  Additional Security Group IDs (optional): (select)
  Machine CIDR [10.0.0.0/16]:
  Service CIDR [172.30.0.0/16]:
  Pod CIDR [10.128.0.0/14]:
  Host prefix [23]:
  Private cluster (y/N):
  ```
  >Note: the installation process should take between 30 - 45 minutes

### Get the web console link to the ROSA cluster

To get the web console link run the following command.

>Substitute your actual cluster name for `<cluster-name>`

  ```bash
  rosa describe cluster --cluster=<cluster-name>
  ```

### Create cluster-admin user

By default, only the OpenShift SRE team will have access to the ROSA cluster.  To add a local admin user, run the following command to create the `cluster-admin` account in your cluster.

>Substitute your actual cluster name for `<cluster-name>`

  ```bash
  rosa create admin --cluster=<cluster-name>
  ```
>Refresh your web browser and you should see the `cluster-admin` option to log in

## Delete Red Hat OpenShift on AWS (ROSA)

Deleting a ROSA cluster consists of two parts

1. Delete the cluster instance, including the removal of AWS resources.

>Substitute your actual cluster name for `<cluster-name>`

  ```bash
  rosa delete cluster --cluster=<cluster-name>
  ```
  Delete Cluster's operator-roles and oidc-provider as shown in the above delete cluster command's output. For e.g.

  ```bash
  rosa delete operator-roles -c <cluster-name>
  rosa delete oidc-provider -c <cluster-name>
  ```

2. Delete the CloudFormation stack, including the removal of the `osdCcsAdmin` user

  ```bash
  rosa init --delete-stack
  ```