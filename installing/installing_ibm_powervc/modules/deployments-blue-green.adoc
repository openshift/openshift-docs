// Module included in the following assemblies:
//
// * applications/deployments/route-based-deployment-strategies.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-blue-green_{context}"]
= Blue-green deployments

Blue-green deployments involve running two versions of an application at the same time and moving traffic from the in-production version (the blue version) to the newer version (the green version). You can use a rolling strategy or switch services in a route.

Because many applications depend on persistent data, you must have an application that supports _N-1 compatibility_, which means it shares data and implements live migration between the database, store, or disk by creating two copies of the data layer.

Consider the data used in testing the new version. If it is the production data, a bug in the new version can break the production version.

[id="deployments-blue-green-setting-up_{context}"]
== Setting up a blue-green deployment

Blue-green deployments use two `Deployment` objects. Both are running, and the one in production depends on the service the route specifies, with each `Deployment` object exposed to a different service.

[NOTE]
====
Routes are intended for web (HTTP and HTTPS) traffic, so this technique is best suited for web applications.
====

You can create a new route to the new version and test it. When ready, change the service in the production route to point to the new service and the new (green) version is live.

If necessary, you can roll back to the older (blue) version by switching the service back to the previous version.

.Procedure

. Create two independent application components.
.. Create a copy of the example application running the `v1` image under the `example-blue` service:
+
[source,terminal]
----
$ oc new-app openshift/deployment-example:v1 --name=example-blue
----
+
.. Create a second copy that uses the `v2` image under the `example-green` service:
+
[source,terminal]
----
$ oc new-app openshift/deployment-example:v2 --name=example-green
----

. Create a route that points to the old service:
+
[source,terminal]
----
$ oc expose svc/example-blue --name=bluegreen-example
----

. Browse to the application at `bluegreen-example-<project>.<router_domain>` to verify you see the `v1` image.

. Edit the route and change the service name to `example-green`:
+
[source,terminal]
----
$ oc patch route/bluegreen-example -p '{"spec":{"to":{"name":"example-green"}}}'
----

. To verify that the route has changed, refresh the browser until you see the `v2` image.
