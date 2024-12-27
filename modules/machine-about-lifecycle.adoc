// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

:_mod-docs-content-type: REFERENCE
[id="machine-about-lifecycle_{context}"]
= The machine lifecycle

The lifecycle begins with the request to provision a machine and continues until the machine no longer exists.

//.Machine lifecycle
//image::to-do-machine-lifecycle.png["The sequence of events in the machine lifecycle."]

The machine lifecycle proceeds in the following order. Interruptions due to errors or lifecycle hooks are not included in this overview.

. There is a request to provision a new machine for one of the following reasons:
** A cluster administrator scales a machine set such that it requires additional machines.
** An autoscaling policy scales machine set such that it requires additional machines.
** A machine that is managed by a machine set fails or is deleted and the machine set creates a replacement to maintain the required number of machines.

. The machine enters the `Provisioning` phase.

. The infrastructure provider creates an instance for the machine.

. The machine has a provider ID or address and enters the `Provisioned` phase.

. The Ignition configuration file is processed.

. The kubelet issues a certificate signing request (CSR).

. The cluster machine approver approves the CSR.

. The machine becomes a node and enters the `Running` phase.

. An existing machine is slated for deletion for one of the following reasons:
** A user with `cluster-admin` permissions uses the `oc delete machine` command.
** The machine gets a `machine.openshift.io/delete-machine` annotation.
** The machine set that manages the machine marks it for deletion to reduce the replica count as part of reconciliation.
** The cluster autoscaler identifies a node that is unnecessary to meet the deployment needs of the cluster.
** A machine health check is configured to replace an unhealthy machine.

. The machine enters the `Deleting` phase, in which it is marked for deletion but is still present in the API.

. The machine controller removes the instance from the infrastructure provider.

. The machine controller deletes the `Node` object.