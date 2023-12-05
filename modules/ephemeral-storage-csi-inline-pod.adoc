// Module included in the following assemblies:
//
// * storage/container_storage_interface/ephemeral-storage-csi-inline-pod-scheduling.adoc

:_mod-docs-content-type: PROCEDURE
[id="ephemeral-storage-csi-inline-pod_{context}"]
= Embedding a CSI inline ephemeral volume in the pod specification

You can embed a CSI inline ephemeral volume in the `Pod` specification in {product-title}. At runtime, nested inline volumes follow the ephemeral lifecycle of their associated pods so that the CSI driver handles all phases of volume operations as pods are created and destroyed.

.Procedure

. Create the `Pod` object definition and save it to a file.

. Embed the CSI inline ephemeral volume in the file.
+
.my-csi-app.yaml
[source,yaml]
----
kind: Pod
apiVersion: v1
metadata:
  name: my-csi-app
spec:
  containers:
    - name: my-frontend
      image: busybox
      volumeMounts:
      - mountPath: "/data"
        name: my-csi-inline-vol
      command: [ "sleep", "1000000" ]
  volumes: <1>
    - name: my-csi-inline-vol
      csi:
        driver: inline.storage.kubernetes.io
        volumeAttributes:
          foo: bar
----
<1> The name of the volume that is used by pods.

. Create the object definition file that you saved in the previous step.
+
[source,terminal]
----
$ oc create -f my-csi-app.yaml
----
