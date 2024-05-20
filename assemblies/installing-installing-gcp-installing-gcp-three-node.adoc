:_mod-docs-content-type: ASSEMBLY
[id="installing-gcp-three-node"]
= Installing a three-node cluster on GCP
include::_attributes/common-attributes.adoc[]
:context: installing-gcp-three-node

toc::[]

In {product-title} version {product-version}, you can install a three-node cluster on Google Cloud Platform (GCP). A three-node cluster consists of three control plane machines, which also act as compute machines. This type of cluster provides a smaller, more resource efficient cluster, for cluster administrators and developers to use for testing, development, and production.

You can install a three-node cluster using either installer-provisioned or user-provisioned infrastructure.

include::modules/installation-three-node-cluster-cloud-provider.adoc[leveloffset=+1]

== Next steps
* xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#installing-gcp-customizations[Installing a cluster on GCP with customizations]
* xref:../../installing/installing_gcp/installing-gcp-user-infra.adoc#installing-gcp-user-infra[Installing a cluster on user-provisioned infrastructure in GCP by using Deployment Manager templates]
