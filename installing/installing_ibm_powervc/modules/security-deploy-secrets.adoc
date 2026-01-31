// Module included in the following assemblies:
//
// * security/container_security/security-deploy.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-deploy-secrets_{context}"]
= Creating secrets and config maps

The `Secret` object type provides a mechanism to hold sensitive information such
as passwords, {product-title} client configuration files, `dockercfg` files,
and private source repository credentials. Secrets decouple sensitive content
from pods. You can mount secrets into containers using a volume plugin or the
system can use secrets to perform actions on behalf of a pod.

For example, to add a secret to your deployment configuration
so that it can access a private image repository, do the following:

.Procedure

. Log in to the {product-title} web console.

. Create a new project.

. Navigate to *Resources* -> *Secrets* and create a new secret. Set `Secret Type` to
`Image Secret` and `Authentication Type` to `Image Registry Credentials` to
enter credentials for accessing a private image repository.

. When creating a deployment configuration (for example, from the *Add to Project* ->
*Deploy Image* page), set the `Pull Secret` to your new secret.

Config maps are similar to secrets, but are designed to support working with
strings that do not contain sensitive information. The `ConfigMap` object holds
key-value pairs of configuration data that can be consumed in pods or used to
store configuration data for system components such as controllers.
