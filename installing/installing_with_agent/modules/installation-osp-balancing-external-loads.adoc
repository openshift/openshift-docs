// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-load-balancing.adoc

[id="installation-osp-balancing-external-loads_{context}"]
= Configuring an external load balancer

Configure an external load balancer in {rh-openstack-first} to use your own load balancer, resolve external networking needs, or scale beyond what the default {product-title} load balancer can provide.

The load balancer serves ports 6443, 443, and 80 to any users of the system. Port 22623 serves Ignition startup configurations to the {product-title} machines and must not be reachable from outside the cluster.

.Prerequisites

* Access to a {rh-openstack} administrator's account
* The https://docs.openstack.org/python-openstackclient/latest/[{rh-openstack} client] installed on the target environment

.Procedure

. Using the {rh-openstack} CLI, add floating IP addresses to all of the control plane machines:
+
[source,terminal]
----
$ openstack floating ip create --port master-port-0 <public network>
----
+
[source,terminal]
----
$ openstack floating ip create --port master-port-1 <public network>
----
+
[source,terminal]
----
$ openstack floating ip create --port master-port-2 <public network>
----

. View the new floating IPs:
+
[source,terminal]
----
$ openstack server list
----

. Incorporate the listed floating IP addresses into the load balancer configuration to allow access the cluster via port 6443.
+
.A HAProxy configuration for port 6443
[source,txt]
----
listen <cluster name>-api-6443
    bind 0.0.0.0:6443
    mode tcp
    balance roundrobin
    server <cluster name>-master-2 <floating ip>:6443 check
    server <cluster name>-master-0 <floating ip>:6443 check
    server <cluster name>-master-1 <floating ip>:6443 check
----

. Repeat the previous three steps for ports 443 and 80.

. Enable network access from the load balancer network to the control plane machines on ports 6443, 443, and 80:
+
[source,terminal]
----
$ openstack security group rule create master --remote-ip <load balancer CIDR> --ingress --protocol tcp --dst-port 6443
----
+
[source,terminal]
----
$ openstack security group rule create master --remote-ip <load balancer CIDR> --ingress --protocol tcp --dst-port 443
----
+
[source,terminal]
----
$ openstack security group rule create master --remote-ip <load balancer CIDR> --ingress --protocol tcp --dst-port 80
----

[TIP]
You can also specify a particular IP address with `/32`.

. Update the DNS entry for `api.<cluster name>.<base domain>` to point to the new load balancer:
+
[source,txt]
----
<load balancer ip> api.<cluster-name>.<base domain>
----
+
The external load balancer is now available.

. Verify the load balancer's functionality by using the following curl command:
+
[source,terminal]
----
$ curl https://<loadbalancer-ip>:6443/version --insecure
----
+
The output resembles the following example:
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

. Optional: Verify that the Ignition configuration files are available only from
within the cluster by running a curl command on port 22623 from outside the cluster:
+
[source,terminal]
----
$ curl https://<loadbalancer ip>:22623/config/master --insecure
----
+
The command fails.
