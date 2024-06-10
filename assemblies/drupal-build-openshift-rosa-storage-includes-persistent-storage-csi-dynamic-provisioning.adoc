// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc


:_mod-docs-content-type: PROCEDURE
[id="csi-dynamic-provisioning_{context}"]
= Dynamic provisioning

Dynamic provisioning of persistent storage depends on the capabilities of
the CSI driver and underlying storage back end. The provider of the CSI
driver should document how to create a storage class in {product-title} and
the parameters available for configuration.

The created storage class can be configured to enable dynamic provisioning.

.Procedure

* Create a default storage class that ensures all PVCs that do not require
any special storage class are provisioned by the installed CSI driver.
+
[source,shell]
----
# oc create -f - << EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class> <1>
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: <provisioner-name> <2>
parameters:
EOF
----
<1> The name of the storage class that will be created.
<2> The name of the CSI driver that has been installed.
