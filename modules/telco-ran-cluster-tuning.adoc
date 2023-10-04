// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-cluster-tuning_{context}"]
= Cluster tuning

New in this release::
* You can remove the Image Registry Operator by using the cluster capabilities feature.
+
[NOTE]
====
You configure cluster capabilities by using the `spec.clusters.installConfigOverrides` field in the `SiteConfig` CR that you use to install the cluster.
====

Description::
The cluster capabilities feature now includes a `MachineAPI` component which, when excluded, disables the following Operators and their resources in the cluster:

* `openshift/cluster-autoscaler-operator`

* `openshift/cluster-control-plane-machine-set-operator`

* `openshift/machine-api-operator`

Limits and requirements::
* Cluster capabilities are not available for installer-provisioned installation methods.

* You must apply all platform tuning configurations.
The following table lists the required platform tuning configurations:
+
.Cluster capabilities configurations
[cols=2*, width="90%", options="header"]
|====
|Feature
|Description

|Remove optional cluster capabilities
a|Reduce the {product-title} footprint by disabling optional cluster Operators on {sno} clusters only.

* Remove all optional Operators except the Marketplace and Node Tuning Operators.

|Configure cluster monitoring
a|Configure the monitoring stack for reduced footprint by doing the following:

* Disable the local `alertmanager` and `telemeter` components.

* If you use {rh-rhacm} observability, the CR must be augmented with appropriate `additionalAlertManagerConfigs` CRs to forward alerts to the hub cluster.

* Reduce the `Prometheus` retention period to 24h.
+
[NOTE]
====
The {rh-rhacm} hub cluster aggregates managed cluster metrics.
====

|Disable networking diagnostics
|Disable networking diagnostics for {sno} because they are not required.

|Configure a single Operator Hub catalog source
|Configure the cluster to use a single catalog source that contains only the Operators required for a RAN DU deployment.
Each catalog source increases the CPU use on the cluster.
Using a single `CatalogSource` fits within the platform CPU budget.
|====
