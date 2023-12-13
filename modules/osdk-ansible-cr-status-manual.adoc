// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-cr-status.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-cr-status-manual_{context}"]
= Tracking custom resource status manually

You can use the `operator_sdk.util` collection to modify your Ansible-based Operator to track custom resource (CR) status manually from your application.

.Prerequisites

* Ansible-based Operator project created by using the Operator SDK

.Procedure

. Update the `watches.yaml` file with a `manageStatus` field set to `false`:
+
[source,yaml]
----
- version: v1
  group: api.example.com
  kind: <kind>
  role: <role>
  manageStatus: false
----

. Use the `operator_sdk.util.k8s_status` Ansible module to update the subresource. For example, to update with key `test` and value `data`, `operator_sdk.util` can be used as shown:
+
[source,yaml]
----
- operator_sdk.util.k8s_status:
    api_version: app.example.com/v1
    kind: <kind>
    name: "{{ ansible_operator_meta.name }}"
    namespace: "{{ ansible_operator_meta.namespace }}"
    status:
      test: data
----

. You can declare collections in the `meta/main.yml` file for the role, which is included for scaffolded Ansible-based Operators:
+
[source,yaml]
----
collections:
  - operator_sdk.util
----

. After declaring collections in the role meta, you can invoke the `k8s_status` module directly:
+
[source,yaml]
----
k8s_status:
  ...
  status:
    key1: value1
----
