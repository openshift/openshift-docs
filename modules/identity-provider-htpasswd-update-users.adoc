// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

:_mod-docs-content-type: PROCEDURE
[id="identity-provider-htpasswd-update-users_{context}"]
= Updating users for an htpasswd identity provider

You can add or remove users from an existing htpasswd identity provider.

.Prerequisites

* You have created a `Secret` object that contains the htpasswd user file. This procedure assumes that it is named `htpass-secret`.
* You have configured an htpasswd identity provider. This procedure assumes that it is named `my_htpasswd_provider`.
* You have access to the `htpasswd` utility. On Red Hat Enterprise Linux this is available by installing the `httpd-tools` package.
* You have cluster administrator privileges.

.Procedure

. Retrieve the htpasswd file from the `htpass-secret` `Secret` object and save the file to your file system:
+
[source,terminal]
----
$ oc get secret htpass-secret -ojsonpath={.data.htpasswd} -n openshift-config | base64 --decode > users.htpasswd
----

. Add or remove users from the `users.htpasswd` file.

** To add a new user:
+
[source,terminal]
----
$ htpasswd -bB users.htpasswd <username> <password>
----
+
.Example output
[source,terminal]
----
Adding password for user <username>
----

** To remove an existing user:
+
[source,terminal]
----
$ htpasswd -D users.htpasswd <username>
----
+
.Example output
[source,terminal]
----
Deleting password for user <username>
----

. Replace the `htpass-secret` `Secret` object with the updated users in the `users.htpasswd` file:
+
[source,terminal]
----
$ oc create secret generic htpass-secret --from-file=htpasswd=users.htpasswd --dry-run=client -o yaml -n openshift-config | oc replace -f -
----
+
[TIP]
====
You can alternatively apply the following YAML to replace the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: htpass-secret
  namespace: openshift-config
type: Opaque
data:
  htpasswd: <base64_encoded_htpasswd_file_contents>
----
====

. If you removed one or more users, you must additionally remove existing resources for each user.

.. Delete the `User` object:
+
[source,terminal]
----
$ oc delete user <username>
----
+
.Example output
[source,terminal]
----
user.user.openshift.io "<username>" deleted
----
+
Be sure to remove the user, otherwise the user can continue using their token as long as it has not expired.

.. Delete the `Identity` object for the user:
+
[source,terminal]
----
$ oc delete identity my_htpasswd_provider:<username>
----
+
.Example output
[source,terminal]
----
identity.user.openshift.io "my_htpasswd_provider:<username>" deleted
----
