// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-a-multicomponent-application-with-odo.adoc
// * cli_reference/developer_cli_odo/creating_and_deploying_applications_with_odo/creating-an-application-with-a-database.adoc

[id="Connecting-the-database-to-the-front-end-application_{context}"]
= Connecting the database to the front-end application

. Link the database to the front-end service:
+
[source,terminal]
----
$ odo link mongodb-persistent
----
+
.Example output
[source,terminal]
----
 ✓  Service mongodb-persistent has been successfully linked from the component nodejs-nodejs-ex-mhbb

Following environment variables were added to nodejs-nodejs-ex-mhbb component:
- database_name
- password
- uri
- username
- admin_password
----

. See the environment variables of the application and the database in the pod:

.. Get the pod name:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                READY     STATUS    RESTARTS   AGE
mongodb-1-gsznc                     1/1       Running   0          28m
nodejs-nodejs-ex-mhbb-app-4-vkn9l   1/1       Running   0          1m
----

.. Connect to the pod:
+
[source,terminal]
----
$ oc rsh nodejs-nodejs-ex-mhbb-app-4-vkn9l
----

.. Check the environment variables:
+
[source,terminal]
----
sh-4.2$ env
----
+
.Example output
[source,terminal]
----
uri=mongodb://172.30.126.3:27017
password=dHIOpYneSkX3rTLn
database_name=sampledb
username=user43U
admin_password=NCn41tqmx7RIqmfv
----

. Open the URL in the browser and notice the database configuration in the bottom right:
+
[source,terminal]
----
$ odo url list
----
+
.Example output
[source,terminal]
----
Request information
Page view count: 24

DB Connection Info:
Type:	MongoDB
URL:	mongodb://172.30.126.3:27017/sampledb
----
