// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-understanding.adoc

[id="file-integrity-node-status-types_{context}"]
= FileIntegrityNodeStatus CR status types

These conditions are reported in the results array of the corresponding `FileIntegrityNodeStatus` CR status:

* `Succeeded` - The integrity check passed; the files and directories covered by the AIDE check have not been modified since the database was last initialized.

* `Failed` - The integrity check failed; some files or directories covered by the AIDE check have been modified since the database was last initialized.

* `Errored` - The AIDE scanner encountered an internal error.
