// Module included in the following assemblies:
//
// * scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed-by-apps.adoc

:_mod-docs-content-type: PROCEDURE
[id="disable-thp_{context}"]
= Disabling Transparent Huge Pages

Transparent Huge Pages (THP) attempt to automate most aspects of creating, managing, and using huge pages. Since THP automatically manages the huge pages, this is not always handled optimally for all types of workloads. THP can lead to performance regressions, since many applications handle huge pages on their own. Therefore, consider disabling THP. The following steps describe how to disable THP using the Node Tuning Operator (NTO).

.Procedure

. Create a file with the following content and name it `thp-disable-tuned.yaml`:
+
[source,yaml]
----
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: thp-workers-profile
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom tuned profile for OpenShift to turn off THP on worker nodes
      include=openshift-node

      [vm]
      transparent_hugepages=never
    name: openshift-thp-never-worker

  recommend:
  - match:
    - label: node-role.kubernetes.io/worker
    priority: 25
    profile: openshift-thp-never-worker
----

. Create the Tuned object:
+
[source,terminal]
----
$ oc create -f thp-disable-tuned.yaml
----

. Check the list of active profiles:
+
[source,terminal]
----
$ oc get profile -n openshift-cluster-node-tuning-operator
----

.Verification

* Log in to one of the nodes and do a regular THP check to verify if the nodes applied the profile successfully:
+
[source,terminal]
----
$ cat /sys/kernel/mm/transparent_hugepage/enabled
----
+
.Example output
[source,terminal]
----
always madvise [never]
----
