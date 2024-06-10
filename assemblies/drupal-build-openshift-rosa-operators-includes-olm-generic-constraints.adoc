// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-dependency-resolution.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-generic-constraints_{context}"]
= Generic constraints

An `olm.constraint` property declares a dependency constraint of a particular type, differentiating non-constraint and constraint properties. Its `value` field is an object containing a `failureMessage` field holding a string-representation of the constraint message. This message is surfaced as an informative comment to users if the constraint is not satisfiable at runtime.

The following keys denote the available constraint types:

`gvk`:: Type whose value and interpretation is identical to the `olm.gvk` type

`package`:: Type whose value and interpretation is identical to the `olm.package` type

`cel`:: A Common Expression Language (CEL) expression evaluated at runtime by the Operator Lifecycle Manager (OLM) resolver over arbitrary bundle properties and cluster information

`all`, `any`, `not`:: Conjunction, disjunction, and negation constraints, respectively, containing one or more concrete constraints, such as `gvk` or a nested compound constraint

[id="olm-cel_{context}"]
== Common Expression Language (CEL) constraints

The `cel` constraint type supports link:https://github.com/google/cel-go[Common Expression Language (CEL)] as the expression language. The `cel` struct has a `rule` field which contains the CEL expression string that is evaluated against Operator properties at runtime to determine if the Operator satisfies the constraint.

.Example `cel` constraint
[source,yaml]
----
type: olm.constraint
value:
  failureMessage: 'require to have "certified"'
  cel:
    rule: 'properties.exists(p, p.type == "certified")'
----

The CEL syntax supports a wide range of logical operators, such as `AND` and `OR`. As a result, a single CEL expression can have multiple rules for multiple conditions that are linked together by these logical operators. These rules are evaluated against a dataset of multiple different properties from a bundle or any given source, and the output is solved into a single bundle or Operator that satisfies all of those rules within a single constraint.

.Example `cel` constraint with multiple rules
[source,yaml]
----
type: olm.constraint
value:
  failureMessage: 'require to have "certified" and "stable" properties'
  cel:
    rule: 'properties.exists(p, p.type == "certified") && properties.exists(p, p.type == "stable")'
----

[id="olm-compound-constraints_{context}"]
== Compound constraints (all, any, not)

Compound constraint types are evaluated following their logical definitions.

The following is an example of a conjunctive constraint (`all`) of two packages and one GVK. That is, they must all be satisfied by installed bundles:

.Example `all` constraint
[source,yaml]
----
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
    failureMessage: All are required for Red because...
    all:
      constraints:
      - failureMessage: Package blue is needed for...
        package:
          name: blue
          versionRange: '>=1.0.0'
      - failureMessage: GVK Green/v1 is needed for...
        gvk:
          group: greens.example.com
          version: v1
          kind: Green
----

The following is an example of a disjunctive constraint (`any`) of three versions of the same GVK. That is, at least one must be satisfied by installed bundles:

.Example `any` constraint
[source,yaml]
----
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
    failureMessage: Any are required for Red because...
    any:
      constraints:
      - gvk:
          group: blues.example.com
          version: v1beta1
          kind: Blue
      - gvk:
          group: blues.example.com
          version: v1beta2
          kind: Blue
      - gvk:
          group: blues.example.com
          version: v1
          kind: Blue
----

The following is an example of a negation constraint (`not`) of one version of a GVK. That is, this GVK cannot be provided by any bundle in the result set:

.Example `not` constraint
[source,yaml]
----
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
  all:
    constraints:
    - failureMessage: Package blue is needed for...
      package:
        name: blue
        versionRange: '>=1.0.0'
    - failureMessage: Cannot be required for Red because...
      not:
        constraints:
        - gvk:
            group: greens.example.com
            version: v1alpha1
            kind: greens
----

The negation semantics might appear unclear in the `not` constraint context. To clarify, the negation is really instructing the resolver to remove any possible solution that includes a particular GVK, package at a version, or satisfies some child compound constraint from the result set.

As a corollary, the `not` compound constraint should only be used within `all` or `any` constraints, because negating without first selecting a possible set of dependencies does not make sense.

[id="olm-nested-compound_{context}"]
== Nested compound constraints

A nested compound constraint, one that contains at least one child compound constraint along with zero or more simple constraints, is evaluated from the bottom up following the procedures for each previously described constraint type.

The following is an example of a disjunction of conjunctions, where one, the other, or both can satisfy the constraint:

.Example nested compound constraint
[source,yaml]
----
schema: olm.bundle
name: red.v1.0.0
properties:
- type: olm.constraint
  value:
    failureMessage: Required for Red because...
    any:
      constraints:
      - all:
          constraints:
          - package:
              name: blue
              versionRange: '>=1.0.0'
          - gvk:
              group: blues.example.com
              version: v1
              kind: Blue
      - all:
          constraints:
          - package:
              name: blue
              versionRange: '<1.0.0'
          - gvk:
              group: blues.example.com
              version: v1beta1
              kind: Blue
----

[NOTE]
====
The maximum raw size of an `olm.constraint` type is 64KB to limit resource exhaustion attacks.
====
