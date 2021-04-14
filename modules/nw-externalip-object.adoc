// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-externalip.adoc

[id="nw-externalip-object_{context}"]
= ExternalIP address block configuration

The configuration for ExternalIP address blocks is defined by a Network custom resource (CR) named `cluster`. The Network CR is part of the `config.openshift.io` API group.

[IMPORTANT]
====
During cluster installation, the Cluster Version Operator (CVO) automatically creates a Network CR named `cluster`.
Creating any other CR objects of this type is not supported.
====

The following YAML describes the ExternalIP configuration:

.Network.config.openshift.io CR named `cluster`
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  externalIP:
    autoAssignCIDRs: [] <1>
    policy: <2>
      ...
----
<1> Defines the IP address block in CIDR format that is available for automatic assignment of external IP addresses to a service.
Only a single IP address range is allowed.

<2> Defines restrictions on manual assignment of an IP address to a service.
If no restrictions are defined, specifying the `spec.externalIP` field in a `Service` object is not allowed.
By default, no restrictions are defined.

The following YAML describes the fields for the `policy` stanza:

.Network.config.openshift.io `policy` stanza
[source,yaml]
----
policy:
  allowedCIDRs: [] <1>
  rejectedCIDRs: [] <2>
----
<1> A list of allowed IP address ranges in CIDR format.
<2> A list of rejected IP address ranges in CIDR format.

[discrete]
== Example external IP configurations

Several possible configurations for external IP address pools are displayed in the following examples:

- The following YAML describes a configuration that enables automatically assigned external IP addresses:
+
.Example configuration with `spec.externalIP.autoAssignCIDRs` set
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  ...
  externalIP:
    autoAssignCIDRs:
    - 192.168.132.254/29
----

- The following YAML configures policy rules for the allowed and rejected CIDR ranges:
+
.Example configuration with `spec.externalIP.policy` set
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  ...
  externalIP:
    policy:
      allowedCIDRs:
      - 192.168.132.0/29
      - 192.168.132.8/29
      rejectedCIDRs:
      - 192.168.132.7/32
----
