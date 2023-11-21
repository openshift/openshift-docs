// Module included in the following assemblies:
//
// * networking/external_dns_operator/nw-creating-dns-records-on-aws.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-control-dns-records-public-aws-with-VPC_{context}"]
= Creating DNS records in a different AWS Account using a shared VPC

You can use the ExternalDNS Operator to create DNS records in a different AWS account using a shared Virtual Private Cloud (VPC). By using a shared VPC, an organization can connect resources from multiple projects to a common VPC network. Organizations can then use VPC sharing to use a single Route 53 instance across multiple AWS accounts.

.Prerequisites
* You have created two Amazon AWS accounts: one with a VPC and a Route 53 private hosted zone configured (Account A), and another for installing a cluster (Account B).
* You have created an IAM Policy and IAM Role with the appropriate permissions in Account A for Account B to create DNS records in the Route 53 hosted zone of Account A.
* You have installed a cluster in Account B into the existing VPC for Account A.
* You have installed the ExternalDNS Operator in the cluster in Account B.

.Procedure

. Get the Role ARN of the IAM Role that you created to allow Account B to access Account A's Route 53 hosted zone by running the following command:
+
[source,terminal]
----
$ aws --profile account-a iam get-role --role-name user-rol1 | head -1
----
+
.Example output
+
[source,terminal]
----
ROLE	arn:aws:iam::1234567890123:role/user-rol1	2023-09-14T17:21:54+00:00	3600	/	AROA3SGB2ZRKRT5NISNJN	user-rol1
----

. Locate the private hosted zone to use with Account A's credentials by running the following command:
+
[source,terminal]
----
$ aws --profile account-a route53 list-hosted-zones | grep testextdnsoperator.apacshift.support
----
+
.Example output
+
[source,terminal]
----
HOSTEDZONES	terraform	/hostedzone/Z02355203TNN1XXXX1J6O	testextdnsoperator.apacshift.support. 5
----

. Create the `ExternalDNS` object by running the following command:
+
[source,terminal]
----
$ cat <<EOF | oc create -f -
apiVersion: externaldns.olm.openshift.io/v1beta1
kind: ExternalDNS
metadata:
  name: sample-aws 
spec:
  domains:
  - filterType: Include   
    matchType: Exact   
    name: testextdnsoperator.apacshift.support 
  provider:
    type: AWS
    aws: 
      assumeRole: 
        arn: arn:aws:iam::12345678901234:role/user-rol1 <1>
  source:  
    type: OpenShiftRoute 
    openshiftRouteOptions:
      routerName: default 
EOF
----
<1> Specify the Role ARN  to have DNS records created in Account A.

. Check the records created for OpenShift Container Platform (OCP) routes by using the following command:
+
[source,terminal]
----
$ aws --profile account-a route53 list-resource-record-sets --hosted-zone-id Z02355203TNN1XXXX1J6O --query "ResourceRecordSets[?Type == 'CNAME']" | grep console-openshift-console
----
