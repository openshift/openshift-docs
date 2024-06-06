// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-inside-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-inside-operator-logs-verbose_{context}"]
= Enabling verbose debugging in logs

While developing an Ansible-based Operator, it can be helpful to enable additional debugging in logs.

.Procedure

* Add the `ansible.sdk.operatorframework.io/verbosity` annotation to your custom resource to enable the verbosity level that you want. For example:
+
[source,terminal]
----
apiVersion: "cache.example.com/v1alpha1"
kind: "Memcached"
metadata:
  name: "example-memcached"
  annotations:
    "ansible.sdk.operatorframework.io/verbosity": "4"
spec:
  size: 4
----
