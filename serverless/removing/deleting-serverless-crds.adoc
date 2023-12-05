:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="deleting-serverless-crds"]
= Deleting {ServerlessProductName} custom resource definitions
:context: deleting-serverless-crds

After uninstalling the {ServerlessProductName}, the Operator and API custom resource definitions (CRDs) remain on the cluster. You can use the following procedure to remove the remaining CRDs.

[IMPORTANT]
====
Removing the Operator and API CRDs also removes all resources that were defined by using them, including Knative services.
====

// deleting serverless CRDs
include::modules/serverless-deleting-crds.adoc[leveloffset=+1]