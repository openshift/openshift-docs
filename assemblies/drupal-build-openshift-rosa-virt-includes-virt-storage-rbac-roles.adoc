// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-storage-rbac-roles_{context}"]
= RBAC roles for storage features in {VirtProductName}

The following permissions are granted to the Containerized Data Importer (CDI), including the `cdi-operator` and `cdi-controller` service accounts.

[id="cluster-wide-rbac-roles-cdi"]
== Cluster-wide RBAC roles

.Aggregated cluster roles for the `cdi.kubevirt.io` API group
[cols="1,2,1",options="header"]
|===
| CDI cluster role
| Resources
| Verbs

.2+.^| `cdi.kubevirt.io:admin`
.^| `datavolumes`, `uploadtokenrequests`
.^| `*` (all)

.^| `datavolumes/source`
.^| `create`

.2+.^| `cdi.kubevirt.io:edit`
.^| `datavolumes`, `uploadtokenrequests`
.^| `*`

.^| `datavolumes/source`
.^| `create`

.2+.^| `cdi.kubevirt.io:view`
.^| `cdiconfigs`, `dataimportcrons`, `datasources`, `datavolumes`, `objecttransfers`, `storageprofiles`, `volumeimportsources`, `volumeuploadsources`, `volumeclonesources`
.^| `get`, `list`, `watch`

.^| `datavolumes/source`
.^| `create`

.^| `cdi.kubevirt.io:config-reader`
.^| `cdiconfigs`, `storageprofiles`
.^| `get`, `list`, `watch`
|===

.Cluster-wide roles for the `cdi-operator` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `rbac.authorization.k8s.io`
.^| `clusterrolebindings`, `clusterroles`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `security.openshift.io`
.^| `securitycontextconstraints`
.^| `get`, `list`, `watch`, `update`, `create`

.^| `apiextensions.k8s.io`
.^| `customresourcedefinitions`, `customresourcedefinitions/status`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `cdi.kubevirt.io`
.^| `*`
.^| `*`

.^| `upload.cdi.kubevirt.io`
.^| `*`
.^| `*`

.^| `admissionregistration.k8s.io`
.^| `validatingwebhookconfigurations`, `mutatingwebhookconfigurations`
.^| `create`, `list`, `watch`

.^| `admissionregistration.k8s.io`
.^| `validatingwebhookconfigurations`

Allow list: `cdi-api-dataimportcron-validate, cdi-api-populator-validate, cdi-api-datavolume-validate, cdi-api-validate, objecttransfer-api-validate`
.^| `get`, `update`, `delete`

.^| `admissionregistration.k8s.io`
.^| `mutatingwebhookconfigurations`

Allow list: `cdi-api-datavolume-mutate`
.^| `get`, `update`, `delete`

.^| `apiregistration.k8s.io`
.^| `apiservices`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`
|===

.Cluster-wide roles for the `cdi-controller` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `""` (core)
.^| `events`
.^| `create`, `patch`

.^| `""` (core)
.^| `persistentvolumeclaims`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`, `deletecollection`, `patch`

.^| `""` (core)
.^| `persistentvolumes`
.^| `get`, `list`, `watch`, `update`

.^| `""` (core)
.^| `persistentvolumeclaims/finalizers`, `pods/finalizers`
.^| `update`

.^| `""` (core)
.^| `pods`, `services`
.^| `get`, `list`, `watch`, `create`, `delete`

.^| `""` (core)
.^| `configmaps`
.^| `get`, `create`

.^| `storage.k8s.io`
.^| `storageclasses`, `csidrivers`
.^| `get`, `list`, `watch`

.^| `config.openshift.io`
.^| `proxies`
.^| `get`, `list`, `watch`

.^| `cdi.kubevirt.io`
.^| `*`
.^| `*`

.^| `snapshot.storage.k8s.io`
.^| `volumesnapshots`, `volumesnapshotclasses`, `volumesnapshotcontents`
.^| `get`, `list`, `watch`, `create`, `delete`

.^| `snapshot.storage.k8s.io`
.^| `volumesnapshots`
.^| `update`, `deletecollection`

.^| `apiextensions.k8s.io`
.^| `customresourcedefinitions`
.^| `get`, `list`, `watch`

.^| `scheduling.k8s.io`
.^| `priorityclasses`
.^| `get`, `list`, `watch`

.^| `image.openshift.io`
.^| `imagestreams`
.^| `get`, `list`, `watch`

.^| `""` (core)
.^| `secrets`
.^| `create`

.^| `kubevirt.io`
.^| `virtualmachines/finalizers`
.^| `update`
|===

[id="namespaced-rbac-roles-cdi"]
== Namespaced RBAC roles

.Namespaced roles for the `cdi-operator` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `rbac.authorization.k8s.io`
.^| `rolebindings`, `roles`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `""` (core)
.^| `serviceaccounts`, `configmaps`, `events`, `secrets`, `services`
.^| `get`, `list`, `watch`, `create`, `update`, `patch`, `delete`

.^| `apps`
.^| `deployments`, `deployments/finalizers`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `route.openshift.io`
.^| `routes`, `routes/custom-host`
.^| `get`, `list`, `watch`, `create`, `update`

.^| `config.openshift.io`
.^| `proxies`
.^| `get`, `list`, `watch`

.^| `monitoring.coreos.com`
.^| `servicemonitors`, `prometheusrules`
.^| `get`, `list`, `watch`, `create`, `delete`, `update`, `patch`

.^| `coordination.k8s.io`
.^| `leases`
.^| `get`, `create`, `update`
|===

.Namespaced roles for the `cdi-controller` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `""` (core)
.^| `configmaps`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `""` (core)
.^| `secrets`
.^| `get`, `list`, `watch`

.^| `batch`
.^| `cronjobs`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `batch`
.^| `jobs`
.^| `create`, `delete`, `list`, `watch`

.^| `coordination.k8s.io`
.^| `leases`
.^| `get`, `create`, `update`

.^| `networking.k8s.io`
.^| `ingresses`
.^| `get`, `list`, `watch`

.^| `route.openshift.io`
.^| `routes`
.^| `get`, `list`, `watch`
|===
