// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-cli-generating-list-of-objects_{context}"]
= Generating a list of objects

Using the CLI, you can process a file defining a template to return the list of objects to standard output.

.Procedure

. Process a file defining a template to return the list of objects to standard output:
+
[source,terminal]
----
$ oc process -f <filename>
----
+
Alternatively, if the template has already been uploaded to the current project:
+
[source,terminal]
----
$ oc process <template_name>
----
+
. Create objects from a template by processing the template and piping the output to `oc create`:
+
[source,terminal]
----
$ oc process -f <filename> | oc create -f -
----
+
Alternatively, if the template has already been uploaded to the current project:
+
[source,terminal]
----
$ oc process <template> | oc create -f -
----
+
. You can override any parameter values defined in the file by adding the `-p` option for each `<name>=<value>` pair you want to override. A parameter reference appears in any text field inside the template items.
+
For example, in the following the `POSTGRESQL_USER` and `POSTGRESQL_DATABASE` parameters of a template are overridden to output a configuration with customized environment variables:
+
.. Creating a List of objects from a template
+
[source,terminal]
----
$ oc process -f my-rails-postgresql \
    -p POSTGRESQL_USER=bob \
    -p POSTGRESQL_DATABASE=mydatabase
----
+
.. The JSON file can either be redirected to a file or applied directly without uploading the template by piping the processed output to the `oc create` command:
+
[source,terminal]
----
$ oc process -f my-rails-postgresql \
    -p POSTGRESQL_USER=bob \
    -p POSTGRESQL_DATABASE=mydatabase \
    | oc create -f -
----
+
.. If you have large number of parameters, you can store them in a file and then pass this file to `oc process`:
+
[source,terminal]
----
$ cat postgres.env
POSTGRESQL_USER=bob
POSTGRESQL_DATABASE=mydatabase
----
+
[source,terminal]
----
$ oc process -f my-rails-postgresql --param-file=postgres.env
----
+
.. You can also read the environment from standard input by using `"-"` as the argument to `--param-file`:
+
[source,terminal]
----
$ sed s/bob/alice/ postgres.env | oc process -f my-rails-postgresql --param-file=-
----
