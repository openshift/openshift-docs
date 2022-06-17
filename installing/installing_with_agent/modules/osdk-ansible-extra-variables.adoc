// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-support.adoc

[id="osdk-ansible-extra-variables_{context}"]
= Extra variables sent to Ansible

Extra variables can be sent to Ansible, which are then managed by the Operator. The `spec` section of the custom resource (CR) passes along the key-value pairs as extra variables. This is equivalent to extra variables passed in to the `ansible-playbook` command.

The Operator also passes along additional variables under the `meta` field for the name of the CR and the namespace of the CR.

For the following CR example:

[source,yaml]
----
apiVersion: "app.example.com/v1alpha1"
kind: "Database"
metadata:
  name: "example"
spec:
  message: "Hello world 2"
  newParameter: "newParam"
----

The structure passed to Ansible as extra variables is:

[source,json]
----
{ "meta": {
        "name": "<cr_name>",
        "namespace": "<cr_namespace>",
  },
  "message": "Hello world 2",
  "new_parameter": "newParam",
  "_app_example_com_database": {
     <full_crd>
   },
}
----

The `message` and `newParameter` fields are set in the top level as extra variables, and `meta` provides the relevant metadata for the CR as defined in the Operator. The `meta` fields can be accessed using dot notation in Ansible, for example:

[source,yaml]
----
---
- debug:
    msg: "name: {{ ansible_operator_meta.name }}, {{ ansible_operator_meta.namespace }}"
----
