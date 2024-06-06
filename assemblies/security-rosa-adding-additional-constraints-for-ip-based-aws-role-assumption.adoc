:_mod-docs-content-type: ASSEMBLY
[id="rosa-adding-additional-constraints-for-ip-based-aws-role-assumption_{context}"]
include::_attributes/attributes-openshift-dedicated.adoc[]
include::_attributes/common-attributes.adoc[]
= Adding additional constraints for IP-based AWS role assumption

:context: rosa-adding-additional-constraints-for-ip-based-aws-role-assumption

toc::[]

You can implement an additional layer of security in your AWS account to prevent role assumption from non-allowlisted IP addresses.

include::modules/rosa-create-an-identity-based-policy.adoc[leveloffset=+1]
include::modules/rosa-attaching-the-policy.adoc[leveloffset=+1]


[role="_additional-resources"]
== Additional resources

* For more information about denying access based on the source IP, see link:https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.html[AWS: Denies access to AWS based on the source IP] in the AWS documentation.
