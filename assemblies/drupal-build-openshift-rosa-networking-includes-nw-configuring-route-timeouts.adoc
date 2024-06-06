// Module filename: nw-configuring-route-timeouts.adoc
// Module included in the following assemblies:
// * networking/configuring-routing.adoc
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-configuring-route-timeouts_{context}"]
= Configuring route timeouts

You can configure the default timeouts for an existing route when you
have services in need of a low timeout, which is required for Service Level
Availability (SLA) purposes, or a high timeout, for cases with a slow
back end.

.Prerequisites
* You need a deployed Ingress Controller on a running cluster.

.Procedure
. Using the `oc annotate` command, add the timeout to the route:
+
[source,terminal]
----
$ oc annotate route <route_name> \
    --overwrite haproxy.router.openshift.io/timeout=<timeout><time_unit> <1>
----
<1> Supported time units are microseconds (us), milliseconds (ms), seconds (s),
minutes (m), hours (h), or days (d).
+
The following example sets  a timeout of two seconds on a route named `myroute`:
+
[source,terminal]
----
$ oc annotate route myroute --overwrite haproxy.router.openshift.io/timeout=2s
----
