// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/deploying-egress-router-ovn-redirection.adoc

ifeval::["{context}" == "deploying-egress-router-ovn-redirection"]
:redirect:
:router-type: redirect
endif::[]
:router-name: egress-router-{router-type}

[id="nw-egress-router-ovn-cr_{context}"]
= Egress router custom resource

Define the configuration for an egress router pod in an egress router custom resource. The following YAML describes the fields for the configuration of an egress router in {router-type} mode:

// cluster-network-operator/manifests/0000_70_cluster-network-operator_01_egr_crd.yaml
[source,yaml,subs="attributes+"]
----
apiVersion: network.operator.openshift.io/v1
kind: EgressRouter
metadata:
  name: <egress_router_name>
  namespace: <namespace>  <.>
spec:
  addresses: [  <.>
    {
      ip: "<egress_router>",  <.>
      gateway: "<egress_gateway>"  <.>
    }
  ]
  mode: Redirect
  redirect: {
    redirectRules: [  <.>
      {
        destinationIP: "<egress_destination>",
        port: <egress_router_port>,
        targetPort: <target_port>,  <.>
        protocol: <network_protocol>  <.>
      },
      ...
    ],
    fallbackIP: "<egress_destination>" <.>
  }
----
// openshift/api:networkoperator/v1/001-egressrouter.crd.yaml
<.> Optional: The `namespace` field specifies the namespace to create the egress router in. If you do not specify a value in the file or on the command line, the `default` namespace is used.

<.> The `addresses` field specifies the IP addresses to configure on the secondary network interface.

<.> The `ip` field specifies the reserved source IP address and netmask from the physical network that the node is on to use with egress router pod. Use CIDR notation to specify the IP address and netmask.

<.> The `gateway` field specifies the IP address of the network gateway.

<.> Optional: The `redirectRules` field specifies a combination of egress destination IP address, egress router port, and protocol. Incoming connections to the egress router on the specified port and protocol are routed to the destination IP address.

<.> Optional: The `targetPort` field specifies the network port on the destination IP address. If this field is not specified, traffic is routed to the same network port that it arrived on.

<.> The `protocol` field supports TCP, UDP, or SCTP.

<.> Optional: The `fallbackIP` field specifies a destination IP address. If you do not specify any redirect rules, the egress router sends all traffic to this fallback IP address. If you specify redirect rules, any connections to network ports that are not defined in the rules are sent by the egress router to this fallback IP address. If you do not specify this field, the egress router rejects connections to network ports that are not defined in the rules.

.Example egress router specification
[source,yaml,subs="attributes+"]
----
apiVersion: network.operator.openshift.io/v1
kind: EgressRouter
metadata:
  name: {router-name}
spec:
  networkInterface: {
    macvlan: {
      mode: "Bridge"
    }
  }
  addresses: [
    {
      ip: "192.168.12.99/24",
      gateway: "192.168.12.1"
    }
  ]
  mode: Redirect
  redirect: {
    redirectRules: [
      {
        destinationIP: "10.0.0.99",
        port: 80,
        protocol: UDP
      },
      {
        destinationIP: "203.0.113.26",
        port: 8080,
        targetPort: 80,
        protocol: TCP
      },
      {
        destinationIP: "203.0.113.27",
        port: 8443,
        targetPort: 443,
        protocol: TCP
      }
    ]
  }
----

// clear temporary attributes
:!router-name:
:!router-type:
ifdef::redirect[]
:!redirect:
endif::[]
