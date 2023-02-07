// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc

:operator-name: vSphere Problem Detector Operator

[id="vsphere-problem-detector-operator_{context}"]
= {operator-name}

[discrete]
== Purpose

The {operator-name} checks clusters that are deployed on vSphere for common installation and misconfiguration issues that are related to storage.

[NOTE]
====
The {operator-name} is only started by the Cluster Storage Operator when the Cluster Storage Operator detects that the cluster is deployed on vSphere.
====

[discrete]
== Configuration

No configuration is required.

[discrete]
== Notes

* The Operator supports {product-title} installations on vSphere.
* The Operator uses the `vsphere-cloud-credentials` to communicate with vSphere.
* The Operator performs checks that are related to storage.

// Clear temporary attributes
:!operator-name:
