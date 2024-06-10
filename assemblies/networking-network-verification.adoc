:_mod-docs-content-type: ASSEMBLY
ifdef::openshift-dedicated[]
[id="osd-network-verification_{context}"]
= Network verification for {product-title} clusters
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
[id="rosa-network-verification_{context}"]
= Network verification for ROSA clusters
endif::openshift-rosa[]
include::_attributes/common-attributes.adoc[]
ifdef::openshift-dedicated,openshift-rosa[]
include::_attributes/attributes-openshift-dedicated.adoc[]
endif::[]
:context: network-verification

toc::[]

Network verification checks run automatically when you deploy
ifdef::openshift-dedicated[]
an {product-title}
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
a {product-title} (ROSA)
endif::openshift-rosa[]
cluster into an existing Virtual Private Cloud (VPC) or create an additional machine pool with a subnet that is new to your cluster. The checks validate your network configuration and highlight errors, enabling you to resolve configuration issues prior to deployment.

You can also run the network verification checks manually to validate the configuration for an existing cluster.

include::modules/understanding-network-verification.adoc[leveloffset=+1]

[id="scope-of-the-network-verification-checks_{context}"]
== Scope of the network verification checks

The network verification includes checks for each of the following requirements:

* The parent Virtual Private Cloud (VPC) exists.
* All specified subnets belong to the VPC.
* The VPC has `enableDnsSupport` enabled.
* The VPC has `enableDnsHostnames` enabled.
ifdef::openshift-dedicated[]
* Egress is available to the required domain and port combinations that are specified in the xref:../osd_planning/aws-ccs.adoc#osd-aws-privatelink-firewall-prerequisites_aws-ccs[AWS firewall prerequisites] section.
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
* Egress is available to the required domain and port combinations that are specified in the xref:../rosa_planning/rosa-sts-aws-prereqs.adoc#osd-aws-privatelink-firewall-prerequisites_rosa-sts-aws-prereqs[AWS firewall prerequisites] section.
endif::openshift-rosa[]

include::modules/automatic-network-verification-bypassing.adoc[leveloffset=+1]
ifdef::openshift-dedicated[]
include::modules/running-network-verification-manually-ocm.adoc[leveloffset=+1]
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
include::modules/running-network-verification-manually.adoc[leveloffset=+1]
include::modules/running-network-verification-manually-ocm.adoc[leveloffset=+2]
include::modules/running-network-verification-manually-cli.adoc[leveloffset=+2]
endif::openshift-rosa[]
