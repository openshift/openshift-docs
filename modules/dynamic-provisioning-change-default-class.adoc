// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc
// * microshift_storage/dynamic-provisioning-microshift.adoc


[id="change-default-storage-class_{context}"]
= Changing the default storage class

Use the following procedure to change the default storage class.

For example, if you have two defined storage classes, `gp3` and `standard`, and you want to change the default storage class from `gp3` to `standard`.

.Prerequisites

* Access to the cluster with cluster-admin privileges.

.Procedure

To change the default storage class:

. List the storage classes:
+
[source,terminal]
----
$ oc get storageclass
----
+
.Example output
[source,terminal]
----
NAME                 TYPE
gp3 (default)        kubernetes.io/aws-ebs <1>
standard             kubernetes.io/aws-ebs
----
<1> `(default)` indicates the default storage class.

. Make the desired storage class the default.
+
For the desired storage class, set the `storageclass.kubernetes.io/is-default-class` annotation to `true` by running the following command:
+
[source,terminal]
----
$ oc patch storageclass standard -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
----
+
[NOTE]
====
You can have multiple default storage classes for a short time. However, you should ensure that only one default storage class exists eventually. 

With multiple default storage classes present, any persistent volume claim (PVC) requesting the default storage class (`pvc.spec.storageClassName`=nil) gets the most recently created default storage class, regardless of the default status of that storage class, and the administrator receives an alert in the alerts dashboard that there are multiple default storage classes, `MultipleDefaultStorageClasses`.

// add xref to multi/no default SC module
====

. Remove the default storage class setting from the old default storage class.
+
For the old default storage class, change the value of the `storageclass.kubernetes.io/is-default-class` annotation to `false` by running the following command:
+
[source,terminal]
----
$ oc patch storageclass gp3 -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "false"}}}'
----

. Verify the changes:
+
[source,terminal]
----
$ oc get storageclass
----
+
.Example output
[source,terminal]
----
NAME                 TYPE
gp3                  kubernetes.io/aws-ebs
standard (default)   kubernetes.io/aws-ebs
----
