:_mod-docs-content-type: ASSEMBLY
[id="coreos-layering"]
= {op-system} image layering
include::_attributes/common-attributes.adoc[]
:context: coreos-layering

toc::[]


{op-system-first} image layering allows you to easily extend the functionality of your base {op-system} image by _layering_ additional images onto the base image. This layering does not modify the base {op-system} image. Instead, it creates a _custom layered image_ that includes all {op-system} functionality and adds additional functionality to specific nodes in the cluster.

You create a custom layered image by using a Containerfile and applying it to nodes by using a `MachineConfig` object. The Machine Config Operator overrides the base {op-system} image, as specified by the `osImageURL` value in the associated machine config, and boots the new image. You can remove the custom layered image by deleting the machine config, The MCO reboots the nodes back to the base {op-system} image.

With {op-system} image layering, you can install RPMs into your base image, and your custom content will be booted alongside {op-system}. The Machine Config Operator (MCO) can roll out these custom layered images and monitor these custom containers in the same way it does for the default {op-system} image. {op-system} image layering gives you greater flexibility in how you manage your {op-system} nodes.

// NOTE from https://issues.redhat.com/browse/OCPBUGS-2214?focusedCommentId=21430101&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-21430101

[IMPORTANT]
====
Installing realtime kernel and extensions RPMs as custom layered content is not recommended. This is because these RPMs can conflict with RPMs installed by using a machine config. If there is a conflict, the MCO enters a `degraded` state when it tries to install the machine config RPM. You need to remove the conflicting extension from your machine config before proceeding.
====

As soon as you apply the custom layered image to your cluster, you effectively _take ownership_ of your custom layered images and those nodes. While Red Hat remains responsible for maintaining and updating the base {op-system} image on standard nodes, you are responsible for maintaining and updating images on nodes that use a custom layered image. You assume the responsibility for the package you applied with the custom layered image and any issues that might arise with the package.

To apply a custom layered image, you create a Containerfile that references an {product-title} image and the RPM that you want to apply. You then push the resulting custom layered image to an image registry. In a non-production {product-title} cluster, create a `MachineConfig` object for the targeted node pool that points to the new image.

[NOTE]
====
Use the same base {op-system} image installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image used in your cluster.
====

{op-system} image layering allows you to use the following types of images to create custom layered images:

* *{product-title} Hotfixes*. You can work with Customer Experience and Engagement (CEE) to obtain and apply link:https://access.redhat.com/solutions/2996001[Hotfix packages] on top of your {op-system} image. In some instances, you might want a bug fix or enhancement before it is included in an official {product-title} release. {op-system} image layering allows you to easily add the Hotfix before it is officially released and remove the Hotfix when the underlying {op-system} image incorporates the fix.
+
[IMPORTANT]
====
Some Hotfixes require a Red Hat Support Exception and are outside of the normal scope of {product-title} support coverage or life cycle policies.
====
+
In the event you want a Hotfix, it will be provided to you based on link:https://access.redhat.com/solutions/2996001[Red Hat Hotfix policy]. Apply it on top of the base image and test that new custom layered image in a non-production environment. When you are satisfied that the custom layered image is safe to use in production, you can roll it out on your own schedule to specific node pools. For any reason, you can easily roll back the custom layered image and return to using the default {op-system}.
+
.Example Containerfile to apply a Hotfix
[source,yaml]
----
# Using a 4.12.0 image
FROM quay.io/openshift-release-dev/ocp-release@sha256...
#Install hotfix rpm
RUN rpm-ostree override replace https://example.com/myrepo/haproxy-1.0.16-5.el8.src.rpm && \
    rpm-ostree cleanup -m && \
    ostree container commit
----

* *{op-system-base} packages*. You can download {op-system-base-full} packages from the link:https://access.redhat.com/downloads/content/479/ver=/rhel---9/9.1/x86_64/packages[Red Hat Customer Portal], such as chrony, firewalld, and iputils.
+
.Example Containerfile to apply the firewalld utility
[source,yaml]
----
FROM quay.io/openshift-release-dev/ocp-release@sha256...
ADD configure-firewall-playbook.yml .
RUN rpm-ostree install firewalld ansible && \
    ansible-playbook configure-firewall-playbook.yml && \
    rpm -e ansible && \
    ostree container commit
----
+
.Example Containerfile to apply the libreswan utility
[source,yaml]
----
include::https://raw.githubusercontent.com/openshift/rhcos-image-layering-examples/master/libreswan/Containerfile[]
----
+
Because libreswan requires additional RHEL packages, the image must be built on an entitled {op-system-base} host.

* *Third-party packages*. You can download and install RPMs from third-party organizations, such as the following types of packages:
+
--
** Bleeding edge drivers and kernel enhancements to improve performance or add capabilities.
** Forensic client tools to investigate possible and actual break-ins.
** Security agents.
** Inventory agents that provide a coherent view of the entire cluster.
** SSH Key management packages.
--
+
.Example Containerfile to apply a third-party package from EPEL
[source,yaml]
----
include::https://raw.githubusercontent.com/openshift/rhcos-image-layering-examples/master/htop/Containerfile[]
----
+
.Example Containerfile to apply a third-party package that has {op-system-base} dependencies
[source,yaml]
----
include::https://raw.githubusercontent.com/openshift/rhcos-image-layering-examples/master/fish/Containerfile[]
----
+
This Containerfile installs the Linux fish program. Because fish requires additional RHEL packages, the image must be built on an entitled {op-system-base} host.

After you create the machine config, the Machine Config Operator (MCO) performs the following steps:

. Renders a new machine config for the specified pool or pools.
. Performs cordon and drain operations on the nodes in the pool or pools.
. Writes the rest of the machine config parameters onto the nodes.
. Applies the custom layered image to the node.
. Reboots the node using the new image.

[IMPORTANT]
====
It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster.
====

include::modules/coreos-layering-configuring.adoc[leveloffset=+1]

.Additional resources
xref:../post_installation_configuration/coreos-layering.adoc#coreos-layering-updating_coreos-layering[Updating with a {op-system} custom layered image]

include::modules/coreos-layering-removing.adoc[leveloffset=+1]
include::modules/coreos-layering-updating.adoc[leveloffset=+1]

////
Sources:
https://docs.google.com/document/d/1Eow2IReNWqnIh5HvCfcKV2MWgHUmFKSnBkt2rH6_V_M/edit
https://hackmd.io/OKc5ZnN7SQm3myHaGqksBg
https://github.com/openshift/enhancements/blob/master/enhancements/ocp-coreos-layering/ocp-coreos-layering.md
https://docs.google.com/document/d/1RbfCJuL_NBaWvUmd9nmiG8-7MwzsvWHjrIS2LglCYM0/edit
////
