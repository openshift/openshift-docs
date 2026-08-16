// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-key-features_{context}"]
= Key features

* Exposal of binding data from services
** Based on annotations present in CRD, custom resources (CRs), or resources.
// ** Based on descriptors present in Operator Lifecycle Manager (OLM) descriptors.
// When the OLM descriptors are supported again, add this sentence.
* Workload projection
** Projection of binding data as files, with volume mounts.
** Projection of binding data as environment variables.
* Service Binding Options
** Bind backing services in a namespace that is different from the workload namespace.
** Project binding data into the specific container workloads.
** Auto-detection of the binding data from resources owned by the backing service CR.
** Compose custom binding data from the exposed binding data.
** Support for non-`PodSpec` compliant workload resources.
* Security
** Support for role-based access control (RBAC).