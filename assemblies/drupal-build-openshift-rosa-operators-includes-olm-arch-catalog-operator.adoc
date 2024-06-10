// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-catalog-operator_{context}"]
= Catalog Operator

The Catalog Operator is responsible for resolving and installing cluster service versions (CSVs) and the required resources they specify. It is also responsible for watching catalog sources for updates to packages in channels and upgrading them, automatically if desired, to the latest available versions.

To track a package in a channel, you can create a `Subscription` object configuring the desired package, channel, and the `CatalogSource` object you want to use for pulling updates. When updates are found, an appropriate `InstallPlan` object is written into the namespace on behalf of the user.

The Catalog Operator uses the following workflow:

. Connect to each catalog source in the cluster.
. Watch for unresolved install plans created by a user, and if found:
.. Find the CSV matching the name requested and add the CSV as a resolved resource.
.. For each managed or required CRD, add the CRD as a resolved resource.
.. For each required CRD, find the CSV that manages it.
. Watch for resolved install plans and create all of the discovered resources for it, if approved by a user or automatically.
. Watch for catalog sources and subscriptions and create install plans based on them.
