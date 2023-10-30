// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-an-application-with-a-database.adoc

:_mod-docs-content-type: PROCEDURE
[id="deploying-a-database-in-interactive-mode_{context}"]
= Deploying a database in interactive mode

{odo-title} provides a command-line interactive mode which simplifies deployment.

.Procedure

* Run the interactive mode and answer the prompts:
+
[source,terminal]
----
$ odo service create
----
+
.Example output
[source,terminal]
----
? Which kind of service do you wish to create database
? Which database service class should we use mongodb-persistent
? Enter a value for string property DATABASE_SERVICE_NAME (Database Service Name): mongodb
? Enter a value for string property MEMORY_LIMIT (Memory Limit): 512Mi
? Enter a value for string property MONGODB_DATABASE (MongoDB Database Name): sampledb
? Enter a value for string property MONGODB_VERSION (Version of MongoDB Image): 3.2
? Enter a value for string property VOLUME_CAPACITY (Volume Capacity): 1Gi
? Provide values for non-required properties No
? How should we name your service  mongodb-persistent
? Output the non-interactive version of the selected options No
? Wait for the service to be ready No
 ✓  Creating service [32ms]
 ✓  Service 'mongodb-persistent' was created
Progress of the provisioning will not be reported and might take a long time.
You can see the current status by executing 'odo service list'
----

[NOTE]
====
Your password or username will be passed to the front-end application as environment variables.
====
