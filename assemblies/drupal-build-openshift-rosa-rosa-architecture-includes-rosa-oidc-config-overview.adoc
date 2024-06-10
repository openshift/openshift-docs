// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-byo-odic-overview_{context}"]
= Creating an OpenID Connect Configuration

When using a cluster hosted by Red Hat, you can create a managed or unmanaged OpenID Connect (OIDC) configuration by using the {product-title} (ROSA) CLI, `rosa`. A managed OIDC configuration is stored within Red Hat's AWS account, while a generated unmanaged OIDC configuration is stored within your AWS account. The OIDC configuration is registered to be used with {cluster-manager}. When creating an unmanaged OIDC configuration, the CLI provides the private key for you.