:_mod-docs-content-type: ASSEMBLY
[id="ibm-z-recommended-host-practices"]
= Recommended host practices for {ibm-z-title} & {ibm-linuxone-title} environments
include::_attributes/common-attributes.adoc[]
:context: ibm-z-recommended-host-practices

toc::[]

This topic provides recommended host practices for {product-title} on {ibm-z-name} and {ibm-linuxone-name}.

[NOTE]
====
The s390x architecture is unique in many aspects. Therefore, some recommendations made here might not apply to other platforms.
====

[NOTE]
====
Unless stated otherwise, these practices apply to both z/VM and {op-system-base-full} KVM installations on {ibm-z-name} and {ibm-linuxone-name}.
====

include::modules/ibm-z-managing-cpu-overcommitment.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* link:https://www.vm.ibm.com/perf/tips/prgcom.html[z/VM Common Performance Problems and Solutions]

* link:https://www.ibm.com/docs/en/linux-on-systems?topic=overcommitment-considerations[z/VM overcommitment considerations]

* link:https://www.ibm.com/docs/en/zos/2.2.0?topic=director-lpar-cpu-management[LPAR CPU management]


include::modules/ibm-z-disable-thp.adoc[leveloffset=+1]

include::modules/ibm-z-boost-networking-performance-with-rfs.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* link:https://developer.ibm.com/tutorials/red-hat-openshift-on-ibm-z-tune-your-network-performance-with-rfs/[{product-title} on {ibm-z-name}: Tune your network performance with RFS]

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/performance_tuning_guide/sect-red_hat_enterprise_linux-performance_tuning_guide-networking-configuration_tools#sect-Red_Hat_Enterprise_Linux-Performance_Tuning_Guide-Configuration_tools-Configuring_Receive_Flow_Steering_RFS[Configuring Receive Flow Steering (RFS)]

* link:https://www.kernel.org/doc/Documentation/networking/scaling.txt[Scaling in the Linux Networking Stack]

include::modules/ibm-z-choose-networking-setup.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* link:https://www.ibm.com/docs/en/linux-on-systems?topic=openshift-performance#openshift_perf__ocp_eval[{product-title} on {ibm-z-name} - Performance Experiences, Hints and Tips]

* link:https://www.ibm.com/docs/en/linux-on-systems?topic=openshift-performance#openshift_perf__ocp_net[{product-title} on {ibm-z-name} Networking Performance]

* xref:../nodes/scheduling/nodes-scheduler-node-affinity.adoc[Controlling pod placement on nodes using node affinity rules]

include::modules/ibm-z-ensure-high-disk-performance-hyperpav.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* link:https://www.ibm.com/docs/en/linux-on-systems?topic=io-using-hyperpav-eckd-dasd[Using HyperPAV for ECKD DASD]

* link:https://public.dhe.ibm.com/software/dw/linux390/perf/zvm_hpav00.pdf[Scaling HyperPAV alias devices on Linux guests on z/VM]

include::modules/ibm-z-rhel-kvm-host-recommendations.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* link:https://www.ibm.com/docs/en/linux-on-systems?topic=v-kvm[Linux on {ibm-z-name} Performance Tuning for KVM]

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_virtualization/getting-started-with-virtualization-in-rhel-8-on-ibm-z_configuring-and-managing-virtualization[Getting started with virtualization on {ibm-z-name}]
