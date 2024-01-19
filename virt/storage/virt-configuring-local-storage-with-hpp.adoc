:_mod-docs-content-type: ASSEMBLY
[id="virt-configuring-local-storage-with-hpp"]
= Configuring local storage by using the hostpath provisioner
include::_attributes/common-attributes.adoc[]
:context: virt-configuring-local-storage-with-hpp

toc::[]

You can configure local storage for virtual machines by using the hostpath provisioner (HPP).

When you install the {VirtProductName} Operator, the Hostpath Provisioner Operator is automatically installed. HPP is a local storage provisioner designed for {VirtProductName} that is created by the Hostpath Provisioner Operator. To use HPP, you create an HPP custom resource (CR) with a basic storage pool.

include::modules/virt-creating-hpp-basic-storage-pool.adoc[leveloffset=+1]

include::modules/virt-about-creating-storage-classes.adoc[leveloffset=+2]

include::modules/virt-creating-storage-class-csi-driver.adoc[leveloffset=+2]

include::modules/virt-about-storage-pools-pvc-templates.adoc[leveloffset=+1]

include::modules/virt-creating-storage-pool-pvc-template.adoc[leveloffset=+2]

