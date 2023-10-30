// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-using-virtctl-ssh-command_{context}"]
= Using the virtctl ssh command

You can access a running virtual machine (VM) by using the `virtcl ssh` command.

.Prerequisites

* You installed the `virtctl` command line tool.
* You added a public SSH key to the VM.
* You have an SSH client installed.
* The environment where you installed the `virtctl` tool has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable.

.Procedure

* Run the `virtctl ssh` command:
+
[source,terminal]
----
$ virtctl -n <namespace> ssh <username>@example-vm -i <ssh_key> <1>
----
<1> Specify the namespace, user name, and the SSH private key. The default SSH key location is `/home/user/.ssh`. If you save the key in a different location, you must specify the path.
+
.Example
[source,terminal]
----
$ virtctl -n my-namespace ssh cloud-user@example-vm -i my-key
----