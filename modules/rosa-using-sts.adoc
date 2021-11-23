// Module included in the following assemblies:
//
// * rosa_architecture/rosa-understanding.adoc

[id="rosa-using-sts_{context}"]
= Using the AWS Security Token Service

The Amazon Web Services (AWS) Security Token Service (STS) is a global web service that provides short-term credentials for IAM or federated users. You can use AWS STS with {product-title} (ROSA) to allocate temporary, limited-privilege credentials for component-specific IAM roles. The service enables cluster components to make AWS API calls using secure cloud resource management practices.

You can use the `rosa` CLI to create the IAM role, policy and identity provider resources that are required for ROSA clusters that use STS.
