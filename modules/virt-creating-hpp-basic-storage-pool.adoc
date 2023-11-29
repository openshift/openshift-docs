// Module included in the following assemblies:
//
// * virt/storage/virt-configuring-local-storage-with-hpp.adoc
// * virt/post_installation_configuration/virt-post-install-storage-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-hpp-basic-storage-pool_{context}"]
= Creating a hostpath provisioner with a basic storage pool

You configure a hostpath provisioner (HPP) with a basic storage pool by creating an HPP custom resource (CR) with a `storagePools` stanza. The storage pool specifies the name and path used by the CSI driver.

[IMPORTANT]
====
Do not create storage pools in the same partition as the operating system. Otherwise, the operating system partition might become filled to capacity, which will impact performance or cause the node to become unstable or unusable.
====

.Prerequisites

* The directories specified in `spec.storagePools.path` must have read/write access.

.Procedure

. Create an `hpp_cr.yaml` file with a `storagePools` stanza as in the following example:
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
  - name: any_name
    path: "/var/myvolumes" <2>
workload:
  nodeSelector:
    kubernetes.io/os: linux
----
<1> The `storagePools` stanza is an array to which you can add multiple entries.
<2> Specify the storage pool directories under this node path.

. Save the file and exit.

. Create the HPP by running the following command:
+
[source,terminal]
----
$ oc create -f hpp_cr.yaml
----
