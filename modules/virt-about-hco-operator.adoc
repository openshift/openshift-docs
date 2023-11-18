// Module included in the following assemblies:
//
// * virt/virt-architecture.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-hco-operator_{context}"]
= About the HyperConverged Operator (HCO)

The HCO, `hco-operator`, provides a single entry point for deploying and managing {VirtProductName} and several helper operators with opinionated defaults. It also creates custom resources (CRs) for those operators.

image::cnv_components_hco-operator.png[hco-operator components]

.HyperConverged Operator components
[cols="1,1"]
|===
|*Component* |*Description*

|`deployment/hco-webhook`
|Validates the `HyperConverged` custom resource contents.

|`deployment/hyperconverged-cluster-cli-download`
|Provides the `virtctl` tool binaries to the cluster so that you can download them directly from the cluster.

|`KubeVirt/kubevirt-kubevirt-hyperconverged`
|Contains all operators, CRs, and objects needed by {VirtProductName}.

|`SSP/ssp-kubevirt-hyperconverged`
|A Scheduling, Scale, and Performance (SSP) CR. This is automatically created by the HCO.

|`CDI/cdi-kubevirt-hyperconverged`
|A Containerized Data Importer (CDI) CR. This is automatically created by the HCO.

|`NetworkAddonsConfig/cluster`
|A CR that instructs and is managed by the `cluster-network-addons-operator`.
|===
