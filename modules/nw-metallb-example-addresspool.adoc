// Module included in the following assemblies:
//
// * networking/metallb/metallb-configure-address-pools.adoc

[id="nw-metallb-example-addresspool_{context}"]
= Example address pool configurations

== Example: IPv4 and CIDR ranges

You can specify a range of IP addresses in CIDR notation.
You can combine CIDR notation with the notation that uses a hyphen to separate lower and upper bounds.

[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-cidr
  namespace: metallb-system
spec:
  addresses:
  - 192.168.100.0/24
  - 192.168.200.0/24
  - 192.168.255.1-192.168.255.5
----

== Example: Reserve IP addresses

You can set the `autoAssign` field to `false` to prevent MetalLB from automatically assigning the IP addresses from the pool.
When you add a service, you can request a specific IP address from the pool or you can specify the pool name in an annotation to request any IP address from the pool.

[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-reserved
  namespace: metallb-system
spec:
  addresses:
  - 10.0.100.0/28
  autoAssign: false
----

== Example: IPv4 and IPv6 addresses

You can add address pools that use IPv4 and IPv6.
You can specify multiple ranges in the `addresses` list, just like several IPv4 examples.

Whether the service is assigned a single IPv4 address, a single IPv6 address, or both is determined by how you add the service.
The `spec.ipFamilies` and `spec.ipFamilyPolicy` fields control how IP addresses are assigned to the service.

[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-combined
  namespace: metallb-system
spec:
  addresses:
  - 10.0.100.0/28
  - 2002:2:2::1-2002:2:2::100
----

== Example: Assign IP address pools to services or namespaces
You can assign IP addresses from an `IPAddressPool` to services and namespaces that you specify.

If you assign a service or namespace to more than one IP address pool, MetalLB uses an available IP address from the higher-priority IP address pool. If no IP addresses are available from the assigned IP address pools with a high priority, MetalLB uses available IP addresses from an IP address pool with lower priority or no priority. 

[NOTE]
====
You can use the `matchLabels` label selector, the `matchExpressions` label selector, or both, for the `namespaceSelectors` and `serviceSelectors` specifications. This example demonstrates one label selector for each specification.
====

[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-service-allocation
  namespace: metallb-system
spec:
  addresses:
    - 192.168.20.0/24
  serviceAllocation:
    priority: 50 <1>
    namespaces: <2>
      - namespace-a 
      - namespace-b
    namespaceSelectors: <3>
      - matchLabels:
          zone: east 
    serviceSelectors: <4>
      - matchExpressions: 
        - key: security 
          operator: In 
          values:
          - S1 
----
<1> Assign a priority to the address pool. A lower number indicates a higher priority.
<2> Assign one or more namespaces to the IP address pool in a list format.
<3> Assign one or more namespace labels to the IP address pool by using label selectors in a list format.
<4> Assign one or more service labels to the IP address pool by using label selectors in a list format.
 
