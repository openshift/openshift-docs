:_mod-docs-content-type: ASSEMBLY
[id="cert-types-monitoring-and-cluster-logging-operator-component-certificates"]
= Monitoring and OpenShift Logging Operator component certificates
include::_attributes/common-attributes.adoc[]
:context: cert-types-monitoring-and-cluster-logging-operator-component-certificates

toc::[]

== Expiration

Monitoring components secure their traffic with service CA certificates. These certificates are valid for 2 years and are replaced automatically on rotation of the service CA, which is every 13 months.

If the certificate lives in the `openshift-monitoring` or `openshift-logging` namespace, it is system managed and rotated automatically.

== Management

These certificates are managed by the system and not the user.
