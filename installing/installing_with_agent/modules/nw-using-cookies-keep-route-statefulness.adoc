// Module filename: nw-using-cookies-keep-route-statefulness.adoc
// Use module with the following module:
// nw-annotating-a-route-with-a-cookie-name.adoc
//
// Module included in the following assemblies:
//
// * networking/configuring-routing.adoc
[id="nw-using-cookies-keep-route-statefulness_{context}"]
= Using cookies to keep route statefulness

{product-title} provides sticky sessions, which enables stateful application
traffic by ensuring all traffic hits the same endpoint. However, if the endpoint
pod terminates, whether through restart, scaling, or a change in configuration,
this statefulness can disappear.

{product-title} can use cookies to configure session persistence. The Ingress
controller selects an endpoint to handle any user requests, and creates a cookie
for the session. The cookie is passed back in the response to the request and
the user sends the cookie back with the next request in the session. The cookie
tells the Ingress Controller which endpoint is handling the session, ensuring
that client requests use the cookie so that they are routed to the same pod.

[NOTE]
====
Cookies cannot be set on passthrough routes, because the HTTP traffic cannot be seen. Instead, a number is calculated based on the source IP address, which determines the backend.

If backends change, the traffic can be directed to the wrong server, making it less sticky. If you are using a load balancer, which hides source IP, the same number is set for all connections and traffic is sent to the same pod.
====
