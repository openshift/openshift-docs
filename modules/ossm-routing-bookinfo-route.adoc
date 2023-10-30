// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc
:_mod-docs-content-type: PROCEDURE
[id="ossm-routing-bookinfo-route_{context}"]
= Route based on user identity

Change the route configuration so that all traffic from a specific user is routed to a specific service version. In this case, all traffic from a user named `jason` will be routed to the service `reviews:v2`.

{SMProductShortName} does not have any special, built-in understanding of user identity. This example is enabled by the fact that the `productpage` service adds a custom `end-user` header to all outbound HTTP requests to the reviews service.

.Procedure

. Run the following command to enable user-based routing in the Bookinfo sample application.
+
[source,bash,subs="attributes"]
----
$ oc apply -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/virtual-service-reviews-test-v2.yaml
----

. Run the following command to confirm the rule is created. This command returns all resources of `kind: VirtualService` in YAML format.
+
[source,terminal]
----
$ oc get virtualservice reviews -o yaml
----

. On the `/productpage` of the Bookinfo app, log in as user `jason` with no password.
+
. Refresh the browser. The star ratings appear next to each review.

. Log in as another user (pick any name you want). Refresh the browser. Now the stars are gone. Traffic is now routed to `reviews:v1` for all users except Jason.

You have successfully configured the Bookinfo sample application to route traffic based on user identity.
