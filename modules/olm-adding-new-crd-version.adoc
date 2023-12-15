// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-dependency-resolution-adding-new-crd-version_{context}"]
= Adding a new CRD version

.Procedure

To add a new version of a CRD to your Operator:

. Add a new entry in the CRD resource under the `versions` section of your CSV.
+
For example, if the current CRD has a version `v1alpha1` and you want to add a new version `v1beta1` and mark it as the new storage version, add a new entry for `v1beta1`:
+
[source,yaml]
----
versions:
  - name: v1alpha1
    served: true
    storage: false
  - name: v1beta1 <1>
    served: true
    storage: true
----
<1> New entry.

. Ensure the referencing version of the CRD in the `owned` section of your CSV is updated if the CSV intends to use the new version:
+
[source,yaml]
----
customresourcedefinitions:
  owned:
  - name: cluster.example.com
    version: v1beta1 <1>
    kind: cluster
    displayName: Cluster
----
<1> Update the `version`.

. Push the updated CRD and CSV to your bundle.
