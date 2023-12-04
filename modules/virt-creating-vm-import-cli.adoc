// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-container-disks.adoc
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-web-images.adoc

ifeval::["{context}" == "virt-creating-vms-from-web-images"]
:url:
:title-frag: from an image on a web page
:a-object: an image
:object: image
:data-source: web page
endif::[]
ifeval::["{context}" == "virt-creating-vms-from-container-disks"]
:container-disks:
:title-frag: from a container disk
:a-object: a container disk
:object: container disk
:data-source: container registry
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-vm-import-cli_{context}"]
= Creating a VM {title-frag} by using the command line

You can create a virtual machine (VM) {title-frag} by using the command line.

When the virtual machine (VM) is created, the data volume with the {object} is imported into persistent storage.

.Prerequisites

* You must have access credentials for the {data-source} that contains the {object}.

.Procedure

. If the {data-source} requires authentication, create a `Secret` manifest, specifying the credentials, and save it as a `data-source-secret.yaml` file:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: data-source-secret
  labels:
    app: containerized-data-importer
type: Opaque
data:
  accessKeyId: "" <1>
  secretKey:   "" <2>
----
<1> Specify the Base64-encoded key ID or user name.
<2> Specify the Base64-encoded secret key or password.

. Apply the `Secret` manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f data-source-secret.yaml
----

. If the VM must communicate with servers that use self-signed certificates or certificates that are not signed by the system CA bundle, create a config map in the same namespace as the VM:
+
[source,terminal]
----
$ oc create configmap tls-certs <1>
  --from-file=</path/to/file/ca.pem> <2>
----
<1> Specify the config map name.
<2> Specify the path to the CA certificate.

. Edit the `VirtualMachine` manifest and save it as a `vm-fedora-datavolume.yaml` file:
+
[%collapsible]
====
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  creationTimestamp: null
  labels:
    kubevirt.io/vm: vm-fedora-datavolume
  name: vm-fedora-datavolume <1>
spec:
  dataVolumeTemplates:
  - metadata:
      creationTimestamp: null
      name: fedora-dv <2>
    spec:
      storage:
        resources:
          requests:
            storage: 10Gi <3>
        storageClassName: <storage_class> <4>
      source:
ifdef::url[]
        http:
          url: "https://mirror.arizona.edu/fedora/linux/releases/35/Cloud/x86_64/images/Fedora-Cloud-Base-35-1.2.x86_64.qcow2" <5>
endif::[]
ifdef::container-disks[]
        registry:
          url: "docker://kubevirt/fedora-cloud-container-disk-demo:latest" <5>
endif::[]
          secretRef: data-source-secret <6>
          certConfigMap: tls-certs <7>
    status: {}
  running: true
  template:
    metadata:
      creationTimestamp: null
      labels:
        kubevirt.io/vm: vm-fedora-datavolume
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: virtio
            name: datavolumedisk1
        machine:
          type: ""
        resources:
          requests:
            memory: 1.5Gi
      terminationGracePeriodSeconds: 180
      volumes:
      - dataVolume:
          name: fedora-dv
        name: datavolumedisk1
status: {}
----
<1> Specify the name of the VM.
<2> Specify the name of the data volume.
<3> Specify the size of the storage requested for the data volume.
<4> Optional: If you do not specify a storage class, the default storage class is used.
ifdef::url,container-disks[]
<5> Specify the URL of the {data-source}.
endif::[]
<6> Optional: Specify the secret name if you created a secret for the {data-source} access credentials.
<7> Optional: Specify a CA certificate config map.
====

. Create the VM by running the following command:
+
[source,terminal]
----
$ oc create -f vm-fedora-datavolume.yaml
----
+
The `oc create` command creates the data volume and the VM. The CDI controller creates an underlying PVC with the correct annotation and the import process begins. When the import is complete, the data volume status changes to `Succeeded`. You can start the VM.
+
Data volume provisioning happens in the background, so there is no need to monitor the process.

.Verification

. The importer pod downloads the {object} from the specified URL and stores it on the provisioned persistent volume. View the status of the importer pod by running the following command:
+
[source,terminal]
----
$ oc get pods
----

. Monitor the data volume until its status is `Succeeded` by running the following command:
+
[source,terminal]
----
$ oc describe dv fedora-dv <1>
----
<1> Specify the data volume name that you defined in the `VirtualMachine` manifest.

. Verify that provisioning is complete and that the VM has started by accessing its serial console:
+
[source,terminal]
----
$ virtctl console vm-fedora-datavolume
----

ifeval::["{context}" == "creating-vms-from-web-images"]
:!url:
endif::[]
ifeval::["{context}" == "creating-vms-from-container-disks"]
:!container-disks:
endif::[]