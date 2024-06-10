// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc
// * operators/operator_sdk/osdk-complying-with-psa.adoc

:_mod-docs-content-type: CONCEPT
[id="security-context-constraints-psa-synchronization_{context}"]
= About pod security admission synchronization

In addition to the global pod security admission control configuration, a controller applies pod security admission control `warn` and `audit` labels to namespaces according to the SCC permissions of the service accounts that are in a given namespace.

The controller examines `ServiceAccount` object permissions to use security context constraints in each namespace. Security context constraints (SCCs) are mapped to pod security profiles based on their field values; the controller uses these translated profiles. Pod security admission `warn` and `audit` labels are set to the most privileged pod security profile in the namespace to prevent displaying warnings and logging audit events when pods are created.

Namespace labeling is based on consideration of namespace-local service account privileges.

Applying pods directly might use the SCC privileges of the user who runs the pod. However, user privileges are not considered during automatic labeling.
