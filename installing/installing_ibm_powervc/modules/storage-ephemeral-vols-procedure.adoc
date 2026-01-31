// Module included in the following assemblies:
//
// * storage/generic-ephemeral-vols.adoc
//* microshift_storage/generic-ephemeral-volumes-microshift.adoc


:_mod-docs-content-type: PROCEDURE
[id="generic-ephemeral-vols-procedure_{context}"]
= Creating generic ephemeral volumes

.Procedure

. Create the `pod` object definition and save it to a file.

. Include the generic ephemeral volume information in the file.
+
.my-example-pod-with-generic-vols.yaml
[source, yaml]
----
kind: Pod
apiVersion: v1
metadata:
  name: my-app
spec:
  containers:
    - name: my-frontend
      image: busybox:1.28
      volumeMounts:
      - mountPath: "/mnt/storage"
        name: data
      command: [ "sleep", "1000000" ]
  volumes:
    - name: data <1>
      ephemeral:
        volumeClaimTemplate:
          metadata:
            labels:
              type: my-app-ephvol
          spec:
            accessModes: [ "ReadWriteOnce" ]
ifndef::microshift[]
            storageClassName: "gp2-csi"
endif::microshift[]
ifdef::microshift[]
            storageClassName: "topolvm-provisioner"
endif::microshift[]
            resources:
              requests:
                storage: 1Gi

----
<1> Generic ephemeral volume claim.
