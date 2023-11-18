// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-network-customizations

:_mod-docs-content-type: PROCEDURE
[id="installation-azure-trusted-launch_{context}"]
= Enabling trusted launch for Azure VMs

You can enable two trusted launch features when installing your cluster on Azure: link:https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#secure-boot[secure boot] and link:https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview[virtualized Trusted Platform Modules].

See the Azure documentation about link:https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#virtual-machines-sizes[virtual machine sizes] to learn what sizes of virtual machines support these features.

:FeatureName: Trusted launch

include::snippets/technology-preview.adoc[]

.Prerequisites
* You have created an `install-config.yaml` file.

.Procedure

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add the following stanza:
+
[source,yaml]
----
controlPlane: <1>
  platform:
    azure:
      settings:
        securityType: TrustedLaunch <2>
        trustedLaunch:
          uefiSettings:
            secureBoot: Enabled <3>
            virtualizedTrustedPlatformModule: Enabled <4>
----
<1> Specify `controlPlane.platform.azure` or `compute.platform.azure` to enable trusted launch on only control plane or compute nodes respectively. Specify `platform.azure.defaultMachinePlatform` to enable trusted launch on all nodes.
<2> Enable trusted launch features.
<3> Enable secure boot. For more information, see the Azure documentation about link:https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#secure-boot[secure boot].
<4> Enable the virtualized Trusted Platform Module. For more information, see the Azure documentation about link:https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview[virtualized Trusted Platform Modules].