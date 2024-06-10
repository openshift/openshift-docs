// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-local-storage-with-hpp.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-storage-pool-pvc-template_{context}"]
= Creating a storage pool with a PVC template

You can create a storage pool for multiple hostpath provisioner (HPP) volumes by specifying a PVC template in the HPP custom resource (CR).

[IMPORTANT]
====
Do not create storage pools in the same partition as the operating system. Otherwise, the operating system partition might become filled to capacity, which will impact performance or cause the node to become unstable or unusable.
====

.Prerequisites

* The directories specified in `spec.storagePools.path` must have read/write access.

.Procedure

. Create an `hpp_pvc_template_pool.yaml` file for the HPP CR that specifies a persistent volume (PVC) template in the `storagePools` stanza according to the following example:
+
[source,yaml]
----
apiVersion: hostpathprovisioner.kubevirt.io/v1beta1
kind: HostPathProvisioner
metadata:
  name: hostpath-provisioner
spec:
  imagePullPolicy: IfNotPresent
  storagePools: <1>
  - name: my-storage-pool
    path: "/var/myvolumes" <2>
    pvcTemplate:
      volumeMode: Block <3>
      storageClassName: my-storage-class <4>
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 5Gi <5>
  workload:
    nodeSelector:
      kubernetes.io/os: linux
----
<1> The `storagePools` stanza is an array that can contain both basic and PVC template storage pools.
<2> Specify the storage pool directories under this node path.
<3> Optional: The `volumeMode` parameter can be either `Block` or `Filesystem` as long as it matches the provisioned volume format. If no value is specified, the default is `Filesystem`. If the `volumeMode` is `Block`, the mounting pod creates an XFS file system on the block volume before mounting it.
<4> If the `storageClassName` parameter is omitted, the default storage class is used to create PVCs. If you omit `storageClassName`, ensure that the HPP storage class is not the default storage class.
<5> You can specify statically or dynamically provisioned storage. In either case, ensure the requested storage size is appropriate for the volume you want to virtually divide or the PVC cannot be bound to the large PV. If the storage class you are using uses dynamically provisioned storage, pick an allocation size that matches the size of a typical request.

. Save the file and exit.

. Create the HPP with a storage pool by running the following command:
+
[source,terminal]
----
$ oc create -f hpp_pvc_template_pool.yaml
----
