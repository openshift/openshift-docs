// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-csv-bundle-files_{context}"]
= Generated files and resources

The `make bundle` command creates the following files and directories in your Operator project:

* A bundle manifests directory named `bundle/manifests` that contains a `ClusterServiceVersion` (CSV) object
* A bundle metadata directory named `bundle/metadata`
* All custom resource definitions (CRDs) in a `config/crd` directory
* A Dockerfile `bundle.Dockerfile`

The following resources are typically included in a CSV:

Role:: Defines Operator permissions within a namespace.
ClusterRole:: Defines cluster-wide Operator permissions.
Deployment:: Defines how an Operand of an Operator is run in pods.
CustomResourceDefinition (CRD):: Defines custom resources that your Operator reconciles.
Custom resource examples:: Examples of resources adhering to the spec of a particular CRD.
