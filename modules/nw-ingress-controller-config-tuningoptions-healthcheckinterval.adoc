// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-controller-config-tuningoptions-healthcheckinterval_{context}"]
= Setting the Ingress Controller health check interval
A cluster administrator can set the health check interval to define how long the router waits between two consecutive health checks. This value is applied globally as a default for all routes. The default value is 5 seconds.

.Prerequisites
* The following assumes that you already created an Ingress Controller.

.Procedure
* Update the Ingress Controller to change the interval between back end health checks:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"healthCheckInterval": "8s"}}}'
----
+
[NOTE]
====
To override the `healthCheckInterval` for a single route, use the route annotation `router.openshift.io/haproxy.health.check.interval`
====
