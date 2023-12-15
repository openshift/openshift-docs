:_mod-docs-content-type: ASSEMBLY
[id="add-service-serving"]
= Securing service traffic using service serving certificate secrets
include::_attributes/common-attributes.adoc[]
:context: service-serving-certificate

toc::[]

include::modules/customize-certificates-understanding-service-serving.adoc[leveloffset=+1]

include::modules/customize-certificates-add-service-serving.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* You can use a service certificate to configure a secure route using reencrypt TLS termination. For more information, see xref:../../networking/routes/secured-routes.adoc#nw-ingress-creating-a-reencrypt-route-with-a-custom-certificate_secured-routes[Creating a re-encrypt route with a custom certificate].

include::modules/customize-certificates-add-service-serving-configmap.adoc[leveloffset=+1]

include::modules/customize-certificates-add-service-serving-apiservice.adoc[leveloffset=+1]

include::modules/customize-certificates-add-service-serving-crd.adoc[leveloffset=+1]

include::modules/customize-certificates-add-service-serving-mutating-webhook.adoc[leveloffset=+1]

include::modules/customize-certificates-add-service-serving-validating-webhook.adoc[leveloffset=+1]

include::modules/customize-certificates-rotate-service-serving.adoc[leveloffset=+1]

include::modules/customize-certificates-manually-rotate-service-ca.adoc[leveloffset=+1]
