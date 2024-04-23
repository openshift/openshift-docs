:_mod-docs-content-type: ASSEMBLY
[id="metering-storage-locations"]
= Storage locations
include::_attributes/common-attributes.adoc[]
:context: metering-storage-locations

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

A `StorageLocation` custom resource configures where data will be stored by the Reporting Operator. This includes the data collected from Prometheus, and the results produced by generating a `Report` custom resource.

You only need to configure a `StorageLocation` custom resource if you want to store data in multiple locations, like multiple S3 buckets or both S3 and HDFS, or if you wish to access a database in Hive and Presto that was not created by metering. For most users this is not a requirement, and the xref:../../metering/configuring_metering/metering-about-configuring.adoc#metering-about-configuring[documentation on configuring metering] is sufficient to configure all necessary storage components.

== Storage location examples

The following example shows the built-in local storage option, and is configured to use Hive. By default, data is stored wherever Hive is configured to use storage, such as HDFS, S3, or a `ReadWriteMany` persistent volume claim (PVC).

.Local storage example
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: StorageLocation
metadata:
  name: hive
  labels:
    operator-metering: "true"
spec:
  hive: <1>
    databaseName: metering <2>
    unmanagedDatabase: false <3>
----

<1> If the `hive` section is present, then the `StorageLocation` resource will be configured to store data in Presto by creating the table using the Hive server. Only `databaseName` and `unmanagedDatabase` are required fields.
<2> The name of the database within hive.
<3> If `true`, the `StorageLocation` resource will not be actively managed, and the `databaseName` is expected to already exist in Hive. If `false`, the Reporting Operator will create the database in Hive.

The following example uses an AWS S3 bucket for storage. The prefix is appended to the bucket name when constructing the path to use.

.Remote storage example
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: StorageLocation
metadata:
  name: example-s3-storage
  labels:
    operator-metering: "true"
spec:
  hive:
    databaseName: example_s3_storage
    unmanagedDatabase: false
    location: "s3a://bucket-name/path/within/bucket" <1>
----
<1> Optional: The filesystem URL for Presto and Hive to use for the database. This can be an `hdfs://` or `s3a://` filesystem URL.

There are additional optional fields that can be specified in the `hive` section:

* `defaultTableProperties`: Contains configuration options for creating tables using Hive.
* `fileFormat`: The file format used for storing files in the filesystem. See the link:https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-StorageFormatsStorageFormatsRowFormat,StorageFormat,andSerDe[Hive Documentation on File Storage Format] for a list of options and more details.
* `rowFormat`: Controls the link:https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-RowFormats&SerDe[ Hive row format]. This controls how Hive serializes and deserializes rows. See the link:https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-RowFormats&SerDe[Hive Documentation on Row Formats and SerDe] for more details.

== Default storage location
If an annotation `storagelocation.metering.openshift.io/is-default` exists and is set to `true` on a `StorageLocation` resource, then that resource becomes the default storage resource.  Any components with a storage configuration option where the storage location is not specified will use the default storage resource. There can be only one default storage resource. If more than one resource with the annotation exists, an error is logged because the Reporting Operator cannot determine the default.

.Default storage example
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: StorageLocation
metadata:
  name: example-s3-storage
  labels:
    operator-metering: "true"
  annotations:
    storagelocation.metering.openshift.io/is-default: "true"
spec:
  hive:
    databaseName: example_s3_storage
    unmanagedDatabase: false
    location: "s3a://bucket-name/path/within/bucket"
----
