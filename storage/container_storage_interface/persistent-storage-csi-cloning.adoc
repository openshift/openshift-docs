:_mod-docs-content-type: ASSEMBLY
[id="persistent-storage-csi-cloning"]
= CSI volume cloning
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-csi-cloning

toc::[]

Volume cloning duplicates an existing persistent volume to help protect against data loss in {product-title}. This feature is only available with supported Container Storage Interface (CSI) drivers. You should be familiar with xref:../../storage/understanding-persistent-storage.adoc#persistent-volumes_understanding-persistent-storage[persistent volumes] before you provision a CSI volume clone.

include::modules/persistent-storage-csi-cloning-overview.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-cloning-provisioning.adoc[leveloffset=+1]
