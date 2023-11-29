:_mod-docs-content-type: ASSEMBLY
[id="using-image-pull-secrets"]
= Using image pull secrets
include::_attributes/common-attributes.adoc[]
:context: using-image-pull-secrets

toc::[]

If you are using the {product-registry} and are pulling from image streams located in the same project, then your pod service account should already have the correct permissions and no additional action should be required.

However, for other scenarios, such as referencing images across {product-title} projects or from secured registries, additional configuration steps are required.

You can obtain the image {cluster-manager-url-pull}. This pull secret is called `pullSecret`.

You use this pull secret to authenticate with the services that are provided by the included authorities, link:https://quay.io/[Quay.io] and link:https://registry.redhat.io[registry.redhat.io], which serve the container images for {product-title} components.

include::modules/images-allow-pods-to-reference-images-across-projects.adoc[leveloffset=+1]

include::modules/images-allow-pods-to-reference-images-from-secure-registries.adoc[leveloffset=+1]

include::modules/images-pulling-from-private-registries.adoc[leveloffset=+2]

// cannot get resource "secrets" in API group "" in the namespace "openshift-config" 
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/images-update-global-pull-secret.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]
