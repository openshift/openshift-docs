:_mod-docs-content-type: ASSEMBLY
[id="configuring-registry-storage-vsphere"]
= Configuring the registry for vSphere
include::_attributes/common-attributes.adoc[]
:context: configuring-registry-storage-vsphere

toc::[]

include::modules/registry-removed.adoc[leveloffset=+1]

include::modules/registry-change-management-state.adoc[leveloffset=+1]

include::modules/installation-registry-storage-config.adoc[leveloffset=+1]

include::modules/registry-configuring-storage-vsphere.adoc[leveloffset=+2]

include::modules/installation-registry-storage-non-production.adoc[leveloffset=+2]

include::modules/installation-registry-storage-block-recreate-rollout.adoc[leveloffset=+2]

For instructions about configuring registry storage so that it references the correct PVC, see xref:../../registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc#registry-configuring-storage-vsphere_configuring-registry-storage-vsphere[Configuring the registry for vSphere].

include::modules/registry-configuring-registry-storage-rhodf-cephrgw.adoc[leveloffset=+2]

include::modules/registry-configuring-registry-storage-rhodf-nooba.adoc[leveloffset=+2]

include::modules/registry-configuring-registry-storage-rhodf-cephfs.adoc[leveloffset=+1]

[id="configuring-registry-storage-vsphere-addtl-resources"]
[role="_additional-resources"]
== Additional resources

* xref:../../scalability_and_performance/optimization/optimizing-storage.adoc#optimizing-storage[Recommended configurable storage technology]
* link:https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.10/html-single/managing_and_allocating_storage_resources/index#configuring-image-registry-to-use-openshift-data-foundation_rhodf[Configuring Image Registry to use OpenShift Data Foundation]
