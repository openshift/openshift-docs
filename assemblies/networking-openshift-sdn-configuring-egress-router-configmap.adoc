:_mod-docs-content-type: ASSEMBLY
[id="configuring-egress-router-configmap"]
= Configuring an egress router pod destination list from a config map
include::_attributes/common-attributes.adoc[]
:context: configuring-egress-router-configmap

toc::[]

As a cluster administrator, you can define a `ConfigMap` object that specifies destination mappings for an egress router pod. The specific format of the configuration depends on the type of egress router pod. For details on the format, refer to the documentation for the specific egress router pod.

include::modules/nw-egress-router-configmap.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="configuring-egress-router-configmap-additional-resources"]
== Additional resources

* xref:../../networking/openshift_sdn/deploying-egress-router-layer3-redirection.adoc#nw-egress-router-dest-var_deploying-egress-router-layer3-redirection[Redirect mode]
* xref:../../networking/openshift_sdn/deploying-egress-router-http-redirection.adoc#nw-egress-router-dest-var_deploying-egress-router-http-redirection[HTTP proxy mode]
* xref:../../networking/openshift_sdn/deploying-egress-router-dns-redirection.adoc#nw-egress-router-dest-var_deploying-egress-router-dns-redirection[DNS proxy mode]
