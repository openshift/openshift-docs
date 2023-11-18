// Module included in the following assemblies:
//
// * operators/understanding/olm-what-operators-are.adoc

[id="olm-operator-framework_{context}"]
= Operator Framework

The Operator Framework is a family of tools and capabilities to deliver on the customer experience described above. It is not just about writing code; testing, delivering, and updating Operators is just as important. The Operator Framework components consist of open source tools to tackle these problems:

Operator SDK::
The Operator SDK assists Operator authors in bootstrapping, building, testing, and packaging their own Operator based on their expertise without requiring knowledge of Kubernetes API complexities.

Operator Lifecycle Manager::
Operator Lifecycle Manager (OLM) controls the installation, upgrade, and role-based access control (RBAC) of Operators in a cluster. It is deployed by default in {product-title} {product-version}.

Operator Registry::
The Operator Registry stores cluster service versions (CSVs) and custom resource definitions (CRDs) for creation in a cluster and stores Operator metadata about packages and channels. It runs in a Kubernetes or OpenShift cluster to provide this Operator catalog data to OLM.

OperatorHub::
OperatorHub is a web console for cluster administrators to discover and select Operators to install on their cluster. It is deployed by default in {product-title}.

These tools are designed to be composable, so you can use any that are useful to you.
