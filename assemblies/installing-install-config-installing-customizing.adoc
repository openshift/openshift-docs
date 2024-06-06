:_mod-docs-content-type: ASSEMBLY
[id="installing-customizing"]
= Customizing nodes
include::_attributes/common-attributes.adoc[]
:context: installing-customizing

toc::[]

{product-title} supports both cluster-wide and per-machine configuration via Ignition,
which allows arbitrary partitioning and file content changes to the operating system.
In general, if a configuration file is documented in {op-system-base-full}, then modifying
it via Ignition is supported.

There are two ways to deploy machine config changes:

* Creating machine configs that are included in manifest files
to start up a cluster during `openshift-install`.

* Creating machine configs that are passed to running
{product-title} nodes via the Machine Config Operator.

Additionally, modifying the reference config, such as
the Ignition config that is passed to `coreos-installer` when installing bare-metal nodes
allows per-machine configuration. These changes are currently not visible
to the Machine Config Operator.

The following sections describe features that you might want to
configure on your nodes in this way.

include::modules/installation-special-config-butane.adoc[leveloffset=+1]
include::modules/installation-special-config-butane-about.adoc[leveloffset=+2]
include::modules/installation-special-config-butane-install.adoc[leveloffset=+2]
include::modules/installation-special-config-butane-create.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../installing/install_config/installing-customizing.adoc#installation-special-config-kmod_installing-customizing[Adding kernel modules to nodes]
* xref:../../installing/install_config/installing-customizing.adoc#installation-special-config-storage_installing-customizing[Encrypting and mirroring disks during installation]

include::modules/installation-special-config-kargs.adoc[leveloffset=+1]
ifdef::openshift-webscale[]
include::modules/installation-special-config-rtkernel.adoc[leveloffset=+1]
endif::openshift-webscale[]
include::modules/installation-special-config-kmod.adoc[leveloffset=+1]
include::modules/installation-special-config-storage.adoc[leveloffset=+1]
include::modules/installation-special-config-raid.adoc[leveloffset=+1]
include::modules/installation-special-config-chrony.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

* For information on Butane, see xref:../../installing/install_config/installing-customizing.adoc#installation-special-config-butane_installing-customizing[Creating machine configs with Butane].

ifndef::openshift-origin[]
* For information on FIPS support, see xref:../../installing/installing-fips.adoc#installing-fips[Support for FIPS cryptography].
endif::[]
