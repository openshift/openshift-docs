// Module included in the following assemblies:
// * builds/creating-build-inputs.adoc

[id="builds-secrets-restrictions_{context}"]
= Secrets restrictions

To use a secret, a pod needs to reference the secret. A secret can be used with a pod in three ways:

* To populate environment variables for containers.
* As files in a volume mounted on one or more of its containers.
* By kubelet when pulling images for the pod.

Volume type secrets write data into the container as a file using the volume mechanism. `imagePullSecrets` use service accounts for the automatic injection of the secret into all pods in a namespaces.

When a template contains a secret definition, the only way for the template to use the provided secret is to ensure that the secret volume sources are validated and that the specified object reference actually points to an object of type `Secret`. Therefore, a secret needs to be created before any pods that depend on it. The most effective way to ensure this is to have it get injected automatically through the use of a service account.

Secret API objects reside in a namespace. They can only be referenced by pods in that same namespace.

Individual secrets are limited to 1MB in size. This is to discourage the creation of large secrets that would exhaust apiserver and kubelet memory. However, creation of a number of smaller secrets could also exhaust memory.
