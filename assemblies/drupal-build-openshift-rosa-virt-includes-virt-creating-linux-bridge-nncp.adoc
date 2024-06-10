// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-linux-bridge-nncp_{context}"]
= Creating a Linux bridge NNCP

You can create a `NodeNetworkConfigurationPolicy` (NNCP) manifest for a Linux bridge network.

.Prerequisites
* You have installed the Kubernetes NMState Operator.

.Procedure

* Create the `NodeNetworkConfigurationPolicy` manifest. This example includes sample values that you must replace with your own information.
+
[source,yaml]
----
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-policy <1>
spec:
  desiredState:
    interfaces:
      - name: br1 <2>
        description: Linux bridge with eth1 as a port <3>
        type: linux-bridge <4>
        state: up <5>
        ipv4:
          enabled: false <6>
        bridge:
          options:
            stp:
              enabled: false <7>
          port:
            - name: eth1 <8>
----
<1> Name of the policy.
<2> Name of the interface.
<3> Optional: Human-readable description of the interface.
<4> The type of interface. This example creates a bridge.
<5> The requested state for the interface after creation.
<6> Disables IPv4 in this example.
<7> Disables STP in this example.
<8> The node NIC to which the bridge is attached.
