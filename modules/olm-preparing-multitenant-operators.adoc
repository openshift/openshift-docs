// Module included in the following assemblies:
//
// * operators/admin/olm-adding-operators-to-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-preparing-operators-multitenant_{context}"]
= Preparing for multiple instances of an Operator for multitenant clusters

ifndef::openshift-dedicated,openshift-rosa[]
As a cluster administrator,
endif::[]
ifdef::openshift-dedicated,openshift-rosa[]
As an administrator with the `dedicated-admin` role,
endif::openshift-dedicated,openshift-rosa[]
you can add multiple instances of an Operator for use in multitenant clusters. This is an alternative solution to either using the standard *All namespaces* install mode, which can be considered to violate the principle of least privilege, or the *Multinamespace* mode, which is not widely adopted. For more information, see "Operators in multitenant clusters".

In the following procedure, the _tenant_ is a user or group of users that share common access and privileges for a set of deployed workloads. The _tenant Operator_ is the instance of an Operator that is intended for use by only that tenant.

.Prerequisites

ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]
* All instances of the Operator you want to install must be the same version across a given cluster.
+
[IMPORTANT]
====
For more information on this and other limitations, see "Operators in multitenant clusters".
====

.Procedure

// In OSD/ROSA, dedicated-admins can't create namespaces directly but can create projects.
ifndef::openshift-dedicated,openshift-rosa[]
. Before installing the Operator, create a namespace for the tenant Operator that is separate from the tenant's namespace. For example, if the tenant's namespace is `team1`, you might create a `team1-operator` namespace:

.. Define a `Namespace` resource and save the YAML file, for example, `team1-operator.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: team1-operator
----

.. Create the namespace by running the following command:
+
[source,terminal]
----
$ oc create -f team1-operator.yaml
----
endif::openshift-dedicated,openshift-rosa[]
// Slightly different step for OSD/ROSA since dedicated-admins can't create namespaces directly.
ifdef::openshift-dedicated,openshift-rosa[]
. Before installing the Operator, create a namespace for the tenant Operator that is separate from the tenant's namespace. You can do this by creating a project. For example, if the tenant's namespace is `team1`, you might create a `team1-operator` project:
+
[source,terminal]
----
$ oc new-project team1-operator
----
endif::openshift-dedicated,openshift-rosa[]

. Create an Operator group for the tenant Operator scoped to the tenant's namespace, with only that one namespace entry in the `spec.targetNamespaces` list:

.. Define an `OperatorGroup` resource and save the YAML file, for example, `team1-operatorgroup.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: team1-operatorgroup
  namespace: team1-operator
spec:
  targetNamespaces:
  - team1 <1>
----
<1> Define only the tenant's namespace in the `spec.targetNamespaces` list.

.. Create the Operator group by running the following command:
+
[source,terminal]
----
$ oc create -f team1-operatorgroup.yaml
----

