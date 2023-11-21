// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-export-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-virtualmachineexport_{context}"]
= Creating a VirtualMachineExport custom resource

You can create a `VirtualMachineExport` custom resource (CR) to export the following objects:

* Virtual machine (VM): Exports the persistent volume claims (PVCs) of a specified VM.
* VM snapshot: Exports PVCs contained in a `VirtualMachineSnapshot` CR.
* PVC: Exports a PVC. If the PVC is used by another pod, such as the `virt-launcher` pod, the export remains in a `Pending` state until the PVC is no longer in use.

The `VirtualMachineExport` CR creates internal and external links for the exported volumes. Internal links are valid within the cluster. External links can be accessed by using an `Ingress` or `Route`.

The export server supports the following file formats:

* `raw`: Raw disk image file.
* `gzip`: Compressed disk image file.
* `dir`: PVC directory and files.
* `tar.gz`: Compressed PVC file.

.Prerequisites

* The VM must be shut down for a VM export.

.Procedure

. Create a `VirtualMachineExport` manifest to export a volume from a `VirtualMachine`, `VirtualMachineSnapshot`, or `PersistentVolumeClaim` CR according to the following example and save it as `example-export.yaml`:
+
.`VirtualMachineExport` example
[source,yaml]
----
apiVersion: export.kubevirt.io/v1alpha1
kind: VirtualMachineExport
metadata:
  name: example-export
spec:
  source:
    apiGroup: "kubevirt.io" <1>
    kind: VirtualMachine <2>
    name: example-vm
  ttlDuration: 1h <3>
----
<1> Specify the appropriate API group:
+
* `"kubevirt.io"` for `VirtualMachine`.
* `"snapshot.kubevirt.io"` for `VirtualMachineSnapshot`.
* `""` for `PersistentVolumeClaim`.
<2> Specify `VirtualMachine`, `VirtualMachineSnapshot`, or `PersistentVolumeClaim`.
<3> Optional. The default duration is 2 hours.

. Create the `VirtualMachineExport` CR:
+
[source,terminal]
----
$ oc create -f example-export.yaml
----

. Get the `VirtualMachineExport` CR:
+
[source,terminal]
----
$ oc get vmexport example-export -o yaml
----
+
The internal and external links for the exported volumes are displayed in the `status` stanza:
+
.Output example
[source,yaml]
----
apiVersion: export.kubevirt.io/v1alpha1
kind: VirtualMachineExport
metadata:
  name: example-export
  namespace: example
spec:
  source:
    apiGroup: ""
    kind: PersistentVolumeClaim
    name: example-pvc
  tokenSecretRef: example-token
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2022-06-21T14:10:09Z"
    reason: podReady
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2022-06-21T14:09:02Z"
    reason: pvcBound
    status: "True"
    type: PVCReady
  links:
    external: <1>
      cert: |-
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
      volumes:
      - formats:
        - format: raw
          url: https://vmexport-proxy.test.net/api/export.kubevirt.io/v1alpha1/namespaces/example/virtualmachineexports/example-export/volumes/example-disk/disk.img
        - format: gzip
          url: https://vmexport-proxy.test.net/api/export.kubevirt.io/v1alpha1/namespaces/example/virtualmachineexports/example-export/volumes/example-disk/disk.img.gz
        name: example-disk
    internal:  <2>
      cert: |-
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
      volumes:
      - formats:
        - format: raw
          url: https://virt-export-example-export.example.svc/volumes/example-disk/disk.img
        - format: gzip
          url: https://virt-export-example-export.example.svc/volumes/example-disk/disk.img.gz
        name: example-disk
  phase: Ready
  serviceName: virt-export-example-export
----
<1> External links are accessible from outside the cluster by using an `Ingress` or `Route`.
<2> Internal links are only valid inside the cluster.