// Module included in the following assemblies:
// TODO
// * networking/TBD
// * networking/load-balancing-openstack.adoc
// * installing/installing_bare_metal_ipi/ipi-install-post-installation-configuration.adoc jowilkin
// * installing/installing-vsphere-installer-provisioned.adoc
// * installing/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing-vsphere-installer-provisioned-network-customizations.adoc
// * installing/installing-restricted-networks-installer-provisioned-vsphere.adoc


ifeval::["{context}" == "installing-vsphere-installer-provisioned"]
:vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere-installer-provisioned-customizations"]
:vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere-installer-provisioned-network-customizations"]
:vsphere:
endif::[]
ifeval::["{context}" == installing-restricted-networks-installer-provisioned-vsphere]
:vsphere:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="nw-osp-configuring-external-load-balancer_{context}"]
= Configuring an external load balancer

You can configure an {product-title} cluster
ifeval::["{context}" == "load-balancing-openstack"]
on {rh-openstack-first}
endif::[]
to use an external load balancer in place of the default load balancer.

[IMPORTANT]
====
Configuring an external load balancer depends on your vendor's load balancer.

The information and examples in this section are for guideline purposes only. Consult the vendor documentation for more specific information about the vendor's load balancer.
====

Red Hat supports the following services for an external load balancer:

* OpenShift API
* Ingress Controller

You can choose to configure one or both of these services for an external load balancer. Configuring only the Ingress Controller service is a common configuration option.

The following configuration options are supported for external load balancers:

* Use a node selector to map the Ingress Controller to a specific set of nodes. You must assign a static IP address to each node in this set, or configure each node to receive the same IP address from the Dynamic Host Configuration Protocol (DHCP). Infrastructure nodes commonly receive this type of configuration.

* Target all IP addresses on a subnet. This configuration can reduce maintenance overhead, because you can create and destroy nodes within those networks without reconfiguring the load balancer targets. If you deploy your ingress pods by using a machine set on a smaller network, such as a `/27` or `/28`, you can simplify your load balancer targets.
+
[TIP]
====
You can list all IP addresses that exist in a network by checking the machine config pool's resources.
====

.Considerations

* For a front-end IP address, you can use the same IP address for the front-end IP address, the Ingress Controller's load balancer, and API load balancer. Check the vendor's documentation for this capability.

* For a back-end IP address, ensure that an IP address for an {product-title} control plane node does not change during the lifetime of the external load balancer. You can achieve this by completing one of the following actions:
** Assign a static IP address to each control plane node.
** Configure each node to receive the same IP address from the DHCP every time the node requests a DHCP lease. Depending on the vendor, the DHCP lease might be in the form of an IP reservation or a static DHCP assignment.

* Manually define each node that runs the Ingress Controller in the external load balancer for the Ingress Controller back-end service. For example, if the Ingress Controller moves to an undefined node, a connection outage can occur.

.OpenShift API prerequisites

* You defined a front-end IP address.
* TCP ports 6443 and 22623 are exposed on the front-end IP address of your load balancer. Check the following items:
** Port 6443 provides access to the OpenShift API service.
** Port 22623 can provide ignition startup configurations to nodes.
* The front-end IP address and port 6443 are reachable by all users of your system with a location external to your {product-title} cluster.
* The front-end IP address and port 22623 are reachable only by {product-title} nodes.
* The load balancer backend can communicate with {product-title} control plane nodes on port 6443 and 22623.

.Ingress Controller prerequisites

* You defined a front-end IP address.
* TCP ports 443 and 80 are exposed on the front-end IP address of your load balancer.
* The front-end IP address, port 80 and port 443 are be reachable by all users of your system with a location external to your {product-title} cluster.
* The front-end IP address, port 80 and port 443 are reachable to all nodes that operate in your {product-title} cluster.
* The load balancer backend can communicate with {product-title} nodes that run the Ingress Controller on ports 80, 443, and 1936.

.Prerequisite for health check URL specifications

You can configure most load balancers by setting health check URLs that determine if a service is available or unavailable. {product-title} provides these health checks for the OpenShift API, Machine Configuration API, and Ingress Controller backend services.

The following examples demonstrate health check specifications for the previously listed backend services:

.Example of a Kubernetes API health check specification

[source,terminal]
----
Path: HTTPS:6443/readyz
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 10
Interval: 10
----

.Example of a Machine Config API health check specification

[source,terminal]
----
Path: HTTPS:22623/healthz
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 10
Interval: 10
----

.Example of an Ingress Controller health check specification

[source,terminal]
----
Path: HTTP:1936/healthz/ready
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 5
Interval: 10
----

.Procedure

. Configure the HAProxy Ingress Controller, so that you can enable access to the cluster from your load balancer on ports 6443, 443, and 80:
+
.Example HAProxy configuration
[source,terminal]
----
#...
listen my-cluster-api-6443
    bind 192.168.1.100:6443
    mode tcp
    balance roundrobin
  option httpchk
  http-check connect
  http-check send meth GET uri /readyz
  http-check expect status 200
    server my-cluster-master-2 192.168.1.101:6443 check inter 10s rise 2 fall 2
    server my-cluster-master-0 192.168.1.102:6443 check inter 10s rise 2 fall 2
    server my-cluster-master-1 192.168.1.103:6443 check inter 10s rise 2 fall 2

listen my-cluster-machine-config-api-22623
    bind 192.168.1.1000.0.0.0:22623
    mode tcp
    balance roundrobin
  option httpchk
  http-check connect
  http-check send meth GET uri /healthz
  http-check expect status 200
    server my-cluster-master-2 192.0168.21.2101:22623 check inter 10s rise 2 fall 2
    server my-cluster-master-0 192.168.1.1020.2.3:22623 check inter 10s rise 2 fall 2
    server my-cluster-master-1 192.168.1.1030.2.1:22623 check inter 10s rise 2 fall 2

listen my-cluster-apps-443
        bind 192.168.1.100:443
        mode tcp
        balance roundrobin
    option httpchk
    http-check connect
    http-check send meth GET uri /healthz/ready
    http-check expect status 200
        server my-cluster-worker-0 192.168.1.111:443 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-1 192.168.1.112:443 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-2 192.168.1.113:443 check port 1936 inter 10s rise 2 fall 2

listen my-cluster-apps-80
        bind 192.168.1.100:80
        mode tcp
        balance roundrobin
    option httpchk
    http-check connect
    http-check send meth GET uri /healthz/ready
    http-check expect status 200
        server my-cluster-worker-0 192.168.1.111:80 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-1 192.168.1.112:80 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-2 192.168.1.113:80 check port 1936 inter 10s rise 2 fall 2
# ...
----

. Use the `curl` CLI command to verify that the external load balancer and its resources are operational:
+
.. Verify that the cluster machine configuration API is accessible to the Kubernetes API server resource, by running the following command and observing the response:
+
[source,terminal]
----
$ curl https://<loadbalancer_ip_address>:6443/version --insecure
----
+
If the configuration is correct, you receive a JSON object in response:
+
[source,json]
----
{
  "major": "1",
  "minor": "11+",
  "gitVersion": "v1.11.0+ad103ed",
  "gitCommit": "ad103ed",
  "gitTreeState": "clean",
  "buildDate": "2019-01-09T06:44:10Z",
  "goVersion": "go1.10.3",
  "compiler": "gc",
  "platform": "linux/amd64"
}
----
+
.. Verify that the cluster machine configuration API is accessible to the Machine config server resource, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -v https://<loadbalancer_ip_address>:22623/healthz --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
Content-Length: 0
----
+
.. Verify that the controller is accessible to the Ingress Controller resource on port 80, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -I -L -H "Host: console-openshift-console.apps.<cluster_name>.<base_domain>" http://<load_balancer_front_end_IP_address>
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 302 Found
content-length: 0
location: https://console-openshift-console.apps.ocp4.private.opequon.net/
cache-control: no-cache
----
+
.. Verify that the controller is accessible to the Ingress Controller resource on port 443, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -I -L --insecure --resolve console-openshift-console.apps.<cluster_name>.<base_domain>:443:<Load Balancer Front End IP Address> https://console-openshift-console.apps.<cluster_name>.<base_domain>
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
referrer-policy: strict-origin-when-cross-origin
set-cookie: csrf-token=UlYWOyQ62LWjw2h003xtYSKlh1a0Py2hhctw0WmV2YEdhJjFyQwWcGBsja261dGLgaYO0nxzVErhiXt6QepA7g==; Path=/; Secure; SameSite=Lax
x-content-type-options: nosniff
x-dns-prefetch-control: off
x-frame-options: DENY
x-xss-protection: 1; mode=block
date: Wed, 04 Oct 2023 16:29:38 GMT
content-type: text/html; charset=utf-8
set-cookie: 1e2670d92730b515ce3a1bb65da45062=1bf5e9573c9a2760c964ed1659cc1673; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----

. Configure the DNS records for your cluster to target the front-end IP addresses of the external load balancer. You must update records to your DNS server for the cluster API and applications over the load balancer.
+
.Examples of modified DNS records
+
[source,dns]
----
<load_balancer_ip_address>  A  api.<cluster_name>.<base_domain>
A record pointing to Load Balancer Front End
----
+
[source,dns]
----
<load_balancer_ip_address>   A apps.<cluster_name>.<base_domain>
A record pointing to Load Balancer Front End
----
+
[IMPORTANT]
====
DNS propagation might take some time for each DNS record to become available. Ensure that each DNS record propagates before validating each record.
====

. Use the `curl` CLI command to verify that the external load balancer and DNS record configuration are operational:
+
.. Verify that you can access the cluster API, by running the following command and observing the output:
+
[source,terminal]
----
$ curl https://api.<cluster_name>.<base_domain>:6443/version --insecure
----
+
If the configuration is correct, you receive a JSON object in response:
+
[source,json]
----
{
  "major": "1",
  "minor": "11+",
  "gitVersion": "v1.11.0+ad103ed",
  "gitCommit": "ad103ed",
  "gitTreeState": "clean",
  "buildDate": "2019-01-09T06:44:10Z",
  "goVersion": "go1.10.3",
  "compiler": "gc",
  "platform": "linux/amd64"
  }
----
+
.. Verify that you can access the cluster machine configuration, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -v https://api.<cluster_name>.<base_domain>:22623/healthz --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
Content-Length: 0
----
+
.. Verify that you can access each cluster application on port, by running the following command and observing the output:
+
[source,terminal]
----
$ curl http://console-openshift-console.apps.<cluster_name>.<base_domain> -I -L --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 302 Found
content-length: 0
location: https://console-openshift-console.apps.<cluster-name>.<base domain>/
cache-control: no-cacheHTTP/1.1 200 OK
referrer-policy: strict-origin-when-cross-origin
set-cookie: csrf-token=39HoZgztDnzjJkq/JuLJMeoKNXlfiVv2YgZc09c3TBOBU4NI6kDXaJH1LdicNhN1UsQWzon4Dor9GWGfopaTEQ==; Path=/; Secure
x-content-type-options: nosniff
x-dns-prefetch-control: off
x-frame-options: DENY
x-xss-protection: 1; mode=block
date: Tue, 17 Nov 2020 08:42:10 GMT
content-type: text/html; charset=utf-8
set-cookie: 1e2670d92730b515ce3a1bb65da45062=9b714eb87e93cf34853e87a92d6894be; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----
+
.. Verify that you can access each cluster application on port 443, by running the following command and observing the output:
+
[source,terminal]
----
$ curl https://console-openshift-console.apps.<cluster_name>.<base_domain> -I -L --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
referrer-policy: strict-origin-when-cross-origin
set-cookie: csrf-token=UlYWOyQ62LWjw2h003xtYSKlh1a0Py2hhctw0WmV2YEdhJjFyQwWcGBsja261dGLgaYO0nxzVErhiXt6QepA7g==; Path=/; Secure; SameSite=Lax
x-content-type-options: nosniff
x-dns-prefetch-control: off
x-frame-options: DENY
x-xss-protection: 1; mode=block
date: Wed, 04 Oct 2023 16:29:38 GMT
content-type: text/html; charset=utf-8
set-cookie: 1e2670d92730b515ce3a1bb65da45062=1bf5e9573c9a2760c964ed1659cc1673; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----

ifeval::["{context}" == "installing-vsphere-installer-provisioned"]
:!vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere-installer-provisioned-customizations"]
:!vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere-installer-provisioned-network-customizations"]
:!vsphere:
endif::[]
ifeval::["{context}" == installing-restricted-networks-installer-provisioned-vsphere]
:!vsphere:
endif::[]
