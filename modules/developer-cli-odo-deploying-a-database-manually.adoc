// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-an-application-with-a-database.adoc

[id="deploying-a-database-manually_{context}"]
= Deploying a database manually

. List the available services:
+
[source,terminal]
----
$ odo catalog list services
----
+
.Example output
[source,terminal]
----
NAME                         PLANS
django-psql-persistent       default
jenkins-ephemeral            default
jenkins-pipeline-example     default
mariadb-persistent           default
mongodb-persistent           default
mysql-persistent             default
nodejs-mongo-persistent      default
postgresql-persistent        default
rails-pgsql-persistent       default
----

. Choose the `mongodb-persistent` type of service and see the required parameters:
+
[source,terminal]
----
$ odo catalog describe service mongodb-persistent
----
+
.Example output
[source,terminal]
----
  ***********************        | *****************************************************
  Name                           | default
  -----------------              | -----------------
  Display Name                   |
  -----------------              | -----------------
  Short Description              | Default plan
  -----------------              | -----------------
  Required Params without a      |
  default value                  |
  -----------------              | -----------------
  Required Params with a default | DATABASE_SERVICE_NAME
  value                          | (default: 'mongodb'),
                                 | MEMORY_LIMIT (default:
                                 | '512Mi'), MONGODB_VERSION
                                 | (default: '3.2'),
                                 | MONGODB_DATABASE (default:
                                 | 'sampledb'), VOLUME_CAPACITY
                                 | (default: '1Gi')
  -----------------              | -----------------
  Optional Params                | MONGODB_ADMIN_PASSWORD,
                                 | NAMESPACE, MONGODB_PASSWORD,
                                 | MONGODB_USER
----

. Pass the required parameters as flags and wait for the deployment of the database:
+
[source,terminal]
----
$ odo service create mongodb-persistent --plan default --wait -p DATABASE_SERVICE_NAME=mongodb -p MEMORY_LIMIT=512Mi -p MONGODB_DATABASE=sampledb -p VOLUME_CAPACITY=1Gi
----
