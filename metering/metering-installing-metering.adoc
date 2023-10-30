:_mod-docs-content-type: ASSEMBLY
[id="installing-metering"]
= Installing metering
include::_attributes/common-attributes.adoc[]
:context: installing-metering

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

Review the following sections before installing metering into your cluster.

To get started installing metering, first install the Metering Operator from OperatorHub. Next, configure your instance of metering by creating a `MeteringConfig` custom resource (CR). Installing the Metering Operator creates a default `MeteringConfig` resource that you can modify using the examples in the documentation. After creating your `MeteringConfig` resource, install the metering stack. Last, verify your installation.

include::modules/metering-install-prerequisites.adoc[leveloffset=+1]

include::modules/metering-install-operator.adoc[leveloffset=+1]

// Including this content directly in the assembly because the workflow requires linking off to the config docs, and we don't current link
// inside of modules - klamenzo 2019-09-23
[id="metering-install-metering-stack_{context}"]
== Installing the metering stack

After adding the Metering Operator to your cluster you can install the components of metering by installing the metering stack.

== Prerequisites

* Review the xref:../metering/configuring_metering/metering-about-configuring.adoc#metering-about-configuring[configuration options]
* Create a `MeteringConfig` resource. You can begin the following process to generate a default `MeteringConfig` resource, then use the examples in the documentation to modify this default file for your specific installation. Review the following topics to create your `MeteringConfig` resource:
** For configuration options, review xref:../metering/configuring_metering/metering-about-configuring.adoc#metering-about-configuring[About configuring metering].
** At a minimum, you need to xref:../metering/configuring_metering/metering-configure-persistent-storage.adoc#metering-configure-persistent-storage[configure persistent storage] and xref:../metering/configuring_metering/metering-configure-hive-metastore.adoc#metering-configure-hive-metastore[configure the Hive metastore].

[IMPORTANT]
====
There can only be one `MeteringConfig` resource in the `openshift-metering` namespace. Any other configuration is not supported.
====

.Procedure

. From the web console, ensure you are on the *Operator Details* page for the Metering Operator in the `openshift-metering` project. You can navigate to this page by clicking *Operators* -> *Installed Operators*, then selecting the Metering Operator.

. Under *Provided APIs*, click *Create Instance* on the Metering Configuration card. This opens a YAML editor with the default `MeteringConfig` resource file where you can define your configuration.
+
[NOTE]
====
For example configuration files and all supported configuration options, review the xref:../metering/configuring_metering/metering-about-configuring.adoc#metering-about-configuring[configuring metering documentation].
====

. Enter your `MeteringConfig` resource into the YAML editor and click *Create*.

The `MeteringConfig` resource begins to create the necessary resources for your metering stack. You can now move on to verifying your installation.

include::modules/metering-install-verify.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="metering-install-additional-resources_{context}"]
== Additional resources

* For more information on configuration steps and available storage platforms, see xref:../metering/configuring_metering/metering-configure-persistent-storage.adoc#metering-configure-persistent-storage[Configuring persistent storage].

* For the steps to configure Hive, see xref:../metering/configuring_metering/metering-configure-hive-metastore.adoc#metering-configure-hive-metastore[Configuring the Hive metastore].
