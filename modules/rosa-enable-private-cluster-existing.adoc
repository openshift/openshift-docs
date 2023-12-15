// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-private-cluster.adoc


:_mod-docs-content-type: PROCEDURE
[id="rosa-enabling-private-cluster-existing_{context}"]
= Enabling private cluster on an existing cluster

After a cluster has been created, you can later enable the cluster to be private.

[IMPORTANT]
====
Private clusters cannot be used with AWS security token service (STS). However, STS supports AWS PrivateLink clusters.
====

.Prerequisites

AWS VPC Peering, VPN, DirectConnect, or link:https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html[TransitGateway] has been configured to allow private access.

.Procedure

Enter the following command to enable the `--private` option on an existing cluster.

[source,terminal]
----
$ rosa edit cluster --cluster=<cluster_name> --private
----

[NOTE]
====
Transitioning your cluster between private and public can take several minutes to complete.
====
