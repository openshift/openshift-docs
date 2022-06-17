// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-dependency-resolution.adoc

[id="olm-dependency-resolution-examples_{context}"]
= Example dependency resolution scenarios

In the following examples, a _provider_ is an Operator which "owns" a CRD or API service.

[discrete]
=== Example: Deprecating dependent APIs

A and B are APIs (CRDs):

* The provider of A depends on B.
* The provider of B has a subscription.
* The provider of B updates to provide C but deprecates B.

This results in:

* B no longer has a provider.
* A no longer works.

This is a case OLM prevents with its upgrade strategy.

[discrete]
=== Example: Version deadlock

A and B are APIs:

* The provider of A requires B.
* The provider of B requires A.
* The provider of A updates to (provide A2, require B2) and deprecate A.
* The provider of B updates to (provide B2, require A2) and deprecate B.

If OLM attempts to update A without simultaneously updating B, or vice-versa, it is unable to progress to new versions of the Operators, even though a new compatible set can be found.

This is another case OLM prevents with its upgrade strategy.
