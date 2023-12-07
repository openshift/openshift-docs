// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-routing-ingress-gateway_{context}"]
= Configuring an ingress gateway

An ingress gateway is a load balancer operating at the edge of the mesh that receives incoming HTTP/TCP connections. It configures exposed ports and protocols but does not include any traffic routing configuration. Traffic routing for ingress traffic is instead configured with routing rules, the same way as for internal service requests.

The following steps show how to create a gateway and configure a `VirtualService` to expose a service in the Bookinfo sample application to outside traffic for paths `/productpage` and `/login`.

.Procedure

. Create a gateway to accept traffic.
+
.. Create a YAML file, and copy the following YAML into it.
+
.Gateway example gateway.yaml
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: bookinfo-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
----
+
.. Apply the YAML file.
+
[source,terminal]
----
$ oc apply -f gateway.yaml
----

. Create a `VirtualService` object to rewrite the host header.
+
.. Create a YAML file, and copy the following YAML into it.
+
.Virtual service example
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
  - "*"
  gateways:
  - bookinfo-gateway
  http:
  - match:
    - uri:
        exact: /productpage
    - uri:
        prefix: /static
    - uri:
        exact: /login
    - uri:
        exact: /logout
    - uri:
        prefix: /api/v1/products
    route:
    - destination:
        host: productpage
        port:
          number: 9080
----
+
.. Apply the YAML file.
+
[source,terminal]
----
$ oc apply -f vs.yaml
----

. Test that the gateway and VirtualService have been set correctly.
+
.. Set the Gateway URL.
+
[source,terminal]
----
export GATEWAY_URL=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.host}')
----
+
.. Set the port number. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
export TARGET_PORT=$(oc -n istio-system get route istio-ingressgateway -o jsonpath='{.spec.port.targetPort}')
----
+
.. Test a page that has been explicitly exposed.
+
[source,terminal]
----
curl -s -I "$GATEWAY_URL/productpage"
----
+
The expected result is `200`.
