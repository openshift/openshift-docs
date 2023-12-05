// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

:_mod-docs-content-type: PROCEDURE
[id="lvms-upgrading-lvms-on-sno_{context}"]
= Upgrading {lvms} on {sno} clusters

You can upgrade the {lvms-first} Operator to ensure compatibility with your {sno} version.

.Prerequisites

* You have upgraded your {sno} cluster.

* You have installed a previous version of the {lvms} Operator.

* You have installed the OpenShift CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Update the `Subscription` resource for the {lvms} Operator by running the following command:
+
[source,terminal]
----
$ oc patch subscription lvms-operator -n openshift-storage --type merge --patch '{"spec":{"channel":"<update-channel>"}}' <1>
----
<1> Replace `<update-channel>` with the version of the {lvms} Operator that you want to install, for example `stable-{product-version}`.

. View the upgrade events to check that the installation is complete by running the following command:
+
[source,terminal]
----
$ oc get events -n openshift-storage
----
+
.Example output
[source,terminal, subs="attributes"]
----
...
8m13s       Normal    RequirementsUnknown   clusterserviceversion/lvms-operator.v{product-version}   requirements not yet checked
8m11s       Normal    RequirementsNotMet    clusterserviceversion/lvms-operator.v{product-version}   one or more requirements couldn't be found
7m50s       Normal    AllRequirementsMet    clusterserviceversion/lvms-operator.v{product-version}   all requirements found, attempting install
7m50s       Normal    InstallSucceeded      clusterserviceversion/lvms-operator.v{product-version}   waiting for install components to report healthy
7m49s       Normal    InstallWaiting        clusterserviceversion/lvms-operator.v{product-version}   installing: waiting for deployment lvms-operator to become ready: deployment "lvms-operator" waiting for 1 outdated replica(s) to be terminated
7m39s       Normal    InstallSucceeded      clusterserviceversion/lvms-operator.v{product-version}   install strategy completed with no errors
...
----

.Verification

* Verify the version of the {lvms} Operator by running the following command:
+
[source,terminal]
----
$ oc get subscription lvms-operator -n openshift-storage -o jsonpath='{.status.installedCSV}'
----
+
.Example output
[source,terminal, subs="attributes"]
----
lvms-operator.v{product-version}
----