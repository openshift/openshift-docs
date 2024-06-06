:_mod-docs-content-type: ASSEMBLY
[id="virt-managing-vms-openshift-pipelines"]
= Managing virtual machines with OpenShift Pipelines
include::_attributes/common-attributes.adoc[]
:context: virt-managing-vms-openshift-pipelines

toc::[]

link:https://docs.openshift.com/pipelines/latest/about/understanding-openshift-pipelines.html[{pipelines-title}] is a Kubernetes-native CI/CD framework that allows developers to design and run each step of the CI/CD pipeline in its own container.

The Scheduling, Scale, and Performance (SSP) Operator integrates {VirtProductName} with {pipelines-shortname}. The SSP Operator includes tasks and example pipelines that allow you to:

* Create and manage virtual machines (VMs), persistent volume claims (PVCs), and data volumes
* Run commands in VMs
* Manipulate disk images with `libguestfs` tools

:FeatureName: Managing virtual machines with {pipelines-title}
include::snippets/technology-preview.adoc[]


[id="prerequisites_virt-managing-vms-openshift-pipelines"]
== Prerequisites

* You have access to an {product-title} cluster with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).
* You have link:https://docs.openshift.com/pipelines/latest/install_config/installing-pipelines.html[installed {pipelines-shortname}].


include::modules/virt-deploying-ssp.adoc[leveloffset=+1]

include::modules/virt-supported-ssp-tasks.adoc[leveloffset=+1]


[id="example-pipelines_virt-managing-vms-openshift-pipelines"]
== Example pipelines

The SSP Operator includes the following example `Pipeline` manifests. You can run the example pipelines by using the web console or CLI.

You might have to run more than one installer pipeline if you need multiple versions of Windows. If you run more than one installer pipeline, each one requires unique parameters, such as the `autounattend` config map and base image name. For example, if you need Windows 10 and Windows 11 or Windows Server 2022 images, you have to run both the Windows efi installer pipeline and the Windows bios installer pipeline. However, if you need Windows 11 and Windows Server 2022 images, you have to run only the Windows efi installer pipeline.

Windows EFI installer pipeline:: This pipeline installs Windows 11 or Windows Server 2022 into a new data volume from a Windows installation image (ISO file). A custom answer file is used to run the installation process.

Windows BIOS installer pipeline:: This pipeline installs Windows 10 into a new data volume from a Windows installation image, also called an ISO file. A custom answer file is used to run the installation process.

Windows customize pipeline:: This pipeline clones the data volume of a basic Windows 10, 11, or Windows Server 2022 installation, customizes it by installing Microsoft SQL Server Express or Microsoft Visual Studio Code, and then creates a new image and template.

[NOTE]
====
The example pipelines use a config map file with `sysprep` predefined by {product-title} and suitable for Microsoft ISO files. For ISO files pertaining to different Windows editions, it may be necessary to create a new config map file with a system-specific sysprep definition.
====

include::modules/virt-running-ssp-pipeline-web.adoc[leveloffset=+2]

include::modules/virt-running-ssp-pipeline-cli.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_virt-managing-vms-openshift-pipelines"]
== Additional resources
* link:https://docs.openshift.com/pipelines/latest/create/creating-applications-with-cicd-pipelines.html[Creating CI/CD solutions for applications using {pipelines-title}]
* xref:../../virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc#virt-creating-windows-vm_virt-creating-vms-uploading-images[Creating a Windows VM]