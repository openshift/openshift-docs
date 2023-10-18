// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-install-ztp.adoc

:_module-type: PROCEDURE
[id="ztp-customizing-the-install-extra-manifests_{context}"]
= Customizing extra installation manifests in the {ztp} pipeline

You can define a set of extra manifests for inclusion in the installation phase of the {ztp-first} pipeline. These manifests are linked to the `SiteConfig` custom resources (CRs) and are applied to the cluster during installation. Including `MachineConfig` CRs at install time makes the installation process more efficient.

.Prerequisites

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

.Procedure

. Create a set of extra manifest CRs that the {ztp} pipeline uses to customize the cluster installs.

. In your custom `/siteconfig` directory, create a subdirectory `/custom-manifest` for your extra manifests. The following example illustrates a sample `/siteconfig` with `/custom-manifest` folder:
+
[source,text]
----
siteconfig
├── site1-sno-du.yaml
├── site2-standard-du.yaml
├── extra-manifest/
└── custom-manifest
    └── 01-example-machine-config.yaml
----
+
[NOTE]
====
The subdirectory names `/custom-manifest` and `/extra-manifest` used throughout are example names only. There is no requirement to use these names and no restriction on how you name these subdirectories.
In this example `/extra-manifest` refers to the Git subdirectory that stores the contents of `/extra-manifest` from the `ztp-site-generate` container.
====

. Add your custom extra manifest CRs to the `siteconfig/custom-manifest` directory.

. In your `SiteConfig` CR, enter the directory name in the `extraManifests.searchPaths` field, for example:
+
[source,yaml]
----
clusters:
- clusterName: "example-sno"
  networkType: "OVNKubernetes"
  extraManifests:
    searchPaths:
      - extra-manifest/ <1>
      - custom-manifest/ <2>
----
<1> Folder for manifests copied from the `ztp-site-generate` container.
<2> Folder for custom manifests.

. Save the `SiteConfig`, `/extra-manifest`, and `/custom-manifest` CRs, and push them to the site configuration repo.

During cluster provisioning, the {ztp} pipeline appends the CRs in the `/custom-manifest` directory to the default set of extra manifests stored in `extra-manifest/`.

[NOTE]
====
As of version 4.14 `extraManifestPath` is subject to a deprecation warning. 

While `extraManifestPath` is still supported, we recommend that you use `extraManifests.searchPaths`. 
If you define `extraManifests.searchPaths` in the `SiteConfig` file, the {ztp} pipeline does not fetch manifests from the `ztp-site-generate` container during site installation.

If you define both `extraManifestPath` and `extraManifests.searchPaths` in the `Siteconfig` CR, the setting defined for `extraManifests.searchPaths` takes precedence.

It is strongly recommended that you extract the contents of `/extra-manifest` from the `ztp-site-generate` container and push it to the GIT repository.
====