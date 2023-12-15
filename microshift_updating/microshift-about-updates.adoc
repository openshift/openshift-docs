:_mod-docs-content-type: ASSEMBLY
[id="microshift-about-updates"]
=  About {product-title} updates
include::_attributes/attributes-microshift.adoc[]
:context: microshift-about-updates

toc::[]

Upgrades are supported on {product-title} beginning with the General Availability version 4.14. Supported upgrades include those from one minor version to the next in sequence, for example, from 4.14 to 4.15. Patch updates are also supported from z-stream to z-stream, for example 4.14.1 to 4.14.2.

[id="microshift-about-updates-understanding-microshift-updates_{context}"]
== Understanding {microshift-short} updates
{product-title} updates are supported on both `rpm-ostree` edge-deployed hosts and non-OSTree hosts. You can complete updates using the following methods:

* Embed the latest version of {microshift-short} in a new `rpm-ostree` system image such as {op-system-ostree-first}. See * xref:../microshift_updating/microshift-update-rpms-ostree.adoc#microshift-update-rpms-ostree[Applying updates on an OSTree system]
* Manually update the RPMs on a non-OSTree system such as {op-system-base-full}. See * xref:../microshift_updating/microshift-update-rpms-manually.adoc#microshift-update-rpms-manually[Applying updates manually with RPMs]

[NOTE]
====
Only `rpm-ostree` updates include automatic rollbacks.
====

[id="microshift-about-updates-rpm-ostree-updates_{context}"]
=== RPM OSTree updates
Using the {op-system-ostree} `rpm-ostree` update path allows for automated backup and system rollback in case any part of the update fails. You must build a new `rpm-ostree` image and embed the new {microshift-short} version in that image. The `rpm-ostree` image can be the same version or an updated version, but the versions of {op-system-ostree} and {microshift-short} must be compatible.

Check following compatibility table for details:

include::snippets/microshift-rhde-compatibility-table-snip.adoc[leveloffset=+1]

[id="microshift-about-updates-rpm-updates_{context}"]
=== Manual RPM updates
You can use the manual RPM update path to replace your existing version of {microshift-short}. The versions of {op-system} and {microshift-short} must be compatible. Ensuring system health and completing additional system backups are manual processes.

[id="microshift-about-updates-checking-version-update-path_{context}"]
== Checking version update path
Before attempting an update of either {op-system-bundle} component, determine which versions of {microshift-short} and {op-system-ostree} or {op-system} you have installed. Plan for the versions of each that you intend to use.

*{product-title} update paths*

* Generally Available Version 4.14 to 4.14.z on {op-system-ostree} 9.2
* Generally Available Version 4.14 to 4.14.z on {op-system} 9.2