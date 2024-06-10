// Module included in the following assemblies:
//
// * operators/understanding/olm-understanding-operatorhub.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-operatorhub-overview_{context}"]
= About OperatorHub

_OperatorHub_ is the web console interface in {product-title} that cluster administrators use to discover and install Operators. With one click, an Operator can be pulled from its off-cluster source, installed and subscribed on the cluster, and made ready for engineering teams to self-service manage the product across deployment environments using Operator Lifecycle Manager (OLM).

ifndef::openshift-origin[]
Cluster administrators can choose from catalogs grouped into the following categories:

[cols="2a,8a",options="header"]
|===
|Category |Description

|Red Hat Operators
|Red Hat products packaged and shipped by Red Hat. Supported by Red Hat.

|Certified Operators
|Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV.

|Red Hat Marketplace
|Certified software that can be purchased from link:https://marketplace.redhat.com/[Red Hat Marketplace].

|Community Operators
|Optionally-visible software maintained by relevant representatives in the link:https://github.com/redhat-openshift-ecosystem/community-operators-prod/tree/main/operators[redhat-openshift-ecosystem/community-operators-prod/operators] GitHub repository. No official support.

|Custom Operators
|Operators you add to the cluster yourself. If you have not added any custom Operators, the *Custom* category does not appear in the web console on your OperatorHub.
|===
endif::[]

Operators on OperatorHub are packaged to run on OLM. This includes a YAML file called a cluster service version (CSV) containing all of the CRDs, RBAC rules, deployments, and container images required to install and securely run the Operator. It also contains user-visible information like a description of its features and supported Kubernetes versions.

The Operator SDK can be used to assist developers packaging their Operators for use on OLM and OperatorHub. If you have a commercial application that you want to make accessible to your customers, get it included using the certification workflow provided on the Red Hat Partner Connect portal at link:https://connect.redhat.com[connect.redhat.com].
