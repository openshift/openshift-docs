:_mod-docs-content-type: ASSEMBLY
[id="kernel-module-management-operator"]
= Kernel Module Management Operator
include::_attributes/common-attributes.adoc[]
:context: kernel-module-management-operator

toc::[]

Learn about the Kernel Module Management (KMM) Operator and how you can use it to deploy out-of-tree kernel modules and device plugins on {product-title} clusters.

:FeatureName: Kernel Module Management Operator

include::modules/kmm-about-kmm.adoc[leveloffset=+1]
include::modules/kmm-installation.adoc[leveloffset=+1]
include::modules/kmm-installing-using-web-console.adoc[leveloffset=+2]
include::modules/kmm-installing-using-cli.adoc[leveloffset=+2]
include::modules/kmm-installing-older-versions.adoc[leveloffset=+2]
// Added for TELCODOCS-1309
include::modules/kmm-uninstalling-kmm.adoc[leveloffset=+1]
include::modules/kmm-uninstalling-kmmo-red-hat-catalog.adoc[leveloffset=+2]
include::modules/kmm-uninstalling-kmmo-cli.adoc[leveloffset=+2]

include::modules/kmm-deploying-modules.adoc[leveloffset=+1]
include::modules/kmm-creating-module-cr.adoc[leveloffset=+2]

// Added for TELCODOCS-1280
include::modules/kmm-setting-soft-dependencies-between-kernel-modules.adoc[leveloffset=+2]

include::modules/kmm-security.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../authentication/understanding-and-managing-pod-security-admission.adoc#understanding-and-managing-pod-security-admission[Understanding and managing pod security admission].

// Added for TELCODOCS-1279
include::modules/kmm-replacing-in-tree-modules-with-out-of-tree-modules.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* link:https://fastbitlab.com/building-a-linux-kernel-module/[Building a linux kernel module]

include::modules/kmm-example-module-cr.adoc[leveloffset=+2]
include::modules/kmm-creating-moduleloader-image.adoc[leveloffset=+1]
include::modules/kmm-running-depmod.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../hardware_enablement/psap-driver-toolkit.adoc#driver-toolkit[Driver Toolkit].

include::modules/kmm-building-in-cluster.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../cicd/builds/build-configuration.adoc#build-configuration[Build configuration resources].

include::modules/kmm-using-driver-toolkit.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../hardware_enablement/psap-driver-toolkit.adoc#driver-toolkit[Driver Toolkit].

//Deploying kernel modules (Might just leave this short intro in the assembly and put further module below it)
//    * Running ModuleLoader images (CONCEPT, or could be included in the assembly with the intro)
//    * Using the device plugin (CONCEPT, or could be included in the assembly with the intro)
//  * Creating the Module Custom Resource (PROCEDURE? Seems like not a process the user does after reading it. Maybe a REFERENCE)
//  * Security and permissions (CONCEPT or REFERENCE)
//    * ServiceAccounts and SecurityContextConstraints (can include in Security and permissions)
//    * Pod Security Standards (can include in Security and permissions)
//  * Example Module CR (REFERENCE)

// Added for TELCODOCS-1065
include::modules/kmm-using-signing-with-kmm.adoc[leveloffset=+1]
include::modules/kmm-adding-the-keys-for-secureboot.adoc[leveloffset=+1]
include::modules/kmm-checking-the-keys.adoc[leveloffset=+2]
include::modules/kmm-signing-a-prebuilt-driver-container.adoc[leveloffset=+1]
include::modules/kmm-building-and-signing-a-moduleloader-container-image.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
For information on creating a service account, see link:https://docs.openshift.com/container-platform/4.12/authentication/understanding-and-creating-service-accounts.html#service-accounts-managing_understanding-service-accounts[Creating service accounts].

// Added for TELCODOCS-1109
include::modules/kmm-hub-hub-and-spoke.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* link:https://www.redhat.com/en/technologies/management/advanced-cluster-management[Red{nbsp}Hat Advanced Cluster Management (RHACM)]

include::modules/kmm-hub-kmm-hub.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* link:https://openshift-kmm.netlify.app/documentation/install/[Installing KMM]

include::modules/kmm-hub-installing-kmm-hub.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* link:https://catalog.redhat.com/software/containers/kmm/kernel-module-management-hub-operator-bundle/63d84cc33862da54bb19b8c6?architecture=amd64&image=654273ac86f7e537ae452f6ehttps://catalog.redhat.com/software/containers/kmm/kernel-module-management-hub-operator-bundle/63d84cc33862da54bb19b8c6?architecture=amd64&image=654273ac86f7e537ae452f6e[KMM Operator bundle]

include::modules/kmm-hub-installing-kmm-hub-olm.adoc[leveloffset=+3]
include::modules/kmm-hub-installing-kmm-hub-creating-resources.adoc[leveloffset=+3]

include::modules/kmm-hub-using-the-managedclustermodule.adoc[leveloffset=+2]
include::modules/kmm-hub-running-kmm-on-the-spoke.adoc[leveloffset=+2]


// Added for TELCODOCS-1277
include::modules/kmm-customizing-upgrades-for-kernel-modules.adoc[leveloffset=+1]

// Added for TELCODOCS-1278
include::modules/kmm-day1-kernel-module-loading.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* link:https://docs.openshift.com/container-platform/4.13/post_installation_configuration/machine-configuration-tasks.html#machine-config-operator_post-install-machine-configuration-tasks[Machine Config Operator]

include::modules/kmm-day1-supported-use-cases.adoc[leveloffset=+2]
include::modules/kmm-day1-oot-kernel-module-loading-flow.adoc[leveloffset=+2]
include::modules/kmm-day1-kernel-module-image.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* link:https://docs.openshift.com/container-platform/4.13/hardware_enablement/psap-driver-toolkit.html[Driver Toolkit]

include::modules/kmm-day1-in-tree-module-replacement.adoc[leveloffset=+2]
include::modules/kmm-day1-mco-yaml-creation.adoc[leveloffset=+2]
include::modules/kmm-day1-machineconfigpool.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* link:https://www.redhat.com/en/blog/openshift-container-platform-4-how-does-machine-config-pool-work[About MachineConfigPool]

include::modules/kmm-debugging-and-troubleshooting.adoc[leveloffset=+1]

// Added for TELCODOCS-1067
include::modules/kmm-firmware-support.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../hardware_enablement/kmm-kernel-module-management.adoc#kmm-creating-moduleloader-image_kernel-module-management-operator[Creating a ModuleLoader image].

include::modules/kmm-configuring-the-lookup-path-on-nodes.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../post_installation_configuration/machine-configuration-tasks.adoc#understanding-the-machine-config-operator[Machine Config Operator].

include::modules/kmm-building-a-moduleloader-image.adoc[leveloffset=+2]
include::modules/kmm-tuning-the-module-resource.adoc[leveloffset=+2]

// Added for TELCODOCS-1059
include::modules/kmm-troubleshooting.adoc[leveloffset=+1]
include::modules/kmm-must-gather-tool.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources
* xref:../support/gathering-cluster-data.adoc#about-must-gather_gathering-cluster-data[About the must-gather tool]

include::modules/kmm-gathering-data-for-kmm.adoc[leveloffset=+3]
include::modules/kmm-gathering-data-for-kmm-hub.adoc[leveloffset=+3]
