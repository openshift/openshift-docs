:_mod-docs-content-type: ASSEMBLY
[id="ossm-security"]
= Security
include::_attributes/common-attributes.adoc[]
:context: ossm-security

toc::[]

If your service mesh application is constructed with a complex array of microservices, you can use {SMProductName} to customize the security of the communication between those services. The infrastructure of {product-title} along with the traffic management features of {SMProductShortName} help you manage the complexity of your applications and secure microservices.

.Before you begin

If you have a project, add your project to the xref:../../service_mesh/v2x/ossm-create-mesh.adoc#ossm-member-roll-create_ossm-create-mesh[`ServiceMeshMemberRoll` resource].

If you don't have a project, install the xref:../../service_mesh/v2x/ossm-create-mesh.adoc#ossm-tutorial-bookinfo-overview_ossm-create-mesh[Bookinfo sample application] and add it to the `ServiceMeshMemberRoll` resource. The sample application helps illustrate security concepts.

include::modules/ossm-security-mtls.adoc[leveloffset=+1]

include::modules/ossm-config-sec-mtls-mesh.adoc[leveloffset=+2]

include::modules/ossm-config-sidecar-mtls.adoc[leveloffset=+3]

include::modules/ossm-config-sidecar-out-mtls.adoc[leveloffset=+2]

include::modules/ossm-config-mtls-min-max.adoc[leveloffset=+2]

include::modules/ossm-validate-encryption-kiali.adoc[leveloffset=+2]

include::modules/ossm-security-auth-policy.adoc[leveloffset=+1]

include::modules/ossm-security-cipher.adoc[leveloffset=+1]

include::modules/ossm-configuring-jwks-resolver-ca.adoc[leveloffset=+1]

include::modules/ossm-security-cert-manage.adoc[leveloffset=+1]

include::modules/ossm-cert-manage-add-cert-key.adoc[leveloffset=+1]

include::modules/ossm-cert-manage-verify-cert.adoc[leveloffset=+2]

include::modules/ossm-cert-cleanup.adoc[leveloffset=+1]

include::modules/ossm-cert-manager-integration-istio.adoc[leveloffset=+1]

include::modules/ossm-cert-manager-installation.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_cert-manager-operator-red-hat-openshift"]
== Additional resources

For information about how to install the cert-manager Operator for {product-title}, see:
ifndef::openshift-rosa,openshift-dedicated[]
xref:../../security/cert_manager_operator/cert-manager-operator-install.adoc[Installing the cert-manager Operator for Red Hat OpenShift].
endif::[]
ifdef::openshift-rosa,openshift-dedicated[]
link:https://access.redhat.com/documentation/en-us/openshift_container_platform/4.12/html-single/security_and_compliance/index#cert-manager-operator-install[Installing the cert-manager Operator for Red Hat OpenShift].
endif::[]