// Module included in the following assemblies:
//
// * networking/metallb/metallb-troubleshoot-support.adoc

[id="nw-metallb-collecting-data_{context}"]
= About collecting MetalLB data

You can use the `oc adm must-gather` CLI command to collect information about your cluster, your MetalLB configuration, and the MetalLB Operator.
The following features and objects are associated with MetalLB and the MetalLB Operator:

* The namespace and child objects that the MetalLB Operator is deployed in

* All MetalLB Operator custom resource definitions (CRDs)

The `oc adm must-gather` CLI command collects the following information from FRRouting (FRR) that Red Hat uses to implement BGP and BFD:

* `/etc/frr/frr.conf`
* `/etc/frr/frr.log`
* `/etc/frr/daemons` configuration file
* `/etc/frr/vtysh.conf`

The log and configuration files in the preceding list are collected from the `frr` container in each `speaker` pod.

In addition to the log and configuration files, the `oc adm must-gather` CLI command collects the output from the following `vtysh` commands:

* `show running-config`
* `show bgp ipv4`
* `show bgp ipv6`
* `show bgp neighbor`
* `show bfd peer`

No additional configuration is required when you run the `oc adm must-gather` CLI command.
