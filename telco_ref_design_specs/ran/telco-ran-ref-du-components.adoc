:_mod-docs-content-type: ASSEMBLY
:telco-ran:
[id="telco-ran-ref-du-components"]
= {rds-caps} {product-version} reference design components
:context: ran-ref-design-components
include::_attributes/common-attributes.adoc[]

toc::[]

The following sections describe the various {product-title} components and configurations that you use to configure and deploy clusters to run RAN DU workloads.

include::modules/telco-ran-bios-tuning.adoc[leveloffset=+1]

include::modules/telco-ran-node-tuning-operator.adoc[leveloffset=+1]

include::modules/telco-ran-ptp-operator.adoc[leveloffset=+1]

include::modules/telco-ran-sr-iov-operator.adoc[leveloffset=+1]

include::modules/telco-ran-logging.adoc[leveloffset=+1]

include::modules/telco-ran-sriov-fec-operator.adoc[leveloffset=+1]

include::modules/telco-ran-local-storage-operator.adoc[leveloffset=+1]

include::modules/telco-ran-lvms-operator.adoc[leveloffset=+1]

include::modules/telco-ran-workload-partitioning.adoc[leveloffset=+1]

include::modules/telco-ran-cluster-tuning.adoc[leveloffset=+1]

include::modules/telco-ran-machine-configuration.adoc[leveloffset=+1]

[id="telco-reference-ran-du-deployment-components_{context}"]
== Reference design deployment components

The following sections describe the various {product-title} components and configurations that you use to configure the hub cluster with {rh-rhacm-first}.

include::modules/telco-ran-red-hat-advanced-cluster-management-rhacm.adoc[leveloffset=+2]

include::modules/telco-ran-topology-aware-lifecycle-manager-talm.adoc[leveloffset=+2]

include::modules/telco-ran-gitops-operator-and-ztp-plugins.adoc[leveloffset=+2]

include::modules/telco-ran-agent-based-installer-abi.adoc[leveloffset=+2]

[id="telco-ran-additional-components_{context}"]
== Additional components

include::modules/telco-ran-redfish-operator.adoc[leveloffset=+2]

:!telco-ran:
