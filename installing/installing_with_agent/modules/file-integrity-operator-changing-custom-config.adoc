// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="file-integrity-operator-changing-custom-config_{context}"]
= Changing the custom File Integrity configuration

To change the File Integrity configuration, never change the generated
config map. Instead, change the config map that is linked to the `FileIntegrity`
object through the `spec.name`, `namespace`, and `key` attributes.
