// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-lvms-operator_{context}"]
= LVMS Operator

New in this release::
* No reference design updates in this release

New in this release::
* Simplified LVMS `deviceSelector` logic

* LVM Storage with `ext4` and `PV` resources

[NOTE]
====
LVMS Operator is an optional component.
====

Description::
The LVMS Operator provides dynamic provisioning of block and file storage.
The LVMS Operator creates logical volumes from local devices that can be used as `PVC` resources by applications.
Volume expansion and snapshots are also possible.
+
The following example configuration creates a `vg1` volume group that leverages all available disks on the node except the installation disk:
+
.StorageLVMCluster.yaml
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: storage-lvmcluster
  namespace: openshift-storage
  annotations:
    ran.openshift.io/ztp-deploy-wave: "10"
spec: {}
  storage:
    deviceClasses:
    - name: vg1
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
----

Limits and requirements::
* In {sno} clusters, persistent storage must be provided  by either LVMS or Local Storage, not both.

Engineering considerations::
* The LVMS Operator is not the reference storage solution for the DU use case.
If you require LVMS Operator for application workloads, the resource use is accounted for against the application cores.

* Ensure that sufficient disks or partitions are available for storage requirements.
