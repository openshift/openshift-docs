// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-rails-writing-application_{context}"]
= Writing your application

If you are starting your Rails application from scratch, you must install the Rails gem first. Then you can proceed with writing your application.

.Procedure

. Install the Rails gem:
+
[source,terminal]
----
$ gem install rails
----
+
.Example output
[source,terminal]
----
Successfully installed rails-4.3.0
1 gem installed
----

. After you install the Rails gem, create a new application with PostgreSQL as your database:
+
[source,terminal]
----
$ rails new rails-app --database=postgresql
----

. Change into your new application directory:
+
[source,terminal]
----
$ cd rails-app
----

. If you already have an application, make sure the `pg` (postgresql) gem is present in your `Gemfile`. If not, edit your `Gemfile` by adding the gem:
+
[source,terminal]
----
gem 'pg'
----

. Generate a new `Gemfile.lock` with all your dependencies:
+
[source,terminal]
----
$ bundle install
----

. In addition to using the `postgresql` database with the `pg` gem, you also must ensure that the `config/database.yml` is using the `postgresql` adapter.
+
Make sure you updated `default` section in the `config/database.yml` file, so it looks like this:
+
[source,yaml]
----
default: &default
  adapter: postgresql
  encoding: unicode
  pool: 5
  host: localhost
  username: rails
  password: <password>
----

. Create your application's development and test databases:
+
[source,terminal]
----
$ rake db:create
----
+
This creates `development` and `test` database in your PostgreSQL server.
