// Module included in the following assemblies:
//
// * authentication/bound-service-account-tokens.adoc

:_mod-docs-content-type: CONCEPT
[id="bound-sa-tokens-about_{context}"]
= About bound service account tokens

You can use bound service account tokens to limit the scope of permissions for a given service account token. These tokens are audience and time-bound. This facilitates the authentication of a service account to an IAM role and the generation of temporary credentials mounted to a pod. You can request bound service account tokens by using volume projection and the TokenRequest API.
