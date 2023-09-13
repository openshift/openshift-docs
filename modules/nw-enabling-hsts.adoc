// Module filename: nw-enabling-hsts.adoc
// Module included in the following assemblies:
// * networking/configuring-routing.adoc

[id="nw-enabling-hsts_{context}"]
= HTTP Strict Transport Security

HTTP Strict Transport Security (HSTS) policy is a security enhancement, which signals to the browser client that only HTTPS traffic is allowed on the route host. HSTS also optimizes web traffic by signaling HTTPS transport is required, without using HTTP redirects. HSTS is useful for speeding up interactions with websites.

When HSTS policy is enforced, HSTS adds a Strict Transport Security header to HTTP and HTTPS responses from the site. You can use the `insecureEdgeTerminationPolicy` value in a route to redirect HTTP to HTTPS. When HSTS is enforced, the client changes all requests from the HTTP URL to HTTPS before the request is sent, eliminating the need for a redirect.

Cluster administrators can configure HSTS to do the following:

* Enable HSTS per-route
* Disable HSTS per-route
* Enforce HSTS per-domain, for a set of domains, or use namespace labels in combination with domains

[IMPORTANT]
====
HSTS works only with secure routes, either edge-terminated or re-encrypt. The configuration is ineffective on HTTP or passthrough routes.
====
