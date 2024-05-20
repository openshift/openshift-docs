:_mod-docs-content-type: ASSEMBLY
[id="metering-configure-hive-metastore"]
= Configuring the Hive metastore
include::_attributes/common-attributes.adoc[]
:context: metering-configure-hive-metastore

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

Hive metastore is responsible for storing all the metadata about the database tables created in Presto and Hive. By default, the metastore stores this information in a local embedded Derby database in a persistent volume attached to the pod.

Generally, the default configuration of the Hive metastore works for small clusters, but users may wish to improve performance or move storage requirements out of cluster by using a dedicated SQL database for storing the Hive metastore data.

include::modules/metering-configure-persistentvolumes.adoc[leveloffset=+1]

include::modules/metering-use-mysql-or-postgresql-for-hive.adoc[leveloffset=+1]
