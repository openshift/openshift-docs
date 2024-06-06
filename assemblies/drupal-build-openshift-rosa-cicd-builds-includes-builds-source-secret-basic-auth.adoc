// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-source-secret-basic-auth_{context}"]
= Creating a secret from source code basic authentication

Basic authentication requires either a combination of `--username` and `--password`, or a token to authenticate against the software configuration management (SCM) server.

.Prerequisites

* User name and password to access the private repository.

.Procedure

. Create the secret first before using the `--username` and `--password` to access the private repository:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --type=kubernetes.io/basic-auth
----
+
. Create a basic authentication secret with a token:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=password=<token> \
    --type=kubernetes.io/basic-auth
----
