:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-ossm-setup"]
= Integrating {SMProductShortName} with {ServerlessProductName}
:context: serverless-ossm-setup

toc::[]

The {ServerlessOperatorName} provides Kourier as the default ingress for Knative. However, you can use {SMProductShortName} with {ServerlessProductName} whether Kourier is enabled or not. Integrating with Kourier disabled allows you to configure additional networking and routing options that the Kourier ingress does not support, such as mTLS functionality.

[IMPORTANT]
====
{ServerlessProductName} only supports the use of {SMProductName} functionality that is explicitly documented in this guide, and does not support other undocumented features.
====

[id="prerequsites_serverless-ossm-setup"]
== Prerequisites

* The examples in the following procedures use the domain `example.com`. The example certificate for this domain is used as a certificate authority (CA) that signs the subdomain certificate.
+
To complete and verify these procedures in your deployment, you need either a certificate signed by a widely trusted public CA or a CA provided by your organization. Example commands must be adjusted according to your domain, subdomain, and CA.

* You must configure the wildcard certificate to match the domain of your {product-title} cluster. For example, if your {product-title} console address is `https://console-openshift-console.apps.openshift.example.com`, you must configure the wildcard certificate so that the domain is `*.apps.openshift.example.com`. For more information about configuring wildcard certificates, see the following topic about _Creating a certificate to encrypt incoming external traffic_.

* If you want to use any domain name, including those which are not subdomains of the default {product-title} cluster domain, you must set up domain mapping for those domains. For more information, see the {ServerlessProductName} documentation about xref:../../serverless/knative-serving/config-custom-domains/create-domain-mapping.adoc#serverless-create-domain-mapping_create-domain-mapping[Creating a custom domain mapping].

include::modules/serverless-ossm-external-certs.adoc[leveloffset=+1]
// without kourier
include::modules/serverless-ossm-setup.adoc[leveloffset=+1]
include::modules/serverless-ossm-enabling-serving-metrics.adoc[leveloffset=+1]
// With kourier
include::modules/serverless-ossm-setup-with-kourier.adoc[leveloffset=+1]
include::modules/serverless-ossm-secret-filtering-net-istio.adoc[leveloffset=+1]
