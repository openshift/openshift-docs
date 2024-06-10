// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-cli-parameters_{context}"]
= Listing parameters

The list of parameters that you can override are listed in the `parameters` section of the template.

.Procedure

. You can list parameters with the CLI by using the following command and specifying the file to be used:
+
[source,terminal]
----
$ oc process --parameters -f <filename>
----
+
Alternatively, if the template is already uploaded:
+
[source,terminal]
----
$ oc process --parameters -n <project> <template_name>
----
+
For example, the following shows the output when listing the parameters for one of the quick start templates in the default `openshift` project:
+
[source,terminal]
----
$ oc process --parameters -n openshift rails-postgresql-example
----
+
.Example output
[source,terminal]
----
NAME                         DESCRIPTION                                                                                              GENERATOR           VALUE
SOURCE_REPOSITORY_URL        The URL of the repository with your application source code                                                                  https://github.com/sclorg/rails-ex.git
SOURCE_REPOSITORY_REF        Set this to a branch name, tag or other ref of your repository if you are not using the default branch
CONTEXT_DIR                  Set this to the relative path to your project if it is not in the root of your repository
APPLICATION_DOMAIN           The exposed hostname that will route to the Rails service                                                                    rails-postgresql-example.openshiftapps.com
GITHUB_WEBHOOK_SECRET        A secret string used to configure the GitHub webhook                                                     expression          [a-zA-Z0-9]{40}
SECRET_KEY_BASE              Your secret key for verifying the integrity of signed cookies                                            expression          [a-z0-9]{127}
APPLICATION_USER             The application user that is used within the sample application to authorize access on pages                                 openshift
APPLICATION_PASSWORD         The application password that is used within the sample application to authorize access on pages                             secret
DATABASE_SERVICE_NAME        Database service name                                                                                                        postgresql
POSTGRESQL_USER              database username                                                                                        expression          user[A-Z0-9]{3}
POSTGRESQL_PASSWORD          database password                                                                                        expression          [a-zA-Z0-9]{8}
POSTGRESQL_DATABASE          database name                                                                                                                root
POSTGRESQL_MAX_CONNECTIONS   database max connections                                                                                                     10
POSTGRESQL_SHARED_BUFFERS    database shared buffers                                                                                                      12MB
----
+
The output identifies several parameters that are generated with a regular expression-like generator when the template is processed.
