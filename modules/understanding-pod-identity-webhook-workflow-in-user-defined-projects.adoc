// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

:_mod-docs-content-type: CONCEPT
[id="how-service-accounts-assume-aws-iam-roles-in-user-defined-projects_{context}"]
= How service accounts assume AWS IAM roles in user-defined projects

When you install a {product-title} cluster
ifdef::openshift-rosa[]
that uses the AWS Security Token Service (STS),
endif::openshift-rosa[]
ifndef::openshift-rosa[]
,
endif::openshift-rosa[]
pod identity webhook resources are included by default.

You can use the pod identity webhook to enable a service account in a user-defined project to assume an AWS Identity and Access Management (IAM) role in a pod in the same project. When the IAM role is assumed, temporary STS credentials are provided for use by the service account in the pod. If the assumed role has the necessary AWS privileges, the service account can run AWS SDK operations in the pod.

To enable the pod identity webhook for a pod, you must create a service account with an `eks.amazonaws.com/role-arn` annotation in your project. The annotation must reference the Amazon Resource Name (ARN) of the AWS IAM role that you want the service account to assume. You must also reference the service account in your `Pod` specification and deploy the pod in the same project as the service account.

[discrete]
[id="pod-identity-webhook-workflow-in-user-defined-projects_{context}"]
== Pod identity webhook workflow in user-defined projects

The following diagram illustrates the pod identity webhook workflow in user-defined projects:

.Pod identity webhook workflow in user-defined projects
image::pod-identity-webhook-workflow-in-user-defined-projects.png[Pod identity webhook workflow]

The workflow has the following stages:

. Within a user-defined project, a user creates a service account that includes an `eks.amazonaws.com/role-arn` annotation. The annotation points to the ARN of the AWS IAM role that you want your service account to assume.

. When a pod is deployed in the same project using a configuration that references the annotated service account, the pod identity webhook mutates the pod. The mutation injects the following components into the pod without the need to specify them in your `Pod` or `Deployment` resource configurations:

** An `$AWS_ARN_ROLE` environment variable that contains the ARN for the IAM role that has the permissions required to run AWS SDK operations.

** An `$AWS_WEB_IDENTITY_TOKEN_FILE` environment variable that contains the full path in the pod to the OpenID Connect (OIDC) token for the service account. The full path is `/var/run/secrets/eks.amazonaws.com/serviceaccount/token`.

** An `aws-iam-token` volume mounted on the mount point `/var/run/secrets/eks.amazonaws.com/serviceaccount`. An OIDC token file named `token` is contained in the volume.

. The OIDC token is passed from the pod to the OIDC provider. The provider authenticates the service account identity if the following requirements are met:

** The identity signature is valid and signed by the private key.

** The `sts.amazonaws.com` audience is listed in the OIDC token and matches the audience configured in the OIDC provider.
+
[NOTE]
====
The pod identity webhook applies the `sts.amazonaws.com` audience to the OIDC token by default.
ifdef::openshift-rosa[]

In {product-title} with STS clusters, the OIDC provider is created during install and set as the service account issuer by default. The `sts.amazonaws.com` audience is set by default in the OIDC provider.
endif::openshift-rosa[]
====

** The OIDC token has not expired.

** The issuer value in the token contains the URL for the OIDC provider.

. If the project and service account are in the scope of the trust policy for the IAM role that is being assumed, then authorization succeeds.

. After successful authentication and authorization, temporary AWS STS credentials in the form of a session token are passed to the pod for use by the service account. By using the credentials, the service account is temporarily granted the AWS permissions enabled in the IAM role.

. When you run AWS SDK operations in the pod, the service account provides the temporary STS credentials to the AWS API to verify its identity.
