:_mod-docs-content-type: CONCEPT
[id="agent-install-load-balancing-none_{context}"]
= Platform "none" Load balancing requirements


Before you install {product-title}, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

[NOTE]
====
These requirements do not apply to single-node OpenShift clusters using the platform `none` option.
====

[NOTE]
====
If you want to deploy the API and application Ingress load balancers with a {op-system-base-full} instance, you must purchase the {op-system-base} subscription separately.
====

The load balancing infrastructure must meet the following requirements:

. *API load balancer*: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:
+
--
  ** Layer 4 load balancing only. This can be referred to as Raw TCP, SSL Passthrough, or SSL Bridge mode. If you use SSL Bridge mode, you must enable Server Name Indication (SNI) for the API routes.
  ** A stateless load balancing algorithm. The options vary based on the load balancer implementation.
--
+
[IMPORTANT]
====
Do not configure session persistence for an API load balancer.
====
+
Configure the following ports on both the front and back of the load balancers:
+
.API load balancer
[cols="2,5,^2,^2,2",options="header"]
|===

|Port
|Back-end machines (pool members)
|Internal
|External
|Description

|`6443`
|Control plane. You must configure the `/readyz` endpoint for the API server health check probe.
|X
|X
|Kubernetes API server

|`22623`
|Control plane.
|X
|
|Machine config server

|===
+
[NOTE]
====
The load balancer must be configured to take a maximum of 30 seconds from the
time the API server turns off the `/readyz` endpoint to the removal of the API
server instance from the pool. Within the time frame after `/readyz` returns an
error or becomes healthy, the endpoint must have been removed or added. Probing
every 5 or 10 seconds, with two successful requests to become healthy and three
to become unhealthy, are well-tested values.
====
+
. *Application Ingress load balancer*: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an {product-title} cluster.
+
Configure the following conditions:
+
--
  ** Layer 4 load balancing only. This can be referred to as Raw TCP, SSL Passthrough, or SSL Bridge mode. If you use SSL Bridge mode, you must enable Server Name Indication (SNI) for the ingress routes.
  ** A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.
--
+
[TIP]
====
If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.
====
+
Configure the following ports on both the front and back of the load balancers:
+
.Application Ingress load balancer
[cols="2,5,^2,^2,2",options="header"]
|===

|Port
|Back-end machines (pool members)
|Internal
|External
|Description

|`443`
|The machines that run the Ingress Controller pods, compute, or worker, by default.
|X
|X
|HTTPS traffic

|`80`
|The machines that run the Ingress Controller pods, compute, or worker, by default.
|X
|X
|HTTP traffic

|===
+
[NOTE]
====
If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
====

[id="agent-install-load-balancing-none-example_{context}"]
== Example load balancer configuration for platform "none" clusters

This section provides an example API and application Ingress load balancer configuration that meets the load balancing requirements for clusters using the platform `none` option. The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

[NOTE]
====
If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.
====

.Sample API and application Ingress load balancer configuration
[%collapsible]
====
[source,text]
----
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443 <1>
  bind *:6443
  mode tcp
  server master0 master0.ocp4.example.com:6443 check inter 1s
  server master1 master1.ocp4.example.com:6443 check inter 1s
  server master2 master2.ocp4.example.com:6443 check inter 1s
listen machine-config-server-22623 <2>
  bind *:22623
  mode tcp
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443 <3>
  bind *:443
  mode tcp
  balance source
  server worker0 worker0.ocp4.example.com:443 check inter 1s
  server worker1 worker1.ocp4.example.com:443 check inter 1s
listen ingress-router-80 <4>
  bind *:80
  mode tcp
  balance source
  server worker0 worker0.ocp4.example.com:80 check inter 1s
  server worker1 worker1.ocp4.example.com:80 check inter 1s
----

<1> Port `6443` handles the Kubernetes API traffic and points to the control plane machines.
<2> Port `22623` handles the machine config server traffic and points to the control plane machines.
<3> Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
<4> Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
+
[NOTE]
=====
If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
=====
====

[TIP]
====
If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.
====