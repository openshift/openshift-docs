// Module included in the following assemblies:
//
// * networking/configuring-ipfailover.adoc

[id="nw-ipfailover-configuring-keepalived-multicast_{context}"]
= Configuring Keepalived multicast

{product-title} IP failover internally uses Keepalived.

[IMPORTANT]
====
Ensure that multicast is enabled on the nodes labeled above and they can accept network traffic for `224.0.0.18`, the Virtual Router Redundancy Protocol (VRRP) multicast IP address.
====

Before starting the Keepalived daemon, the startup script verifies the `iptables` rule that allows multicast traffic to flow. If there is no such rule, the startup script creates a new rule and adds it to the IP tables configuration. Where this new rule gets added to the IP tables configuration depends on the OPENSHIFT_HA_IPTABLES_CHAIN` variable. If there is an `OPENSHIFT_HA_IPTABLES_CHAIN` variable specified, the rule gets added to the specified chain. Otherwise, the rule is added to the `INPUT` chain.

[IMPORTANT]
====
The `iptables` rule must be present whenever there is one or more Keepalived daemon running on the node.
====

The `iptables` rule can be removed after the last Keepalived daemon terminates. The rule is not automatically removed.

.Procedure

* The `iptables` rule only gets created when it is not already present and the `OPENSHIFT_HA_IPTABLES_CHAIN` variable is specified. You can manually manage the `iptables` rule on each of the nodes if you unset the `OPENSHIFT_HA_IPTABLES_CHAIN` variable:
+
[IMPORTANT]
====
You must ensure that the manually added rules persist after a system restart.

Be careful since every Keepalived daemon uses the VRRP protocol over multicast `224.0.0.18` to negotiate with its peers. There must be a different `VRRP-id`, in the range `0..255`, for each VIP.
====
+
[source,terminal]
----
$ for node in openshift-node-{5,6,7,8,9}; do   ssh $node <<EOF

export interface=${interface:-"eth0"}
echo "Check multicast enabled ... ";
ip addr show $interface | grep -i MULTICAST

echo "Check multicast groups ... "
ip maddr show $interface | grep 224.0.0

EOF
done;
----
