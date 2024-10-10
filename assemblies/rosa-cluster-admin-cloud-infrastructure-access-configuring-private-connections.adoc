:_mod-docs-content-type: ASSEMBLY
[id="rosa-configuring-private-connections"]
= Configuring private connections
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-configuring-private-connections

toc::[]

Private cluster access can be implemented to suit the needs of your {product-title} (ROSA) environment.

.Procedure
. Access your ROSA AWS account and use one or more of the following methods to establish a private connection to your cluster:

- xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc#dedicated-aws-peering[Configuring AWS VPC peering]: Enable VPC peering to route network traffic between two private IP addresses.

- xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-vpn.adoc#dedicated-aws-vpn[Configuring AWS VPN]: Establish a Virtual Private Network to securely connect your private network to your Amazon Virtual Private Cloud.

- xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-dc.adoc#dedicated-aws-dc[Configuring AWS Direct Connect]: Configure AWS Direct Connect to establish a dedicated network connection between your private network and an AWS Direct Connect location.

. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-private-cluster.adoc#rosa-private-cluster[Configure a private cluster on ROSA].