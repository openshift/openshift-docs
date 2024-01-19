// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-hostpath.adoc

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-hostpath-pod_{context}"]
= Mounting the hostPath share in a privileged pod

After the persistent volume claim has been created, it can be used inside by an application. The following example demonstrates mounting this share inside of a pod.

.Prerequisites
* A persistent volume claim exists that is mapped to the underlying hostPath share.

.Procedure

* Create a privileged pod that mounts the existing persistent volume claim:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: pod-name <1>
spec:
  containers:
    ...
    securityContext:
      privileged: true <2>
    volumeMounts:
    - mountPath: /data <3>
      name: hostpath-privileged
  ...
  securityContext: {}
  volumes:
    - name: hostpath-privileged
      persistentVolumeClaim:
        claimName: task-pvc-volume <4>
----
<1> The name of the pod.
<2> The pod must run as privileged to access the node's storage.
<3> The path to mount the host path share inside the privileged pod. Do not mount to the container root, `/`, or any path that is the same in the host and the container. This can corrupt your host system if the container is sufficiently privileged, such as the host `/dev/pts` files. It is safe to mount the host by using `/host`.
<4> The name of the `PersistentVolumeClaim` object that has been previously created.
