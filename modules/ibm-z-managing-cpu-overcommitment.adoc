// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

:_mod-docs-content-type: CONCEPT
[id="ibm-z-managing-cpu-overcommitment_{context}"]
= Managing CPU overcommitment

In a highly virtualized {ibm-z-name} environment, you must carefully plan the infrastructure setup and sizing. One of the most important features of virtualization is the capability to do resource overcommitment, allocating more resources to the virtual machines than actually available at the hypervisor level. This is very workload dependent and there is no golden rule that can be applied to all setups.

Depending on your setup, consider these best practices regarding CPU overcommitment:

* At LPAR level (PR/SM hypervisor), avoid assigning all available physical cores (IFLs) to each LPAR. For example, with four physical IFLs available, you should not define three LPARs with four logical IFLs each.
* Check and understand LPAR shares and weights.
* An excessive number of virtual CPUs can adversely affect performance. Do not define more virtual processors to a guest than logical processors are defined to the LPAR.
* Configure the number of virtual processors per guest for peak workload, not more.
* Start small and monitor the workload. Increase the vCPU number incrementally if necessary.
* Not all workloads are suitable for high overcommitment ratios. If the workload is CPU intensive, you will probably not be able to achieve high ratios without performance problems. Workloads that are more I/O intensive can keep consistent performance even with high overcommitment ratios.