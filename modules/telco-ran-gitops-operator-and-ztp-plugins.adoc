// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-gitops-operator-and-ztp-plugins_{context}"]
= {gitops-shortname} and {ztp} plugins

New in this release::
* GA support for inclusion of user-provided CRs in Git for {ztp} deployments

* {ztp} independence from the deployed cluster version

Description::
{gitops-shortname} and {ztp} plugins provide a {gitops-shortname}-based infrastructure for managing cluster deployment and configuration.
Cluster definitions and configurations are maintained as a declarative state in Git.
ZTP plugins provide support for generating installation CRs from the `SiteConfig` CR and automatic wrapping of configuration CRs in policies based on `PolicyGenTemplate` CRs.
+
You can deploy and manage multiple versions of {product-title} on managed clusters with the baseline reference configuration CRs in a `/source-crs` subdirectory provided that subdirectory also contains the `kustomization.yaml` file.
You add user-provided CRs to this subdirectory that you use with the predefined CRs that are specified in the `PolicyGenTemplate` CRs.
This allows you to tailor your configurations to suit your specific requirements and provides {ztp} version independence between managed clusters and the hub cluster.
+
For more information, see the following:

* link:https://docs.openshift.com/container-platform/latest/scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.html#ztp-preparing-the-ztp-git-repository-ver-ind_ztp-preparing-the-hub-cluster[Preparing the site configuration repository for version independence]
* link:https://docs.openshift.com/container-platform/latest/scalability_and_performance/ztp_far_edge/ztp-advanced-policy-config.html#ztp-adding-new-content-to-gitops-ztp_ztp-advanced-policy-config[Adding custom content to the {ztp} pipeline]

Limits::
* 300 `SiteConfig` CRs per ArgoCD application.
You can use multiple applications to achieve the maximum number of clusters supported by a single hub cluster.

* Content in the `/source-crs` folder in Git overrides content provided in the {ztp} plugin container.
Git takes precedence in the search path.

* Add the `/source-crs` folder in the same directory as the `kustomization.yaml` file, which includes the `PolicyGenTemplate` as a generator.
+
[NOTE]
====
Alternative locations for the `/source-crs` directory are not supported in this context.
====

Engineering considerations::
* To avoid confusion or unintentional overwriting of files when updating content, use unique and distinguishable names for user-provided CRs in the `/source-crs` folder and extra manifests in Git.

* The `SiteConfig` CR allows multiple extra-manifest paths.
When files with the same name are found in multiple directory paths, the last file found takes precedence.
This allows the full set of version specific Day 0 manifests (extra-manifests) to be placed in Git and referenced from the `SiteConfig`.
With this feature, you can deploy multiple {product-title} versions to managed clusters simultaneously.

* The `extraManifestPath` field of the `SiteConfig` CR is deprecated from {product-title} 4.15 and later.
Use the new `extraManifests.searchPaths` field instead.
