// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-sharing-vpc-creation-and-sharing_{context}"]
= Step One - VPC Owner: Configuring a VPC to share within your AWS organization

You can share subnets within a configured VPC with another AWS user account if that account is within your current AWS organization.

image::372_OpenShift_on_AWS_persona_worflows_0923_1.png[]
.Procedure

. Create or modify a VPC to your specifications in the link:https://us-east-1.console.aws.amazon.com/vpc/[VPC section of the AWS console].
+
. Create a custom policy file to allow for necessary shared VPC permissions that uses the name `SharedVPCPolicy`:
+
[source,terminal]
----
$ cat <<EOF > /tmp/shared-vpc-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets",
                "route53:ListHostedZones",
                "route53:ListHostedZonesByName",
                "route53:ListResourceRecordSets",
                "route53:ChangeTagsForResource",
                "route53:GetAccountLimit",
                "route53:GetChange",
                "route53:GetHostedZone",
                "route53:ListTagsForResource",
                "route53:UpdateHostedZoneComment",
                "tag:GetResources",
                "tag:UntagResources"
            ],
            "Resource": "*"
        }
    ]
}
EOF
----
+
. Create the policy in AWS:
+
[source,terminal]
----
$ aws iam create-policy \
    --policy-name SharedVPCPolicy \
    --policy-document file:///tmp/shared-vpc-policy.json
----
+
You will attach this policy to a role necessary for the shared VPC permissions.
+
. Create a custom trust policy file that grants permission to assume roles:
+
[source,terminal]
----
$ cat <<EOF > /tmp/shared-vpc-role.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<Account-ID>:root"  <1>
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
----
+
--
<1> The principal will be scoped down after the *Cluster Creator* creates the necessary cluster roles. On creation, you must create a root user placeholder by using the *Cluster Creator's* AWS account ID as `arn:aws:iam::{Account}:root`.
--
+
. Create the IAM role:
+
[source,terminal]
----
$ aws iam create-role --role-name <role_name> \  <1>
    --assume-role-policy-document file:///tmp/shared-vpc-role.json
----
+
--
<1> Replace _<role_name>_ with the name of the role you want to create.
--
+
. Attach the custom `SharedVPCPolicy` permissions policy:
+
[source, terminal]
----
$ aws iam attach-role-policy --role-name <role_name> --policy-arn \  <1>
    arn:aws:iam::<AWS_account_ID>:policy/SharedVPCPolicy  <2>
----
+
--
<1> Replace _<role_name>_ with the name of the role you created.
<2> Replace _<AWS_account_ID>_ with the *VPC Owner's* AWS account ID.
--
+

. Provide the `SharedVPCRole` ARN to the *Cluster Creator* to continue configuration.
