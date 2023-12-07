// Module included in the following assemblies:
//
// * operators/understanding/olm-multitenancy.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-multitenancy-solution_{context}"]
= Recommended solution for multitenant clusters

While a *Multinamespace* install mode does exist, it is supported by very few Operators. As a middle ground solution between the standard *All namespaces* and *Single namespace* install modes, you can install multiple instances of the same Operator, one for each tenant, by using the following workflow:

// In OSD/ROSA, dedicated-admins can create projects, but not namespaces.
ifndef::openshift-dedicated,openshift-rosa[]
. Create a namespace for the tenant Operator that is separate from the tenant's namespace.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
. Create a namespace for the tenant Operator that is separate from the tenant's namespace. You can do this by creating a project.
endif::openshift-dedicated,openshift-rosa[]

. Create an Operator group for the tenant Operator scoped only to the tenant's namespace.
. Install the Operator in the tenant Operator namespace.

As a result, the Operator resides in the tenant Operator namespace and watches the tenant namespace, but neither the Operator's pod nor its service account are visible or usable by the tenant.

This solution provides better tenant separation, least privilege principle at the cost of resource usage, and additional orchestration to ensure the constraints are met. For a detailed procedure, see "Preparing for multiple instances of an Operator for multitenant clusters".

.Limitations and considerations

This solution only works when the following constraints are met:

* All instances of the same Operator must be the same version.
* The Operator cannot have dependencies on other Operators.
* The Operator cannot ship a CRD conversion webhook.

[IMPORTANT]
====
You cannot use different versions of the same Operator on the same cluster. Eventually, the installation of another instance of the Operator would be blocked when it meets the following conditions:

* The instance is not the newest version of the Operator.
* The instance ships an older revision of the CRDs that lack information or versions that newer revisions have that are already in use on the cluster.
====

// In OSD/ROSA, tenants shouldn't be able to install Operators. Dedicated-admins can, but they can't grant non-admin users the ability to install their own Operators.
ifndef::openshift-dedicated,openshift-rosa[]
[WARNING]
====
As an administrator, use caution when allowing non-cluster administrators to install Operators self-sufficiently, as explained in "Allowing non-cluster administrators to install Operators". These tenants should only have access to a curated catalog of Operators that are known to not have dependencies. These tenants must also be forced to use the same version line of an Operator, to ensure the CRDs do not change. This requires the use of namespace-scoped catalogs and likely disabling the global default catalogs.
====
endif::openshift-dedicated,openshift-rosa[]
