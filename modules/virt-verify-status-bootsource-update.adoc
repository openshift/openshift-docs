// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="virt-verify-status-bootsource-update_{context}"]
= Verifying the status of a boot source

You can determine if a boot source is system-defined or custom by viewing the `HyperConverged` custom resource (CR).

.Procedure

. View the contents of the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get hyperconverged kubevirt-hyperconverged -n {CNVNamespace} -o yaml
----
+
.Example output

[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
# ...
status:
# ...
  dataImportCronTemplates:
  - metadata:
      annotations:
        cdi.kubevirt.io/storage.bind.immediate.requested: "true"
      name: centos-7-image-cron
    spec:
      garbageCollect: Outdated
      managedDataSource: centos7
      schedule: 55 8/12 * * *
      template:
        metadata: {}
        spec:
          source:
            registry:
              url: docker://quay.io/containerdisks/centos:7-2009
          storage:
            resources:
              requests:
                storage: 30Gi
        status: {}
    status:
      commonTemplate: true <1>
# ...
  - metadata:
      annotations:
        cdi.kubevirt.io/storage.bind.immediate.requested: "true"
      name: user-defined-dic
    spec:
      garbageCollect: Outdated
      managedDataSource: user-defined-centos-stream8
      schedule: 55 8/12 * * *
      template:
        metadata: {}
        spec:
          source:
            registry:
              pullMethod: node
              url: docker://quay.io/containerdisks/centos-stream:8
          storage:
            resources:
              requests:
                storage: 30Gi
        status: {}
    status: {} <2>
# ...
----
<1> Indicates a system-defined boot source.
<2> Indicates a custom boot source.

. Verify the status of the boot source by reviewing the `status.dataImportCronTemplates.status` field.
* If the field contains `commonTemplate: true`, it is a system-defined boot source.
* If the `status.dataImportCronTemplates.status` field has the value `{}`, it is a custom boot source.