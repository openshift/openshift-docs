// Module included in the following assembly:
//
// * configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-installing-olm-operators-using-gitops_{context}"]
= Installing OLM Operators using {gitops-title}

{gitops-title} with cluster configurations manages specific cluster-scoped resources and takes care of installing cluster Operators or any namespace-scoped OLM Operators.

Consider a case where as a cluster administrator, you have to install an OLM Operator such as Tekton. You use the {product-title} web console to manually install a Tekton Operator or the OpenShift CLI to manually install a Tekton subscription and Tekton Operator group on your cluster.

{gitops-title} places your Kubernetes resources in your Git repository. As a cluster administrator, use {gitops-title} to manage and automate the installation of other OLM Operators without any manual procedures. For example, after you place the Tekton subscription in your Git repository by using {gitops-title}, the {gitops-title} automatically takes this Tekton subscription from your Git repository and installs the Tekton Operator on your cluster.

== Installing cluster-scoped Operators

Operator Lifecycle Manager (OLM) uses a default `global-operators` Operator group in the `openshift-operators` namespace for cluster-scoped Operators. Hence you do not have to manage the `OperatorGroup` resource in your Gitops repository. However, for namespace-scoped Operators, you must manage the `OperatorGroup` resource in that namespace.

To install cluster-scoped Operators, create and place the `Subscription` resource of the required Operator in your Git repository.

.Example: Grafana Operator subscription

[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: grafana
spec:
  channel: v4
  installPlanApproval: Automatic
  name: grafana-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

== Installing namepace-scoped Operators

To install namespace-scoped Operators, create and place the `Subscription` and `OperatorGroup` resources of the required Operator in your Git repository.

.Example: Ansible Automation Platform Resource Operator

[source,yaml]
----
...
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
  name: ansible-automation-platform
...
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ansible-automation-platform-operator
  namespace: ansible-automation-platform
spec:
  targetNamespaces:
    - ansible-automation-platform
...
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: ansible-automation-platform
  namespace: ansible-automation-platform
spec:
  channel: patch-me
  installPlanApproval: Automatic
  name: ansible-automation-platform-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
...
----

[IMPORTANT]
====
When deploying multiple Operators using {gitops-title}, you must create only a single Operator group in the corresponding namespace. If more than one Operator group exists in a single namespace, any CSV created in that namespace transition to a `failure` state with the `TooManyOperatorGroups` reason. After the number of Operator groups in their corresponding namespaces reaches one, all the previous `failure` state CSVs transition to `pending` state. You must manually approve the pending install plan to complete the Operator installation.
====

