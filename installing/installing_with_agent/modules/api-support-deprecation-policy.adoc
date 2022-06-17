// Module included in the following assemblies:
//
// * rest_api/understanding-api-support-tiers.adoc

[id="api-deprecation-policy_{context}"]
= API deprecation policy

{product-title} is composed of many components sourced from many upstream communities. It is anticipated that the set of components, the associated API interfaces, and correlated features will evolve over time and might require formal deprecation in order to remove the capability.

[id="deprecating-parts-of-the-api_{context}"]
== Deprecating parts of the API

{product-title} is a distributed system where multiple components interact with a shared state managed by the cluster control plane through a set of structured APIs. Per Kubernetes conventions, each API presented by {product-title} is associated with a group identifier and each API group is independently versioned.  Each API group is managed in a distinct upstream community including Kubernetes, Metal3, Multus, Operator Framework, Open Cluster Management, OpenShift itself, and more.

While each upstream community might define their own unique deprecation policy for a given API group and version, Red Hat normalizes the community specific policy to one of the compatibility levels defined prior based on our integration in and awareness of each upstream community to simplify end-user consumption and support.

The deprecation policy and schedule for APIs vary by compatibility level.

The deprecation policy covers all elements of the API including:

* REST resources, also known as API objects
* Fields of REST resources
* Annotations on REST resources, excluding version-specific qualifiers
* Enumerated or constant values

Other than the most recent API version in each group, older API versions must be supported after their announced deprecation for a duration of no less than:

[cols="2",options="header"]
|===
|API tier
|Duration

|Tier 1
|Stable within a major release. They may be deprecated within a major release, but they will not be removed until a subsequent major release.

|Tier 2
|9 months or 3 releases from the announcement of deprecation, whichever is longer.

|Tier 3
|See the component-specific schedule.

|Tier 4
|None. No compatibility is guaranteed.

|===

The following rules apply to all tier 1 APIs:

* API elements can only be removed by incrementing the version of the group.
* API objects must be able to round-trip between API versions without information loss, with the exception of whole REST resources that do not exist in some versions.  In cases where equivalent fields do not exist between versions, data will be preserved in the form of annotations during conversion.
* API versions in a given group can not deprecate until a new API version at least as stable is released, except in cases where the entire API object is being removed.

[id="deprecating-cli-elements_{context}"]
== Deprecating CLI elements

Client-facing CLI commands are not versioned in the same way as the API, but are user-facing component systems. The two major ways a user interacts with a CLI are through a command or flag, which is referred to in this context as CLI elements.

All CLI elements default to API tier 1 unless otherwise noted or the CLI depends on a lower tier API.

[cols="3",options="header"]
|===

|
|Element
|API tier

|Generally available (GA)
|Flags and commands
|Tier 1

|Technology Preview
|Flags and commands
|Tier 3

|Developer Preview
|Flags and commands
|Tier 4

|===

[id="deprecating-entire-component_{context}"]
== Deprecating an entire component

The duration and schedule for deprecating an entire component maps directly to the duration associated with the highest API tier of an API exposed by that component. For example, a component that surfaced APIs with tier 1 and 2 could not be removed until the tier 1 deprecation schedule was met.

[cols="2",options="header"]
|===
|API tier
|Duration

|Tier 1
|Stable within a major release. They may be deprecated within a major release, but they will not be removed until a subsequent major release.

|Tier 2
|9 months or 3 releases from the announcement of deprecation, whichever is longer.

|Tier 3
|See the component-specific schedule.

|Tier 4
|None. No compatibility is guaranteed.

|===
