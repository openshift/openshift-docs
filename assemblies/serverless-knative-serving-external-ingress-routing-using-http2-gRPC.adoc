:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="using-http2-gRPC_{context}"]
= Using HTTP2 and gRPC
:context: using-http2-gRPC

{ServerlessProductName} supports only insecure or edge-terminated routes. Insecure or edge-terminated routes do not support HTTP2 on {product-title}. These routes also do not support gRPC because gRPC is transported by HTTP2. If you use these protocols in your application, you must call the application using the ingress gateway directly. To do this you must find the ingress gateway's public address and the application's specific host.

include::modules/interacting-serverless-apps-http2-gRPC.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../networking/ingress-operator.adoc#nw-http2-haproxy_configuring-ingress[Enabling HTTP/2 Ingress connectivity]

include::modules/interacting-serverless-apps-http2-gRPC-up-to-4-9.adoc[leveloffset=+1]
