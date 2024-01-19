// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-blocking-nodeport-access_{context}"]
= Blocking external access to the NodePort service on a specific host interface

OVN-Kubernetes does not restrict the host interface where a NodePort service can be accessed from outside a {product-title} node. The following procedure explains how to block the NodePort service on a specific host interface and restrict external access.

.Prerequisites

* You must have an account with root privileges.

.Procedure

. Change the `NODEPORT` variable to the host port number assigned to your Kubernetes NodePort service by running the following command:
+
[source,terminal]
----
# export NODEPORT=30700
----

. Change the `INTERFACE_IP` value to the IP address from the host interface that you want to block. For example:
+
[source,terminal]
----
# export INTERFACE_IP=192.168.150.33
----

. Insert a new rule in the `nat` table PREROUTING chain to drop all packets that match the destination port and IP address. For example:
+
[source,terminal]
----
$ sudo nft -a insert rule ip nat PREROUTING tcp dport $NODEPORT ip daddr $INTERFACE_IP drop
----

. List the new rule by running the following command:
+
[source,terminal]
----
$ sudo nft -a list chain ip nat PREROUTING
table ip nat {
	chain PREROUTING { # handle 1
		type nat hook prerouting priority dstnat; policy accept;
		tcp dport 30700 ip daddr 192.168.150.33 drop # handle 134
		counter packets 108 bytes 18074 jump OVN-KUBE-ETP # handle 116
		counter packets 108 bytes 18074 jump OVN-KUBE-EXTERNALIP # handle 114
		counter packets 108 bytes 18074 jump OVN-KUBE-NODEPORT # handle 112
	}
}
----
+
[NOTE]
====
Note the `handle` number of the newly added rule. You need to remove the `handle` number in the following step.
====

. Remove the custom rule with the following sample command:
+
[source,terminal]
----
$ sudo nft -a delete rule ip nat PREROUTING handle 134
----

