:_mod-docs-content-type: ASSEMBLY
[id="configuring-registry-storage-nutanix"]
= Configuring the registry for Nutanix
include::_attributes/common-attributes.adoc[]
:context: configuring-registry-storage-nutanix
toc::[]

By following the steps outlined in this documentation, users can optimize container image distribution, security, and access controls, enabling a robust foundation for Nutanix applications on {product-title}

include::modules/registry-removed.adoc[leveloffset=+1]

include::modules/registry-change-management-state.adoc[leveloffset=+1]

include::modules/installation-registry-storage-config.adoc[leveloffset=+1]

include::modules/configuring-registry-storage-nutanix.adoc[leveloffset=+2]

include::modules/installation-registry-storage-non-production.adoc[leveloffset=+2]

include::modules/installation-registry-storage-block-recreate-rollout-nutanix.adoc[leveloffset=+2]

include::modules/registry-configuring-registry-storage-rhodf-cephrgw.adoc[leveloffset=+2]

include::modules/registry-configuring-registry-storage-rhodf-nooba.adoc[leveloffset=+2]

include::modules/registry-configuring-registry-storage-rhodf-cephfs.adoc[leveloffset=+1]

[id="configuring-registry-storage-nutanix-addtl-resources"]
[role="_additional-resources"]
== Additional resources

* xref:../../scalability_and_performance/optimization/optimizing-storage.adoc#optimizing-storage[Recommended configurable storage technology]
* link:https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.10/html-single/managing_and_allocating_storage_resources/index#configuring-image-registry-to-use-openshift-data-foundation_rhodf[Configuring Image Registry to use OpenShift Data Foundation]
