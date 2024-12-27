:_mod-docs-content-type: SNIPPET
[IMPORTANT]
====
The following guidelines are based on internal lab benchmark testing only and do not represent a complete real-world host specification.
====

.Representative three-node hub cluster machine specifications
[cols=2*, width="90%", options="header"]
|====
|Requirement
|Description

|{product-title}
|version 4.13

|{rh-rhacm}
|version 2.7

|{cgu-operator-first}
|version 4.13

|Server hardware
|3 x Dell PowerEdge R650 rack servers

|NVMe hard disks
a|* 50 GB disk for `/var/lib/etcd`
* 2.9 TB disk for `/var/lib/containers`

|SSD hard disks
a|* 1 SSD split into 15 200GB thin-provisioned logical volumes provisioned as `PV` CRs
* 1 SSD serving as an extra large `PV` resource

|Number of applied DU profile policies
|5
|====

[IMPORTANT]
====
The following network specifications are representative of a typical real-world RAN network and were applied to the scale lab environment during testing.
====

.Simulated lab environment network specifications
[cols=2*, width="90%", options="header"]
|====
|Specification
|Description

|Round-trip time (RTT) latency
|50 ms

|Packet loss
|0.02% packet loss

|Network bandwidth limit
|20 Mbps
|====
