// Module included in the following assemblies:
//
// * architecture/control-plane.adoc

[id="olm-operators_{context}"]
= Add-on Operators

Operator Lifecycle Manager (OLM) and OperatorHub are default components in {product-title} that help manage Kubernetes-native applications as Operators. Together they provide the system for discovering, installing, and managing the optional add-on Operators available on the cluster.

Using OperatorHub in the {product-title} web console,
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
administrators with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
and authorized users can select Operators to install from catalogs of Operators. After installing an Operator from OperatorHub, it can be made available globally or in specific namespaces to run in user applications.

Default catalog sources are available that include Red Hat Operators, certified Operators, and community Operators.
ifndef::openshift-dedicated,openshift-rosa[]
Cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
Administrators with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
can also add their own custom catalog sources, which can contain a custom set of Operators.

ifdef::openshift-dedicated,openshift-rosa[]
[NOTE]
====
All Operators listed in the Operator Hub marketplace should be available for installation. These Operators are considered customer workloads, and are not monitored by Red Hat Site Reliability Engineering (SRE).
====
endif::openshift-dedicated,openshift-rosa[]

Developers can use the Operator SDK to help author custom Operators that take advantage of OLM features, as well. Their Operator can then be bundled and added to a custom catalog source, which can be added to a cluster and made available to users.

[NOTE]
====
OLM does not manage the cluster Operators that comprise the {product-title} architecture.
====
