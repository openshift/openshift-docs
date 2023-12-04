[id="persistent-storage-csi-secrets-store"]
= {secrets-store-driver}
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-csi-secrets-store

toc::[]

include::modules/persistent-storage-csi-secrets-store-driver-overview.adoc[leveloffset=+1]

For more information about CSI inline volumes, see xref:../../storage/container_storage_interface/ephemeral-storage-csi-inline.adoc#ephemeral-storage-csi-inline[CSI inline ephemeral volumes].

:FeatureName: The {secrets-store-operator}
include::snippets/technology-preview.adoc[leveloffset=+1]

Familiarity with xref:../../storage/understanding-persistent-storage.adoc#understanding-persistent-storage[persistent storage] and xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[configuring CSI volumes] is recommended when working with a CSI driver.

// Secrets store providers
include::modules/secrets-store-providers.adoc[leveloffset=+2]

include::modules/persistent-storage-csi-about.adoc[leveloffset=+1]

include::modules/persistent-storage-csi-secrets-store-driver-install.adoc[leveloffset=+1]

.Next steps

* xref:../../nodes/pods/nodes-pods-secrets-store.adoc#mounting-secrets-external-secrets-store[Mounting secrets from an external secrets store to a CSI volume]

include::modules/persistent-storage-csi-secrets-store-driver-uninstall.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources
* xref:../../storage/container_storage_interface/persistent-storage-csi.adoc#persistent-storage-csi[Configuring CSI volumes]
