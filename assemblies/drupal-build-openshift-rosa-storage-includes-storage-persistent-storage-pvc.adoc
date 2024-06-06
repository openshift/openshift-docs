// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc


[id="persistent-volume-claims_{context}"]
= Persistent volume claims

Each `PersistentVolumeClaim` object contains a `spec` and `status`, which
is the specification and status of the persistent volume claim (PVC), for example:

.`PersistentVolumeClaim` object definition example
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim <1>
spec:
  accessModes:
    - ReadWriteOnce <2>
  resources:
    requests:
      storage: 8Gi <3>
  storageClassName: gold <4>
status:
  ...
----
<1> Name of the PVC.
<2> The access mode, defining the read-write and mount permissions.
<3> The amount of storage available to the PVC.
<4> Name of the `StorageClass` required by the claim.

[id="pvc-storage-class_{context}"]
== Storage classes

Claims can optionally request a specific storage class by specifying the
storage class's name in the `storageClassName` attribute. Only PVs of the
requested class, ones with the same `storageClassName` as the PVC, can be
bound to the PVC. The cluster administrator can configure dynamic
provisioners to service one or more storage classes. The cluster
administrator can create a PV on demand that matches the specifications
in the PVC.

ifndef::microshift,openshift-rosa[]
[IMPORTANT]
====
The Cluster Storage Operator might install a default storage class depending
on the platform in use. This storage class is owned and controlled by the
Operator. It cannot be deleted or modified beyond defining annotations
and labels. If different behavior is desired, you must define a custom
storage class.
====
endif::microshift,openshift-rosa[]
ifdef::openshift-rosa[]
[IMPORTANT]
====
The Cluster Storage Operator installs a default storage class. This storage class is owned and controlled by the Operator. It cannot be deleted or modified beyond defining annotations and labels. If different behavior is desired, you must define a custom storage class.
====
endif::openshift-rosa[]

The cluster administrator can also set a default storage class for all PVCs.
When a default storage class is configured, the PVC must explicitly ask for
`StorageClass` or `storageClassName` annotations set to `""` to be bound
to a PV without a storage class.

[NOTE]
====
If more than one storage class is marked as default, a PVC can only be created if the `storageClassName` is explicitly specified. Therefore, only one storage class should be set as the default.
====

[id="pvc-access-modes_{context}"]
== Access modes

Claims use the same conventions as volumes when requesting storage with
specific access modes.

[id="pvc-resources_{context}"]
== Resources

Claims, such as pods, can request specific quantities of a resource. In
this case, the request is for storage. The same resource model applies to
volumes and claims.

[id="pvc-claims-as-volumes_{context}"]
== Claims as volumes

Pods access storage by using the claim as a volume. Claims must exist in the
same namespace as the pod using the claim. The cluster finds the claim
in the pod's namespace and uses it to get the `PersistentVolume` backing
the claim. The volume is mounted to the host and into the pod, for example:

.Mount volume to the host and into the pod example
[source,yaml]
----
kind: Pod
apiVersion: v1
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: dockerfile/nginx
      volumeMounts:
      - mountPath: "/var/www/html" <1>
        name: mypd <2>
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim <3>
----
<1> Path to mount the volume inside the pod.
<2> Name of the volume to mount. Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged, such as the host `/dev/pts` files. It is safe to mount the host by using `/host`.
<3> Name of the PVC, that exists in the same namespace, to use.
