// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc

[id="ceph-rbd-definition_{context}"]
= Ceph RBD object definition

.ceph-storageclass.yaml
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: cephfs
provisioner: kubernetes.io/rbd
parameters:
  monitors: 10.16.153.105:6789  <1>
  adminId: admin  <2>
  adminSecretName: ceph-secret  <3>
  adminSecretNamespace: kube-system  <4>
  pool: kube  <5>
  userId: kube  <6>
  userSecretName: ceph-secret-user  <7>
  fsType: ext4 <8>
  imageFormat: "2" <9>
----
<1> (required) A comma-delimited list of Ceph monitors.
<2> Optional: Ceph client ID that is capable of creating images in the
pool. Default is `admin`.
<3> (required) Secret Name for `adminId`. The provided secret must have
type `kubernetes.io/rbd`.
<4> Optional: The namespace for `adminSecret`. Default is `default`.
<5> Optional: Ceph RBD pool. Default is `rbd`.
<6> Optional: Ceph client ID that is used to map the Ceph RBD image.
Default is the same as `adminId`.
<7> (required) The name of Ceph Secret for `userId` to map Ceph RBD image.
It must exist in the same namespace as PVCs.
<8> Optional: File system that is created on dynamically provisioned
volumes. This value is copied to the `fsType` field of dynamically
provisioned persistent volumes and the file system is created when the
volume is mounted for the first time. The default value is `ext4`.
<9> Optional: Ceph RBD image format. The default value is `2`.
