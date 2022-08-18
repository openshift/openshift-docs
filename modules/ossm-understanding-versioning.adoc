// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc

[id="ossm-versioning_{context}"]
= Understanding versioning

Red Hat uses semantic versioning for product releases. Semantic Versioning is a 3-component number in the format of X.Y.Z, where:

* X stands for a Major version. Major releases usually denote some sort of breaking change: architectural changes, API changes, schema changes, and similar major updates.

* Y stands for a Minor version. Minor releases contain new features and functionality while maintaining backwards compatibility.

* Z stands for a Patch version (also known as a z-stream release). Patch releases are used to addresses Common Vulnerabilities and Exposures (CVEs) and release bug fixes. New features and functionality are generally not released as part of a Patch release.

== How versioning affects Service Mesh upgrades

Depending on the version of the update you are making, the upgrade process is different.

* *Patch updates* - Patch upgrades are managed by the Operator Lifecycle Manager (OLM); they happen automatically when you update your Operators.

* *Minor upgrades* - Minor upgrades require both updating to the most recent {SMProductName} Operator version and manually modifying the `spec.version` value in your `ServiceMeshControlPlane` resources.

* *Major upgrades* - Major upgrades require both updating to the most recent {SMProductName} Operator version and manually modifying the `spec.version` value in your `ServiceMeshControlPlane` resources. Because major upgrades can contain changes that are not backwards compatible, additional manual changes might be required.
