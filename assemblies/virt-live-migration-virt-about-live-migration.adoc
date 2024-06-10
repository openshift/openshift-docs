:_mod-docs-content-type: ASSEMBLY
[id="virt-about-live-migration"]
= About live migration
include::_attributes/common-attributes.adoc[]
:context: virt-about-live-migration

toc::[]

Live migration is the process of moving a running virtual machine (VM) to another node in the cluster without interrupting the virtual workload. By default, live migration traffic is encrypted using Transport Layer Security (TLS).

[id="live-migration-requirements_virt-about-live-migration"]
== Live migration requirements

Live migration has the following requirements:

* The cluster must have shared storage with `ReadWriteMany` (RWX) access mode.
* The cluster must have sufficient RAM and network bandwidth.
+
[NOTE]
====
You must ensure that there is enough memory request capacity in the cluster to support node drains that result in live migrations. You can determine the approximate required spare memory by using the following calculation:

----
Product of (Maximum number of nodes that can drain in parallel) and (Highest total VM memory request allocations across nodes)
----

The default number of migrations that can run in parallel in the cluster is 5.
====

* If a VM uses a host model CPU, the nodes must support the CPU.
* xref:../../virt/vm_networking/virt-dedicated-network-live-migration.adoc#virt-dedicated-network-live-migration[Configuring a dedicated Multus network] for live migration is highly recommended. A dedicated network minimizes the effects of network saturation on tenant workloads during migration.

[id="common-live-migration-tasks_virt-about-live-migration"]
== Common live migration tasks

You can perform the following live migration tasks:

* Configure live migration settings:

** xref:../../virt/live_migration/virt-configuring-live-migration.adoc#virt-configuring-live-migration-limits_virt-configuring-live-migration[Limits and timeouts]
** xref:../../virt/getting_started/virt-web-console-overview.adoc#overview-settings-cluster_virt-web-console-overview[Maximum number of migrations per node or cluster]
** xref:../../virt/getting_started/virt-web-console-overview.adoc#overview-settings-cluster_virt-web-console-overview[Select a dedicated live migration network from existing networks]

* xref:../../virt/live_migration/virt-initiating-live-migration.adoc#virt-initiating-live-migration[Initiate and cancel live migration]
* xref:../../virt/getting_started/virt-web-console-overview.adoc#overview-migrations_virt-web-console-overview[Monitor the progress of all live migrations]
* xref:../../virt/getting_started/virt-web-console-overview.adoc#virtualmachine-details-metrics_virt-web-console-overview[View VM migration metrics]


[id="additional-resources_virt-about-live-migration"]
== Additional resources
* xref:../../virt/monitoring/virt-prometheus-queries.adoc#virt-live-migration-metrics_virt-prometheus-queries[Prometheus queries for live migration]
* link:https://access.redhat.com/articles/6994974#vm-migration-tuning[VM migration tuning]
* xref:../../virt/nodes/virt-node-maintenance.adoc#run-strategies[VM run strategies]
* xref:../../virt/nodes/virt-node-maintenance.adoc#eviction-strategies[VM and cluster eviction strategies]