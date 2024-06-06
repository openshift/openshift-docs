:_mod-docs-content-type: ASSEMBLY
[id="upgrading-mtc"]
= Upgrading the Migration Toolkit for Containers
include::_attributes/common-attributes.adoc[]
:context: upgrading-mtc
:upgrading-mtc:

toc::[]

You can upgrade the {mtc-full} ({mtc-short}) on {product-title} {product-version} by using Operator Lifecycle Manager.

You can upgrade {mtc-short} on {product-title} 4.5, and earlier versions, by reinstalling the legacy {mtc-full} Operator.

[IMPORTANT]
====
If you are upgrading from {mtc-short} version 1.3, you must perform an additional procedure to update the `MigPlan` custom resource (CR).
====

include::modules/migration-upgrading-mtc-on-ocp-4.adoc[leveloffset=+1]
include::modules/upgrading-mtc-1-8-0.adoc[leveloffset=+1]
include::modules/upgrading-oadp10-to12-in-mtc.adoc[leveloffset=+2]
include::modules/migration-upgrading-mtc-with-legacy-operator.adoc[leveloffset=+1]
include::modules/migration-upgrading-from-mtc-1-3.adoc[leveloffset=+1]
:upgrading-mtc!:
