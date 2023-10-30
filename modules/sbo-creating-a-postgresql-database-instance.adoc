// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/getting-started-with-service-binding.adoc

:_mod-docs-content-type: PROCEDURE
[id="sbo-creating-a-postgresql-database-instance_{context}"]
= Creating a PostgreSQL database instance

To create a PostgreSQL database instance, you must create a `PostgresCluster` custom resource (CR) and configure the database.

[discrete]
.Procedure

. Create the `PostgresCluster` CR in the `my-petclinic` namespace by running the following command in shell:
+
[source,terminal]
----
$ oc apply -n my-petclinic -f - << EOD
---
apiVersion: postgres-operator.crunchydata.com/v1beta1
kind: PostgresCluster
metadata:
  name: hippo
spec:
  image: registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-14.4-0
  postgresVersion: 14
  instances:
    - name: instance1
      dataVolumeClaimSpec:
        accessModes:
        - "ReadWriteOnce"
        resources:
          requests:
            storage: 1Gi
  backups:
    pgbackrest:
      image: registry.developers.crunchydata.com/crunchydata/crunchy-pgbackrest:ubi8-2.38-0
      repos:
      - name: repo1
        volume:
          volumeClaimSpec:
            accessModes:
            - "ReadWriteOnce"
            resources:
              requests:
                storage: 1Gi
EOD
----
+
The annotations added in this `PostgresCluster` CR enable the service binding connection and trigger the Operator reconciliation.
+
The output verifies that the database instance is created:
+
.Example output
[source,terminal]
----
postgrescluster.postgres-operator.crunchydata.com/hippo created
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
hippo-backup-9rxm-88rzq                   0/1     Completed   0          2m2s
hippo-instance1-6psd-0                    4/4     Running     0          3m28s
hippo-repo-host-0                         2/2     Running     0          3m28s
----
+
After the database is configured, you can deploy the sample application and connect it to the database service.