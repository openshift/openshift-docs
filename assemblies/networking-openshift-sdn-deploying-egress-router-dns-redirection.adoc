:_mod-docs-content-type: ASSEMBLY
[id="deploying-egress-router-dns-redirection"]
= Deploying an egress router pod in DNS proxy mode
include::_attributes/common-attributes.adoc[]
:context: deploying-egress-router-dns-redirection

toc::[]

As a cluster administrator, you can deploy an egress router pod configured to proxy traffic to specified DNS names and IP addresses.

include::modules/nw-egress-router-pod.adoc[leveloffset=+1]

include::modules/nw-egress-router-dest-var.adoc[leveloffset=+1]

include::modules/nw-egress-router-dns-mode.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="deploying-egress-router-dns-redirection-additional-resources"]
== Additional resources

* xref:../../networking/openshift_sdn/configuring-egress-router-configmap.adoc#configuring-egress-router-configmap[Configuring an egress router destination mappings with a ConfigMap]
