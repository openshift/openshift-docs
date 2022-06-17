// Module included in the following assemblies:
//
// * networking/openshift_sdn/deploying-egress-router-layer3-redirection.adoc
// * networking/openshift_sdn/deploying-egress-router-http-redirection.adoc
// * networking/openshift_sdn/deploying-egress-router-dns-redirection.adoc

// Every redirection mode supports an expanded environment variable

// Conditional per flavor of Pod
ifeval::["{context}" == "deploying-egress-router-layer3-redirection"]
:redirect:
endif::[]
ifeval::["{context}" == "deploying-egress-router-http-redirection"]
:http:
endif::[]
ifeval::["{context}" == "deploying-egress-router-dns-redirection"]
:dns:
endif::[]

[id="nw-egress-router-dest-var_{context}"]
= Egress destination configuration format

ifdef::redirect[]
When an egress router pod is deployed in redirect mode, you can specify redirection rules by using one or more of the following formats:

- `<port> <protocol> <ip_address>` - Incoming connections to the given `<port>` should be redirected to the same port on the given `<ip_address>`. `<protocol>` is either `tcp` or `udp`.
- `<port> <protocol> <ip_address> <remote_port>` - As above, except that the connection is redirected to a different `<remote_port>` on `<ip_address>`.
- `<ip_address>` - If the last line is a single IP address, then any connections on any other port will be redirected to the corresponding port on that IP address. If there is no fallback IP address then connections on other ports are rejected.

In the example that follows several rules are defined:

- The first line redirects traffic from local port `80` to port `80` on `203.0.113.25`.
- The second and third lines redirect local ports `8080` and `8443` to remote ports `80` and `443` on `203.0.113.26`.
- The last line matches traffic for any ports not specified in the previous rules.

.Example configuration
[source,text]
----
80   tcp 203.0.113.25
8080 tcp 203.0.113.26 80
8443 tcp 203.0.113.26 443
203.0.113.27
----
endif::redirect[]

ifdef::http[]
When an egress router pod is deployed in HTTP proxy mode, you can specify redirection rules by using one or more of the following formats. Each line in the configuration specifies one group of connections to allow or deny:

- An IP address allows connections to that IP address, such as `192.168.1.1`.
- A CIDR range allows connections to that CIDR range, such as `192.168.1.0/24`.
- A hostname allows proxying to that host, such as `www.example.com`.
- A domain name preceded by `+*.+` allows proxying to that domain and all of its subdomains, such as `*.example.com`.
- A `!` followed by any of the previous match expressions denies the connection instead.
- If the last line is `*`, then anything that is not explicitly denied is allowed. Otherwise, anything that is not allowed is denied.

You can also use `*` to allow connections to all remote destinations.

.Example configuration
[source,text]
----
!*.example.com
!192.168.1.0/24
192.168.2.1
*
----
endif::http[]

ifdef::dns[]
When the router is deployed in DNS proxy mode, you specify a list of port and destination mappings. A destination may be either an IP address or a DNS name.

An egress router pod supports the following formats for specifying port and destination mappings:

Port and remote address::

You can specify a source port and a destination host by using the two field format: `<port> <remote_address>`.

The host can be an IP address or a DNS name. If a DNS name is provided, DNS resolution occurs at runtime. For a given host, the proxy connects to the specified source port on the destination host when connecting to the destination host IP address.

.Port and remote address pair example
[source,text]
----
80 172.16.12.11
100 example.com
----

Port, remote address, and remote port::

You can specify a source port, a destination host, and a destination port by using the three field format: `<port> <remote_address> <remote_port>`.

The three field format behaves identically to the two field version, with the exception that the destination port can be different than the source port.

.Port, remote address, and remote port example
[source,text]
----
8080 192.168.60.252 80
8443 web.example.com 443
----
endif::dns[]

// unload flavors
ifdef::redirect[]
:!redirect:
endif::[]
ifdef::http[]
:!http:
endif::[]
ifdef::dns[]
:!dns:
endif::[]
