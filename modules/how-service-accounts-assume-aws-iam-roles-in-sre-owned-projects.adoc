// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-sre-access.adoc

:_mod-docs-content-type: CONCEPT
[id="how-service-accounts-assume-aws-iam-roles-in-sre-owned-projects_{context}"]
= How service accounts assume AWS IAM roles in SRE owned projects

When you install a {product-title} cluster that uses the AWS Security Token Service (STS), cluster-specific Operator AWS Identity and Access Management (IAM) roles are created. These IAM roles permit the {product-title} cluster Operators to run core OpenShift functionality.

Cluster Operators use service accounts to assume IAM roles. When a service account assumes an IAM role, temporary STS credentials are provided for the service account to use in the cluster Operator's pod. If the assumed role has the necessary AWS privileges, the service account can run AWS SDK operations in the pod.

[discrete]
[id="workflow-for-assuming-aws-iam-roles-in-sre-owned-projects_{context}"]
== Workflow for assuming AWS IAM roles in SRE owned projects

The following diagram illustrates the workflow for assuming AWS IAM roles in SRE owned projects:

.Workflow for assuming AWS IAM roles in SRE owned projects
image::workflow-assuming-aws-iam-roles-sre-owned-projects.png[Workflow for assuming AWS IAM roles in SRE owned projects]

The workflow has the following stages:

. Within each project that a cluster Operator runs, the Operator's deployment spec has a volume mount for the projected service account token, and a secret containing AWS credential configuration for the pod. The token is audience-bound and time-bound. Every hour, {product-title} generates a new token, and the AWS SDK reads the mounted secret containing the AWS credential configuration. This configuration has a path to the mounted token and the AWS IAM Role ARN. The secret's credential configuration includes the following:

** An `$AWS_ARN_ROLE` variable that has the ARN for the IAM role that has the permissions required to run AWS SDK operations.

** An `$AWS_WEB_IDENTITY_TOKEN_FILE` variable that has the full path in the pod to the OpenID Connect (OIDC) token for the service account. The full path is `/var/run/secrets/openshift/serviceaccount/token`.

. When a cluster Operator needs to assume an AWS IAM role to access an AWS service (such as EC2), the AWS SDK client code running on the Operator invokes the `AssumeRoleWithWebIdentity` API call.

. The OIDC token is passed from the pod to the OIDC provider. The provider authenticates the service account identity if the following requirements are met:

** The identity signature is valid and signed by the private key.

** The `sts.amazonaws.com` audience is listed in the OIDC token and matches the audience configured in the OIDC provider.
+
[NOTE]
====
In {product-title} with STS clusters, the OIDC provider is created during install and set as the service account issuer by default. The `sts.amazonaws.com` audience is set by default in the OIDC provider.
====

** The OIDC token has not expired.

** The issuer value in the token has the URL for the OIDC provider.

. If the project and service account are in the scope of the trust policy for the IAM role that is being assumed, then authorization succeeds.

. After successful authentication and authorization, temporary AWS STS credentials in the form of an AWS access token, secret key, and session token are passed to the pod for use by the service account. By using the credentials, the service account is temporarily granted the AWS permissions enabled in the IAM role.

. When the cluster Operator runs, the Operator that is using the AWS SDK in the pod consumes the secret that has the path to the projected service account and AWS IAM Role ARN to authenticate against the OIDC provider. The OIDC provider returns temporary STS credentials for authentication against the AWS API.
