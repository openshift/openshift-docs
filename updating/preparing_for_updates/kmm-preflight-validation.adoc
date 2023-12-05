:_mod-docs-content-type: ASSEMBLY
[id="kmm-preflight-validation"]
= Preflight validation for Kernel Module Management (KMM) Modules
include::_attributes/common-attributes.adoc[]
:context: kmm-preflight-validation

toc::[]

////
WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.
////

Before performing an upgrade on the cluster with applied KMM modules, the administrator must verify that kernel modules installed using KMM are able to be installed on the nodes after the cluster upgrade and possible kernel upgrade. Preflight attempts to validate every `Module` loaded in the cluster, in parallel. Preflight does not wait for validation of one `Module` to complete before starting validation of another `Module`.

:FeatureName: Kernel Module Management Operator Preflight validation

include::modules/kmm-validation-kickoff.adoc[leveloffset=+1]
include::modules/kmm-validation-lifecycle.adoc[leveloffset=+1]
include::modules/kmm-validation-status.adoc[leveloffset=+1]
include::modules/kmm-preflight-validation-stages-per-module.adoc[leveloffset=+1]
include::modules/kmm-image-validation-stage.adoc[leveloffset=+2]
include::modules/kmm-build-validation-stage.adoc[leveloffset=+2]
include::modules/kmm-sign-validation-stage.adoc[leveloffset=+2]
include::modules/kmm-example-cr.adoc[leveloffset=+1]
