// Module included in the following assemblies:
//
// * operators/admin/olm-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-disabling-copied-csvs_{context}"]
= Disabling copied CSVs

When an Operator is installed by Operator Lifecycle Manager (OLM), a simplified copy of its cluster service version (CSV) is created by default in every namespace that the Operator is configured to watch. These CSVs are known as _copied CSVs_ and communicate to users which controllers are actively reconciling resource events in a given namespace.

When an Operator is configured to use the `AllNamespaces` install mode, versus targeting a single or specified set of namespaces, a copied CSV for the Operator is created in every namespace on the cluster. On especially large clusters, with namespaces and installed Operators potentially in the hundreds or thousands, copied CSVs consume an untenable amount of resources, such as OLM's memory usage, cluster etcd limits, and networking.

To support these larger clusters, cluster administrators can disable copied CSVs for Operators globally installed with the `AllNamespaces` mode.

[NOTE]
====
If you disable copied CSVs, an Operator installed in `AllNamespaces` mode has their CSV copied only to the `openshift` namespace, instead of every namespace on the cluster. In disabled copied CSVs mode, the behavior differs between the web console and CLI:

* In the web console, the default behavior is modified to show copied CSVs from the `openshift` namespace in every namespace, even though the CSVs are not actually copied to every namespace. This allows regular users to still be able to view the details of these Operators in their namespaces and create related custom resources (CRs).
* In the OpenShift CLI (`oc`), regular users can view Operators installed directly in their namespaces by using the `oc get csvs` command, but the copied CSVs from the `openshift` namespace are not visible in their namespaces. Operators affected by this limitation are still available and continue to reconcile events in the user's namespace.
+
To view a full list of installed global Operators, similar to the web console behavior, all authenticated users can run the following command:
+
[source,terminal]
----
$ oc get csvs -n openshift
----
====

.Procedure

* Edit the `OLMConfig` object named `cluster` and set the `spec.features.disableCopiedCSVs` field to `true`:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: operators.coreos.com/v1
kind: OLMConfig
metadata:
  name: cluster
spec:
  features:
    disableCopiedCSVs: true <1>
EOF
----
<1> Disabled copied CSVs for `AllNamespaces` install mode Operators

.Verification

* When copied CSVs are disabled, OLM captures this information in an event in the Operator's namespace:
+
[source,terminal]
----
$ oc get events
----
+
.Example output
[source,terminal]
----
LAST SEEN   TYPE      REASON               OBJECT                                MESSAGE
85s         Warning   DisabledCopiedCSVs   clusterserviceversion/my-csv.v1.0.0   CSV copying disabled for operators/my-csv.v1.0.0
----
+
When the `spec.features.disableCopiedCSVs` field is missing or set to `false`, OLM recreates the copied CSVs for all Operators installed with the `AllNamespaces` mode and deletes the previously mentioned events.
