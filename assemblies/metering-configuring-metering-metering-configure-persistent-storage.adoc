:_mod-docs-content-type: ASSEMBLY
[id="metering-configure-persistent-storage"]
= Configuring persistent storage
include::_attributes/common-attributes.adoc[]
:context: metering-configure-persistent-storage

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

Metering requires persistent storage to persist data collected by the Metering Operator and to store the results of reports. A number of different storage providers and storage formats are supported. Select your storage provider and modify the example configuration files to configure persistent storage for your metering installation.

include::modules/metering-store-data-in-s3.adoc[leveloffset=+1]

include::modules/metering-store-data-in-s3-compatible.adoc[leveloffset=+1]

include::modules/metering-store-data-in-azure.adoc[leveloffset=+1]

include::modules/metering-store-data-in-gcp.adoc[leveloffset=+1]

include::modules/metering-store-data-in-shared-volumes.adoc[leveloffset=+1]
