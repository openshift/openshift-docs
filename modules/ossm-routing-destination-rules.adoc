// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-routing-destination-rules_{context}"]
= Understanding destination rules

Destination rules are applied after virtual service routing rules are evaluated, so they apply to the traffic's real destination. Virtual services route traffic to a destination. Destination rules configure what happens to traffic at that destination.

By default, {SMProductName} uses a least requests load balancing policy, where the service instance in the pool with the least number of active connections receives the request. {SMProductName} also supports the following models, which you can specify in destination rules for requests to a particular service or service subset.

* Random: Requests are forwarded at random to instances in the pool.
* Weighted: Requests are forwarded to instances in the pool according to a specific percentage.
* Least requests: Requests are forwarded to instances with the least number of requests.

.Destination rule example

The following example destination rule configures three different subsets for the `my-svc` destination service, with different load balancing policies:

[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-destination-rule
spec:
  host: my-svc
  trafficPolicy:
    loadBalancer:
      simple: RANDOM
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
    trafficPolicy:
      loadBalancer:
        simple: ROUND_ROBIN
  - name: v3
    labels:
      version: v3
----
