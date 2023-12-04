// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-k8s-collection.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-k8s-local_{context}"]
= Testing the Kubernetes Collection locally

Operator developers can run the Ansible code from their local machine as opposed to running and rebuilding the Operator each time.

.Prerequisites

* Initialize an Ansible-based Operator project and create an API that has a generated Ansible role by using the Operator SDK
* Install the Kubernetes Collection for Ansible

.Procedure

. In your Ansible-based Operator project directory, modify the `roles/<kind>/tasks/main.yml` file with the Ansible logic that you want. The `roles/<kind>/` directory is created when you use the `--generate-role` flag while creating an API. The `<kind>` replaceable matches the kind that you specified for the API.
+
The following example creates and deletes a config map based on the value of a variable named `state`:
+
[source,yaml]
----
---
- name: set ConfigMap example-config to {{ state }}
  community.kubernetes.k8s:
    api_version: v1
    kind: ConfigMap
    name: example-config
    namespace: <operator_namespace> <1>
    state: "{{ state }}"
  ignore_errors: true <2>
----
<1> Specify the namespace where you want the config map created.
<2> Setting `ignore_errors: true` ensures that deleting a nonexistent config map does not fail.

. Modify the `roles/<kind>/defaults/main.yml` file to set `state` to `present` by default:
+
[source,yaml]
----
---
state: present
----

. Create an Ansible playbook by creating a `playbook.yml` file in the top-level of your project directory, and include your `<kind>` role:
+
[source,yaml]
----
---
- hosts: localhost
  roles:
    - <kind>
----

. Run the playbook:
+
[source,terminal]
----
$ ansible-playbook playbook.yml
----
+
.Example output
[source,terminal]
----
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [localhost] ********************************************************************************

TASK [Gathering Facts] ********************************************************************************
ok: [localhost]

TASK [memcached : set ConfigMap example-config to present] ********************************************************************************
changed: [localhost]

PLAY RECAP ********************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
----

. Verify that the config map was created:
+
[source,terminal]
----
$ oc get configmaps
----
+
.Example output
[source,terminal]
----
NAME               DATA   AGE
example-config     0      2m1s
----

. Rerun the playbook setting `state` to `absent`:
+
[source,terminal]
----
$ ansible-playbook playbook.yml --extra-vars state=absent
----
+
.Example output
[source,terminal]
----
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [localhost] ********************************************************************************

TASK [Gathering Facts] ********************************************************************************
ok: [localhost]

TASK [memcached : set ConfigMap example-config to absent] ********************************************************************************
changed: [localhost]

PLAY RECAP ********************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
----

. Verify that the config map was deleted:
+
[source,terminal]
----
$ oc get configmaps
----
