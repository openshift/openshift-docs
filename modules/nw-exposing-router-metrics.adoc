// Module included in the following assemblies:
//
// * networking/ingress_operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-exposing-router-metrics_{context}"]
= Exposing router metrics

You can expose the HAProxy router metrics by default in Prometheus format on the default stats port, 1936. The external metrics collection and aggregation systems such as Prometheus can access the HAProxy router metrics. You can view the HAProxy router metrics in a browser in the HTML and comma separated values (CSV) format.

.Prerequisites

* You configured your firewall to access the default stats port, 1936.

.Procedure

. Get the router pod name by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ingress
----
+
.Example output
[source,terminal]
----
NAME                              READY   STATUS    RESTARTS   AGE
router-default-76bfffb66c-46qwp   1/1     Running   0          11h
----

. Get the router's username and password, which the router pod stores in the `/var/lib/haproxy/conf/metrics-auth/statsUsername` and `/var/lib/haproxy/conf/metrics-auth/statsPassword` files:

.. Get the username by running the following command:
+
[source,terminal]
----
$ oc rsh <router_pod_name> cat metrics-auth/statsUsername
----

.. Get the password by running the following command:
+
[source,terminal]
----
$ oc rsh <router_pod_name> cat metrics-auth/statsPassword
----

. Get the router IP and metrics certificates by running the following command:
+
[source,terminal]
----
$ oc describe pod <router_pod>
----

. Get the raw statistics in Prometheus format by running the following command:
+
[source,terminal]
----
$ curl -u <user>:<password> http://<router_IP>:<stats_port>/metrics
----

. Access the metrics securely by running the following command:
+
[source,terminal]
----
$ curl -u user:password https://<router_IP>:<stats_port>/metrics -k
----

. Access the default stats port, 1936, by running the following command:
+
[source,terminal]
----
$ curl -u <user>:<password> http://<router_IP>:<stats_port>/metrics
----
+
--
.Example output
[%collapsible]
====
[source,terminal]
...
# HELP haproxy_backend_connections_total Total number of connections.
# TYPE haproxy_backend_connections_total gauge
haproxy_backend_connections_total{backend="http",namespace="default",route="hello-route"} 0
haproxy_backend_connections_total{backend="http",namespace="default",route="hello-route-alt"} 0
haproxy_backend_connections_total{backend="http",namespace="default",route="hello-route01"} 0
...
# HELP haproxy_exporter_server_threshold Number of servers tracked and the current threshold value.
# TYPE haproxy_exporter_server_threshold gauge
haproxy_exporter_server_threshold{type="current"} 11
haproxy_exporter_server_threshold{type="limit"} 500
...
# HELP haproxy_frontend_bytes_in_total Current total of incoming bytes.
# TYPE haproxy_frontend_bytes_in_total gauge
haproxy_frontend_bytes_in_total{frontend="fe_no_sni"} 0
haproxy_frontend_bytes_in_total{frontend="fe_sni"} 0
haproxy_frontend_bytes_in_total{frontend="public"} 119070
...
# HELP haproxy_server_bytes_in_total Current total of incoming bytes.
# TYPE haproxy_server_bytes_in_total gauge
haproxy_server_bytes_in_total{namespace="",pod="",route="",server="fe_no_sni",service=""} 0
haproxy_server_bytes_in_total{namespace="",pod="",route="",server="fe_sni",service=""} 0
haproxy_server_bytes_in_total{namespace="default",pod="docker-registry-5-nk5fz",route="docker-registry",server="10.130.0.89:5000",service="docker-registry"} 0
haproxy_server_bytes_in_total{namespace="default",pod="hello-rc-vkjqx",route="hello-route",server="10.130.0.90:8080",service="hello-svc-1"} 0
...
====
--

. Launch the stats window by entering the following URL in a browser:
+
[source,terminal]
----
http://<user>:<password>@<router_IP>:<stats_port>
----

. Optional: Get the stats in CSV format by entering the following URL in a browser:
+
[source,terminal]
----
http://<user>:<password>@<router_ip>:1936/metrics;csv
----
