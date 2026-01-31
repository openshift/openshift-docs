// Module included in the following assemblies:
// * openshift_images/templates-ruby-on-rails.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-rails-configuring-application_{context}"]
= Configuring application for {product-title}

To have your application communicate with the PostgreSQL database service running in {product-title} you must edit the `default` section in your `config/database.yml` to use environment variables, which you must define later, upon the database service creation.

.Procedure

* Edit the `default` section in your `config/database.yml` with pre-defined variables as follows:
+
.Sample `config/database` YAML file
[source,eruby]
----
<% user = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? "root" : ENV["POSTGRESQL_USER"] %>
<% password = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? ENV["POSTGRESQL_ADMIN_PASSWORD"] : ENV["POSTGRESQL_PASSWORD"] %>
<% db_service = ENV.fetch("DATABASE_SERVICE_NAME","").upcase %>

default: &default
  adapter: postgresql
  encoding: unicode
  # For details on connection pooling, see rails configuration guide
  # http://guides.rubyonrails.org/configuring.html#database-pooling
  pool: <%= ENV["POSTGRESQL_MAX_CONNECTIONS"] || 5 %>
  username: <%= user %>
  password: <%= password %>
  host: <%= ENV["#{db_service}_SERVICE_HOST"] %>
  port: <%= ENV["#{db_service}_SERVICE_PORT"] %>
  database: <%= ENV["POSTGRESQL_DATABASE"] %>
----
