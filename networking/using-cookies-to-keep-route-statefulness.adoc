:_mod-docs-content-type: ASSEMBLY
[id="using-cookies-to-keep-route-statefulness"]
= Using cookies to keep route statefulness
{product-author}
{product-version}
:data-uri:
:icons:
:experimental:
:toc: macro
:toc-title:
:prewrap!:
:context: using-cookies-to-keep-route-statefulness

toc::[]

{product-title} provides sticky sessions, which enables stateful application
traffic by ensuring all traffic hits the same endpoint. However, if the endpoint
pod terminates, whether through restart, scaling, or a change in configuration,
this statefulness can disappear.

{product-title} can use cookies to configure session persistence. The router
selects an endpoint to handle any user requests, and creates a cookie for the
session. The cookie is passed back in the response to the request and the user
sends the cookie back with the next request in the session. The cookie tells the
router which endpoint is handling the session, ensuring that client requests use
the cookie so that they are routed to the same pod.

include::modules/annotating-a-route-with-a-cookie-name.adoc[leveloffset=+1]
