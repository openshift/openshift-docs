// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

:_mod-docs-content-type: CONCEPT
[id="cco-short-term-creds-aws-olm_{context}"]
= OLM-managed Operator support for authentication with AWS STS

In addition to {product-title} cluster components, some Operators managed by the Operator Lifecycle Manager (OLM) on AWS clusters can use manual mode with STS. These Operators authenticate with limited-privilege, short-term credentials that are managed outside the cluster. To determine if an Operator supports authentication with AWS STS, see the Operator description in OperatorHub.
