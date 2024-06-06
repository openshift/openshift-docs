:_mod-docs-content-type: ASSEMBLY
// Assembly filename:route-configuration.adoc
// Explains route configuration.
[id="route-configuration"]
= Route configuration
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: route-configuration

toc::[]

//Creating an insecure route
include::modules/nw-creating-a-route.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
// Creating a route for router sharding
include::modules/nw-ingress-sharding-route-configuration.adoc[leveloffset=+1]
endif::[]

//Creating route timeouts
include::modules/nw-configuring-route-timeouts.adoc[leveloffset=+1]

//HTTP Strict Transport Security
include::modules/nw-enabling-hsts.adoc[leveloffset=+1]

//Enabling HTTP strict transport security per-route
include::modules/nw-enabling-hsts-per-route.adoc[leveloffset=+2]

//Disabling HTTP strict transport security per-route
include::modules/nw-disabling-hsts.adoc[leveloffset=+2]

ifndef::openshift-rosa,openshift-dedicated[]
//Enforcing HTTP strict transport security per-domain
include::modules/nw-enforcing-hsts-per-domain.adoc[leveloffset=+2]

//Troubleshooting Throughput Issues
include::modules/nw-throughput-troubleshoot.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../nodes/edge/nodes-edge-remote-workers.adoc#nodes-edge-remote-workers-latency[Latency spikes or temporary reduction in throughput to remote workers]


* xref:../../networking/ingress-operator.adoc#nw-ingress-controller-configuration-parameters_configuring-ingress[Ingress Controller configuration
parameters]
endif::[]

//Using cookies to keep route statefulness
include::modules/nw-using-cookies-keep-route-statefulness.adoc[leveloffset=+1]

include::modules/nw-annotating-a-route-with-a-cookie-name.adoc[leveloffset=+2]

include::modules/nw-path-based-routes.adoc[leveloffset=+1]

include::modules/nw-http-header-configuration.adoc[leveloffset=+1]

include::modules/nw-route-set-or-delete-http-headers.adoc[leveloffset=+1]

include::modules/nw-route-specific-annotations.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
include::modules/nw-route-admission-policy.adoc[leveloffset=+1]

include::modules/nw-ingress-creating-a-route-via-an-ingress.adoc[leveloffset=+1]
endif::[]

include::modules/nw-ingress-edge-route-default-certificate.adoc[leveloffset=+1]

include::modules/nw-ingress-reencrypt-route-custom-cert.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
include::modules/nw-router-configuring-dual-stack.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]

[role="_additional-resources"]
.Additional resources

* xref:../../networking/ingress-operator.adoc#configuring-ingress[Specifying an alternative cluster domain using the appsDomain option]
