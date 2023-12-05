:_mod-docs-content-type: CONCEPT

[id="performance-challenges-in-machine-configurations-and-argo-cd"]
= Solution: Enhance performance in machine configurations and Argo CD

When you are using a Machine Config Operator as part of a GitOps workflow, the following sequence can produce suboptimal performance:

* Argo CD starts an automated sync job after a commit to the Git repository that contains application resources.

* If Argo CD notices a new or an updated machine configuration while the sync operation is in process, MCO picks up the change to the machine configuration and starts rebooting the nodes to apply the change.

* If a rebooting node in the cluster contains the Argo CD application controller, the application controller terminates, and the application sync is aborted.

As the MCO reboots the nodes in sequential order, and the Argo CD workloads can be rescheduled on each reboot, it can take some time for the sync to be completed. This results in an undefined behavior until the MCO has rebooted all nodes affected by the machine configurations within the sync.
