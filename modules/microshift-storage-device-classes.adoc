// Module included in the following assemblies:
//
// * microshift_storage/volume-snapshots-microshift.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-storage-device-classes_{context}"]
= Device classes

You can create custom device classes by adding a `device-classes` array to your logical volume manager storage (LVMS) configuration. Add the array to the `/etc/microshift/lvmd.yaml` configuration file. A single device class must be set as the default. You must restart {microshift-short} for configuration changes to take effect.

[WARNING]
====
Removing a device class while there are still persistent volumes or `VolumeSnapshotContent` objects connected to that device class breaks both thick and thin provisioning.
====

You can define multiple device classes in the `device-classes` array. These classes can be a mix of thick and thin volume configurations.

.Example of a mixed `device-class` array
[source,terminal]
----
socket-name: /run/topolvm/lvmd.sock
device-classes:
  - name: ssd
    volume-group: ssd-vg
    spare-gb: 0 <1>
    default: true
  - name: hdd
    volume-group: hdd-vg
    spare-gb: 0
  - name: thin
    spare-gb: 0
    thin-pool:
      name: thin
      overprovision-ratio: 10
    type: thin
    volume-group: ssd
  - name: striped
    volume-group: multi-pv-vg
    spare-gb: 0
    stripe: 2
    stripe-size: "64"
    lvcreate-options:<2>
----
<1> When you set the spare capacity to anything other than `0`, more space can be allocated than expected.
<2> Extra arguments to pass to the `lvcreate` command, such as `--type=<type>`. Neither {microshift-short} nor the LVMS verifies `lvcreate-options` values. These optional values are passed as is to the `lvcreate` command. Ensure that the options specified here are correct.
