// Module included in the following assemblies:
//
// * storage/persistent_storage-iscsi.adoc

[id="iscsi-custom-iqn_{context}"]
= iSCSI custom initiator IQN
Configure the custom initiator iSCSI Qualified Name (IQN) if the iSCSI
targets are restricted to certain IQNs, but the nodes that the iSCSI PVs
are attached to are not guaranteed to have these IQNs.

To specify a custom initiator IQN, use `initiatorName` field.

[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: iscsi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  iscsi:
    targetPortal: 10.0.0.1:3260
    portals: ['10.0.2.16:3260', '10.0.2.17:3260', '10.0.2.18:3260']
    iqn: iqn.2016-04.test.com:storage.target00
    lun: 0
    initiatorName: iqn.2016-04.test.com:custom.iqn <1>
    fsType: ext4
    readOnly: false
----
<1> Specify the name of the initiator.
