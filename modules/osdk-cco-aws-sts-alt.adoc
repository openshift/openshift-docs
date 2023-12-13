// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-token-auth.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-cco-aws-sts-alt_{context}"]
= Alternative method

As an alternative method for Operator authors, you can indicate that the user is responsible for creating the `CredentialsRequest` object for the Cloud Credential Operator (CCO) before installing the Operator.

The Operator instructions must indicate the following to users:

* Provide a YAML version of a `CredentialsRequest` object, either by providing the YAML inline in the instructions or pointing users to a download location
* Instruct the user to create the `CredentialsRequest` object

In {product-title} 4.14 and later, after the `CredentialsRequest` object appears on the cluster with the appropriate STS information added, the Operator can then read the CCO-generated `Secret` or mount it, having defined the mount in the cluster service version (CSV).

For earlier versions of {product-title}, the Operator instructions must also indicate the following to users:

* Use the CCO utility (`ccoctl`) to generate the `Secret` YAML object from the `CredentialsRequest` object
* Apply the `Secret` object to the cluster in the appropriate namespace

The Operator still must be able to consume the resulting secret to communicate with cloud APIs. Because in this case the secret is created by the user before the Operator is installed, the Operator can do either of the following:

* Define an explicit mount in the `Deployment` object within the CSV
* Programmatically read the `Secret` object from the API server, as shown in the recommended "Enabling Operators to support CCO-based workflows with AWS STS" method