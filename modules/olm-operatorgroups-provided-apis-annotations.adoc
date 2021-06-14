// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-provided-apis-annotation_{context}"]
= Provided APIs annotation

A _group/version/kind (GVK)_ is a unique identifier for a Kubernetes API. Information about what GVKs are provided by an Operator group are shown in an `olm.providedAPIs` annotation. The value of the annotation is a string consisting of `<kind>.<version>.<group>` delimited with commas. The GVKs of CRDs and API services provided by all active member CSVs of an Operator group are included.

Review the following example of an `OperatorGroup` object with a single active member CSV that provides the `PackageManifest` resource:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  annotations:
    olm.providedAPIs: PackageManifest.v1alpha1.packages.apps.redhat.com
  name: olm-operators
  namespace: local
  ...
spec:
  selector: {}
  serviceAccount:
    metadata:
      creationTimestamp: null
  targetNamespaces:
  - local
status:
  lastUpdated: 2019-02-19T16:18:28Z
  namespaces:
  - local
----
