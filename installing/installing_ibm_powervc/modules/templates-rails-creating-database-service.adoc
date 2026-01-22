// Module included in the following assemblies:
//  * openshift_images/templates-ruby-on-rails.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-rails-creating-database-service_{context}"]
= Creating the database service

Your Rails application expects a running database service. For this service use PostgreSQL database image.

To create the database service, use the `oc new-app` command. To this command you must pass some necessary environment variables which are used inside the database container. These environment variables are required to set the username, password, and name of the database. You can change the values of these environment variables to anything you would like. The variables are as follows:

* POSTGRESQL_DATABASE
* POSTGRESQL_USER
* POSTGRESQL_PASSWORD

Setting these variables ensures:

* A database exists with the specified name.
* A user exists with the specified name.
* The user can access the specified database with the specified password.

.Procedure

. Create the database service:
+
[source,terminal]
----
$ oc new-app postgresql -e POSTGRESQL_DATABASE=db_name -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password
----
+
To also set the password for the database administrator, append to the previous command with:
+
[source,terminal]
----
-e POSTGRESQL_ADMIN_PASSWORD=admin_pw
----

. Watch the progress:
+
[source,terminal]
----
$ oc get pods --watch
----
