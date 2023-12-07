// Module included in the following assemblies:
// * networking/configuring-routing.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-enabling-hsts-per-route_{context}"]
= Enabling HTTP Strict Transport Security per-route

HTTP strict transport security (HSTS) is implemented in the HAProxy template and applied to edge and re-encrypt routes that have the `haproxy.router.openshift.io/hsts_header` annotation.

.Prerequisites

* You are logged in to the cluster with a user with administrator privileges for the project.
* You installed the `oc` CLI.

.Procedure

* To enable HSTS on a route, add the `haproxy.router.openshift.io/hsts_header` value to the edge-terminated or re-encrypt route. You can use the `oc annotate` tool to do this by running the following command:
+
[source,terminal]
----
$ oc annotate route <route_name> -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=31536000;\ <1>
includeSubDomains;preload"
----
<1> In this example, the maximum age is set to `31536000` ms, which is approximately eight and a half hours.
+
[NOTE]
====
In this example, the equal sign (`=`) is in quotes. This is required to properly execute the annotate command.
====
+
.Example route configured with an annotation
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/hsts_header: max-age=31536000;includeSubDomains;preload <1> <2> <3>
...
spec:
  host: def.abc.com
  tls:
    termination: "reencrypt"
    ...
  wildcardPolicy: "Subdomain"
----
<1> Required. `max-age` measures the length of time, in seconds, that the HSTS policy is in effect. If set to `0`, it negates the policy.
<2> Optional. When included, `includeSubDomains` tells the client
that all subdomains of the host must have the same HSTS policy as the host.
<3> Optional. When `max-age` is greater than 0, you can add `preload` in  `haproxy.router.openshift.io/hsts_header` to allow external services to include this site in their HSTS preload lists. For example, sites such as Google can construct a list of sites that have `preload` set. Browsers can then use these lists to determine which sites they can communicate with over HTTPS, even before they have interacted with the site. Without `preload` set, browsers must have interacted with the site over HTTPS, at least once, to get the header.
