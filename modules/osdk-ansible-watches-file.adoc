// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-support.adoc

[id="osdk-ansible-watches-file_{context}"]
= watches.yaml file

A _group/version/kind (GVK)_ is a unique identifier for a Kubernetes API. The `watches.yaml` file contains a list of mappings from custom resources (CRs), identified by its GVK, to an Ansible role or playbook. The Operator expects this mapping file in a predefined location at `/opt/ansible/watches.yaml`.

.`watches.yaml` file mappings
[cols="3,7",options="header"]
|===
|Field
|Description

|`group`
|Group of CR to watch.

|`version`
|Version of CR to watch.

|`kind`
|Kind of CR to watch

|`role` (default)
|Path to the Ansible role added to the container. For example, if your `roles` directory is at `/opt/ansible/roles/` and your role is named `busybox`, this value would be `/opt/ansible/roles/busybox`. This field is mutually exclusive with the `playbook` field.

|`playbook`
|Path to the Ansible playbook added to the container. This playbook is expected to be a way to call roles. This field is mutually exclusive with the `role` field.

|`reconcilePeriod` (optional)
|The reconciliation interval, how often the role or playbook is run, for a given CR.

|`manageStatus` (optional)
|When set to `true` (default), the Operator manages the status of the CR generically. When set to `false`, the status of the CR is managed elsewhere, by the specified role or playbook or in a separate controller.
|===

.Example `watches.yaml` file
[source,yaml]
----
- version: v1alpha1 <1>
  group: test1.example.com
  kind: Test1
  role: /opt/ansible/roles/Test1

- version: v1alpha1 <2>
  group: test2.example.com
  kind: Test2
  playbook: /opt/ansible/playbook.yml

- version: v1alpha1 <3>
  group: test3.example.com
  kind: Test3
  playbook: /opt/ansible/test3.yml
  reconcilePeriod: 0
  manageStatus: false
----
<1> Simple example mapping `Test1` to the `test1` role.
<2> Simple example mapping `Test2` to a playbook.
<3> More complex example for the `Test3` kind. Disables re-queuing and managing the CR status in the playbook.

[id="osdk-ansible-watches-file-advanced_{context}"]
== Advanced options

Advanced features can be enabled by adding them to your `watches.yaml` file per GVK. They can go below the `group`, `version`, `kind` and `playbook` or `role` fields.

Some features can be overridden per resource using an annotation on that CR. The options that can be overridden have the annotation specified below.

.Advanced watches.yaml file options
[cols="3,2,4,2,1",options="header"]
|===
|Feature
|YAML key
|Description
|Annotation for override
|Default value

|Reconcile period
|`reconcilePeriod`
|Time between reconcile runs for a particular CR.
|`ansible.operator-sdk/reconcile-period`
|`1m`

|Manage status
|`manageStatus`
|Allows the Operator to manage the `conditions` section of each CR `status` section.
|
|`true`

|Watch dependent resources
|`watchDependentResources`
|Allows the Operator to dynamically watch resources that are created by Ansible.
|
|`true`

|Watch cluster-scoped resources
|`watchClusterScopedResources`
|Allows the Operator to watch cluster-scoped resources that are created by Ansible.
|
|`false`

|Max runner artifacts
|`maxRunnerArtifacts`
|Manages the number of link:https://ansible-runner.readthedocs.io/en/latest/intro.html#runner-artifacts-directory-hierarchy[artifact directories] that Ansible Runner keeps in the Operator container for each individual resource.
|`ansible.operator-sdk/max-runner-artifacts`
|`20`
|===

.Example watches.yml file with advanced options
[source,yaml]
----
- version: v1alpha1
  group: app.example.com
  kind: AppService
  playbook: /opt/ansible/playbook.yml
  maxRunnerArtifacts: 30
  reconcilePeriod: 5s
  manageStatus: False
  watchDependentResources: False
----
