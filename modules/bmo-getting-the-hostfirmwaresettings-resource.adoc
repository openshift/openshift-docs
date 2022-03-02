// This is included in the following assemblies:
//
// post_installation_configuration/bare-metal-configuration.adoc

[id="getting-the-hostfirmwaresettings-resource_{context}"]
= Getting the HostFirmwareSettings resource

The `HostFirmwareSettings` resource contains the vendor-specific BIOS properties of a physical host. You must get the `HostFirmwareSettings` resource for a physical host to review its BIOS properties.

.Procedure

. Get the detailed list of `HostFirmwareSettings` resources:
+
[source,terminal]
----
$ oc get hfs -n openshift-machine-api -o yaml
----
+
[NOTE]
====
You can use `hostfirmwaresettings` as the long form of `hfs` with the `oc get` command.
====

. Get the list of `HostFirmwareSettings` resources:
+
[source,terminal]
----
$ oc get hfs -n openshift-machine-api
----

. Get the `HostFirmwareSettings` resource for a particular host
+
[source,terminal]
----
$ oc get hfs <host_name> -n openshift-machine-api -o yaml
----
+
Where `<host_name>` is the name of the host.
