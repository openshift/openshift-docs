:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="resolving-image-tags-to-digests"]
= Resolving image tags to digests
:context: resolving-image-tags-to-digests

If the Knative Serving controller has access to the container registry, Knative Serving resolves image tags to a digest when you create a revision of a service. This is known as _tag-to-digest resolution_, and helps to provide consistency for deployments.

// Tag to digest resolution
include::modules/serverless-tag-to-digest-resolution.adoc[leveloffset=+1]
include::modules/knative-serving-controller-custom-certs-secrets.adoc[leveloffset=+2]

