// Module included in the following assemblies:
//
// * microshift/using-config-tools.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-config-yaml_{context}"]
= Using a YAML configuration file

On start up, {microshift-short} searches the system-wide `/etc/microshift/` directory for a configuration file named `config.yaml`. To use custom configurations, you must create the configuration file and specify any settings that should override the defaults before starting {microshift-short}.

[id="microshift-yaml-default_{context}"]
== Default settings
If you do not create a `config.yaml` file, the default values are used. The following example shows the default configuration settings.

* You can use the following command to see the default values:
+
[source,terminal]
----
$ microshift show-config
----
+
.Default values example output in YAML form
[source,yaml]
----
dns:
  baseDomain: microshift.example.com <1>
network:
  clusterNetwork:
    - 10.42.0.0/16 <2>
  serviceNetwork:
    - 10.43.0.0/16 <3>
  serviceNodePortRange: 30000-32767 <4>
node:
  hostnameOverride: "" <5>
  nodeIP: "" <6>
apiServer:
  advertiseAddress: 10.44.0.0 <7>
  subjectAltNames: [] <8>
debugging:
  logLevel: "Normal" <9>
----
<1> Base domain of the cluster. All managed DNS records will be subdomains of this base.
<2> A block of IP addresses from which Pod IP addresses are allocated.
<3> A block of virtual IP addresses for Kubernetes services.
<4> The port range allowed for Kubernetes services of type NodePort.
<5> The name of the node. The default value is the hostname.
<6> The IP address of the node. The default value is the IP address of the default route.
<7> A string that specifies the IP address from which the API server is advertised to members of the cluster. The default value is calculated based on the address of the service network.
<8> Subject Alternative Names for API server certificates.
<9> Log verbosity. Valid values for this field are `Normal`, `Debug`, `Trace`, or `TraceAll`.

[id="microshift-yaml-custom_{context}"]
== Custom settings
To create custom configurations, you must create a `config.yaml` file in the `/etc/microshift/` directory, then change any settings that should override the defaults before starting or restarting {microshift-short}.

[IMPORTANT]
====
Restart {microshift-short} after changing any configuration settings to have them take effect. The `config.yaml` file is read only when {microshift-short} starts.
====

[id="microshift-yaml-advertiseAddress_{context}"]
=== advertiseAddress
The `apiserver.advertiseAddress` flag specifies the IP address on which to advertise the API server to members of the cluster. This address must be reachable by the cluster. You can set a custom IP address here, but you must also add the IP address to a host interface. Customizing this parameter preempts {microshift-short} from adding a default IP address to the `br-ex` network interface.

[IMPORTANT]
====
If you customize the `advertiseAddress` IP address, make sure it is reachable by the cluster when {microshift-short} starts by adding the IP address to a host interface.
====

If unset, the default value is `10.44.0.0/32`. It will be set to the next immediate subnet after the service network. For example, when the service network is `10.43.0.0/16`, the `advertiseAddress` is set to `10.44.0.0/32`.
