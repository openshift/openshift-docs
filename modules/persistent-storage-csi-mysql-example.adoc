// Module included in the following assemblies
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc


:_mod-docs-content-type: PROCEDURE
[id="csi-example-usage_{context}"]
= Example using the CSI driver

The following example installs a default MySQL template without any
changes to the template.

.Prerequisites

* The CSI driver has been deployed.
* A storage class has been created for dynamic provisioning.

.Procedure

* Create the MySQL template:
+
[source,terminal]
----
# oc new-app mysql-persistent
----
+
.Example output
[source,terminal]
----
--> Deploying template "openshift/mysql-persistent" to project default
...
----
+
[source,terminal]
----
# oc get pvc
----
+
.Example output
[source,terminal]
----
NAME              STATUS    VOLUME                                   CAPACITY
ACCESS MODES   STORAGECLASS   AGE
mysql             Bound     kubernetes-dynamic-pv-3271ffcb4e1811e8   1Gi
RWO            cinder         3s
----
