:_mod-docs-content-type: ASSEMBLY
[id="preparing-to-install-on-alibaba"]
= Preparing to install on Alibaba Cloud
include::_attributes/common-attributes.adoc[]
:context: preparing-to-install-on-alibaba

toc::[]

:FeatureName: Alibaba Cloud on {product-title}
include::snippets/technology-preview.adoc[]

[id="prerequisites_preparing-to-install-on-alibaba"]
== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].

[id="requirements-for-installing-ocp-on-alibaba"]
== Requirements for installing {product-title} on Alibaba Cloud

Before installing {product-title} on Alibaba Cloud, you must configure and register your domain, create a Resource Access Management (RAM) user for the installation, and review the supported Alibaba Cloud data center regions and zones for the installation.

include::modules/installation-alibaba-dns.adoc[leveloffset=+1]

// include modules/installation-alibaba-limits.adoc[leveloffset=+1]

// include modules/installation-alibaba-ram-user.adoc[leveloffset=+1]

include::modules/installation-alibaba-regions.adoc[leveloffset=+1]

[id="next-steps_preparing-to-install-on-alibaba"]
== Next steps

* xref:../../installing/installing_alibaba/manually-creating-alibaba-ram.adoc#manually-creating-alibaba-ram[Create the required Alibaba Cloud resources].

