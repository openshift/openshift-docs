:_mod-docs-content-type: ASSEMBLY
[id="enable-cluster-wide-proxy"]
= Configuring the cluster-wide proxy
include::_attributes/common-attributes.adoc[]
:context: config-cluster-wide-proxy

toc::[]

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure {product-title} to use a proxy by xref:../networking/enable-cluster-wide-proxy.adoc#nw-proxy-configure-object_config-cluster-wide-proxy[modifying the Proxy object for existing clusters] or by configuring the proxy settings in the `install-config.yaml` file for new clusters.

== Prerequisites

* Review the xref:../installing/install_config/configuring-firewall.adoc#configuring-firewall[sites that your cluster requires access to] and determine whether any of them must bypass the proxy. By default, all cluster system egress traffic is proxied, including calls to the cloud provider API for the cloud that hosts your cluster. System-wide proxy affects system components only, not user workloads. Add sites to the Proxy object's `spec.noProxy` field to bypass the proxy if necessary.
+
[NOTE]
====
The Proxy object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration with most installation types.

For installations on Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, and {rh-openstack-first}, the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).
====
+
[IMPORTANT]
====
If your installation type does not include setting the `networking.machineNetwork[].cidr` field, you must include the machine IP addresses manually in the `.status.noProxy` field to make sure that the traffic between nodes can bypass the proxy.
====

include::modules/nw-proxy-configure-object.adoc[leveloffset=+1]

include::modules/nw-proxy-remove.adoc[leveloffset=+1]

[discrete]
[role="_additional-resources"]
== Additional resources

* xref:../security/certificates/updating-ca-bundle.adoc#ca-bundle-understanding_updating-ca-bundle[Replacing the CA Bundle certificate]
* xref:../security/certificate_types_descriptions/proxy-certificates.adoc#customization[Proxy certificate customization]
