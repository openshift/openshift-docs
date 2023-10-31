// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-dependency.adoc

:_mod-docs-content-type: CONCEPT

[id="olmv1-dependency-concepts_{context}"]
= Concepts

There are a set of expectations from the user that the package manager should never do the following:

* Install a package whose dependencies can not be fulfilled or that conflict with the dependencies of another package
* Install a package whose constraints can not be met by the current set of installable packages
* Update a package in a way that breaks another that depends on it

[id="olmv1-dependency-example-successful_{context}"]
== Example: Successful resolution

A user wants to install packages A and B that have the following dependencies:

|===
|Package A `v0.1.0`                |Package B `latest`
|↓ (depends on)                    |↓ (depends on)
|Package C `v0.1.0`                |Package D `latest`
|===

Additionally, the user wants to pin the version of A to `v0.1.0`.

*Packages and constraints passed to {olmv1}*

.Packages
* A
* B

.Constraints
* A `v0.1.0` depends on C `v0.1.0`
* A pinned to `v0.1.0`
* B depends on D

.Output
* Resolution set:
** A `v0.1.0`
** B `latest`
** C `v0.1.0`
** D `latest`

[id="olmv1-dependency-example-unsuccessful_{context}"]
== Example: Unsuccessful resolution

A user wants to install packages A and B that have the following dependencies:

|===
|Package A `v0.1.0`                |Package B `latest`
|↓ (depends on)                    |↓ (depends on)
|Package C `v0.1.0`                |Package C `v0.2.0`
|===

Additionally, the user wants to pin the version of A to `v0.1.0`.

*Packages and constraints passed to {olmv1}*

.Packages
* A
* B

.Constraints
* A `v0.1.0` depends on C `v0.1.0`
* A pinned to `v0.1.0`
* B `latest` depends on C `v0.2.0`

.Output
* Resolution set:
** Unable to resolve because A `v0.1.0` requires C `v0.1.0`, which conflicts with B `latest` requiring C `v0.2.0`