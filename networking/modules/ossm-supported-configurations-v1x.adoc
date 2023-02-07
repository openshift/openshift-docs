// Module included in the following assemblies:
//
// * service_mesh/v1x/preparing-ossm-install.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * post_installation_configuration/network-configuration.adoc

[id="ossm-supported-configurations-v1x_{context}"]
= {SMProductName} supported configurations

The following are the only supported configurations for the {SMProductName}:

* {product-title} version 4.6 or later.

[NOTE]
====
OpenShift Online and {product-dedicated} are not supported for {SMProductName}.
====

* The deployment must be contained within a single {product-title} cluster that is not federated.
* This release of {SMProductName} is only available on {product-title} x86_64.
* This release only supports configurations where all {SMProductShortName} components are contained in the {product-title} cluster in which it operates. It does not support management of microservices that reside outside of the cluster, or in a multi-cluster scenario.
* This release only supports configurations that do not integrate external services such as virtual machines.

For additional information about {SMProductName} lifecycle and supported configurations, refer to the link:https://access.redhat.com/support/policy/updates/openshift#ossm[Support Policy].

[id="ossm-supported-configurations-kiali_{context}"]
== Supported configurations for Kiali on {SMProductName}

* The Kiali observability console is only supported on the two most recent releases of the Chrome, Edge, Firefox, or Safari browsers.

[id="ossm-supported-configurations-adapters_{context}"]
== Supported Mixer adapters

* This release only supports the following Mixer adapter:
** 3scale Istio Adapter
