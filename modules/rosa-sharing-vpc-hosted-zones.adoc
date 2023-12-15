// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-sharing-vpc-hosted-zones_{context}"]
= Step Three - VPC Owner: Updating the shared VPC role and creating hosted zones

After the *Cluster Creator* provides the DNS domain and the IAM roles, create a private hosted zone and update the trust policy on the IAM role that was created for sharing the VPC.

image::372_OpenShift_on_AWS_persona_worflows_0923_3.png[]
.Prerequisites

* You have the full domain name from the *Cluster Creator*.
* You have the _Ingress Operator Cloud Credentials_ role's ARN from the *Cluster Creator*.
* You have the _Installer_ role's ARN from the *Cluster Creator*.

.Procedure

. In the link:https://console.aws.amazon.com/ram/[Resource Access Manager of the AWS console], create a resource share that shares the previously created public and private subnets with the *Cluster Creator's* AWS account ID.

. Update the VPC sharing IAM role and add the _Installer_ and _Ingress Operator Cloud Credentials_ roles to the principal section of the trust policy.
+
[source,terminal]
----
{
  "Version": "2012-10-17",
  "Statement": [
    {
	  "Sid": "Statement1",
	  "Effect": "Allow",
	  "Principal": {
	  	"AWS": [
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-ingress-operator-cloud-credentials",
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-Installer-Role"
        ]
	  },
	  "Action": "sts:AssumeRole"
	}
  ]
}
----
. Create a private hosted zone in the link:https://us-east-1.console.aws.amazon.com/route53/v2/[Route 53 section of the AWS console]. In the hosted zone configuration, the domain name is `<cluster_name>.<reserved_dns_domain>`. The private hosted zone must be associated with the created VPC.
. After the hosted zone is created and associated with the VPC, provide the following to the *Cluster Creator* to continue configuration:
* Hosted zone ID
* AWS region
* Subnet IDs