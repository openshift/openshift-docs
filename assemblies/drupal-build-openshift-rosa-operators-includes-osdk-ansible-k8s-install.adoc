// Module included in the following assemblies:
//
// * operators/operator_sdk/ansible/osdk-ansible-k8s-collection.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-ansible-installing-k8s-collection_{context}"]
= Installing the Kubernetes Collection for Ansible

You can install the Kubernetes Collection for Ansible on your local workstation.

.Procedure

. Install Ansible 2.15+:
+
[source,terminal]
----
$ sudo dnf install ansible
----

. Install the link:https://pypi.org/project/kubernetes/[Python Kubernetes client] package:
+
[source,terminal]
----
$ pip install kubernetes
----

. Install the Kubernetes Collection using one of the following methods:

* You can install the collection directly from Ansible Galaxy:
+
[source,terminal]
----
$ ansible-galaxy collection install community.kubernetes
----

* If you have already initialized your Operator, you might have a `requirements.yml` file at the top level of your project. This file specifies Ansible dependencies that must be installed for your Operator to function. By default, this file installs the `community.kubernetes` collection as well as the `operator_sdk.util` collection, which provides modules and plugins for Operator-specific functions.
+
To install the dependent modules from the `requirements.yml` file:
+
[source,terminal]
----
$ ansible-galaxy collection install -r requirements.yml
----
