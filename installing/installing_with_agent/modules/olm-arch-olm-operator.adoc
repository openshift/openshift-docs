// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-olm-operator_{context}"]
= OLM Operator

The OLM Operator is responsible for deploying applications defined by CSV resources after the required resources specified in the CSV are present in the cluster.

The OLM Operator is not concerned with the creation of the required resources; you can choose to manually create these resources using the CLI or using the Catalog Operator. This separation of concern allows users incremental buy-in in terms of how much of the OLM framework they choose to leverage for their application.

The OLM Operator uses the following workflow:

. Watch for cluster service versions (CSVs) in a namespace and check that requirements are met.
. If requirements are met, run the install strategy for the CSV.
+
[NOTE]
====
A CSV must be an active member of an Operator group for the install strategy to run.
====
