// Module included in the following assemblies:
//
// * virt/storage/virt-preparing-cdi-scratch-space.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-defining-storageclass_{context}"]
= Defining a storage class

You can define the storage class that the Containerized Data Importer (CDI) uses when allocating scratch space by adding the `spec.scratchSpaceStorageClass` field to the `HyperConverged` custom resource (CR).

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Edit the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the `spec.scratchSpaceStorageClass` field to the CR, setting the value to the name of a storage class that exists in the cluster:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  scratchSpaceStorageClass: "<storage_class>" <1>
----
<1> If you do not specify a storage class, CDI uses the storage class of the persistent volume claim that is being populated.

. Save and exit your default editor to update the `HyperConverged` CR.
