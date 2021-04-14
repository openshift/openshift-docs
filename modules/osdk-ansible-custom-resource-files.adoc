// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-support.adoc

[id="osdk-ansible-custom-resource-files_{context}"]
= Custom resource files

Operators use the Kubernetes extension mechanism, custom resource definitions (CRDs), so your custom resource (CR) looks and acts just like the built-in, native Kubernetes objects.

The CR file format is a Kubernetes resource file. The object has mandatory and optional fields:

.Custom resource fields
[cols="3,7",options="header"]
|===
|Field
|Description

|`apiVersion`
|Version of the CR to be created.

|`kind`
|Kind of the CR to be created.

|`metadata`
|Kubernetes-specific metadata to be created.

|`spec` (optional)
|Key-value list of variables which are passed to Ansible. This field is empty by default.

|`status`
|Summarizes the current state of the object. For Ansible-based Operators, the link:https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#status-subresource[`status` subresource] is enabled for CRDs and managed by the `operator_sdk.util.k8s_status` Ansible module by default, which includes `condition` information to the CR `status`.

|`annotations`
|Kubernetes-specific annotations to be appended to the CR.
|===

The following list of CR annotations modify the behavior of the Operator:

.Ansible-based Operator annotations
[cols="3,7",options="header"]
|===
|Annotation
|Description

|`ansible.operator-sdk/reconcile-period`
|Specifies the reconciliation interval for the CR. This value is parsed using the standard Golang package link:https://golang.org/pkg/time/[`time`]. Specifically, link:https://golang.org/pkg/time/#ParseDuration[`ParseDuration`] is used which applies the default suffix of `s`, giving the value in seconds.
|===

.Example Ansible-based Operator annotation
[source,yaml]
----
apiVersion: "test1.example.com/v1alpha1"
kind: "Test1"
metadata:
  name: "example"
annotations:
  ansible.operator-sdk/reconcile-period: "30s"
----
