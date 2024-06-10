// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-cr-status.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-ansible-cr-status-about_{context}"]
= About custom resource status in Ansible-based Operators

Ansible-based Operators automatically update custom resource (CR) link:https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#status-subresource[`status` subresources] with generic information about the previous Ansible run. This includes the number of successful and failed tasks and relevant error messages as shown:

[source,yaml]
----
status:
  conditions:
  - ansibleResult:
      changed: 3
      completion: 2018-12-03T13:45:57.13329
      failures: 1
      ok: 6
      skipped: 0
    lastTransitionTime: 2018-12-03T13:45:57Z
    message: 'Status code was -1 and not [200]: Request failed: <urlopen error [Errno
      113] No route to host>'
    reason: Failed
    status: "True"
    type: Failure
  - lastTransitionTime: 2018-12-03T13:46:13Z
    message: Running reconciliation
    reason: Running
    status: "True"
    type: Running
----

Ansible-based Operators also allow Operator authors to supply custom status values with the `k8s_status` Ansible module, which is included in the link:https://galaxy.ansible.com/operator_sdk/util[`operator_sdk.util` collection]. This allows the author to update the `status` from within Ansible with any key-value pair as desired.

By default, Ansible-based Operators always include the generic Ansible run output as shown above. If you would prefer your application did _not_ update the status with Ansible output, you can track the status manually from your application.
