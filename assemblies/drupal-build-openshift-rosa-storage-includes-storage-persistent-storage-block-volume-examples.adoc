// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//
// This module should only be present in openshift-enterprise and
// openshift-origin distributions.

[id="block-volume-examples_{context}"]
= Block volume examples

.PV example
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: block-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  volumeMode: Block <1>
  persistentVolumeReclaimPolicy: Retain
  fc:
    targetWWNs: ["50060e801049cfd1"]
    lun: 0
    readOnly: false
----
<1> `volumeMode` must be set to `Block` to indicate that this PV is a raw
block volume.

.PVC example
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: block-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Block <1>
  resources:
    requests:
      storage: 10Gi
----
<1> `volumeMode` must be set to `Block` to indicate that a raw block PVC
is requested.

.`Pod` specification example
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-block-volume
spec:
  containers:
    - name: fc-container
      image: fedora:26
      command: ["/bin/sh", "-c"]
      args: [ "tail -f /dev/null" ]
      volumeDevices:  <1>
        - name: data
          devicePath: /dev/xvda <2>
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: block-pvc <3>
----
<1> `volumeDevices`, instead of `volumeMounts`, is used for block
devices. Only `PersistentVolumeClaim` sources can be used with
raw block volumes.
<2> `devicePath`, instead of `mountPath`, represents the path to the
physical device where the raw block is mapped to the system.
<3> The volume source must be of type `persistentVolumeClaim` and must
match the name of the PVC as expected.

.Accepted values for `volumeMode`
[cols="1,2",options="header"]
|===

|Value
|Default

|Filesystem
|Yes

|Block
|No
|===

.Binding scenarios for block volumes
[cols="1,2,3",options="header"]
|===

|PV `volumeMode`
|PVC `volumeMode`
|Binding result

|Filesystem
|Filesystem
|Bind

|Unspecified
|Unspecified
|Bind

|Filesystem
|Unspecified
|Bind

|Unspecified
|Filesystem
|Bind

|Block
|Block
|Bind

|Unspecified
|Block
|No Bind

|Block
|Unspecified
|No Bind

|Filesystem
|Block
|No Bind

|Block
|Filesystem
|No Bind
|===

[IMPORTANT]
====
Unspecified values result in the default value of `Filesystem`.
====
