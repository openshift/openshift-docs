// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-hive-metastore.adoc

[id="metering-configure-persistentvolumes_{context}"]
= Configuring persistent volumes

By default, Hive requires one persistent volume to operate.

`hive-metastore-db-data` is the main persistent volume claim (PVC) required by default. This PVC is used by the Hive metastore to store metadata about tables, such as table name, columns, and location. Hive metastore is used by Presto and the Hive server to look up table metadata when processing queries. You remove this requirement by using MySQL or PostgreSQL for the Hive metastore database.

To install, Hive metastore requires that dynamic volume provisioning is enabled in a storage class, a persistent volume of the correct size must be manually pre-created, or you use a pre-existing MySQL or PostgreSQL database.

[id="metering-configure-persistentvolumes-storage-class-hive_{context}"]
== Configuring the storage class for the Hive metastore
To configure and specify a storage class for the `hive-metastore-db-data` persistent volume claim, specify the storage class in your `MeteringConfig` custom resource. An example `storage` section with the `class` field is included in the `metastore-storage.yaml` file below.

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: MeteringConfig
metadata:
  name: "operator-metering"
spec:
  hive:
    spec:
      metastore:
        storage:
          # Default is null, which means using the default storage class if it exists.
          # If you wish to use a different storage class, specify it here
          # class: "null" <1>
          size: "5Gi"
----
<1> Uncomment this line and replace `null` with the name of the storage class to use. Leaving the value `null` will cause metering to use the default storage class for the cluster.

[id="metering-configure-persistentvolumes-volume-size-hive_{context}"]
== Configuring the volume size for the Hive metastore

Use the `metastore-storage.yaml` file below as a template to configure the volume size for the Hive metastore.

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: MeteringConfig
metadata:
  name: "operator-metering"
spec:
  hive:
    spec:
      metastore:
        storage:
          # Default is null, which means using the default storage class if it exists.
          # If you wish to use a different storage class, specify it here
          # class: "null"
          size: "5Gi" <1>
----
<1> Replace the value for `size` with your desired capacity. The example file shows "5Gi".
