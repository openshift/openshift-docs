// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-sc-manage.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-csi-sc-managing_{context}"]
= Managing the default storage class using the web console

.Prerequisites
* Access to the {product-title} web console.

* Access to the cluster with cluster-admin privileges.

.Procedure

To manage the default storage class using the web console:

. Log in to the web console.

. Click *Administration* > *CustomResourceDefinitions*.

. On the *CustomResourceDefinitions* page, type `clustercsidriver` to find the `ClusterCSIDriver` object.

. Click *ClusterCSIDriver*, and then click the *Instances* tab.

. Click the name of the desired instance, and then click the *YAML* tab.

. Add the `spec.storageClassState` field with a value of `Managed`, `Unmanaged`, or `Removed`.
+
.Example
[source, yaml]
----
...
spec:
  driverConfig:
    driverType: ''
  logLevel: Normal
  managementState: Managed
  observedConfig: null
  operatorLogLevel: Normal
  storageClassState: Unmanaged <1>
...
----
<1> `spec.storageClassState` field set to "Unmanaged"

. Click *Save*.