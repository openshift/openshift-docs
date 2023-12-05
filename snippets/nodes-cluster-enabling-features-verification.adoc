// Text snippet included in the following modules:
//
// * modules/clusters/nodes-cluster-enabling-features-install.adoc
// * modules/clusters/nodes-cluster-enabling-features-console.adoc
// * modules/nodes-cluster-enabling-features-cli.adoc

:_mod-docs-content-type: SNIPPET


You can verify that the feature gates are enabled by looking at the `kubelet.conf` file on a node after the nodes return to the ready state.

. From the *Administrator* perspective in the web console, navigate to *Compute* -> *Nodes*.

. Select a node.

. In the *Node details* page, click *Terminal*.

. In the terminal window, change your root directory to `/host`:
+
[source,terminal]
----
sh-4.2# chroot /host
----

. View the `kubelet.conf` file:
+
[source,terminal]
----
sh-4.2# cat /etc/kubernetes/kubelet.conf
----
+
.Sample output
+
[source,terminal]
----
# ...
featureGates:
  InsightsOperatorPullingSCA: true,
  LegacyNodeRoleBehavior: false
# ...
----
+
The features that are listed as `true` are enabled on your cluster.
+
[NOTE]
====
The features listed vary depending upon the {product-title} version.
====
