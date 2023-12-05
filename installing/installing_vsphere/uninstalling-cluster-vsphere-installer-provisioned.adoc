:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-cluster-vsphere-installer-provisioned"]
= Uninstalling a cluster on vSphere that uses installer-provisioned infrastructure
include::_attributes/common-attributes.adoc[]
:context: uninstalling-cluster-vsphere-installer-provisioned

toc::[]

You can remove a cluster that you deployed in your VMware vSphere instance by using installer-provisioned infrastructure.

[NOTE]
====
When you run the `openshift-install destroy cluster` command to uninstall {product-title}, vSphere volumes are not automatically deleted. The cluster administrator must manually find the vSphere volumes and delete them.
====

include::modules/installation-uninstall-clouds.adoc[leveloffset=+1]
