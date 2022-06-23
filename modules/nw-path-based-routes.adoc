// Module filename: nw-path-based-routes.adoc
// Module included in the following assemblies:
// * networking/routes/route-configuration.adoc

[id="nw-path-based-routes_{context}"]
= Path-based routes

Path-based routes specify a path component that can be compared against a URL, which requires that the traffic for the route be HTTP based. Thus, multiple routes can be served using the same hostname, each with a different path. Routers should match routes based on the most specific path to the least. However, this depends on the router implementation.

The following table shows example routes and their accessibility:

.Route availability
[cols="3*", options="header"]
|===
|Route | When Compared to | Accessible
.2+|_www.example.com/test_ |_www.example.com/test_|Yes
|_www.example.com_|No
.2+|_www.example.com/test_ and _www.example.com_ | _www.example.com/test_|Yes
|_www.example.com_|Yes
.2+|_www.example.com_|_www.example.com/text_|Yes (Matched by the host, not the route)
|_www.example.com_|Yes
|===

.An unsecured route with a path

[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: route-unsecured
spec:
  host: www.example.com
  path: "/test" <1>
  to:
    kind: Service
    name: service-name
----
<1> The path is the only added attribute for a path-based route.

[NOTE]
====
Path-based routing is not available when using passthrough TLS, as the router does not terminate TLS in that case and cannot read the contents of the request.
====
