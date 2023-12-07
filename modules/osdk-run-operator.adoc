// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc
// * operators/operator_sdk/helm/osdk-hybrid-helm.adoc

ifeval::["{context}" == "osdk-golang-tutorial"]
:golang:
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:ansible:
endif::[]
ifeval::["{context}" == "osdk-helm-tutorial"]
:helm:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:java:
endif::[]

[id="osdk-run-operator_{context}"]
= Running the Operator

// The "run locally" and "run as a deployment" options require cluster-admin. Therefore, these options are not available for OSD/ROSA.

// Deployment options for OCP
ifndef::openshift-dedicated,openshift-rosa[]
There are three ways you can use the Operator SDK CLI to build and run your Operator:

* Run locally outside the cluster as a Go program.
* Run as a deployment on the cluster.
* Bundle your Operator and use Operator Lifecycle Manager (OLM) to deploy on the cluster.

ifdef::golang[]
[NOTE]
====
Before running your Go-based Operator as either a deployment on {product-title} or as a bundle that uses OLM, ensure that your project has been updated to use supported images.
====
endif::[]
endif::openshift-dedicated,openshift-rosa[]

// Deployment options for OSD/ROSA
ifdef::openshift-dedicated,openshift-rosa[]
To build and run your Operator, use the Operator SDK CLI to bundle your Operator, and then use Operator Lifecycle Manager (OLM) to deploy on the cluster.

[NOTE]
====
If you wish to deploy your Operator on an OpenShift Container Platform cluster instead of a {product-title} cluster, two additional deployment options are available:

* Run locally outside the cluster as a Go program.
* Run as a deployment on the cluster.
====

ifdef::golang[]
[NOTE]
====
Before running your Go-based Operator as a bundle that uses OLM, ensure that your project has been updated to use supported images.
====
endif::[]
endif::openshift-dedicated,openshift-rosa[]

ifeval::["{context}" == "osdk-golang-tutorial"]
:!golang:
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:!ansible:
endif::[]
ifeval::["{context}" == "osdk-helm-tutorial"]
:!helm:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:!java:
endif::[]
