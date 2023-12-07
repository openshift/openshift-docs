:_mod-docs-content-type: ASSEMBLY
[id="installing-openstack-troubleshooting"]
= Troubleshooting
include::_attributes/common-attributes.adoc[]
:context: installing-openstack-troubleshooting

toc::[]

//Very much a WIP. Chop up sections into mod docs as they're finalized.

In the event of a failure in {product-title} on OpenStack installation, you can recover by understanding the likely failure modes and then starting to troubleshoot the problem.

== View OpenStack instance logs

== Prerequisites

* OpenStack CLI tools are installed

.Procedure

. In a terminal window, run `openstack console log show <instance>`

The console logs appear.

== SSH access to an instance

== Prerequisites

* OpenStack CLI tools are installed

.Procedure

. Get the IP address of the node on the private network:
+
[source,terminal]
----
$ openstack server list | grep master
----
+
.Example output
[source,terminal]
----
| 0dcd756b-ad80-42f1-987a-1451b1ae95ba | cluster-wbzrr-master-1     | ACTIVE    | cluster-wbzrr-openshift=172.24.0.21                | rhcos           | m1.s2.xlarge |
| 3b455e43-729b-4e64-b3bd-1d4da9996f27 | cluster-wbzrr-master-2     | ACTIVE    | cluster-wbzrr-openshift=172.24.0.18                | rhcos           | m1.s2.xlarge |
| 775898c3-ecc2-41a4-b98b-a4cd5ae56fd0 | cluster-wbzrr-master-0     | ACTIVE    | cluster-wbzrr-openshift=172.24.0.12                | rhcos           | m1.s2.xlarge |
----

. Connect to the instance from the master that holds the API VIP (and API FIP) as a jumpbox:
+
[source,terminal]
----
$ ssh -J core@${FIP} core@<host>
----
