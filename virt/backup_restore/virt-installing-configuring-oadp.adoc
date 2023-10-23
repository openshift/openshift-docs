:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="virt-installing-configuring-oadp"]
= Installing and configuring OADP
:context: virt-installing-configuring-oadp
:virt-installing-configuring-oadp:
:credentials: cloud-credentials
:provider: gcp

toc::[]

As a cluster administrator, you install the OpenShift API for Data Protection (OADP) by installing the OADP Operator. The Operator installs link:https://{velero-domain}/docs/v{velero-version}/[Velero {velero-version}].

You create a default `Secret` for your backup storage provider and then you install the Data Protection Application.

include::modules/oadp-installing-operator.adoc[leveloffset=+1]

include::modules/oadp-about-backup-snapshot-locations-secrets.adoc[leveloffset=+1]
include::modules/oadp-creating-default-secret.adoc[leveloffset=+2]
include::modules/oadp-secrets-for-different-credentials.adoc[leveloffset=+2]

[id="configuring-dpa-ocs"]
== Configuring the Data Protection Application

You can configure the Data Protection Application by setting Velero resource allocations or enabling self-signed CA certificates.

include::modules/oadp-setting-resource-limits-and-requests.adoc[leveloffset=+2]
include::modules/oadp-self-signed-certificate.adoc[leveloffset=+2]

include::modules/oadp-installing-dpa-1-2-and-earlier.adoc[leveloffset=+1]
include::modules/oadp-installing-dpa-1-3.adoc[leveloffset=+1]
include::modules/oadp-enabling-csi-dpa.adoc[leveloffset=+2]

[id="uninstalling-oadp_{context}"]
== Uninstalling OADP

You uninstall the OpenShift API for Data Protection (OADP) by deleting the OADP Operator. See xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-cluster[Deleting Operators from a cluster] for details.

:virt-installing-configuring-oadp!:
