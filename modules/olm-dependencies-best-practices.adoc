// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-dependency-resolution.adoc

[id="olm-dependency-best-practices_{context}"]
= Dependency best practices

When specifying dependencies, there are best practices you should consider.

Depend on APIs or a specific version range of Operators::
Operators can add or remove APIs at any time; always specify an `olm.gvk` dependency on any APIs your Operators requires. The exception to this is if you are specifying `olm.package` constraints instead.

Set a minimum version::
The Kubernetes documentation on API changes describes what changes are allowed for Kubernetes-style Operators. These versioning conventions allow an Operator to update an API without bumping the API version, as long as the API is backwards-compatible.
+
For Operator dependencies, this means that knowing the API version of a dependency might not be enough to ensure the dependent Operator works as intended.
+
For example:
+
--
* TestOperator v1.0.0 provides v1alpha1 API version of the `MyObject` resource.
* TestOperator v1.0.1 adds a new field `spec.newfield` to `MyObject`, but still at v1alpha1.
--
+
Your Operator might require the ability to write `spec.newfield` into the `MyObject` resource. An `olm.gvk` constraint alone is not enough for OLM to determine that you need TestOperator v1.0.1 and not TestOperator v1.0.0.
+
Whenever possible, if a specific Operator that provides an API is known ahead of time, specify an additional `olm.package` constraint to set a minimum.

Omit a maximum version or allow a very wide range::
Because Operators provide cluster-scoped resources such as API services and CRDs, an Operator that specifies a small window for a dependency might unnecessarily constrain updates for other consumers of that dependency.
+
Whenever possible, do not set a maximum version. Alternatively, set a very wide semantic range to prevent conflicts with other Operators. For example, `>1.0.0 <2.0.0`.
+
Unlike with conventional package managers, Operator authors explicitly encode that updates are safe through channels in OLM. If an update is available for an existing subscription, it is assumed that the Operator author is indicating that it can update from the previous version. Setting a maximum version for a dependency overrides the update stream of the author by unnecessarily truncating it at a particular upper bound.
+
[NOTE]
====
Cluster administrators cannot override dependencies set by an Operator author.
====
+
However, maximum versions can and should be set if there are known incompatibilities that must be avoided. Specific versions can be omitted with the version range syntax, for example `> 1.0.0 !1.2.1`.
