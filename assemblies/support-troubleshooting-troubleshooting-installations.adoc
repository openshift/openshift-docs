:_mod-docs-content-type: ASSEMBLY
[id="troubleshooting-installations"]
= Troubleshooting installations
include::_attributes/common-attributes.adoc[]
:context: troubleshooting-installations

toc::[]

// Determining where installation issues occur
include::modules/determining-where-installation-issues-occur.adoc[leveloffset=+1]

// User-provisioned infrastructure installation considerations
include::modules/upi-installation-considerations.adoc[leveloffset=+1]

// Checking load balancer configuration before {product-title} installation
include::modules/checking-load-balancer-configuration.adoc[leveloffset=+1]

// Specifying {product-title} installer log levels
include::modules/specifying-openshift-installer-log-levels.adoc[leveloffset=+1]

// Troubleshooting `openshift-install` command issues
include::modules/troubleshooting-openshift-install-command-issues.adoc[leveloffset=+1]

// Monitoring installation progress
include::modules/monitoring-installation-progress.adoc[leveloffset=+1]

// Gathering bootstrap node diagnostic data
include::modules/gathering-bootstrap-diagnostic-data.adoc[leveloffset=+1]

// Investigating control plane node installation issues
include::modules/investigating-master-node-installation-issues.adoc[leveloffset=+1]

// Investigating etcd installation issues
include::modules/investigating-etcd-installation-issues.adoc[leveloffset=+1]

// Investigating control plane node kubelet and API server issues
include::modules/investigating-kubelet-api-installation-issues.adoc[leveloffset=+1]

// Investigating worker node installation issues
include::modules/investigating-worker-node-installation-issues.adoc[leveloffset=+1]

// Querying Operator status after installation
include::modules/querying-operator-status-after-installation.adoc[leveloffset=+1]

// Gathering logs from a failed installation
include::modules/installation-bootstrap-gather.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
[role="_additional-resources"]
== Additional resources

* See xref:../../architecture/architecture-installation.adoc#installation-process_architecture-installation[Installation process] for more details on {product-title} installation types and process.
endif::openshift-rosa,openshift-dedicated[]

// TODO: xref to UPI recommendations for respective versions, with ifdefs.
