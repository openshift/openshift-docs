:_mod-docs-content-type: ASSEMBLY
[id="configuring-registry-storage-rhodf"]
= Configuring the registry for Red Hat OpenShift Data Foundation
include::_attributes/common-attributes.adoc[]
:context: configuring-registry-storage-rhodf

toc::[]

To configure the {product-registry} on bare metal and vSphere to use {rh-storage-first} storage, you must install {rh-storage} and then configure image registry using Ceph or Noobaa.

include::modules/registry-configuring-registry-storage-rhodf-cephrgw.adoc[leveloffset=+1]

include::modules/registry-configuring-registry-storage-rhodf-nooba.adoc[leveloffset=+1]

include::modules/registry-configuring-registry-storage-rhodf-cephfs.adoc[leveloffset=+1]

[id="configuring-registry-storage-ocs"]
[role="_additional-resources"]
== Additional resources

* link:https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.10/html-single/managing_and_allocating_storage_resources/index#configuring-image-registry-to-use-openshift-data-foundation_rhodf[Configuring Image Registry to use OpenShift Data Foundation]
* link:https://access.redhat.com/solutions/6719951[Performance tuning guide for Multicloud Object Gateway (NooBaa)]
