
:_mod-docs-content-type: ASSEMBLY
[id="osdk-complying-with-psa"]
= Complying with pod security admission
include::_attributes/common-attributes.adoc[]
:context: osdk-complying-with-psa

toc::[]

_Pod security admission_ is an implementation of the link:https://kubernetes.io/docs/concepts/security/pod-security-standards/[Kubernetes pod security standards]. link:https://kubernetes.io/docs/concepts/security/pod-security-admission/[Pod security admission] restricts the behavior of pods. Pods that do not comply with the pod security admission defined globally or at the namespace level are not admitted to the cluster and cannot run.

If your Operator project does not require escalated permissions to run, you can ensure your workloads run in namespaces set to the `restricted` pod security level. If your Operator project requires escalated permissions to run, you must set the following security context configurations:

* The allowed pod security admission level for the Operator's namespace
* The allowed security context constraints (SCC) for the workload's service account

For more information, see xref:../../authentication/understanding-and-managing-pod-security-admission.adoc#understanding-and-managing-pod-security-admission[Understanding and managing pod security admission].

// About pod security admission
include::modules/security-context-constraints-psa-about.adoc[leveloffset=+1]

include::modules/security-context-constraints-psa-synchronization.adoc[leveloffset=+1]

// Pod security admission synchronization namespace exclusions
include::modules/security-context-constraints-psa-sync-exclusions.adoc[leveloffset=+2]

include::modules/osdk-ensuring-operator-workloads-run-restricted-psa.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../authentication/managing-security-context-constraints.adoc#managing-security-context-constraints[Managing security context constraints]

include::modules/osdk-managing-psa-for-operators-with-escalated-permissions.adoc[leveloffset=+1]

[id="osdk-complying-with-psa-additional-resources"]
[role="_additional-resources"]
== Additional resources

* xref:../../authentication/understanding-and-managing-pod-security-admission.adoc#understanding-and-managing-pod-security-admission[Understanding and managing pod security admission]
