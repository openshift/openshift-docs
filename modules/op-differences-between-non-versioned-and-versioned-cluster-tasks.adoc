// This module is part of the following assembly:
//
// *cicd/pipelines/managing-nonversioned-and-versioned-cluster-tasks.adoc
:_mod-docs-content-type: CONCEPT
[id="differences-between-non-versioned-and-versioned-cluster-tasks_{context}"]
= Differences between non-versioned and versioned cluster tasks

Non-versioned and versioned cluster tasks have different naming conventions. And, the {pipelines-title} Operator upgrades them differently.

.Differences between non-versioned and versioned cluster tasks
[options="header"]
|===

| | Non-versioned cluster task | Versioned cluster task

| Nomenclature
| The NVCT only contains the name of the cluster task. For example, the name of the NVCT of Buildah installed with Operator v1.7 is `buildah`.
| The VCT contains the name of the cluster task, followed by the version as a suffix. For example, the name of the VCT of Buildah installed with Operator v1.7 is `buildah-1-7-0`.

| Upgrade
| When you upgrade the Operator, it updates the non-versioned cluster task with the latest changes. The name of the NVCT remains unchanged.
| Upgrading the Operator installs the latest version of the VCT and retains the earlier version. The latest version of a VCT corresponds to the upgraded Operator. For example, installing Operator 1.7 installs `buildah-1-7-0` and retains `buildah-1-6-0`.

|===