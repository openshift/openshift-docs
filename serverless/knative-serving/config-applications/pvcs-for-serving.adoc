:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="pvcs-for-serving"]
= Persistent Volume Claims for Serving
:context: pvcs-for-serving

Some serverless applications need permanent data storage.
To achieve this, you can configure persistent volume claims (PVCs) for your Knative services.

// Enabling PVC for Serving
include::modules/serverless-enabling-pvc-support.adoc[leveloffset=+1]

ifdef::openshift-enterprise[]
[id="additional-resources_pvcs-for-serving"]
[role="_additional-resources"]
== Additional resources
* xref:../../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[Understanding persistent storage]
endif::[]