// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-red-hat-advanced-cluster-management-rhacm_{context}"]
= {rh-rhacm-first}

New in this release::
* Additional node labels can be configured during installation.

Description::
{rh-rhacm} provides Multi Cluster Engine (MCE) installation and ongoing lifecycle management functionality for deployed clusters.
You declaratively specify configurations and upgrades with `Policy` CRs and apply the policies to clusters with the {rh-rhacm} policy controller as managed by {cgu-operator-full}.
+
* {ztp-first} uses the MCE feature of {rh-rhacm}
* Configuration, upgrades, and cluster status are managed with the {rh-rhacm} policy controller

Limits and requirements::
* A single hub cluster supports up to 3500 deployed {sno} clusters with 5 `Policy` CRs bound to each cluster.

Engineering considerations::
* Cluster specific configuration: managed clusters typically have some number of configuration values that are specific to the individual cluster.
These configurations should be managed using {rh-rhacm} policy hub-side templating with values pulled from `ConfigMap` CRs based on the cluster name.

* To save CPU resources on managed clusters, policies that apply static configurations should be unbound from managed clusters after {ztp} installation of the cluster.
For more information, see link:https://docs.openshift.com/container-platform/latest/storage/understanding-persistent-storage.html#releasing_understanding-persistent-storage[Release a persistent volume].
