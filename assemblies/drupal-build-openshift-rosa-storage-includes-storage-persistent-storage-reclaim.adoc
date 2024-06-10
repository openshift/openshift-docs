// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc


[id="reclaim-policy_{context}"]
= Changing the reclaim policy of a persistent volume

To change the reclaim policy of a persistent volume:

. List the persistent volumes in your cluster:
+
[source,terminal]
----
$ oc get pv
----
+
.Example output
[source,terminal]
----
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
 pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
 pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
 pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim3    manual                     3s
----

. Choose one of your persistent volumes and change its reclaim policy:
+
[source,terminal]
----
$ oc patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
----

+
. Verify that your chosen persistent volume has the right policy:
+
[source,terminal]
----
$ oc get pv
----
+
.Example output
[source,terminal]
----
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
 pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
 pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
 pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Retain          Bound     default/claim3    manual                     3s
----
+
In the preceding output, the volume bound to claim `default/claim3` now has a `Retain` reclaim policy. The volume will not be automatically deleted when a user deletes claim `default/claim3`.
