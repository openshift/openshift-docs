// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-rails-setting-up-database_{context}"]
= Setting up the database

Rails applications are almost always used with a database. For local development use the PostgreSQL database.

.Procedure

. Install the database:
+
[source,terminal]
----
$ sudo yum install -y postgresql postgresql-server postgresql-devel
----

. Initialize the database:
+
[source,terminal]
----
$ sudo postgresql-setup initdb
----
+
This command creates the `/var/lib/pgsql/data` directory, in which the data is stored.

. Start the database:
+
[source,terminal]
----
$ sudo systemctl start postgresql.service
----

. When the database is running, create your `rails` user:
+
[source,terminal]
----
$ sudo -u postgres createuser -s rails
----
+
Note that the user created has no password.
