:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="olmv1-components"]
= {olmv1} components overview (Technology Preview)
:context: olmv1-components

toc::[]

:FeatureName: {olmv1}
include::snippets/technology-preview.adoc[]

{olmv1-first} comprises the following component projects:

Operator Controller:: xref:../../../operators/olm_v1/arch/olmv1-operator-controller.adoc#olmv1-operator-controller[Operator Controller] is the central component of {olmv1} that extends Kubernetes with an API through which users can install and manage the lifecycle of Operators and extensions. It consumes information from each of the following components.

RukPak:: xref:../../../operators/olm_v1/arch/olmv1-rukpak.adoc#olmv1-rukpak[RukPak] is a pluggable solution for packaging and distributing cloud-native content. It supports advanced strategies for installation, updates, and policy.
+
RukPak provides a content ecosystem for installing a variety of artifacts on a Kubernetes cluster. Artifact examples include Git repositories, Helm charts, and OLM bundles. RukPak can then manage, scale, and upgrade these artifacts in a safe way to enable powerful cluster extensions.

Catalogd:: xref:../../../operators/olm_v1/arch/olmv1-catalogd.adoc#olmv1-catalogd[Catalogd] is a Kubernetes extension that unpacks file-based catalog (FBC) content packaged and shipped in container images for consumption by on-cluster clients. As a component of the {olmv1} microservices architecture, catalogd hosts metadata for Kubernetes extensions packaged by the authors of the extensions, and as a result helps users discover installable content.