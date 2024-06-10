:_mod-docs-content-type: ASSEMBLY
[id="oadp-api"]
= APIs used with OADP
include::_attributes/common-attributes.adoc[]
:context: oadp-api
:namespace: openshift-adp
:local-product: OADP
:velero-domain: velero.io

toc::[]

The document provides information about the following APIs that you can use with OADP:

* Velero API
* OADP API

[id="velero-api"]
== Velero API

Velero API documentation is maintained by Velero, not by Red Hat. It can be found at link:https://velero.io/docs/main/api-types/[Velero API types].

[id="oadp-api-tables"]
== OADP API

The following tables provide the structure of the OADP API:

.DataProtectionApplicationSpec
[options="header"]
|===
|Property|Type|Description

|`backupLocations`
|[] link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#BackupLocation[`BackupLocation`]
|Defines the list of configurations to use for `BackupStorageLocations`.

|`snapshotLocations`
|[] link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#SnapshotLocation[`SnapshotLocation`]
|Defines the list of configurations to use for `VolumeSnapshotLocations`.

|`unsupportedOverrides`
|map [ link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#UnsupportedImageKey[UnsupportedImageKey] ]  link:https://pkg.go.dev/builtin#string[string]
|Can be used to override the deployed dependent images for development. Options are `veleroImageFqin`, `awsPluginImageFqin`, `openshiftPluginImageFqin`, `azurePluginImageFqin`, `gcpPluginImageFqin`, `csiPluginImageFqin`, `dataMoverImageFqin`, `resticRestoreImageFqin`, `kubevirtPluginImageFqin`, and `operator-type`.

|`podAnnotations`
|map [ link:https://pkg.go.dev/builtin#string[string] ] link:https://pkg.go.dev/builtin#string[string]
|Used to add annotations to pods deployed by Operators.

|`podDnsPolicy`
|link:https://pkg.go.dev/k8s.io/api/core/v1#DNSPolicy[`DNSPolicy`]
|Defines the configuration of the DNS of a pod.

|`podDnsConfig`
|link:https://pkg.go.dev/k8s.io/api/core/v1#PodDNSConfig[`PodDNSConfig`]
|Defines the DNS parameters of a pod in addition to those generated from `DNSPolicy`.

|`backupImages`
|*link:https://pkg.go.dev/builtin#bool[bool]
|Used to specify whether or not you want to deploy a registry for enabling backup and restore of images.

|`configuration`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ApplicationConfig[`ApplicationConfig`]
|Used to define the data protection application's server configuration.

|`features`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#Features[`Features`]
|Defines the configuration for the DPA to enable the Technology Preview features.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#DataProtectionApplicationSpec[Complete schema definitions for the OADP API].

.BackupLocation
[options="header"]
|===
|Property|Type|Description

|`velero`
|*link:https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#BackupStorageLocationSpec[velero.BackupStorageLocationSpec]
|Location to store volume snapshots, as described in link:https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#BackupStorageLocation[Backup Storage Location].

|`bucket`
| *link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#CloudStorageLocation[CloudStorageLocation]
| [Technology Preview] Automates creation of a bucket at some cloud storage providers for use as a backup storage location.
|===

:FeatureName: The `bucket` parameter
include::snippets/technology-preview.adoc[leveloffset=+1]

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#BackupLocation[Complete schema definitions for the type `BackupLocation`].

.SnapshotLocation
[options="header"]
|===
|Property|Type|Description

|`velero`
|*link:https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#VolumeSnapshotLocationSpec[VolumeSnapshotLocationSpec]
|Location to store volume snapshots, as described in link:https://pkg.go.dev/github.com/vmware-tanzu/velero/pkg/apis/velero/v1#VolumeSnapshotLocation[Volume Snapshot Location].
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#SnapshotLocation[Complete schema definitions for the type `SnapshotLocation`].

.ApplicationConfig
[options="header"]
|===
|Property|Type|Description

|`velero`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#VeleroConfig[VeleroConfig]
|Defines the configuration for the Velero server.

|`restic`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ResticConfig[ResticConfig]
|Defines the configuration for the Restic server.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ApplicationConfig[Complete schema definitions for the type `ApplicationConfig`].

.VeleroConfig
[options="header"]
|===
|Property|Type|Description

|`featureFlags`
|[] link:https://pkg.go.dev/builtin#string[string]
|Defines the list of features to enable for the Velero instance.

|`defaultPlugins`
|[] link:https://pkg.go.dev/builtin#string[string]
|The following types of default Velero plugins can be installed: `aws`,`azure`, `csi`, `gcp`, `kubevirt`, and `openshift`.

|`customPlugins`
|[]link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#CustomPlugin[CustomPlugin]
|Used for installation of custom Velero plugins.

Default and custom plugins are described in xref:../../backup_and_restore/application_backup_and_restore/oadp-features-plugins#oadp-features-plugins[OADP plugins]

|`restoreResourcesVersionPriority`
|link:https://pkg.go.dev/builtin#string[string]
|Represents a config map that is created if defined for use in conjunction with the `EnableAPIGroupVersions` feature flag. Defining this field automatically adds `EnableAPIGroupVersions` to the Velero server feature flag.

|`noDefaultBackupLocation`
|link:https://pkg.go.dev/builtin#bool[bool]
|To install Velero without a default backup storage location, you must set the `noDefaultBackupLocation` flag in order to confirm installation.

|`podConfig`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#PodConfig[`PodConfig`]
|Defines the configuration of the `Velero` pod.

|`logLevel`
|link:https://pkg.go.dev/builtin#string[string]
|Velero server’s log level (use `debug` for the most granular logging, leave unset for Velero default). Valid options are `trace`, `debug`, `info`, `warning`, `error`, `fatal`, and `panic`.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#VeleroConfig[Complete schema definitions for the type `VeleroConfig`].

.CustomPlugin
[options="header"]
|===
|Property|Type|Description

|`name`
|link:https://pkg.go.dev/builtin#string[string]
|Name of custom plugin.

|`image`
|link:https://pkg.go.dev/builtin#string[string]
|Image of custom plugin.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#CustomPlugin[Complete schema definitions for the type `CustomPlugin`].

.ResticConfig
[options="header"]
|===
|Property|Type|Description

|`enable`
|*link:https://pkg.go.dev/builtin#bool[bool]
|If set to `true`, enables backup and restore using Restic. If set to `false`, snapshots are needed.

|`supplementalGroups`
|[]link:https://pkg.go.dev/builtin#int64[int64]
|Defines the Linux groups to be applied to the `Restic` pod.

|`timeout`
|link:https://pkg.go.dev/builtin#string[string]
|A user-supplied duration string that defines the Restic timeout. Default value is `1hr` (1 hour). A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as `300ms`, -1.5h` or `2h45m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`.

|`podConfig`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#PodConfig[`PodConfig`]
|Defines the configuration of the `Restic` pod.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#ResticConfig[Complete schema definitions for the type `ResticConfig`].

.PodConfig
[options="header"]
|===
|Property|Type|Description

|`nodeSelector`
|map [ link:https://pkg.go.dev/builtin#string[string] ] link:https://pkg.go.dev/builtin#string[string]
|Defines the `nodeSelector` to be supplied to a `Velero` `podSpec` or a `Restic` `podSpec`.

|`tolerations`
|[]link:https://pkg.go.dev/k8s.io/api/core/v1#Toleration[Toleration]
|Defines the list of tolerations to be applied to a Velero deployment or a Restic `daemonset`.

|`resourceAllocations`
|link:https://pkg.go.dev/k8s.io/api/core/v1#ResourceRequirements[ResourceRequirements]
|Set specific resource `limits` and `requests` for a `Velero` pod or a `Restic` pod as described in xref:../../backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc#oadp-setting-resource-limits-and-requests_installing-oadp-aws[Setting Velero CPU and memory resource allocations].

|`labels`
|map [ link:https://pkg.go.dev/builtin#string[string] ] link:https://pkg.go.dev/builtin#string[string]
|Labels to add to pods.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#PodConfig[Complete schema definitions for the type `PodConfig`].

.Features
[options="header"]
|===
|Property|Type|Description

|`dataMover`
|*link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#DataMover[`DataMover`]
|Defines the configuration of the Data Mover.
|===

link:https://pkg.go.dev/github.com/openshift/oadp-operator/api/v1alpha1#Features[Complete schema definitions for the type `Features`].

.DataMover
[options="header"]
|===
|Property|Type|Description

|`enable`
|link:https://pkg.go.dev/builtin#bool[bool]
|If set to `true`, deploys the volume snapshot mover controller and a modified CSI Data Mover plugin. If set to `false`, these are not deployed.

|`credentialName`
|link:https://pkg.go.dev/builtin#string[string]
|User-supplied Restic `Secret` name for Data Mover.

|`timeout`
|link:https://pkg.go.dev/builtin#string[string]
|A user-supplied duration string for `VolumeSnapshotBackup` and `VolumeSnapshotRestore` to complete. Default is `10m` (10 minutes). A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as `300ms`, -1.5h` or `2h45m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`.
|===

The OADP API is more fully detailed in link:https://pkg.go.dev/github.com/openshift/oadp-operator[OADP Operator].

