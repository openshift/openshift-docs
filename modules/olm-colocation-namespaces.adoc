// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-colocation.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-colocation-namespaces_{context}"]
= Colocation of Operators in a namespace

Operator Lifecycle Manager (OLM) handles OLM-managed Operators that are installed in the same namespace, meaning their `Subscription` resources are colocated in the same namespace, as related Operators. Even if they are not actually related, OLM considers their states, such as their version and update policy, when any one of them is updated.

This default behavior manifests in two ways:

* `InstallPlan` resources of pending updates include `ClusterServiceVersion` (CSV) resources of all other Operators that are in the same namespace.
* All Operators in the same namespace share the same update policy. For example, if one Operator is set to manual updates, all other Operators' update policies are also set to manual.

These scenarios can lead to the following issues:

* It becomes hard to reason about install plans for Operator updates, because there are many more resources defined in them than just the updated Operator.
* It becomes impossible to have some Operators in a namespace update automatically while other are updated manually, which is a common desire for cluster administrators.

These issues usually surface because, when installing Operators with the {product-title} web console, the default behavior installs Operators that support the *All namespaces* install mode into the default `openshift-operators` global namespace.

ifndef::openshift-dedicated,openshift-rosa[]
As a cluster administrator,
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
As an administrator with the `dedicated-admin` role,
endif::openshift-dedicated,openshift-rosa[]
you can bypass this default behavior manually by using the following workflow:

ifndef::openshift-dedicated,openshift-rosa[]
. Create a namespace for the installation of the Operator.
endif::openshift-dedicated,openshift-rosa[]
// In OSD/ROSA, dedicated-admins can create projects, but not namespaces.
ifdef::openshift-dedicated,openshift-rosa[]
. Create a project for the installation of the Operator.
endif::openshift-dedicated,openshift-rosa[]
. Create a custom _global Operator group_, which is an Operator group that watches all namespaces. By associating this Operator group with the namespace you just created, it makes the installation namespace a global namespace, which makes Operators installed there available in all namespaces.
. Install the desired Operator in the installation namespace.

If the Operator has dependencies, the dependencies are automatically installed in the pre-created namespace. As a result, it is then valid for the dependency Operators to have the same update policy and shared install plans. For a detailed procedure, see "Installing global Operators in custom namespaces".
