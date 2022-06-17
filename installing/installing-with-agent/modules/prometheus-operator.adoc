// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="prometheus-operator_{context}"]
= Prometheus Operator

[discrete]
== Purpose

The Prometheus Operator for Kubernetes provides easy monitoring definitions for Kubernetes services and deployment and management of Prometheus instances.

Once installed, the Prometheus Operator provides the following features:

* Create and Destroy: Easily launch a Prometheus instance for your Kubernetes namespace, a specific application or team easily using the Operator.

* Simple Configuration: Configure the fundamentals of Prometheus like versions, persistence, retention policies, and replicas from a native Kubernetes resource.

* Target Services via Labels: Automatically generate monitoring target configurations based on familiar Kubernetes label queries; no need to learn a Prometheus specific configuration language.

[discrete]
== Project

link:https://github.com/openshift/prometheus-operator[prometheus-operator]
