:_mod-docs-content-type: ASSEMBLY
[id="deploying-egress-router-ovn-redirection"]
= Deploying an egress router pod in redirect mode
include::_attributes/common-attributes.adoc[]
:context: deploying-egress-router-ovn-redirection

toc::[]

As a cluster administrator, you can deploy an egress router pod to redirect traffic to specified destination IP addresses from a reserved source IP address.

The egress router implementation uses the egress router Container Network Interface (CNI) plugin.

// Describe the CR and provide an example.
include::modules/nw-egress-router-cr.adoc[leveloffset=+1]

// Deploying an egress router pod in {router-type} mode
include::modules/nw-egress-router-redirect-mode-ovn.adoc[leveloffset=+1]
