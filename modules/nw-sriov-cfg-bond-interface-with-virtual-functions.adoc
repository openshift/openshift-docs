// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc
:_mod-docs-content-type: PROCEDURE
[id="nw-sriov-cfg-bond-interface-with-virtual-functions_{context}"]
= Configuring a bond interface from two SR-IOV interfaces

Bonding enables multiple network interfaces to be aggregated into a single logical "bonded" interface. Bond Container Network Interface (Bond-CNI) brings bond capability into containers.

Bond-CNI can be created using Single Root I/O Virtualization (SR-IOV) virtual functions and placing them in the container network namespace.

{product-title} only supports Bond-CNI using SR-IOV virtual functions. The SR-IOV Network Operator provides the SR-IOV CNI plugin needed to manage the virtual functions. Other CNIs or types of interfaces are not supported.

.Prerequisites

* The SR-IOV Network Operator must be installed and configured to obtain virtual functions in a container.
* To configure SR-IOV interfaces, an SR-IOV network and policy must be created for each interface.
* The SR-IOV Network Operator creates a network attachment definition for each SR-IOV interface, based on the SR-IOV network and policy defined.
* The `linkState` is set to the default value `auto` for the SR-IOV virtual function.

[id="nw-sriov-cfg-creating-bond-network-attachment-definition_{context}"]
== Creating a bond network attachment definition

Now that the SR-IOV virtual functions are available, you can create a bond network attachment definition.

[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: bond-net1
      namespace: demo
    spec:
      config: '{
      "type": "bond", <1>
      "cniVersion": "0.3.1",
      "name": "bond-net1",
      "mode": "active-backup", <2>
      "failOverMac": 1, <3>
      "linksInContainer": true, <4>
      "miimon": "100",
      "mtu": 1500,
      "links": [ <5>
            {"name": "net1"},
            {"name": "net2"}
        ],
      "ipam": {
            "type": "host-local",
            "subnet": "10.56.217.0/24",
            "routes": [{
            "dst": "0.0.0.0/0"
            }],
            "gateway": "10.56.217.1"
        }
      }'
----
<1> The cni-type is always set to `bond`.
<2> The `mode` attribute specifies the bonding mode.
+
[NOTE]
====
The bonding modes supported are:

* `balance-rr` - 0
* `active-backup` - 1
* `balance-xor` - 2

For `balance-rr` or `balance-xor` modes, you must set the `trust` mode to `on` for the SR-IOV virtual function.
====
<3> The `failover` attribute is mandatory for active-backup mode and must be set to 1.
<4> The `linksInContainer=true` flag informs the Bond CNI that the required interfaces are to be found inside the container. By default, Bond CNI looks for these interfaces on the host which does not work for integration with SRIOV and Multus.
<5> The `links` section defines which interfaces will be used to create the bond. By default, Multus names the attached interfaces as: "net", plus a consecutive number, starting with one.

[id="nw-sriov-cfg-creating-pod-using-interface_{context}"]
== Creating a pod using a bond interface

. Test the setup by creating a pod with a YAML file named for example `podbonding.yaml` with content similar to the following:
+
[source,yaml]
----
apiVersion: v1
    kind: Pod
    metadata:
      name: bondpod1
      namespace: demo
      annotations:
        k8s.v1.cni.cncf.io/networks: demo/sriovnet1, demo/sriovnet2, demo/bond-net1 <1>
    spec:
      containers:
      - name: podexample
        image: quay.io/openshift/origin-network-interface-bond-cni:4.11.0
        command: ["/bin/bash", "-c", "sleep INF"]
----
<1> Note the network annotation: it contains two SR-IOV network attachments, and one bond network attachment. The bond attachment uses the two SR-IOV interfaces as bonded port interfaces.

. Apply the yaml by running the following command:
+
[source,terminal]
----
$ oc apply -f podbonding.yaml
----

. Inspect the pod interfaces with the following command:
+
[source,yaml]
----
$ oc rsh -n demo bondpod1
sh-4.4#
sh-4.4# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo
valid_lft forever preferred_lft forever
3: eth0@if150: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1450 qdisc noqueue state UP
link/ether 62:b1:b5:c8:fb:7a brd ff:ff:ff:ff:ff:ff
inet 10.244.1.122/24 brd 10.244.1.255 scope global eth0
valid_lft forever preferred_lft forever
4: net3: <BROADCAST,MULTICAST,UP,LOWER_UP400> mtu 1500 qdisc noqueue state UP qlen 1000
link/ether 9e:23:69:42:fb:8a brd ff:ff:ff:ff:ff:ff <1>
inet 10.56.217.66/24 scope global bond0
valid_lft forever preferred_lft forever
43: net1: <BROADCAST,MULTICAST,UP,LOWER_UP800> mtu 1500 qdisc mq master bond0 state UP qlen 1000
link/ether 9e:23:69:42:fb:8a brd ff:ff:ff:ff:ff:ff <2>
44: net2: <BROADCAST,MULTICAST,UP,LOWER_UP800> mtu 1500 qdisc mq master bond0 state UP qlen 1000
link/ether 9e:23:69:42:fb:8a brd ff:ff:ff:ff:ff:ff <3>
----
<1> The bond interface is automatically named `net3`. To set a specific interface name add `@name` suffix to the pod’s `k8s.v1.cni.cncf.io/networks` annotation.
<2> The `net1` interface is based on an SR-IOV virtual function.
<3> The `net2` interface is based on an SR-IOV virtual function.
+
[NOTE]
====
If no interface names are configured in the pod annotation, interface names are assigned automatically as `net<n>`, with `<n>` starting at `1`.
====

. Optional: If you want to set a specific interface name for example `bond0`, edit the `k8s.v1.cni.cncf.io/networks` annotation and set `bond0` as the interface name as follows:
+
[source,terminal]
----
annotations:
        k8s.v1.cni.cncf.io/networks: demo/sriovnet1, demo/sriovnet2, demo/bond-net1@bond0
----