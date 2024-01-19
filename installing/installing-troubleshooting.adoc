:_mod-docs-content-type: ASSEMBLY
[id="installing-troubleshooting"]
= Troubleshooting installation issues
include::_attributes/common-attributes.adoc[]
:context: installing-troubleshooting

toc::[]

To assist in troubleshooting a failed {product-title} installation, you can gather logs from the bootstrap and control plane machines. You can also get debug information from the installation program. If you are unable to resolve the issue using the logs and debug information, see xref:../support/troubleshooting/troubleshooting-installations.adoc#determining-where-installation-issues-occur_troubleshooting-installations[Determining where installation issues occur] for component-specific troubleshooting.

[NOTE]
====
If your {product-title} installation fails and the debug output or logs contain network timeouts or other connectivity errors, review the guidelines for xref:../installing/install_config/configuring-firewall.adoc#configuring-firewall[configuring your firewall]. Gathering logs from your firewall and load balancer can help you diagnose network-related errors.
====

== Prerequisites

* You attempted to install an {product-title} cluster and the installation failed.

include::modules/installation-bootstrap-gather.adoc[leveloffset=+1]

include::modules/manually-gathering-logs-with-ssh.adoc[leveloffset=+1]

include::modules/manually-gathering-logs-without-ssh.adoc[leveloffset=+1]

include::modules/installation-getting-debug-information.adoc[leveloffset=+1]

include::modules/restarting-installation.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../installing/index.adoc#ocp-installation-overview[Installing an {product-title} cluster]
