// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-workflow.adoc

[id="olm-upgrades_{context}"]
= Operator installation and upgrade workflow in OLM

In the Operator Lifecycle Manager (OLM) ecosystem, the following resources are used to resolve Operator installations and upgrades:

* `ClusterServiceVersion` (CSV)
* `CatalogSource`
* `Subscription`

Operator metadata, defined in CSVs, can be stored in a collection called a catalog source. OLM uses catalog sources, which use the link:https://github.com/operator-framework/operator-registry[Operator Registry API], to query for available Operators as well as upgrades for installed Operators.

.Catalog source overview
image::olm-catalogsource.png[]

Within a catalog source, Operators are organized into _packages_ and streams of updates called _channels_, which should be a familiar update pattern from {product-title} or other software on a continuous release cycle like web browsers.

.Packages and channels in a Catalog source
image::olm-channels.png[]

A user indicates a particular package and channel in a particular catalog source in a _subscription_, for example an `etcd` package and its `alpha` channel. If a subscription is made to a package that has not yet been installed in the namespace, the latest Operator for that package is installed.

[NOTE]
====
OLM deliberately avoids version comparisons, so the "latest" or "newest" Operator available from a given _catalog_ -> _channel_ -> _package_ path does not necessarily need to be the highest version number. It should be thought of more as the _head_ reference of a channel, similar to a Git repository.
====

Each CSV has a `replaces` parameter that indicates which Operator it replaces. This builds a graph of CSVs that can be queried by OLM, and updates can be shared between channels. Channels can be thought of as entry points into the graph of updates:

.OLM graph of available channel updates
image::olm-replaces.png[]

.Example channels in a package
[source,yaml]
----
packageName: example
channels:
- name: alpha
  currentCSV: example.v0.1.2
- name: beta
  currentCSV: example.v0.1.3
defaultChannel: alpha
----

For OLM to successfully query for updates, given a catalog source, package, channel, and CSV, a catalog must be able to return, unambiguously and deterministically, a single CSV that `replaces` the input CSV.

[id="olm-upgrades-example-upgrade-path_{context}"]
== Example upgrade path

For an example upgrade scenario, consider an installed Operator corresponding to CSV version `0.1.1`. OLM queries the catalog source and detects an upgrade in the subscribed channel with new CSV version `0.1.3` that replaces an older but not-installed CSV version `0.1.2`, which in turn replaces the older and installed CSV version `0.1.1`.

OLM walks back from the channel head to previous versions via the `replaces` field specified in the CSVs to determine the upgrade path `0.1.3` -> `0.1.2` -> `0.1.1`; the direction of the arrow indicates that the former replaces the latter. OLM upgrades the Operator one version at the time until it reaches the channel head.

For this given scenario, OLM installs Operator version `0.1.2` to replace the existing Operator version `0.1.1`. Then, it installs Operator version `0.1.3` to replace the previously installed Operator version `0.1.2`. At this point, the installed operator version `0.1.3` matches the channel head and the upgrade is completed.

[id="olm-upgrades-skipping_{context}"]
== Skipping upgrades

The basic path for upgrades in OLM is:

* A catalog source is updated with one or more updates to an Operator.
* OLM traverses every version of the Operator until reaching the latest version the catalog source contains.

However, sometimes this is not a safe operation to perform. There will be cases where a published version of an Operator should never be installed on a cluster if it has not already, for example because a version introduces a serious vulnerability.

In those cases, OLM must consider two cluster states and provide an update graph that supports both:

* The "bad" intermediate Operator has been seen by the cluster and installed.
* The "bad" intermediate Operator has not yet been installed onto the cluster.

By shipping a new catalog and adding a _skipped_ release, OLM is ensured that it can always get a single unique update regardless of the cluster state and whether it has seen the bad update yet.

.Example CSV with skipped release
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  name: etcdoperator.v0.9.2
  namespace: placeholder
  annotations:
spec:
    displayName: etcd
    description: Etcd Operator
    replaces: etcdoperator.v0.9.0
    skips:
    - etcdoperator.v0.9.1
----

Consider the following example of *Old CatalogSource* and *New CatalogSource*.

.Skipping updates
image::olm-skipping-updates.png[]

This graph maintains that:

* Any Operator found in *Old CatalogSource* has a single replacement in *New CatalogSource*.
* Any Operator found in *New CatalogSource* has a single replacement in *New CatalogSource*.
* If the bad update has not yet been installed, it will never be.

[id="olm-upgrades-replacing-multiple_{context}"]
== Replacing multiple Operators

Creating *New CatalogSource* as described requires publishing CSVs that `replace` one Operator, but can `skip` several. This can be accomplished using the `skipRange` annotation:

[source,yaml]
----
olm.skipRange: <semver_range>
----

where `<semver_range>` has the version range format supported by the link:https://github.com/blang/semver#ranges[semver library].

When searching catalogs for updates, if the head of a channel has a `skipRange` annotation and the currently installed Operator has a version field that falls in the range, OLM updates to the latest entry in the channel.

The order of precedence is:

. Channel head in the source specified by `sourceName` on the subscription, if the other criteria for skipping are met.
. The next Operator that replaces the current one, in the source specified by `sourceName`.
. Channel head in another source that is visible to the subscription, if the other criteria for skipping are met.
. The next Operator that replaces the current one in any source visible to the
subscription.

.Example CSV with `skipRange`
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
    name: elasticsearch-operator.v4.1.2
    namespace: <namespace>
    annotations:
        olm.skipRange: '>=4.1.0 <4.1.2'
----

[id="olm-upgrades-z-stream_{context}"]
== Z-stream support

A _z-stream_, or patch release, must replace all previous z-stream releases for the same minor version. OLM does not consider major, minor, or patch versions, it just needs to build the correct graph in a catalog.

In other words, OLM must be able to take a graph as in *Old CatalogSource* and, similar to before, generate a graph as in *New CatalogSource*:

.Replacing several Operators
image::olm-z-stream.png[]

This graph maintains that:

* Any Operator found in *Old CatalogSource* has a single replacement in *New CatalogSource*.
* Any Operator found in *New CatalogSource* has a single replacement in *New CatalogSource*.
* Any z-stream release in *Old CatalogSource* will update to the latest z-stream release in *New CatalogSource*.
* Unavailable releases can be considered "virtual" graph nodes; their content does not need to exist, the registry just needs to respond as if the graph looks like this.
