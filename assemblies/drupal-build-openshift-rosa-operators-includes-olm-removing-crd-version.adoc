// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-dependency-resolution-removing-crd-version_{context}"]
= Deprecating or removing a CRD version

Operator Lifecycle Manager (OLM) does not allow a serving version of a custom resource definition (CRD) to be removed right away. Instead, a deprecated version of the CRD must be first disabled by setting the `served` field in the CRD to `false`. Then, the non-serving version can be removed on the subsequent CRD upgrade.

.Procedure

To deprecate and remove a specific version of a CRD:

. Mark the deprecated version as non-serving to indicate this version is no longer in use and may be removed in a subsequent upgrade. For example:
+
[source,yaml]
----
versions:
  - name: v1alpha1
    served: false <1>
    storage: true
----
<1> Set to `false`.

. Switch the `storage` version to a serving version if the version to be deprecated is currently the `storage` version. For example:
+
[source,yaml]
----
versions:
  - name: v1alpha1
    served: false
    storage: false <1>
  - name: v1beta1
    served: true
    storage: true <1>
----
<1> Update the `storage` fields accordingly.
+
[NOTE]
====
To remove a specific version that is or was the `storage` version from a CRD, that version must be removed from the `storedVersion` in the status of the CRD. OLM will attempt to do this for you if it detects a stored version no longer exists in the new CRD.
====

. Upgrade the CRD with the above changes.

. In subsequent upgrade cycles, the non-serving version can be removed completely from the CRD. For example:
+
[source,yaml]
----
versions:
  - name: v1beta1
    served: true
    storage: true
----

. Ensure the referencing CRD version in the `owned` section of your CSV is updated accordingly if that version is removed from the CRD.
