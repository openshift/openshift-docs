:_mod-docs-content-type: ASSEMBLY
[id="troubleshooting-windows-container-workload-issues"]
= Troubleshooting Windows container workload issues
include::_attributes/common-attributes.adoc[]
:context: troubleshooting-windows-container-workload-issues

toc::[]

include::modules/wmco-does-not-install.adoc[leveloffset=+1]

For more information, see xref:../../networking/ovn_kubernetes_network_provider/configuring-hybrid-networking.adoc#configuring-hybrid-ovnkubernetes[Configuring hybrid networking].

include::modules/investigating-why-windows-machine-compute-node.adoc[leveloffset=+1]

[id="accessing-windows-node"]
== Accessing a Windows node

Windows nodes cannot be accessed using the `oc debug node` command; the command requires running a privileged pod on the node, which is not yet supported for Windows. Instead, a Windows node can be accessed using a secure shell (SSH) or Remote Desktop Protocol (RDP). An SSH bastion is required for both methods.

include::modules/accessing-windows-node-using-ssh.adoc[leveloffset=+2]
include::modules/accessing-windows-node-using-rdp.adoc[leveloffset=+2]

include::modules/collecting-kube-node-logs-windows.adoc[leveloffset=+1]
include::modules/collecting-windows-application-event-logs.adoc[leveloffset=+1]
include::modules/collecting-docker-logs-windows.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

* link:https://docs.microsoft.com/en-us/virtualization/windowscontainers/troubleshooting[Containers on Windows troubleshooting]
* link:https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/update-containers#troubleshoot-host-and-container-image-mismatches[Troubleshoot host and container image mismatches]
* link:https://docs.docker.com/docker-for-windows/troubleshoot/[Docker for Windows troubleshooting]
* link:https://docs.microsoft.com/en-us/virtualization/windowscontainers/kubernetes/common-problems[Common Kubernetes problems with Windows]
