// Module included in the following assemblies:
//
// * storage/persistent_storage-iscsi.adoc

[id="volume-security-iscsi_{context}"]
= iSCSI volume security
Users request storage with a `PersistentVolumeClaim` object. This claim only
lives in the user's namespace and can only be referenced by a pod within
that same namespace. Any attempt to access a persistent volume claim across a
namespace causes the pod to fail.

Each iSCSI LUN must be accessible by all nodes in the cluster.

== Challenge Handshake Authentication Protocol (CHAP) configuration

Optionally, {product-title} can use CHAP to authenticate itself to iSCSI targets:

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
    iqn: iqn.2016-04.test.com:storage.target00
    lun: 0
    fsType: ext4
    chapAuthDiscovery: true <1>
    chapAuthSession: true <2>
    secretRef:
      name: chap-secret <3>
----
<1> Enable CHAP authentication of iSCSI discovery.
<2> Enable CHAP authentication of iSCSI session.
<3> Specify name of Secrets object with user name + password. This `Secret`
object must be available in all namespaces that can use the referenced volume.
