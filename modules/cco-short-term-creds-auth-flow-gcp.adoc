// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

:_mod-docs-content-type: REFERENCE
[id="cco-short-term-creds-auth-flow-gcp_{context}"]
= GCP Workload Identity authentication process

Requests for new and refreshed credentials are automated by using an appropriately configured OpenID Connect (OIDC) identity provider combined with IAM service accounts. Service account tokens that are trusted by GCP are signed by {product-title} and can be projected into a pod and used for authentication. Tokens are refreshed after one hour.

The following diagram details the authentication flow between GCP and the {product-title} cluster when using GCP Workload Identity.

.GCP Workload Identity authentication flow
image::347_OpenShift_credentials_with_STS_updates_0623_GCP.png[Detailed authentication flow between GCP and the cluster when using GCP Workload Identity]