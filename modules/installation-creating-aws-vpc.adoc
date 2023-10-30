// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-creating-aws-vpc_{context}"]
= Creating a VPC in AWS

You must create a Virtual Private Cloud (VPC) in Amazon Web Services (AWS) for your {product-title}
cluster to use. You can customize the VPC to meet your requirements, including
VPN and route tables.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent the VPC.

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS
infrastructure, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You configured an AWS account.
* You added your AWS keys and region to your local AWS profile by running `aws configure`.
* You generated the Ignition config files for your cluster.

.Procedure

. Create a JSON file that contains the parameter values that the template
requires:
+
[source,json]
----
[
  {
    "ParameterKey": "VpcCidr", <1>
    "ParameterValue": "10.0.0.0/16" <2>
  },
  {
    "ParameterKey": "AvailabilityZoneCount", <3>
    "ParameterValue": "1" <4>
  },
  {
    "ParameterKey": "SubnetBits", <5>
    "ParameterValue": "12" <6>
  }
]
----
<1> The CIDR block for the VPC.
<2> Specify a CIDR block in the format `x.x.x.x/16-24`.
<3> The number of availability zones to deploy the VPC in.
<4> Specify an integer between `1` and `3`.
<5> The size of each subnet in each availability zone.
<6> Specify an integer between  `5` and `13`, where `5` is `/27` and `13` is `/19`.

. Copy the template from the *CloudFormation template for the VPC*
section of this topic and save it as a YAML file on your computer. This template
describes the VPC that your cluster requires.

. Launch the CloudFormation template to create a stack of AWS resources that represent the VPC:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml <2>
     --parameters file://<parameters>.json <3>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-vpc`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-vpc/dbedae40-2fd3-11eb-820e-12a48460849f
----

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values
for the following parameters. You must provide these parameter values to
the other CloudFormation templates that you run to create your cluster:
[horizontal]
`VpcId`:: The ID of your VPC.
`PublicSubnetIds`:: The IDs of the new public subnets.
`PrivateSubnetIds`:: The IDs of the new private subnets.
