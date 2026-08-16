:_mod-docs-content-type: ASSEMBLY
[id="olm-config"]
= Configuring Operator Lifecycle Manager features
include::_attributes/common-attributes.adoc[]
:context: olm-config

toc::[]

The Operator Lifecycle Manager (OLM) controller is configured by an `OLMConfig` custom resource (CR) named `cluster`. Cluster administrators can modify this resource to enable or disable certain features.

This document outlines the features currently supported by OLM that are configured by the `OLMConfig` resource.

include::modules/olm-disabling-copied-csvs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../operators/understanding/olm/olm-understanding-operatorgroups.adoc#olm-operatorgroups-membership_olm-understanding-operatorgroups[Install modes]
