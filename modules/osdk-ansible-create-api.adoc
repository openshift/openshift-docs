// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-create-api-controller_{context}"]
= Creating an API

Use the Operator SDK CLI to create a Memcached API.

.Procedure

* Run the following command to create an API with group `cache`, version, `v1`, and kind `Memcached`:
+
[source,terminal]
----
$ operator-sdk create api \
    --group cache \
    --version v1 \
    --kind Memcached \
    --generate-role <1>
----
<1> Generates an Ansible role for the API.

After creating the API, your Operator project updates with the following structure:

Memcached CRD:: Includes a sample `Memcached` resource

Manager:: Program that reconciles the state of the cluster to the desired state by using:
+
--
* A reconciler, either an Ansible role or playbook
* A `watches.yaml` file, which connects the `Memcached` resource to the `memcached` Ansible role
--
