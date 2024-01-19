:_mod-docs-content-type: ASSEMBLY
[id="ephemeral-storage-shared-resource-csi-driver-operator"]
= Shared Resource CSI Driver Operator
include::_attributes/common-attributes.adoc[]
:context: ephemeral-storage-shared-resource-csi-driver-operator

toc::[]


[role="_abstract"]
As a cluster administrator, you can use the Shared Resource CSI Driver in {product-title} to provision inline ephemeral volumes that contain the contents of `Secret` or `ConfigMap` objects. This way, pods and other Kubernetes types that expose volume mounts, and {product-title} Builds can securely use the contents of those objects across potentially any namespace in the cluster. To accomplish this, there are currently two types of shared resources: a `SharedSecret` custom resource for `Secret` objects, and a `SharedConfigMap` custom resource for `ConfigMap` objects.

// The Shared Resource CSI Driver in {product-title}, as opposed to the driver for upstream Kubernetes...

:FeatureName: The Shared Resource CSI Driver
include::snippets/technology-preview.adoc[leveloffset=+1]

[NOTE]
====
To enable the Shared Resource CSI Driver, you must xref:../../nodes/clusters/nodes-cluster-enabling-features.adoc#nodes-cluster-enabling[enable features using feature gates].
====

include::modules/persistent-storage-csi-about.adoc[leveloffset=+1]

include::modules/ephemeral-storage-sharing-secrets-across-namespaces.adoc[leveloffset=+1]

include::modules/ephemeral-storage-using-a-sharedsecrets-resource-in-a-pod.adoc[leveloffset=+1]

include::modules/ephemeral-storage-sharing-configmaps-across-namespaces.adoc[leveloffset=+1]

include::modules/ephemeral-storage-using-a-sharedconfigmap-object-in-a-pod.adoc[leveloffset=+1]

include::modules/ephemeral-storage-additional-support-limitations-for-shared-resource-csi-driver.adoc[leveloffset=+1]

include::modules/ephemeral-storage-additional-details-about-volumeattributes-on-shared-resource-pod-volumes.adoc[leveloffset=+1]

include::modules/ephemeral-storage-integration-between-shared-resources-insights-operator-and-openshift-builds.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../support/remote_health_monitoring/insights-operator-simple-access.adoc#insights-operator-simple-access[Importing simple content access certificates with Insights Operator]
* xref:../../cicd/builds/running-entitled-builds.adoc#builds-source-secrets-entitlements_running-entitled-builds[Adding subscription entitlements as a build secret]
