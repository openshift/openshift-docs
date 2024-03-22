:_mod-docs-content-type: ASSEMBLY
[id="telco-ran-ref-du-crs"]
= {rds-first} reference configuration CRs
:telco-ran:
:context: ran-ref-design-crs
include::_attributes/common-attributes.adoc[]

toc::[]

Use the following custom resources (CRs) to configure and deploy {product-title} clusters with the {rds} profile.
Some of the CRs are optional depending on your requirements.
CR fields you can change are annotated in the CR with YAML comments.

[NOTE]
====
You can extract the complete set of RAN DU CRs from the `ztp-site-generate` container image.
See link:https://docs.openshift.com/container-platform/latest/scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.html#ztp-preparing-the-ztp-git-repository_ztp-preparing-the-hub-cluster[Preparing the GitOps ZTP site configuration repository] for more information.
====

include::modules/telco-ran-crs-day-2-operators.adoc[leveloffset=+1]

include::modules/telco-ran-crs-cluster-tuning.adoc[leveloffset=+1]

include::modules/telco-ran-crs-machine-configuration.adoc[leveloffset=+1]

[id="telco-reference-ran-du-use-case-yaml_{context}"]
== YAML reference

The following is a complete reference for all the custom resources (CRs) that make up the {rds} {product-version} reference configuration.

include::modules/telco-ran-yaml-ref-day-2-operators.adoc[leveloffset=+2]

include::modules/telco-ran-yaml-ref-cluster-tuning.adoc[leveloffset=+2]

include::modules/telco-ran-yaml-ref-machine-configuration.adoc[leveloffset=+2]

:!telco-ran:
