// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-catalog-registry_{context}"]
= Catalog Registry

The Catalog Registry stores CSVs and CRDs for creation in a cluster and stores metadata about packages and channels.

A _package manifest_ is an entry in the Catalog Registry that associates a package identity with sets of CSVs. Within a package, channels point to a particular CSV. Because CSVs explicitly reference the CSV that they replace, a package manifest provides the Catalog Operator with all of the information that is required to update a CSV to the latest version in a channel, stepping through each intermediate version.
