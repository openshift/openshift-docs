// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: CONCEPT
[id="about-kmm_{context}"]
= About the Kernel Module Management Operator

The Kernel Module Management (KMM) Operator manages, builds, signs, and deploys out-of-tree kernel modules and device plugins on {product-title} clusters.

KMM adds a new `Module` CRD which describes an out-of-tree kernel module and its associated device plugin.
You can use `Module` resources to configure how to load the module, define `ModuleLoader` images for kernel versions, and include instructions for building and signing modules for specific kernel versions.

KMM is designed to accommodate multiple kernel versions at once for any kernel module, allowing for seamless node upgrades and reduced application downtime.