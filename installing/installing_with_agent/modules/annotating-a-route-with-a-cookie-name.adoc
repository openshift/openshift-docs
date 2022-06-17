// Module included in the following assemblies:
//
// *using-cookies-to-keep-route-statefulness

[id="annotating-a-route-with-a-cookie_{context}"]
= Annotating a route with a cookie

You can set a cookie name to overwrite the default, auto-generated one for the
route. This allows the application receiving route traffic to know the cookie
name. By deleting the cookie it can force the next request to re-choose an
endpoint. So, if a server was overloaded it tries to remove the requests from the
client and redistribute them.

.Procedure

. Annotate the route with the desired cookie name:
+
[source,terminal]
----
$ oc annotate route <route_name> router.openshift.io/<cookie_name>="-<cookie_annotation>"
----
+
For example, to annotate the cookie name of `my_cookie` to the `my_route` with
the annotation of `my_cookie_anno`:
+
[source,terminal]
----
$ oc annotate route my_route router.openshift.io/my_cookie="-my_cookie_anno"
----

. Save the cookie, and access the route:
+
[source,terminal]
----
$ curl $my_route -k -c /tmp/my_cookie
----
