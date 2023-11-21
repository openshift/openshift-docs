:_mod-docs-content-type: ASSEMBLY
[id="k8s-nmstate-troubleshooting-node-network"]
= Troubleshooting node network configuration
include::_attributes/common-attributes.adoc[]
:VirtProductName: OpenShift Container Platform
:context: k8s-nmstate-troubleshooting-node-network

toc::[]

If the node network configuration encounters an issue, the policy is automatically rolled back and the enactments report failure.
This includes issues such as:

* The configuration fails to be applied on the host.
* The host loses connection to the default gateway.
* The host loses connection to the API server.

include::modules/virt-troubleshooting-incorrect-policy-config.adoc[leveloffset=+1]
