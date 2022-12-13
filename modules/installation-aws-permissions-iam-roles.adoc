// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-account.adoc

[id="installation-aws-permissions-iam-roles_{context}"]
= Default permissions for IAM instance profiles

By default, the installation program creates IAM instance profiles for the bootstrap, control plane and worker instances with the necessary permissions for the cluster to operate.

The following lists specify the default permissions for control plane and compute machines:

.Default IAM role permissions for control plane instance profiles
[%collapsible]
====
* `ec2:AttachVolume`
* `ec2:AuthorizeSecurityGroupIngress`
* `ec2:CreateSecurityGroup`
* `ec2:CreateTags`
* `ec2:CreateVolume`
* `ec2:DeleteSecurityGroup`
* `ec2:DeleteVolume`
* `ec2:Describe*`
* `ec2:DetachVolume`
* `ec2:ModifyInstanceAttribute`
* `ec2:ModifyVolume`
* `ec2:RevokeSecurityGroupIngress`
* `elasticloadbalancing:AddTags`
* `elasticloadbalancing:AttachLoadBalancerToSubnets`
* `elasticloadbalancing:ApplySecurityGroupsToLoadBalancer`
* `elasticloadbalancing:CreateListener`
* `elasticloadbalancing:CreateLoadBalancer`
* `elasticloadbalancing:CreateLoadBalancerPolicy`
* `elasticloadbalancing:CreateLoadBalancerListeners`
* `elasticloadbalancing:CreateTargetGroup`
* `elasticloadbalancing:ConfigureHealthCheck`
* `elasticloadbalancing:DeleteListener`
* `elasticloadbalancing:DeleteLoadBalancer`
* `elasticloadbalancing:DeleteLoadBalancerListeners`
* `elasticloadbalancing:DeleteTargetGroup`
* `elasticloadbalancing:DeregisterInstancesFromLoadBalancer`
* `elasticloadbalancing:DeregisterTargets`
* `elasticloadbalancing:Describe*`
* `elasticloadbalancing:DetachLoadBalancerFromSubnets`
* `elasticloadbalancing:ModifyListener`
* `elasticloadbalancing:ModifyLoadBalancerAttributes`
* `elasticloadbalancing:ModifyTargetGroup`
* `elasticloadbalancing:ModifyTargetGroupAttributes`
* `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
* `elasticloadbalancing:RegisterTargets`
* `elasticloadbalancing:SetLoadBalancerPoliciesForBackendServer`
* `elasticloadbalancing:SetLoadBalancerPoliciesOfListener`
* `kms:DescribeKey`
====

.Default IAM role permissions for compute instance profiles
[%collapsible]
====
* `ec2:DescribeInstances`
* `ec2:DescribeRegions`
====
