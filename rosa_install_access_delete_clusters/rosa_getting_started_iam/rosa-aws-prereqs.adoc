:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: prerequisites

[id="prerequisites"]
= AWS prerequisites for ROSA

toc::[]

{product-title} (ROSA) provides a model that allows Red Hat to deploy clusters into a customer’s existing Amazon Web Service (AWS) account.

You must ensure that the prerequisites are met before installing ROSA. This requirements document does not apply to AWS Security Token Service (STS). If you are using STS, see the xref:../../rosa_planning/rosa-sts-aws-prereqs.adoc#rosa-aws-prereqs_rosa-sts-aws-prereqs[STS-specific requirements].

include::snippets/rosa-sts.adoc[]

include::modules/rosa-aws-requirements.adoc[leveloffset=+1]
include::modules/rosa-aws-procedure.adoc[leveloffset=+1]
include::modules/rosa-aws-scp.adoc[leveloffset=+2]
include::modules/rosa-aws-iam.adoc[leveloffset=+1]
include::modules/rosa-aws-provisioned.adoc[leveloffset=+1]
include::modules/osd-aws-privatelink-firewall-prerequisites.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../support/remote_health_monitoring/about-remote-health-monitoring.adoc#about-remote-health-monitoring[About remote health monitoring]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc#rosa-security-groups_prerequisites[Security groups]
* xref:../../rosa_planning/rosa-sts-required-aws-service-quotas.adoc#rosa-sts-required-aws-service-quotas[Required AWS service quotas]

== Next steps
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-required-aws-service-quotas.adoc#rosa-required-aws-service-quotas[Review the required AWS service quotas]

[role="_additional-resources"]
== Additional resources
* xref:../../rosa_planning/rosa-limits-scalability.adoc#rosa-limits-scalability[Limits and scalability]
* xref:../../rosa_architecture/rosa_policy_service_definition/rosa-policy-process-security.adoc#rosa-policy-sre-access_rosa-policy-process-security[SRE access to all Red Hat OpenShift Service on AWS clusters]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-getting-started-workflow.adoc#rosa-understanding-the-deployment-workflow[Understanding the ROSA deployment workflow]
