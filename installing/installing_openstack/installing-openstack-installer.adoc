:_mod-docs-content-type: ASSEMBLY
[id="installing-openstack-installer"]
= Installing a cluster on OpenStack
include::_attributes/common-attributes.adoc[]
:context: installing-openstack-installer

toc::[]

In {product-title} version {product-version}, you can install a cluster on
{rh-openstack-first}.

== Prerequisites

* You reviewed details about the xref:../../architecture/architecture-installation.adoc#architecture-installation[{product-title} installation and update] processes.
* You read the documentation on xref:../../installing/installing-preparing.adoc#installing-preparing[selecting a cluster installation method and preparing it for users].
* On {rh-openstack}, you have access to an external network that does not overlap these CIDR ranges:
** `10.0.0.0/16`
** `172.30.0.0/16`
** `10.128.0.0/14`
+
If the external network overlaps these ranges, go to xref:./installing-openstack-installer-custom.adoc#installing-openstack-installer-custom[Installing a cluster on OpenStack with customizations]

include::modules/installation-osp-default-deployment.adoc[leveloffset=+1]
include::modules/cluster-entitlements.adoc[leveloffset=+1]
include::modules/installation-osp-enabling-swift.adoc[leveloffset=+1]
include::modules/installation-osp-verifying-external-network.adoc[leveloffset=+1]
include::modules/installation-osp-describing-cloud-parameters.adoc[leveloffset=+1]
include::modules/ssh-agent-using.adoc[leveloffset=+1]
include::modules/installation-osp-accessing-api.adoc[leveloffset=+1]
include::modules/installation-osp-accessing-api-floating.adoc[leveloffset=+2]
include::modules/installation-osp-accessing-api-no-floating.adoc[leveloffset=+2]
include::modules/installation-launching-installer.adoc[leveloffset=+1]
include::modules/installation-osp-verifying-cluster-status.adoc[leveloffset=+1]
include::modules/cli-logging-in-kubeadmin.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* See xref:../../web_console/web-console.adoc#web-console[Accessing the web console] for more details about accessing and understanding the {product-title} web console.

include::modules/cluster-telemetry.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* See xref:../../support/remote_health_monitoring/about-remote-health-monitoring.adoc#about-remote-health-monitoring[About remote health monitoring] for more information about the Telemetry service

== Next steps

* xref:../../post_installation_configuration/cluster-tasks.adoc#available_cluster_customizations[Customize your cluster].
* If necessary, you can
xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#opting-out-remote-health-reporting_opting-out-remote-health-reporting[opt out of remote health reporting].
