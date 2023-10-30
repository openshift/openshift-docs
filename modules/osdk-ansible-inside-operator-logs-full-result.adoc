// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-inside-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-inside-operator-logs-full-result_{context}"]
= Enabling full Ansible results in logs

You can set the environment variable `ANSIBLE_DEBUG_LOGS` to `True` to enable checking the full Ansible result in logs, which can be helpful when debugging.

.Procedure

* Edit the `config/manager/manager.yaml` and `config/default/manager_auth_proxy_patch.yaml` files to include the following configuration:
+
[source,terminal]
----
      containers:
      - name: manager
        env:
        - name: ANSIBLE_DEBUG_LOGS
          value: "True"
----
