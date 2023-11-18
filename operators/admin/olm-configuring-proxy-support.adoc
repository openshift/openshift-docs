:_mod-docs-content-type: ASSEMBLY
[id="olm-configuring-proxy-support"]
= Configuring proxy support in Operator Lifecycle Manager
include::_attributes/common-attributes.adoc[]
:context: olm-configuring-proxy-support

toc::[]

If a global proxy is configured on the {product-title} cluster, Operator Lifecycle Manager (OLM) automatically configures Operators that it manages with the cluster-wide proxy. However, you can also configure installed Operators to override the global proxy or inject a custom CA certificate.

[role="_additional-resources"]
.Additional resources

// Configuring the cluster-wide proxy is a different topic in OSD/ROSA.
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../networking/enable-cluster-wide-proxy.adoc#enable-cluster-wide-proxy[Configuring the cluster-wide proxy]
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* xref:../../networking/configuring-cluster-wide-proxy.adoc[Configuring a cluster-wide proxy]
endif::openshift-dedicated,openshift-rosa[]

// This xref points to a topic that is not currently included in the OSD and ROSA docs.
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../networking/configuring-a-custom-pki.adoc#configuring-a-custom-pki[Configuring a custom PKI] (custom CA certificate)
endif::openshift-dedicated,openshift-rosa[]

* Developing Operators that support proxy settings for xref:../../operators/operator_sdk/golang/osdk-golang-tutorial.adoc#osdk-run-proxy_osdk-golang-tutorial[Go], xref:../../operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc#osdk-run-proxy_osdk-ansible-tutorial[Ansible], and xref:../../operators/operator_sdk/helm/osdk-helm-tutorial.adoc#osdk-run-proxy_osdk-helm-tutorial[Helm]


include::modules/olm-overriding-proxy-settings.adoc[leveloffset=+1]
include::modules/olm-injecting-custom-ca.adoc[leveloffset=+1]
