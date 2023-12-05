// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-lvms-using_{context}"]
= Using the LVMS

The LVMS `StorageClass` is deployed with a default `StorageClass`. Any `PersistentVolumeClaim` objects without a `.spec.storageClassName` defined automatically has a `PersistentVolume` provisioned from the default `StorageClass`. Use the following procedure to provision and mount a logical volume to a pod.

.Procedure

* To provision and mount a logical volume to a pod, run the following command:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: my-lv-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1G
---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx
    image: nginx
    command: ["/usr/bin/sh", "-c"]
    args: ["sleep", "1h"]
    volumeMounts:
    - mountPath: /mnt
      name: my-volume
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
          - ALL
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
  volumes:
    - name: my-volume
      persistentVolumeClaim:
        claimName: my-lv-pvc
EOF
----
