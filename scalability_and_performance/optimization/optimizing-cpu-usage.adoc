:_mod-docs-content-type: ASSEMBLY
[id="optimizing-cpu-usage"]
= Optimizing CPU usage with mount namespace encapsulation
include::_attributes/common-attributes.adoc[]
:context: optimizing-cpu-usage

toc::[]

You can optimize CPU usage in {product-title} clusters by using mount namespace encapsulation to provide a private namespace for kubelet and CRI-O processes. This reduces the cluster CPU resources used by systemd with no difference in functionality.

:FeatureName: Mount namespace encapsulation
include::snippets/technology-preview.adoc[]

include::modules/optimizing-by-encapsulation.adoc[leveloffset=+1]

include::modules/enabling-encapsulation.adoc[leveloffset=+1]

include::modules/supporting-encapsulation.adoc[leveloffset=+1]

include::modules/running-services-with-encapsulation.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="optimizing-cpu-usage-additional-resources"]
== Additional resources

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/setting-limits-for-applications_monitoring-and-managing-system-status-and-performance#what-namespaces-are_setting-limits-for-applications[What are namespaces]

* link:https://www.redhat.com/sysadmin/container-namespaces-nsenter[Manage containers in namespaces by using nsenter]

* xref:../../rest_api/machine_apis/machineconfig-machineconfiguration-openshift-io-v1.adoc[MachineConfig]
