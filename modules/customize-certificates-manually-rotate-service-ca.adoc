// Module included in the following assemblies:
//
// * authentication/certificates/service-signing-certificates.adoc

:_mod-docs-content-type: PROCEDURE
[id="manually-rotate-service-ca_{context}"]
= Manually rotate the service CA certificate

The service CA is valid for 26 months and is automatically refreshed when there is less than 13 months validity left.

If necessary, you can manually refresh the service CA by using the following procedure.

[WARNING]
====
A manually-rotated service CA does not maintain trust with the previous service CA. You might experience a temporary service disruption until the pods in the cluster are restarted, which ensures that pods are using service serving certificates issued by the new service CA.
====

.Prerequisites

* You must be logged in as a cluster admin.

.Procedure

. View the expiration date of the current service CA certificate by
using the following command.
+
[source,terminal]
----
$ oc get secrets/signing-key -n openshift-service-ca \
     -o template='{{index .data "tls.crt"}}' \
     | base64 --decode \
     | openssl x509 -noout -enddate
----

. Manually rotate the service CA. This process generates a new service CA
which will be used to sign the new service certificates.
+
[source,terminal]
----
$ oc delete secret/signing-key -n openshift-service-ca
----

. To apply the new certificates to all services, restart all the pods
in your cluster. This command ensures that all services use the
updated certificates.
+
[source,terminal]
----
$ for I in $(oc get ns -o jsonpath='{range .items[*]} {.metadata.name}{"\n"} {end}'); \
      do oc delete pods --all -n $I; \
      sleep 1; \
      done
----
+
[WARNING]
====
This command will cause a service interruption, as it goes through and
deletes every running pod in every namespace. These pods will automatically
restart after they are deleted.
====
