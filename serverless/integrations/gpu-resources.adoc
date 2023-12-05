:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="gpu-resources"]
= Using NVIDIA GPU resources with serverless applications
:context: gpu-resources

toc::[]

NVIDIA supports using GPU resources on {product-title}.
See link:https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/openshift/contents.html[GPU Operator on OpenShift] for more information about setting up GPU resources on {product-title}.

include::modules/serverless-gpu-resources-kn.adoc[leveloffset=+1]

ifdef::openshift-enterprise[]
[id="additional-requirements_gpu-resources"]
[role="_additional-resources"]
== Additional resources
* xref:../../applications/quotas/quotas-setting-per-project.adoc#quotas-setting-per-project[Setting resource quotas for extended resources]
endif::[]
