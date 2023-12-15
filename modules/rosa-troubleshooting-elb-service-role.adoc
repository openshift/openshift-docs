// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-troubleshooting-elb-service-role_{context}"]
= Creating the Elastic Load Balancing (ELB) service-linked role

If you have not created a load balancer in your AWS account, it is possible that the service-linked role for Elastic Load Balancing (ELB) might not exist yet. You may receive the following error:

[source,terminal]
----
Error: Error creating network Load Balancer: AccessDenied: User: arn:aws:sts::xxxxxxxxxxxx:assumed-role/ManagedOpenShift-Installer-Role/xxxxxxxxxxxxxxxxxxx is not authorized to perform: iam:CreateServiceLinkedRole on resource: arn:aws:iam::xxxxxxxxxxxx:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing"
----

.Procedure

To resolve this issue, ensure that the role exists on your AWS account. If not, create this role with the following command:

[source,terminal]
----
aws iam get-role --role-name "AWSServiceRoleForElasticLoadBalancing" || aws iam create-service-linked-role --aws-service-name "elasticloadbalancing.amazonaws.com"
----

[NOTE]
====
This command only needs to be executed once per account.
====
