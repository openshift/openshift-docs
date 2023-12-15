// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage-cinder.adoc

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-cinder-creating-pv_{context}"]
= Creating the persistent volume

You must define your persistent volume (PV) in an object definition before creating
it in {product-title}:

.Procedure

. Save your object definition to a file.
+
.cinder-persistentvolume.yaml
[source,yaml]
----
apiVersion: "v1"
kind: "PersistentVolume"
metadata:
  name: "pv0001" <1>
spec:
  capacity:
    storage: "5Gi" <2>
  accessModes:
    - "ReadWriteOnce"
  cinder: <3>
    fsType: "ext3" <4>
    volumeID: "f37a03aa-6212-4c62-a805-9ce139fab180" <5>
----
<1> The name of the volume that is used by persistent volume claims or pods.
<2> The amount of storage allocated to this volume.
<3> Indicates `cinder` for {rh-openstack-first} Cinder volumes.
<4> The file system that is created when the volume is mounted for the first time.
<5> The Cinder volume to use.
+
[IMPORTANT]
====
Do not change the `fstype` parameter value after the volume is formatted and
provisioned. Changing this value can result in data loss and pod failure.
====

. Create the object definition file you saved in the previous step.
+
[source,terminal]
----
$ oc create -f cinder-persistentvolume.yaml
----
