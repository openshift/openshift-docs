// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-locating-the-tang-servers_{context}"]
= Tang server location planning

When planning your Tang server environment, consider the physical and network locations of the Tang servers.

Physical location::
The geographic location of the Tang servers is relatively unimportant, as long as they are suitably secured from unauthorized access or theft and offer the required availability and accessibility to run a critical service.
+
Nodes with Clevis clients do not require local Tang servers as long as the Tang servers are available at all times.  Disaster recovery requires both redundant power and redundant network connectivity to Tang servers regardless of their location.

Network location::
Any node with network access to the Tang servers can decrypt their own disk partitions, or any other disks encrypted by the same Tang servers.
+
Select network locations for the Tang servers that ensure the presence or absence of network connectivity from a given host allows for permission to decrypt.  For example, firewall protections might be in place to prohibit access from any type of guest or public network, or any network jack located in an unsecured area of the building.
+
Additionally, maintain network segregation between production and development networks. This assists in defining appropriate network locations and adds an additional layer of security.
+
Do not deploy Tang servers on the same resource, for example, the same `rolebindings.rbac.authorization.k8s.io` cluster, that they are responsible for unlocking. However, a cluster of Tang servers and other security resources can be a useful configuration to enable support of multiple additional clusters and cluster resources.
