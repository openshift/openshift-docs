// Module included in the following assemblies:
//
// * networking/aws-load-balancer-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="aws-uninstalling-an-aws-load-balancer-operator_{context}"]
= Uninstalling an AWS Load Balancer Operator
To uninstall an AWS Load Balancer Operator (ALBO) and perform an overall cleanup of the associated resources, perform the following procedure.

.Procedure
. Clean up the sample application by deleting the Load Balancers created and managed by the ALBO. For more information about deleting Load Balancers, see link:https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-delete.html[Delete an Application Load Balancer].
. Clean up the AWS VPC tags by removing the VPC tags that were added to the subnets for discovering subnets and for creating Application Load Balancers (ALBs). For more information, see link:https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics[Tag basics].
. Clean up ALBO components by deleting both the ALBO and the Application Load Balancer Controller (ALBC).
For more information, see link:https://access.redhat.com/documentation/en-us/openshift_container_platform/4.13/html/operators/administrator-tasks#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster].
