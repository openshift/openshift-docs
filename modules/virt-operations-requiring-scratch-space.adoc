// Module included in the following assemblies:
//
// * virt/storage/virt-preparing-cdi-scratch-space.adoc

[id="virt-operations-requiring-scratch-space_{context}"]
= CDI operations that require scratch space

[options="header"]
|===
| Type | Reason

| Registry imports
| CDI must download the image to a scratch space and extract the layers to find the image file. The image file is then passed to QEMU-IMG for conversion to a raw disk.

| Upload image
| QEMU-IMG does not accept input from STDIN. Instead, the image to upload is saved in scratch space before it can be passed to QEMU-IMG for conversion.

| HTTP imports of archived images
| QEMU-IMG does not know how to handle the archive formats CDI supports. Instead, the image is unarchived and saved into scratch space before it is passed to QEMU-IMG.

| HTTP imports of authenticated images
| QEMU-IMG inadequately handles authentication. Instead, the image is saved to scratch space and authenticated before it is passed to QEMU-IMG.

| HTTP imports of custom certificates
| QEMU-IMG inadequately handles custom certificates of HTTPS endpoints. Instead, CDI downloads the image to scratch space before passing the file to QEMU-IMG.
|===
