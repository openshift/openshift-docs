:_mod-docs-content-type: ASSEMBLY
[id="compliance-operator-remediation"]
= Managing Compliance Operator result and remediation
include::_attributes/common-attributes.adoc[]
:context: compliance-remediation

toc::[]

Each `ComplianceCheckResult` represents a result of one compliance rule check. If the rule can be remediated automatically, a `ComplianceRemediation` object with the same name, owned by the `ComplianceCheckResult` is created. Unless requested, the remediations are not applied automatically, which gives an {product-title} administrator the opportunity to review what the remediation does and only apply a remediation once it has been verified.

[IMPORTANT]
====
Full remediation for Federal Information Processing Standards (FIPS) compliance requires enabling FIPS mode for the cluster. To enable FIPS mode, you must run the installation program from a {op-system-base-full} computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/assembly_installing-the-system-in-fips-mode_security-hardening[Installing the system in FIPS mode].

FIPS mode is supported on the following architectures:

* `x86_64`
* `ppc64le`
* `s390x`
====

include::modules/compliance-filtering-results.adoc[leveloffset=+1]

include::modules/compliance-review.adoc[leveloffset=+1]

include::modules/compliance-apply-remediation-for-customized-mcp.adoc[leveloffset=+1]

include::modules/compliance-evaluate-kubeletconfig-rules.adoc[leveloffset=+1]

include::modules/compliance-custom-node-pools.adoc[leveloffset=+1]

include::modules/compliance-kubeletconfig-sub-pool-remediation.adoc[leveloffset=+1]

include::modules/compliance-applying.adoc[leveloffset=+1]

include::modules/compliance-manual.adoc[leveloffset=+1]

include::modules/compliance-updating.adoc[leveloffset=+1]

include::modules/compliance-unapplying.adoc[leveloffset=+1]

include::modules/compliance-removing-kubeletconfig.adoc[leveloffset=+1]

include::modules/compliance-inconsistent.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

*  xref:../../../nodes/nodes/nodes-nodes-managing.adoc#nodes-nodes-managing-about_nodes-nodes-managing[Modifying nodes].
