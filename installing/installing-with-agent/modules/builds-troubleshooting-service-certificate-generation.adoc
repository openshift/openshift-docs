// Module included in the following assemblies:
//
// *builds/troubleshooting-builds.adoc

[id="builds-troubleshooting-service-certificate-generation_{context}"]
= Service certificate generation failure

If your request for access to resources is denied:

Issue::
If a service certificate generation fails with (service's `service.beta.openshift.io/serving-cert-generation-error` annotation contains):

.Example output
[source,terminal]
----
secret/ssl-key references serviceUID 62ad25ca-d703-11e6-9d6f-0e9c0057b608, which does not match 77b6dd80-d716-11e6-9d6f-0e9c0057b60
----

Resolution::
The service that generated the certificate no longer exists, or has a different `serviceUID`. You must force certificates regeneration by removing the old secret, and clearing the following annotations on the service: `service.beta.openshift.io/serving-cert-generation-error` and `service.beta.openshift.io/serving-cert-generation-error-num`:

[source,terminal]
----
$ oc delete secret <secret_name>
----

[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-
----

[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-num-
----

[NOTE]
====
The command removing annotation has a `-` after the annotation name to be
removed.
====
