:_mod-docs-content-type: ASSEMBLY
:context: cluster-logging-deploying
[id="cluster-logging-deploying"]
= Installing Logging
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]

toc::[]

You can install the {logging-title} by deploying the Red Hat OpenShift Logging Operator. The {logging} Operator creates and manages the components of the logging stack.

[IMPORTANT]
====
For new installations, Vector and LokiStack are recommended. Documentation for logging is in the process of being updated to reflect these underlying component changes.
====

ifdef::openshift-origin[]
[id="prerequisites_cluster-logging-deploying"]
== Prerequisites
* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in _Configuring {product-title} to use Red Hat Operators_.
endif::[]

include::snippets/logging-fluentd-dep-snip.adoc[]

//Installing the Red Hat OpenShift Logging Operator via webconsole
include::modules/cluster-logging-deploy-console.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../logging/log_collection_forwarding/cluster-logging-collector.adoc#cluster-logging-collector[Configuring the logging collector]

include::modules/logging-clo-gui-install.adoc[leveloffset=+1]

include::modules/logging-clo-cli-install.adoc[leveloffset=+1]

include::modules/cluster-logging-deploy-cli.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../operators/admin/olm-adding-operators-to-cluster.adoc#olm-installing-operators-from-operatorhub_olm-adding-operators-to-a-cluster[Installing Operators from the OperatorHub]
* xref:../logging/log_storage/logging-config-es-store.adoc#cluster-logging-removing-unused-components-if-no-elasticsearch_logging-config-es-store[Removing unused components if you do not use the default Elasticsearch log store]

[id="cluster-logging-deploying-postinstallation"]
== Postinstallation tasks

After you have installed the {clo}, you can configure your deployment by creating and modifying a `ClusterLogging` custom resource (CR).

include::modules/cluster-logging-about-crd.adoc[leveloffset=+2]
include::modules/configuring-log-storage-cr.adoc[leveloffset=+2]
include::modules/configuring-logging-collector.adoc[leveloffset=+2]
include::modules/configuring-log-visualizer.adoc[leveloffset=+2]
include::modules/cluster-logging-deploy-multitenant.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

ifdef::openshift-enterprise,openshift-origin[]
* xref:../networking/network_policy/about-network-policy.adoc[About network policy]
* xref:../networking/openshift_sdn/about-openshift-sdn.adoc[About the OpenShift SDN default CNI network provider]
* xref:../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.adoc[About the OVN-Kubernetes default Container Network Interface (CNI) network provider]
endif::[]
ifdef::openshift-rosa,openshift-dedicated[]
* link:https://docs.openshift.com/container-platform/latest/networking/network_policy/about-network-policy.html[About network policy]
* link:https://docs.openshift.com/container-platform/latest/networking/openshift_sdn/about-openshift-sdn.html[About the OpenShift SDN default CNI network provider]
* link:https://docs.openshift.com/container-platform/latest/networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.html[About the OVN-Kubernetes default Container Network Interface (CNI) network provider]
endif::[]
