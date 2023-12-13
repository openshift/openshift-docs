// Module included in the following assemblies:
//
// * rosa-adding-additional-constraints-for-ip-based-aws-role-assumption/rosa-create-an-identity-based-policy.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-create-an-identity-based-policy_{context}"]
= Create an identity-based IAM policy

You can create an identity-based Identity and Access Management (IAM) policy that denies access to all AWS actions when the request originates from an IP address other than Red Hat provided IPs.

.Prerequisites

* You have access to the see link:https://aws.amazon.com/console/[AWS Management Console] with the permissions required to create and modify IAM policies.

.Procedure

. Sign in to the AWS Management Console using your AWS account credentials.
. Navigate to the IAM service.
. In the IAM console, select *Policies* from the left navigation menu.
. Click *Create policy*.
. Select the *JSON* tab to define the policy using JSON format.
. Copy and paste the following JSON policy document into the editor:
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": [
                        "3.223.162.20/32",
                        "3.233.177.185/32",
                        "54.209.120.28/32",
                        "23.21.192.204/32",
                        "23.23.16.23/32",
                        "3.217.67.187/32",
                        "34.206.248.211/32",
                        "34.237.192.147/32",
                        "52.1.97.230/32",
                        "18.214.192.218/32",
                        "3.218.132.183/32",
                        "52.202.67.83/32",
                        "18.220.162.161/32",
                        "18.224.36.208/32",
                        "3.143.200.173/32",
                        "54.197.245.192/32",
                        "3.23.162.248/32",
                        "44.217.70.145/32",
                        "52.202.89.184/32",
                        "54.174.41.137/32",
                        "3.231.181.77/32",
                        "44.193.253.218/32",
                        "52.201.38.139/32",
                        "34.205.217.112/32",
                        "23.22.217.39/32",
                        "44.193.121.36/32",
                        "54.211.144.4/32",
                        "34.194.251.19/32",
                        "44.196.79.250/32",
                        "52.45.208.183/32",
                        "100.20.120.76/32",
                        "100.20.197.29/32",
                        "52.26.177.23/32",
                        "34.197.214.203/32",
                        "35.170.167.51/32",
                        "52.23.44.43/32",
                        "44.228.245.162/32",
                        "44.238.205.35/32",
                        "54.203.216.175/32",
                        "34.237.49.153/32",
                        "44.196.177.146/32",
                        "52.23.117.40/32",
                        "44.225.234.235/32",
                        "44.241.225.78/32",
                        "44.241.55.3/32",
                        "34.237.180.56/32",
                        "44.205.240.205/32",
                        "52.54.93.238/32",
                        "35.155.66.53/32",
                        "44.231.249.237/32",
                        "44.233.161.100/32",
                        "3.229.185.234/32",
                        "54.147.98.63/32",
                        "54.163.100.197/32",
                        "23.20.194.86/32",
                        "23.22.242.238/32",
                        "54.147.218.140/32",
                        "52.21.229.141/32",
                        "54.227.5.10/32",
                        "54.146.138.135/32",
                        "23.21.239.1/32",
                        "52.20.145.130/32",
                        "54.157.89.24/32",
                        "107.22.162.110/32",
                        "3.223.147.2/32",
                        "54.88.225.66/32",
                        "54.177.143.128/32",
                        "54.219.250.189/32",
                        "18.135.14.84/32",
                        "18.135.218.119/32",
                        "3.11.51.55/32",
                        "3.233.86.181/32",
                        "34.226.229.129/32",
                        "44.194.44.138/32",
                        "34.216.5.118/32",
                        "52.11.52.9/32",
                        "52.40.203.77/32",
                        "18.217.173.123/32",
                        "3.13.34.119/32",
                        "3.19.160.232/32",
                        "18.188.187.143/32",
                        "18.216.245.132/32",
                        "52.14.85.89/32",
                        "52.21.184.148/32",
                        "44.194.57.131/32",
                        "18.188.65.148/32",
                        "3.130.101.176/32",
                        "3.130.198.233/32",
                        "54.210.128.71/32",
                        "54.227.100.14/32",
                        "54.92.188.93/32",
                        "107.22.5.187/32",
                        "3.217.212.27/32",
                        "52.22.56.3/32",
                        "52.5.10.152/32",
                        "54.237.41.201/32",
                        "34.202.145.72/32",
                        "52.205.239.95/32",
                        "54.236.208.68/32",
                        "3.234.64.191/32",
                        "34.195.159.252/32",
                        "34.228.34.122/32",
                        "54.205.89.242/32",
                        "209.132.0.0/16",
                        "66.187.0.0/16",
                        "2620:0052:0004:0000:0000:0000:0000:0000/48"
                    ]
                },
                "Bool": {
                    "aws:ViaAWSService": "false"
                }
            }
        }
    ]
}
----
+
[NOTE]
====
This list is subject to change. Additionally, you must specify the IP addresses in CIDR notation.
====
+
. Click *Review and create*.
. Provide a name and description for the policy, and review the details for accuracy.
. Click *Create policy* to save the policy.

[NOTE]
====
The condition key `aws:ViaAWSService` must be set to false to enable subsequent calls to succeed based on the initial call. For example, if you make an initial call to `aws ec2 describe-instances`, all subsequent calls made within the AWS API server to retrieve information about the EBS volumes attached to the ec2 instance will fail if the condition key `aws:ViaAWSService` is not set to false. The subsequent calls would fail because they would originate from AWS IP addresses, which are not included in the AllowList.
====
