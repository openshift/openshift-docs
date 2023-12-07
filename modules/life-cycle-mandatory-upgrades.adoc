// Module included in the following assemblies:
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

ifeval::["{context}" == "rosa-hcp-life-cycle"]
:rosa-with-hcp:
endif::[]

:_mod-docs-content-type: REFERENCE
[id="rosa-mandatory-upgrades_{context}"]
= Mandatory upgrades

If a critical or important CVE, or other bug identified by Red Hat, significantly impacts the security or stability of the cluster, the customer must upgrade to the next supported patch release within two link:https://access.redhat.com/articles/2623321[business days].

In extreme circumstances and based on Red Hat's assessment of the CVE criticality to the environment, Red Hat will notify customers that they have two link:https://access.redhat.com/articles/2623321[business days] to schedule or manually update their cluster to the latest, secure patch release. In the case that an update is not performed after two link:https://access.redhat.com/articles/2623321[business days], Red Hat will automatically update the
ifdef::rosa-with-hcp[]
cluster's control plane
endif::rosa-with-hcp[]
ifndef::rosa-with-hcp[]
cluster
endif::rosa-with-hcp[]
to the latest, secure patch release to mitigate potential security breach(es) or instability. Red Hat might, at its own discretion, temporarily delay an automated update if requested by a customer through a link:https://access.redhat.com/support[support case].

ifeval::["{context}" == "rosa-hcp-life-cycle"]
:!rosa-with-hcp:
endif::[]