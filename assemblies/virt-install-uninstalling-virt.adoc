:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-virt"]
= Uninstalling {VirtProductName}
include::_attributes/common-attributes.adoc[]
:context: uninstalling-virt

toc::[]

You uninstall {VirtProductName} by using the web console or the command line interface (CLI) to delete the {VirtProductName} workloads, the Operator, and its resources.

[id='uninstalling-virt-web-console_{context}']
== Uninstalling {VirtProductName} by using the web console

You uninstall {VirtProductName} by using the xref:../../web_console/web-console.adoc#web-console-overview_web-console[web console] to perform the following tasks:

. xref:../../virt/install/uninstalling-virt.adoc#virt-deleting-deployment-custom-resource_uninstalling-virt[Delete the `HyperConverged` CR].
. xref:../../virt/install/uninstalling-virt.adoc#olm-deleting-operators-from-a-cluster-using-web-console_uninstalling-virt[Delete the {VirtProductName} Operator].
. xref:../../virt/install/uninstalling-virt.adoc#deleting-a-namespace-using-the-web-console_uninstalling-virt[Delete the `openshift-cnv` namespace].
. xref:../../virt/install/uninstalling-virt.adoc#virt-deleting-virt-crds-web_uninstalling-virt[Delete the {VirtProductName} custom resource definitions (CRDs)].

[IMPORTANT]
====
You must first delete all xref:../../virt/virtual_machines/virt-delete-vms.adoc#virt-delete-vm-web_virt-delete-vms[virtual machines], and xref:../../virt/virtual_machines/virt-manage-vmis.adoc#virt-deleting-vmis-cli_virt-manage-vmis[virtual machine instances].

You cannot uninstall {VirtProductName} while its workloads remain on the cluster.
====

include::modules/virt-deleting-deployment-custom-resource.adoc[leveloffset=+2]

include::modules/olm-deleting-operators-from-a-cluster-using-web-console.adoc[leveloffset=+2]

include::modules/deleting-a-namespace-using-the-web-console.adoc[leveloffset=+2]

include::modules/virt-deleting-virt-crds-web.adoc[leveloffset=+2]

include::modules/virt-deleting-virt-cli.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../virt/virtual_machines/virt-delete-vms.adoc#virt-delete-vm-web_virt-delete-vms[Deleting virtual machines]
* xref:../../virt/virtual_machines/virt-manage-vmis.adoc#virt-deleting-vmis-cli_virt-manage-vmis[Deleting virtual machine instances]
