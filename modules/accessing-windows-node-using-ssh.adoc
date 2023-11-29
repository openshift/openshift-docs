// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="accessing-windows-node-using-ssh_{context}"]
= Accessing a Windows node using SSH

You can access a Windows node by using a secure shell (SSH).

.Prerequisites

* You have installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.
* You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use.
* You have connected to the Windows node link:https://access.redhat.com/solutions/4073041[using an `ssh-bastion` pod].

.Procedure

* Access the Windows node by running the following command:
+
[source,terminal]
----
$ ssh -t -o StrictHostKeyChecking=no -o ProxyCommand='ssh -A -o StrictHostKeyChecking=no \
    -o ServerAliveInterval=30 -W %h:%p core@$(oc get service --all-namespaces -l run=ssh-bastion \
    -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")' <username>@<windows_node_internal_ip> <1> <2>
----
<1> Specify the cloud provider username, such as `Administrator` for Amazon Web Services (AWS) or `capi` for Microsoft Azure.
<2> Specify the internal IP address of the node, which can be discovered by running the following command:
+
[source,terminal]
----
$ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
----
