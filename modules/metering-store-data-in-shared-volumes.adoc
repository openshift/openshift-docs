// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-persistent-storage.adoc

[id="metering-store-data-in-shared-volumes_{context}"]
= Storing data in shared volumes

Metering does not configure storage by default. However, you can use any ReadWriteMany persistent volume (PV) or any storage class that provisions a ReadWriteMany PV for metering storage.

[NOTE]
====
NFS is not recommended to use in production. Using an NFS server on RHEL as a storage back end can fail to meet metering requirements and to provide the performance that is needed for the Metering Operator to work appropriately.

Other NFS implementations on the marketplace might not have these issues, such as a Parallel Network File System (pNFS). pNFS is an NFS implementation with distributed and parallel capability. Contact the individual NFS implementation vendor for more information on any testing that was possibly completed against {product-title} core components.
====

.Procedure

. Modify the `shared-storage.yaml` file to use a ReadWriteMany persistent volume for storage:
+
.Example `shared-storage.yaml` file
--
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: MeteringConfig
metadata:
  name: "operator-metering"
spec:
  storage:
    type: "hive"
    hive:
      type: "sharedPVC"
      sharedPVC:
        claimName: "metering-nfs" <1>
        # Uncomment the lines below to provision a new PVC using the specified storageClass. <2>
        # createPVC: true
        # storageClass: "my-nfs-storage-class"
        # size: 5Gi
----

Select one of the configuration options below:

<1> Set `storage.hive.sharedPVC.claimName` to the name of an existing ReadWriteMany persistent volume claim (PVC). This configuration is necessary if you do not have dynamic volume provisioning or want to have more control over how the persistent volume is created.

<2> Set `storage.hive.sharedPVC.createPVC` to `true` and set the `storage.hive.sharedPVC.storageClass` to the name of a storage class with ReadWriteMany access mode. This configuration uses dynamic volume provisioning to create a volume automatically.
--

.  Create the following resource objects that are required to deploy an NFS server for metering. Use the `oc create -f <file-name>.yaml` command to create the object YAML files.

..  Configure a `PersistentVolume` resource object:
+
.Example `nfs_persistentvolume.yaml` file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs
  labels:
    role: nfs-server
spec:
  capacity:
    storage: 5Gi
  accessModes:
  - ReadWriteMany
  storageClassName: nfs-server <1>
  nfs:
    path: "/"
    server: REPLACEME
  persistentVolumeReclaimPolicy: Delete
----
<1> Must exactly match the `[kind: StorageClass].metadata.name` field value.

..  Configure a `Pod` resource object with the `nfs-server` role:
+
.Example `nfs_server.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: nfs-server
  labels:
    role: nfs-server
spec:
  containers:
    - name: nfs-server
      image: <image_name> <1>
      imagePullPolicy: IfNotPresent
      ports:
        - name: nfs
          containerPort: 2049
      securityContext:
        privileged: true
      volumeMounts:
      - mountPath: "/mnt/data"
        name: local
  volumes:
    - name: local
      emptyDir: {}
----
<1> Install your NFS server image.

..  Configure a `Service` resource object with the `nfs-server` role:
+
.Example `nfs_service.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: nfs-service
  labels:
    role: nfs-server
spec:
  ports:
  - name: 2049-tcp
    port: 2049
    protocol: TCP
    targetPort: 2049
  selector:
    role: nfs-server
  sessionAffinity: None
  type: ClusterIP
----

..  Configure a `StorageClass` resource object:
+
.Example `nfs_storageclass.yaml` file
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: nfs-server <1>
provisioner: example.com/nfs
parameters:
  archiveOnDelete: "false"
reclaimPolicy: Delete
volumeBindingMode: Immediate
----
<1> Must exactly match the `[kind: PersistentVolume].spec.storageClassName` field value.


[WARNING]
====
Configuration of your NFS storage, and any relevant resource objects, will vary depending on the NFS server image that you use for metering storage.
====
