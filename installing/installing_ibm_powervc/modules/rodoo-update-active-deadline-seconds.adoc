// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-install.adoc

:_mod-docs-content-type: PROCEDURE
[id="rodoo-update-active-deadline-seconds_{context}"]
= Updating the run-once active deadline override value

You can customize the override value that the {run-once-operator} applies to run-once pods. The predefined value is `3600` seconds, or 1 hour.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed the {run-once-operator}.

.Procedure

. Log in to the OpenShift CLI.

. Edit the `RunOnceDurationOverride` resource:
+
[source,terminal]
----
$ oc edit runoncedurationoverride cluster
----

. Update the `activeDeadlineSeconds` field:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: RunOnceDurationOverride
metadata:
# ...
spec:
  runOnceDurationOverride:
    spec:
      activeDeadlineSeconds: 1800 <1>
# ...
----
<1> Set the `activeDeadlineSeconds` field to the desired value, in seconds.

. Save the file to apply the changes.

Any future run-once pods created in namespaces where the run-once duration override is enabled will have their `activeDeadlineSeconds` field set to this new value. Existing run-once pods in these namespaces will receive this new value when they are updated.
