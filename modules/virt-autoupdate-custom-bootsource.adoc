// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="virt-autoupdate-custom-bootsource_{context}"]
= Enabling automatic updates for custom boot sources

{VirtProductName} automatically updates system-defined boot sources by default, but does not automatically update custom boot sources. You must manually enable automatic updates by editing the `HyperConverged` custom resource (CR).

.Prerequisites

* The cluster has a default storage class.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `HyperConverged` CR, adding the appropriate template and boot source in the `dataImportCronTemplates` section. For example:
+
.Example custom resource
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  dataImportCronTemplates:
  - metadata:
      name: centos7-image-cron
      annotations:
        cdi.kubevirt.io/storage.bind.immediate.requested: "true" <1>
    spec:
      schedule: "0 */12 * * *" <2>
      template:
        spec:
          source:
            registry: <3>
              url: docker://quay.io/containerdisks/centos:7-2009
          storage:
            resources:
              requests:
                storage: 10Gi
      managedDataSource: centos7 <4>
      retentionPolicy: "None" <5>
----
<1> This annotation is required for storage classes with `volumeBindingMode` set to `WaitForFirstConsumer`.
<2> Schedule for the job specified in cron format.
<3> Use to create a data volume from a registry source. Use the default `pod` `pullMethod` and not `node` `pullMethod`, which is based on the `node` docker cache. The `node` docker cache is useful when a registry image is available via `Container.Image`, but the CDI importer is not authorized to access it.
<4> For the custom image to be detected as an available boot source, the name of the image's `managedDataSource` must match the name of the template's `DataSource`, which is found under `spec.dataVolumeTemplates.spec.sourceRef.name` in the VM template YAML file.
<5> Use `All` to retain data volumes and data sources when the cron job is deleted. Use `None` to delete data volumes and data sources when the cron job is deleted.

. Save the file.