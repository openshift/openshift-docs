:_mod-docs-content-type: ASSEMBLY
[id="cert-manager-authenticate-gcp"]
= Authenticating the {cert-manager-operator} with GCP Workload Identity
include::_attributes/common-attributes.adoc[]
:context: cert-manager-authenticate-gcp

toc::[]

You can authenticate the {cert-manager-operator} on the GCP Workload Identity cluster by using the cloud credentials. You can configure the cloud credentials by using the `ccoctl` binary.

include::modules/cert-manager-configure-cloud-credentials-gcp-sts.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_cert-manager-authenticate-gcp-workload-identity"]
== Additional resources
* xref:../../installing/installing_gcp/installing-gcp-customizations.adoc#cco-ccoctl-configuring_installing-gcp-customizations[Configuring the Cloud Credential Operator utility]