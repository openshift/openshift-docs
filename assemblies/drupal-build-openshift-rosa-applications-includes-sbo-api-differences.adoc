// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-api-differences_{context}"]
= API differences

The CRD of the {servicebinding-title} supports the following APIs:

* *Service Binding* with the `binding.operators.coreos.com` API group.
* *Service Binding (Spec API)* with the `servicebinding.io` API group.

Both of these API groups have similar features, but they are not completely identical. Here is the complete list of differences between these API groups:

[cols="1,1,1,1"]
|===
| Feature | Supported by the `binding.operators.coreos.com` API group | Supported by the `servicebinding.io` API group | Notes

| Binding to provisioned services
| Yes
| Yes
| Not applicable (N/A)

| Direct secret projection
| Yes
| Yes
| Not applicable (N/A)

| Bind as files
| Yes
| Yes
a| * Default behavior for the service bindings of the `servicebinding.io` API group
* Opt-in functionality for the service bindings of the `binding.operators.coreos.com` API group

| Bind as environment variables
| Yes
| Yes
a| * Default behavior for the service bindings of the `binding.operators.coreos.com` API group.
* Opt-in functionality for the service bindings of the `servicebinding.io` API group: Environment variables are created alongside files.

| Selecting workload with a label selector
| Yes
| Yes
| Not applicable (N/A)

| Detecting binding resources (`.spec.detectBindingResources`)
| Yes
| No
| The `servicebinding.io` API group has no equivalent feature.

| Naming strategies
| Yes
| No
| There is no current mechanism within the `servicebinding.io` API group to interpret the templates that naming strategies use.

| Container path
| Yes
| Partial
| Because a service binding of the `binding.operators.coreos.com` API group can specify mapping behavior within the `ServiceBinding` resource, the `servicebinding.io` API group cannot fully support an equivalent behavior without more information about the workload.

| Container name filtering
| No
| Yes
| The `binding.operators.coreos.com` API group has no equivalent feature.

| Secret path
| Yes
| No
| The `servicebinding.io` API group has no equivalent feature.

| Alternative binding sources (for example, binding data from annotations)
| Yes
| Allowed by {servicebinding-title}
| The specification requires support for getting binding data from provisioned services and secrets. However, a strict reading of the specification suggests that support for other binding data sources is allowed. Using this fact, {servicebinding-title} can pull the binding data from various sources (for example, pulling binding data from annotations). {servicebinding-title} supports these sources on both the API groups.
|===