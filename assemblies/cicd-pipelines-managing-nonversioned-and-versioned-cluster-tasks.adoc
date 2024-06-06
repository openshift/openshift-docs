:_mod-docs-content-type: ASSEMBLY
[id="managing-nonversioned-and-versioned-cluster-tasks"]
= Managing non-versioned and versioned cluster tasks
include::_attributes/common-attributes.adoc[]
:context: managing-nonversioned-and-versioned-cluster-tasks

toc::[]

As a cluster administrator, installing the {pipelines-title} Operator creates variants of each default cluster task known as _versioned cluster tasks_ (VCT) and _non-versioned cluster tasks_ (NVCT). For example, installing the {pipelines-title} Operator v1.7 creates a `buildah-1-7-0` VCT and a `buildah` NVCT.

Both NVCT and VCT have the same metadata, behavior, and specifications, including `params`, `workspaces`, and `steps`. However, they behave differently when you disable them or upgrade the Operator.

[IMPORTANT]
====
In {pipelines-title} 1.10, cluster task functionality is deprecated and is planned to be removed in a future release.
====

include::modules/op-differences-between-non-versioned-and-versioned-cluster-tasks.adoc[leveloffset=+1]

include::modules/op-advantages-and-disadvantages-of-non-versioned-and-versioned-cluster-tasks.adoc[leveloffset=+1]

include::modules/op-disabling-non-versioned-and-versioned-cluster-tasks.adoc[leveloffset=+1]
