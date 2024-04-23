:_mod-docs-content-type: ASSEMBLY
[id="spo-seccomp"]
= Managing seccomp profiles
include::_attributes/common-attributes.adoc[]
:context: spo-seccomp

toc::[]

Create and manage seccomp profiles and bind them to workloads.

[IMPORTANT]
====
The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. Red Hat Enterprise Linux (RHEL) nodes are not supported.
====

include::modules/spo-creating-profiles.adoc[leveloffset=+1]

include::modules/spo-applying-profiles.adoc[leveloffset=+1]

include::modules/spo-binding-workloads.adoc[leveloffset=+2]

include::modules/spo-recording-profiles.adoc[leveloffset=+1]

include::modules/spo-container-profile-instances.adoc[leveloffset=+2]

[discrete]
[role="_additional-resources"]
[id="additional-resources_spo-seccomp"]
== Additional resources

* xref:../../authentication/managing-security-context-constraints.adoc[Managing security context constraints]
* link:https://cloud.redhat.com/blog/managing-sccs-in-openshift[Managing SCCs in OpenShift]
* xref:../../security/security_profiles_operator/spo-advanced.adoc#spo-log-enricher_spo-advanced[Using the log enricher]
* xref:../../security/security_profiles_operator/spo-understanding.adoc#spo-about_spo-understanding[About security profiles]