// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-a-java-application-with-a-database

:_mod-docs-content-type: PROCEDURE
[id="connecting-a-java-application-to-a-database_{context}"]
= Connecting a Java application to a database

To connect your Java application to the database, use the `odo link` command.

.Procedure

. Display the list of services:
+
[source,terminal]
----
$ odo service list
----
+
.Example output
[source,terminal]
----
NAME                        AGE
Database/sampledatabase     6m31s
----

. Connect the database to your application:
+
[source,terminal]
----
$ odo link Database/sampledatabase
----

. Push the changes to your cluster:
+
[source,terminal]
----
$ odo push
----
+
After the link has been created and pushed, a secret that contains the database connection data is created.

. Check the component for values injected from the database service:
+
[source,sh]
----
$ odo exec -- bash -c 'env | grep DATABASE'
declare -x DATABASE_CLUSTERIP="10.106.182.173"
declare -x DATABASE_DB_NAME="sampledb"
declare -x DATABASE_DB_PASSWORD="samplepwd"
declare -x DATABASE_DB_USER="sampleuser"
----

. Open the URL of your Java application and navigate to the `CreatePerson.xhtml` data entry page. Enter a username and age by using the form. Click *Save*.
+
Note that now you can see the data in the database by clicking the *View Persons Record List* link.
+
You can also use a CLI tool such as `psql` to manipulate the database.
