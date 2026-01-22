// Text snippet included in the following modules:
//
// * modules/installation-about-custom-azure-vnet.adoc
// * modules/machine-config-operator.adoc
// * security/certificate_types_descriptions/machine-config-operator-certificates.adoc

:_mod-docs-content-type: SNIPPET

[IMPORTANT]
====
Currently, there is no supported way to block or restrict the machine config server endpoint. The machine config server must be exposed to the network so that newly-provisioned machines, which have no existing configuration or state, are able to fetch their configuration. In this model, the root of trust is the certificate signing requests (CSR) endpoint, which is where the kubelet sends its certificate signing request for approval to join the cluster. Because of this, machine configs should not be used to distribute sensitive information, such as secrets and certificates.

To ensure that the machine config server endpoints, ports 22623 and 22624, are secured in bare metal scenarios, customers must configure proper network policies.
====
