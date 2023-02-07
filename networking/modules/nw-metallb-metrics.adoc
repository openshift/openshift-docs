// Module included in the following assemblies:
//
// * networking/metallb/metallb-troubleshoot-support.adoc

[id="nw-metallb-metrics_{context}"]
= MetalLB metrics for BGP and BFD

{product-title} captures the following metrics that are related to MetalLB and BGP peers and BFD profiles:

* `metallb_bfd_control_packet_input` counts the number of BFD control packets received from each BFD peer.

* `metallb_bfd_control_packet_output` counts the number of BFD control packets sent to each BFD peer.

* `metallb_bfd_echo_packet_input` counts the number of BFD echo packets received from each BFD peer.

* `metallb_bfd_echo_packet_output` counts the number of BFD echo packets sent to each BFD peer.

* `metallb_bfd_session_down_events` counts the number of times the BFD session with a peer entered the `down` state.

* `metallb_bfd_session_up` indicates the connection state with a BFD peer. `1` indicates the session is `up` and `0` indicates the session is `down`.

* `metallb_bfd_session_up_events` counts the number of times the BFD session with a peer entered the `up` state.

* `metallb_bfd_zebra_notifications` counts the number of BFD Zebra notifications for each BFD peer.

* `metallb_bgp_announced_prefixes_total` counts the number of load balancer IP address prefixes that are advertised to BGP peers. The terms _prefix_ and _aggregated route_ have the same meaning.

* `metallb_bgp_session_up` indicates the connection state with a BGP peer. `1` indicates the session is `up` and `0` indicates the session is `down`.

* `metallb_bgp_updates_total` counts the number of BGP `update` messages that were sent to a BGP peer.
