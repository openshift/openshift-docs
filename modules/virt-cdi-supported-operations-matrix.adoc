// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-virtctl.adoc
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-block.adoc
// * virt/storage/virt-preparing-cdi-scratch-space.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-disk-into-new-datavolume.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-using-datavolumetemplate.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-disk-to-new-block-storage-pvc.adoc
// * virt/virtual_machines/importing_vms/virt-importing-virtual-machine-images-datavolumes.adoc
// * virt/virtual_machines/importing_vms/virt-importing-virtual-machine-images-datavolumes-block.adoc
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-web.adoc

[id="virt-cdi-supported-operations-matrix_{context}"]
= CDI supported operations matrix

This matrix shows the supported CDI operations for content types against endpoints, and which of these operations requires scratch space.

|===
|Content types | HTTP | HTTPS | HTTP basic auth | Registry | Upload

| KubeVirt (QCOW2)
|&#10003; QCOW2 +
&#10003; GZ* +
&#10003; XZ*

|&#10003; QCOW2** +
&#10003; GZ* +
&#10003; XZ*

|&#10003; QCOW2 +
&#10003; GZ* +
&#10003; XZ*

| &#10003; QCOW2* +
&#9633; GZ +
&#9633; XZ

| &#10003; QCOW2* +
&#10003; GZ* +
&#10003; XZ*

| KubeVirt (RAW)
|&#10003; RAW +
&#10003; GZ +
&#10003; XZ

|&#10003; RAW +
&#10003; GZ +
&#10003; XZ

| &#10003; RAW +
&#10003; GZ +
&#10003; XZ

| &#10003; RAW* +
&#9633; GZ +
&#9633; XZ

| &#10003; RAW* +
&#10003; GZ* +
&#10003; XZ*
|===

&#10003; Supported operation

&#9633; Unsupported operation

$$*$$ Requires scratch space

$$**$$ Requires scratch space if a custom certificate authority is required
