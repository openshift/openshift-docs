// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

:_mod-docs-content-type: REFERENCE
[id="machine-about-phases_{context}"]
= Machine phases

As a machine moves through its lifecycle, it passes through different phases. Each phase is a basic representation of the state of the machine.

`Provisioning`:: There is a request to provision a new machine. The machine does not yet exist and does not have an instance, a provider ID, or an address.

`Provisioned`:: The machine exists and has a provider ID or an address. The cloud provider has created an instance for the machine. The machine has not yet become a node and the `status.nodeRef` section of the machine object is not yet populated.

`Running`:: The machine exists and has a provider ID or address. Ignition has run successfully and the cluster machine approver has approved a certificate signing request (CSR). The machine has become a node and the `status.nodeRef` section of the machine object contains node details.

`Deleting`:: There is a request to delete the machine. The machine object has a `DeletionTimestamp` field that indicates the time of the deletion request.

`Failed`:: There is an unrecoverable problem with the machine. This can happen, for example, if the cloud provider deletes the instance for the machine.