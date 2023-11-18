:_mod-docs-content-type: ASSEMBLY
[id="ephemeral-storage-csi-inline"]
= CSI inline ephemeral volumes
include::_attributes/common-attributes.adoc[]
:context: ephemeral-storage-csi-inline

// TP features should be excluded from OSD and ROSA. When this feature is GA, it can be included in the OSD/ROSA docs, but with a warning that it is available as of version 4.x.

toc::[]

Container Storage Interface (CSI) inline ephemeral volumes allow you to define a `Pod` spec that creates inline ephemeral volumes when a pod is deployed and delete them when a pod is destroyed.

This feature is only available with supported Container Storage Interface (CSI) drivers:

* Shared Resource CSI driver
* Azure File CSI driver
* {secrets-store-driver}

include::modules/ephemeral-storage-csi-inline-overview.adoc[leveloffset=+1]

include::modules/ephemeral-storage-csi-inline-overview-admin-plugin.adoc[leveloffset=+1]

include::modules/ephemeral-storage-csi-inline-pod.adoc[leveloffset=+1]

[id="additional-resources_ephemeral-storage-csi-inline"]
[role="_additional-resources"]
== Additional resources
* link:https://kubernetes.io/docs/concepts/security/pod-security-standards/[Pod Security Standards]
