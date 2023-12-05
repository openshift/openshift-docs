:_mod-docs-content-type: ASSEMBLY
[id="expanding-persistent-volumes"]
= Expanding persistent volumes
include::_attributes/common-attributes.adoc[]
:context: expanding-persistent-volumes

toc::[]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
include::modules/storage-expanding-add-volume-expansion.adoc[leveloffset=+1]

include::modules/storage-expanding-csi-volumes.adoc[leveloffset=+1]

:FeatureName: Expanding CSI volumes

include::modules/storage-expanding-flexvolume.adoc[leveloffset=+1]

include::modules/storage-expanding-local-volumes.adoc[leveloffset=+1]

include::modules/storage-expanding-filesystem-pvc.adoc[leveloffset=+1]

include::modules/storage-expanding-recovering-failure.adoc[leveloffset=+1]
endif::openshift-enterprise,openshift-webscale,openshift-origin[]

[role="_additional-resources"]
.Additional resources

* The controlling `StorageClass` object has `allowVolumeExpansion` set to `true` (see xref:../storage/expanding-persistent-volumes.adoc#add-volume-expansion_expanding-persistent-volumes[Enabling volume expansion support]).