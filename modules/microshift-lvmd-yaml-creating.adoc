// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-lvmd-yaml-creating_{context}"]
= Creating an LVMS configuration file

When {microshift-short} runs, it uses LVMS configuration from `/etc/microshift/lvmd.yaml`, if provided. You must place any configuration files that you create into the `/etc/microshift/` directory.

.Procedure

* To create the `lvmd.yaml` configuration file, run the following command:
+
[source,terminal]
----
$ sudo cp /etc/microshift/lvmd.yaml.default /etc/microshift/lvmd.yaml
----
