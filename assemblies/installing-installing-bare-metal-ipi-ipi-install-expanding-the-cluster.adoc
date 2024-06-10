:_mod-docs-content-type: ASSEMBLY
[id="ipi-install-expanding-the-cluster"]
= Expanding the cluster
include::_attributes/common-attributes.adoc[]
:context: ipi-install-expanding

toc::[]

After deploying an installer-provisioned {product-title} cluster, you can use the following procedures to expand the number of worker nodes. Ensure that each prospective worker node meets the prerequisites.

[NOTE]
====
Expanding the cluster using RedFish Virtual Media involves meeting minimum firmware requirements. See *Firmware requirements for installing with virtual media* in the *Prerequisites* section for additional details when expanding the cluster using RedFish Virtual Media.
====

include::modules/ipi-install-preparing-the-bare-metal-node.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* See xref:../../installing/installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#configuring-host-network-interfaces-in-the-install-config-yaml-file_ipi-install-installation-workflow[Optional: Configuring host network interfaces in the install-config.yaml file] for details on configuring the NMState syntax.
* See xref:../../scalability_and_performance/managing-bare-metal-hosts.adoc#automatically-scaling-machines-to-available-bare-metal-hosts_managing-bare-metal-hosts[Automatically scaling machines to the number of available bare metal hosts] for details on automatically scaling machines.

include::modules/ipi-install-replacing-a-bare-metal-control-plane-node.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../backup_and_restore/control_plane_backup_and_restore/replacing-unhealthy-etcd-member.adoc#replacing-the-unhealthy-etcd-member[Replacing an unhealthy etcd member]

* xref:../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc#backing-up-etcd-data_backup-etcd[Backing up etcd]

* xref:../../post_installation_configuration/bare-metal-configuration.adoc#post-install-bare-metal-configuration[Bare metal configuration]

* xref:../../installing/installing_bare_metal_ipi/ipi-install-installation-workflow.adoc#bmc-addressing_ipi-install-installation-workflow[BMC addressing]

include::modules/ipi-install-preparing-to-deploy-with-virtual-media-on-the-baremetal-network.adoc[leveloffset=+1]

include::modules/ipi-install-diagnosing-duplicate-mac-address.adoc[leveloffset=+1]

include::modules/ipi-install-provisioning-the-bare-metal-node.adoc[leveloffset=+1]
