// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-additional-network.adoc

:_mod-docs-content-type: REFERENCE
[id="nw-multus-tap-object_{context}"]
= Configuration for a TAP additional network

The following object describes the configuration parameters for the TAP CNI
plugin:

.TAP CNI plugin JSON configuration object
[cols=".^2,.^2,.^6",options="header"]
|====
|Field|Type|Description

|`cniVersion`
|`string`
|The CNI specification version. The `0.3.1` value is required.

|`name`
|`string`
|The value for the `name` parameter you provided previously for the CNO configuration.

|`type`
|`string`
|The name of the CNI plugin to configure: `tap`.

|`mac`
|`string`
|Optional: Request the specified MAC address for the interface.

|`mtu`
|`integer`
|Optional: Set the maximum transmission unit (MTU) to the specified value. The default value is automatically set by the kernel.

|`selinuxcontext`
|`string`
a|Optional: The SELinux context to associate with the tap device.

[NOTE]
====
The value `system_u:system_r:container_t:s0` is required for {product-title}.
====

|`multiQueue`
|`boolean`
|Optional: Set to `true` to enable multi-queue.

|`owner`
|`integer`
|Optional: The user owning the tap device.

|`group`
|`integer`
|Optional: The group owning the tap device.

|`bridge`
|`string`
|Optional: Set the tap device as a port of an already existing bridge.
|====

[id="nw-multus-tap-config-example_{context}"]
== Tap configuration example

The following example configures an additional network named `mynet`:

[source,json]
----
{
 "name": "mynet",
 "cniVersion": "0.3.1",
 "type": "tap",
 "mac": "00:11:22:33:44:55",
 "mtu": 1500,
 "selinuxcontext": "system_u:system_r:container_t:s0",
 "multiQueue": true,
 "owner": 0,
 "group": 0
 "bridge": "br1"
}
----

[id="nw-multus-enable-container_use_devices_{context}"]

== Setting SELinux boolean for the TAP CNI plugin

To create the tap device with the `container_t` SELinux context, enable the `container_use_devices` boolean on the host by using the Machine Config Operator (MCO).

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a new YAML file named, such as `setsebool-container-use-devices.yaml`, with the following details:
+
[source, yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-worker-setsebool
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
      - enabled: true
        name: setsebool.service
        contents: |
          [Unit]
          Description=Set SELinux boolean for the TAP CNI plugin
          Before=kubelet.service

          [Service]
          Type=oneshot
          ExecStart=/usr/sbin/setsebool container_use_devices=on
          RemainAfterExit=true

          [Install]
          WantedBy=multi-user.target graphical.target
----
+

. Create the new `MachineConfig` object by running the following command:
+
[source,terminal]
----
$ oc apply -f setsebool-container-use-devices.yaml
----
+
[NOTE]
====
Applying any changes to the `MachineConfig` object causes all affected nodes to gracefully reboot after the change is applied. This update can take some time to be applied.
====
+
. Verify the change is applied by running the following command:
+
[source,terminal]
----
$ oc get machineconfigpools
----
+
.Expected output
+
[source,terminal,options="nowrap",role="white-space-pre"]
----
NAME        CONFIG                                                UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master      rendered-master-e5e0c8e8be9194e7c5a882e047379cfa      True      False      False      3              3                   3                     0                      7d2h
worker      rendered-worker-d6c9ca107fba6cd76cdcbfcedcafa0f2      True      False      False      3              3                   3                     0                      7d
----
+
[NOTE]
====
All nodes should be in the updated and ready state.
====
