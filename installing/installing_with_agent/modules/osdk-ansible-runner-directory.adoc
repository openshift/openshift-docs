// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-support.adoc

[id="osdk-ansible-runner-directory_{context}"]
= Ansible Runner directory

Ansible Runner keeps information about Ansible runs in the container. This is located at `/tmp/ansible-operator/runner/<group>/<version>/<kind>/<namespace>/<name>`.

[role="_additional-resources"]
.Additional resources

* To learn more about the `runner` directory, see the link:https://ansible-runner.readthedocs.io/en/latest/index.html[Ansible Runner documentation].
