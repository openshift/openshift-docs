:_mod-docs-content-type: ASSEMBLY
[id="configuring-default-certificate"]
= Secured routes
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: secured-routes

toc::[]

Secure routes provide the ability to use several types of TLS termination to serve certificates to the client. The following sections describe how to create re-encrypt, edge, and passthrough routes with custom certificates.

ifndef::openshift-rosa[]
[IMPORTANT]
====
If you create routes in Microsoft Azure through public endpoints, the resource
names are subject to restriction. You cannot create resources that use certain
terms. For a list of terms that Azure restricts, see
link:https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name[Resolve reserved resource name errors]
in the Azure documentation.
====
endif::openshift-rosa[]

include::modules/nw-ingress-creating-a-reencrypt-route-with-a-custom-certificate.adoc[leveloffset=+1]

include::modules/nw-ingress-creating-an-edge-route-with-a-custom-certificate.adoc[leveloffset=+1]

include::modules/nw-ingress-creating-a-passthrough-route.adoc[leveloffset=+1]
