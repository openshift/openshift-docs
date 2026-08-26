// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc
:_mod-docs-content-type: PROCEDURE
[id="ossm-routing-bookinfo-test_{context}"]
= Testing the new route configuration

Test the new configuration by refreshing the `/productpage` of the Bookinfo application.

.Procedure

. Set the value for the `GATEWAY_URL` parameter. You can use this variable to find the URL for your Bookinfo product page later. In this example, istio-system is the name of the control plane project.
+
[source,terminal]
----
export GATEWAY_URL=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.host}')
----

. Run the following command to retrieve the URL for the product page.
+
[source,terminal]
----
echo "http://$GATEWAY_URL/productpage"
----

. Open the Bookinfo site in your browser.

The reviews part of the page displays with no rating stars, no matter how many times you refresh. This is because you configured {SMProductShortName} to route all traffic for the reviews service to the version `reviews:v1` and this version of the service does not access the star ratings service.

Your service mesh now routes traffic to one version of a service.
