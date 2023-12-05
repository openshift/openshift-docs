:_mod-docs-content-type: PROCEDURE
[id="sbo-creating-a-postgresql-database-instance-power-z_{context}"]
= Creating a PostgreSQL database instance

[role="_abstract"]
To create a PostgreSQL database instance, you must create a `Database` custom resource (CR) and configure the database.

.Procedure

. Create the `Database` CR in the `my-petclinic` namespace by running the following command in shell:
+
[source,terminal]
----
$ oc apply -f - << EOD
apiVersion: postgresql.dev4devs.com/v1alpha1
kind: Database
metadata:
  name: sampledatabase
  namespace: my-petclinic
  annotations:
    host: sampledatabase
    type: postgresql
    port: "5432"
    service.binding/database: 'path={.spec.databaseName}'
    service.binding/port: 'path={.metadata.annotations.port}'
    service.binding/password: 'path={.spec.databasePassword}'
    service.binding/username: 'path={.spec.databaseUser}'
    service.binding/type: 'path={.metadata.annotations.type}'
    service.binding/host: 'path={.metadata.annotations.host}'
spec:
  databaseCpu: 30m
  databaseCpuLimit: 60m
  databaseMemoryLimit: 512Mi
  databaseMemoryRequest: 128Mi
  databaseName: "sampledb"
  databaseNameKeyEnvVar: POSTGRESQL_DATABASE
  databasePassword: "samplepwd"
  databasePasswordKeyEnvVar: POSTGRESQL_PASSWORD
  databaseStorageRequest: 1Gi
  databaseUser: "sampleuser"
  databaseUserKeyEnvVar: POSTGRESQL_USER
  image: registry.redhat.io/rhel8/postgresql-13:latest
  databaseStorageClassName: nfs-storage-provisioner
  size: 1
EOD
----
+
The annotations added in this `Database` CR enable the service binding connection and trigger the Operator reconciliation.
+
The output verifies that the database instance is created:
+
.Example output
[source,terminal]
----
database.postgresql.dev4devs.com/sampledatabase created
----

. After you have created the database instance, ensure that all the pods in the `my-petclinic` namespace are running:
+
[source,terminal]
----
$ oc get pods -n my-petclinic
----
+
The output, which takes a few minutes to display, verifies that the database is created and configured:
+
.Example output
[source,terminal]
----
NAME                                     READY    STATUS      RESTARTS   AGE
sampledatabase-cbc655488-74kss            0/1     Running        0       32s
----

After the database is configured, you can deploy the sample application and connect it to the database service.
