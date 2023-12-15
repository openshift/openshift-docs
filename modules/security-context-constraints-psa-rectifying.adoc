// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

:_mod-docs-content-type: CONCEPT
[id="security-context-constraints-psa-rectifying_{context}"]
= About pod security admission alerts

A `PodSecurityViolation` alert is triggered when the Kubernetes API server reports that there is a pod denial on the audit level of the pod security admission controller. This alert persists for one day.

View the Kubernetes API server audit logs to investigate alerts that were triggered. As an example, a workload is likely to fail admission if global enforcement is set to the `restricted` pod security level.

For assistance in identifying pod security admission violation audit events, see link:https://kubernetes.io/docs/reference/labels-annotations-taints/audit-annotations/#pod-security-kubernetes-io-audit-violations[Audit annotations] in the Kubernetes documentation.
