// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-modify-manager_{context}"]
= Modifying the manager

Update your Operator project to provide the reconcile logic, in the form of an Ansible role, which runs every time a `Memcached` resource is created, updated, or deleted.

.Procedure

. Update the `roles/memcached/tasks/main.yml` file with the following structure:
+
[source,yaml]
----
---
- name: start memcached
  k8s:
    definition:
      kind: Deployment
      apiVersion: apps/v1
      metadata:
        name: '{{ ansible_operator_meta.name }}-memcached'
        namespace: '{{ ansible_operator_meta.namespace }}'
      spec:
        replicas: "{{size}}"
        selector:
          matchLabels:
            app: memcached
        template:
          metadata:
            labels:
              app: memcached
          spec:
            containers:
            - name: memcached
              command:
              - memcached
              - -m=64
              - -o
              - modern
              - -v
              image: "docker.io/memcached:1.4.36-alpine"
              ports:
                - containerPort: 11211
----
+
This `memcached` role ensures a `memcached` deployment exist and sets the deployment size.

. Set default values for variables used in your Ansible role by editing the `roles/memcached/defaults/main.yml` file:
+
[source,yaml]
----
---
# defaults file for Memcached
size: 1
----

. Update the `Memcached` sample resource in the `config/samples/cache_v1_memcached.yaml` file with the following structure:
+
[source,yaml]
----
apiVersion: cache.example.com/v1
kind: Memcached
metadata:
  labels:
    app.kubernetes.io/name: memcached
    app.kubernetes.io/instance: memcached-sample
    app.kubernetes.io/part-of: memcached-operator
    app.kubernetes.io/managed-by: kustomize
    app.kubernetes.io/created-by: memcached-operator
  name: memcached-sample
spec:
  size: 3
----
+
The key-value pairs in the custom resource (CR) spec are passed to Ansible as extra variables.

[NOTE]
====
The names of all variables in the `spec` field are converted to snake case, meaning lowercase with an underscore, by the Operator before running Ansible. For example, `serviceAccount` in the spec becomes `service_account` in Ansible.

You can disable this case conversion by setting the `snakeCaseParameters` option to `false` in your `watches.yaml` file. It is recommended that you perform some type validation in Ansible on the variables to ensure that your application is receiving expected input.
====
