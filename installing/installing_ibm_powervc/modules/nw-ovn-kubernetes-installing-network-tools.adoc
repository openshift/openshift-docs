// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-architecture.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ovn-kubernetes-installing-network-tools_{context}"]
= Installing network-tools on local host

Install `network-tools` on your local host to make a collection of tools available for debugging {product-title} cluster network issues.

.Procedure

. Clone the `network-tools` repository onto your workstation with the following command:
+
[source,terminal]
----
$ git clone git@github.com:openshift/network-tools.git
----

. Change into the directory for the repository you just cloned:
+
[source,terminal]
----
$ cd network-tools
----

. Optional: List all available commands:
+
[source,terminal]
----
$ ./debug-scripts/network-tools -h
----