:_mod-docs-content-type: ASSEMBLY
:context: dedicated-understanding-aws
[id="welcome-index"]
= Understanding cloud infrastructure access
include::_attributes/common-attributes.adoc[]

Amazon Web Services (AWS) infrastructure access permits
link:https://access.redhat.com/node/3610411[Customer Portal Organization Administrators]
and cluster owners to enable AWS Identity and Access Management (IAM) users to
have federated access to the AWS Management Console for their {product-title}
cluster.

[id="enabling-aws-access"]
== Enabling AWS access
AWS access can be granted for customer AWS users, and private cluster access can be implemented to suit the needs of your {product-title} environment.

Get started with xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-access.adoc#dedicated-aws-access[Accessing AWS infrastructure] for your {product-title} cluster. By creating an AWS user and account and providing that user with access to the {product-title} AWS account.

After you have access to the {product-title} AWS account, use one or more of the following methods to establish a private connection to your cluster:

- xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-peering.adoc#dedicated-aws-peering[Configuring AWS VPC peering]: Enable VPC peering to route network traffic between two private IP addresses.

- xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-vpn.adoc#dedicated-aws-vpn[Configuring AWS VPN]: Establish a Virtual Private Network to securely connect your private network to your Amazon Virtual Private Cloud.

- xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-dc.adoc#dedicated-aws-dc[Configuring AWS Direct Connect]: Configure AWS Direct Connect to establish a dedicated network connection between your private network and an AWS Direct Connect location.

After configuring your cloud infrastructure access, learn more about xref:../../rosa_cluster_admin/cloud_infrastructure_access/dedicated-aws-private-cluster.adoc#dedicated-aws-private-cluster[Configuring a private cluster].
