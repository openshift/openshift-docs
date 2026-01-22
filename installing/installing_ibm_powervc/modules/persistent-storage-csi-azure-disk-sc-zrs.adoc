//
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-azure.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="persistent-storage-csi-azure-disk-sc-zrs_{context}"]
= Creating a storage class with storage account type


Storage classes are used to differentiate and delineate storage levels and usages. By defining a storage class, you can obtain dynamically provisioned persistent volumes.

When creating a storage class, you can designate the storage account type. This corresponds to your Azure storage account SKU tier. Valid options are `Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS`, `UltraSSD_LRS`, `Premium_ZRS`, and `StandardSSD_ZRS`. For information about finding your Azure SKU tier, see link:https://learn.microsoft.com/en-us/rest/api/storagerp/srp_sku_types[SKU Types].

ZRS has some region limitations. For information about these limitations, see link:https://learn.microsoft.com/en-us/azure/virtual-machines/disks-deploy-zrs?tabs=portal#limitations[ZRS limitations].

Both ZRS and PremiumV2_LRS have some region limitations. For information about these limitations, see link:https://learn.microsoft.com/en-us/azure/virtual-machines/disks-deploy-zrs?tabs=portal#limitations[ZRS limitations] and link:https://learn.microsoft.com/en-us/azure/virtual-machines/disks-deploy-premium-v2?tabs=azure-cli#limitations[Premium_LRS limitations].

.Prerequisites

* Access to an {product-title} cluster with administrator rights

.Procedure

Use the following steps to create a storage class with a storage account type.

. Create a storage class designating the storage account type using a YAML file similar to the following:
+
[source,terminal]
--
$ oc create -f - << EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class> <1>
provisioner: disk.csi.azure.com
parameters:
  skuName: <storage-class-account-type> <2>
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
EOF
--
<1> Storage class name.
<2> Storage account type. This corresponds to your Azure storage account SKU tier:`Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS`, `UltraSSD_LRS`, `Premium_ZRS`, `StandardSSD_ZRS`, `PremiumV2_LRS`.
+
[NOTE]
====
For PremiumV2_LRS, specify `cachingMode: None` in `storageclass.parameters`.
====

. Ensure that the storage class was created by listing the storage classes:
+
[source,terminal]
--
$ oc get storageclass
--
+
[source,terminal]
.Example output
--
$ oc get storageclass
NAME                    PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
azurefile-csi           file.csi.azure.com   Delete          Immediate              true                   68m
managed-csi (default)   disk.csi.azure.com   Delete          WaitForFirstConsumer   true                   68m
sc-prem-zrs             disk.csi.azure.com   Delete          WaitForFirstConsumer   true                   4m25s <1>
--
<1> New storage class with storage account type.
