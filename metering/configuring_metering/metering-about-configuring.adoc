:_mod-docs-content-type: ASSEMBLY
[id="metering-about-configuring"]
= About configuring metering
include::_attributes/common-attributes.adoc[]
:context: metering-about-configuring

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

The `MeteringConfig` custom resource specifies all the configuration details for your metering installation. When you first install the metering stack, a default `MeteringConfig` custom resource is generated. Use the examples in the documentation to modify this default file. Keep in mind the following key points:

* At a minimum, you need to xref:../../metering/configuring_metering/metering-configure-persistent-storage.adoc#metering-configure-persistent-storage[configure persistent storage] and xref:../../metering/configuring_metering/metering-configure-hive-metastore.adoc#metering-configure-hive-metastore[configure the Hive metastore].

* Most default configuration settings work, but larger deployments or highly customized deployments should review all configuration options carefully.

* Some configuration options can not be modified after installation.

For configuration options that can be modified after installation, make the changes in your `MeteringConfig` custom resource and reapply the file.
