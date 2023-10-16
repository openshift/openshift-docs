// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-copied-csvs_{context}"]
= Copied CSVs

OLM creates copies of all active member CSVs of an Operator group in each of the target namespaces of that Operator group. The purpose of a copied CSV is to tell users of a target namespace that a specific Operator is configured to watch resources created there.

Copied CSVs have a status reason `Copied` and are updated to match the status of their source CSV. The `olm.targetNamespaces` annotation is stripped from copied CSVs before they are created on the cluster. Omitting the target namespace selection avoids the duplication of target namespaces between tenants.

Copied CSVs are deleted when their source CSV no longer exists or the Operator group that their source CSV belongs to no longer targets the namespace of the copied CSV.

[NOTE]
====
By default, the `disableCopiedCSVs` field is disabled. After enabling a `disableCopiedCSVs` field, the OLM deletes existing copied CSVs on a cluster. When a `disableCopiedCSVs` field is disabled, the OLM adds copied CSVs again.

* Disable the `disableCopiedCSVs` field:
+
[source,yaml]
----
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OLMConfig
metadata:
  name: cluster
spec:
  features:
    disableCopiedCSVs: false
EOF
----

* Enable the `disableCopiedCSVs` field:
+
[source,yaml]
----
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OLMConfig
metadata:
  name: cluster
spec:
  features:
    disableCopiedCSVs: true
EOF
----
====
