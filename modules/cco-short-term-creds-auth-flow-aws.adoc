// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

:_mod-docs-content-type: REFERENCE
[id="cco-short-term-creds-auth-flow-aws_{context}"]
= AWS Security Token Service authentication process

The AWS Security Token Service (STS) and the link:https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html[`AssumeRole`] API action allow pods to retrieve access keys that are defined by an IAM role policy.

The {product-title} cluster includes a Kubernetes service account signing service. This service uses a private key to sign service account JSON web tokens (JWT). A pod that requires a service account token requests one through the pod specification. When the pod is created and assigned to a node, the node retrieves a signed service account from the service account signing service and mounts it onto the pod.

Clusters that use STS contain an IAM role ID in their Kubernetes configuration secrets. Workloads assume the identity of this IAM role ID. The signed service account token issued to the workload aligns with the configuration in AWS, which allows AWS STS to grant access keys for the specified IAM role to the workload.

AWS STS grants access keys only for requests that include service account tokens that meet the following conditions:

* The token name and namespace match the service account name and namespace.

* The token is signed by a key that matches the public key.

The public key pair for the service account signing key used by the cluster is stored in an AWS S3 bucket. AWS STS federation validates that the service account token signature aligns with the public key stored in the S3 bucket.

[id="cco-short-term-creds-auth-flow-aws-diagram_{context}"]
== Authentication flow for AWS STS

The following diagram illustrates the authentication flow between AWS and the {product-title} cluster when using AWS STS.

* _Token signing_ is the Kubernetes service account signing service on the {product-title} cluster.
* The _Kubernetes service account_ in the pod is the signed service account token.

.AWS Security Token Service authentication flow
image::347_OpenShift_credentials_with_STS_updates_0623_AWS.png[Detailed authentication flow between AWS and the cluster when using AWS STS]

Requests for new and refreshed credentials are automated by using an appropriately configured AWS IAM OpenID Connect (OIDC) identity provider combined with AWS IAM roles. Service account tokens that are trusted by AWS IAM are signed by {product-title} and can be projected into a pod and used for authentication.

[id="cco-short-term-creds-auth-flow-aws-refresh-policy_{context}"]
== Token refreshing for AWS STS

The signed service account token that a pod uses expires after a period of time. For clusters that use AWS STS, this time period is 3600 seconds, or one hour.

The kubelet on the node that the pod is assigned to ensures that the token is refreshed. The kubelet attempts to rotate a token when it is older than 80 percent of its time to live.

[id="cco-short-term-creds-auth-flow-aws-oidc_{context}"]
== OpenID Connect requirements for AWS STS

You can store the public portion of the encryption keys for your OIDC configuration in a public or private S3 bucket.

The OIDC spec requires the use of HTTPS. AWS services require a public endpoint to expose the OIDC documents in the form of JSON web key set (JWKS) public keys. This allows AWS services to validate the bound tokens signed by Kubernetes and determine whether to trust certificates. As a result, both S3 bucket options require a public HTTPS endpoint and private endpoints are not supported.

To use AWS STS, the public AWS backbone for the AWS STS service must be able to communicate with a public S3 bucket or a private S3 bucket with a public CloudFront endpoint. You can choose which type of bucket to use when you process `CredentialsRequest` objects during installation:

* By default, the CCO utility (`ccoctl`) stores the OIDC configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint.

* As an alternative, you can have the `ccoctl` utility store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL.