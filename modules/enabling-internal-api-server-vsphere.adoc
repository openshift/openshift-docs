// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc

:_mod-docs-content-type: PROCEDURE
[id="enabling-internal-api-server-vsphere_{context}"]
= Enabling communication with the internal API server for the WMCO on vSphere

The Windows Machine Config Operator (WMCO) downloads the Ignition config files from the internal API server endpoint. You must enable communication with the internal API server so that your Windows virtual machine (VM) can download the Ignition config files, and the kubelet on the configured VM can only communicate with the internal API server.

.Prerequisites

* You have installed a cluster on vSphere.

.Procedure

* Add a new DNS entry for `api-int.<cluster_name>.<base_domain>` that points to the external API server URL `api.<cluster_name>.<base_domain>`. This can be a CNAME or an additional A record.

[NOTE]
====
The external API endpoint was already created as part of the initial cluster installation on vSphere.
====
