// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-profiles.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-scheduler-profiles-configuring_{context}"]
= Configuring a scheduler profile

You can configure the scheduler to use a scheduler profile.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `Scheduler` object:
+
[source,terminal]
----
$ oc edit scheduler cluster
----

. Specify the profile to use in the `spec.profile` field:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
#...
spec:
  mastersSchedulable: false
  profile: HighNodeUtilization <1>
#...
----
<1> Set to `LowNodeUtilization`, `HighNodeUtilization`, or `NoScoring`.

. Save the file to apply the changes.
