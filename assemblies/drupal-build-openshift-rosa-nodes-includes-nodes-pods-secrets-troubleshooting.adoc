// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-troubleshooting_{context}"]
= Troubleshooting secrets

If a service certificate generation fails with (service's
`service.beta.openshift.io/serving-cert-generation-error` annotation
contains):

[source,terminal]
----
secret/ssl-key references serviceUID 62ad25ca-d703-11e6-9d6f-0e9c0057b608, which does not match 77b6dd80-d716-11e6-9d6f-0e9c0057b60
----

The service that generated the certificate no longer exists, or has a different
`serviceUID`. You must force certificates regeneration by removing the old
secret, and clearing the following annotations on the service
`service.beta.openshift.io/serving-cert-generation-error`,
`service.beta.openshift.io/serving-cert-generation-error-num`:

. Delete the secret:
+
[source,terminal]
----
$ oc delete secret <secret_name>
----

. Clear the annotations:
+
[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-
----
+
[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-num-
----

[NOTE]
====
The command removing annotation has a `-` after the annotation name to be
removed.
====
